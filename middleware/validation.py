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
                # Return error jika validasi gagal
                return jsonify({"errors": err.messages}), 400
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
    alamat = fields.Str(
        required=False,
        validate=[
            validate.Length(min=3, max=150),
            validate.Regexp(r"^[A-Za-z0-9\s,.\-/()]+$", error="Alamat hanya boleh mengandung simbol () , . - /")
        ]
    )