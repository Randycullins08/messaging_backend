from sqlalchemy.dialects.postgresql import UUID
import uuid
import marshmallow as ma
from datetime import datetime
from db import db

from models.conversation_model import ConversationSchema

class Message(db.Model):
    __tablename__ = 'message'
    message_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    message_text = db.Column(db.String(), nullable=False)
    created_date = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    conversation_id = db.Column(UUID(as_uuid=True), db.ForeignKey('conversation.conversation_id'), nullable=False)
    conversation = db.relationship('conversation', backref= 'conversation', lazy=True)

    def __init__(self, message_text, created_date, conversation_id):
        self.message_text = message_text
        self.created_date = created_date
        self.conversation_id = conversation_id

class MessageSchema(ma.Schema):
    class Meta:
        fields = ['message_id', 'message_text', 'created_date', 'conversation']
    conversation = ma.fields.Nested(ConversationSchema(only=('conversation_name')))

message_schema = MessageSchema()
messages_schema = MessageSchema(many=True)