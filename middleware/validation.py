from functools import wraps
from flask import request, jsonify
from marshmallow import Schema, fields, validate, ValidationError

def validate_input(schema_class):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            schema = schema_class()
            data = request.get_json()
            try:
                # Validasi data
                schema.load(data)
            except ValidationError as err:
                # Gabungkan semua pesan error menjadi satu string
                error_messages = [message for messages in err.messages.values() for message in messages]
                error_string = " | ".join(error_messages)
                return jsonify({"error": error_string}), 400
            # Jika validasi sukses, lanjutkan ke fungsi endpoint
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Skema validasi yang sama
class UserSchema(Schema):
    nama = fields.Str(
        required=True,
        validate=[
            validate.Length(min=3, max=100),
            validate.Regexp(r"^[A-Za-z\s]+$", error="Nama tidak boleh mengandung simbol")
        ]
    )
    # Marshmallow memiliki validator bawaan untuk email
    email = fields.Email(
        required=True,
        error_messages={"invalid": "Email harus valid"})
    
    no_telp = fields.Str(
        required=True,
        validate=validate.Regexp(r"^08[0-9]{8,13}$", error="Nomor telepon harus diawali dengan '08' dan panjang 10-15 digit")
    )