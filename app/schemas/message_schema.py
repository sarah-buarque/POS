from app.extensions import ma
from app.models.message import Message
from marshmallow import validate
from marshmallow_sqlalchemy import auto_field

class MessageSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Message

    id = auto_field(dump_only=True)

    content = auto_field(
        required=True,
        validate=validate.Length(min=1, max=255)
    )

    created_at = auto_field(dump_only=True)