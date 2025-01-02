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
                schema.load(data)
            except ValidationError as err:
                # Combine all error messages into one string
                error_messages = [message for messages in err.messages.values() for message in messages]
                error_string = " | ".join(error_messages)
                return jsonify({"error": error_string}), 400
            # If validation is successful, proceed to the endpoint function.
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Table validation schema
class LoginSchema(Schema):
    # Marshmallow memiliki validator bawaan untuk email
    email = fields.Email(
        required=True,
        error_messages={"invalid": "Invalid credentials"})

    password = fields.Str(
        required=True, 
        validate=validate.Length(min=3, error="Invalid credentials")
    )

class UserSchema(Schema):
    username = fields.Str(
        required=True,
        validate=[
            validate.Length(min=3, max=100),
            validate.Regexp(r"^[A-Za-z\s]+$", error="Names must not contain symbols")
        ]
    )
    
    # Marshmallow memiliki validator bawaan untuk email
    email = fields.Email(
        required=True,
        error_messages={"invalid": "Invalid email"})

    password = fields.Str(
        required=False,
        validate=validate.Length(min=3, error="Minimum password tree character")
    )