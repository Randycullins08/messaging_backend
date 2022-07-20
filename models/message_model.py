from sqlalchemy.dialects.postgresql import UUID
import uuid
import marshmallow as ma
from datetime import datetime
from db import db

class Message(db.Model):
    __tablename__ = 'message'
    message_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    message_text = db.Column(db.String(), nullable=False)
    created_date = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    conversation_id = db.Column(UUID(as_uuid=True), db.ForeignKey('conversation.conversation_id'), nullable=False)

    def __init__(self, message_text, created_date, conversation_id):
        self.message_text = message_text
        self.created_date = created_date
        self.conversation_id = conversation_id

class MessageSchema(ma.Schema):
    class Meta:
        fields = ['message_id', 'message_text', 'created_date', 'conversation_id']

message_schema = MessageSchema()
messages_schema = MessageSchema(many=True)