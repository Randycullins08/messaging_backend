from sqlalchemy.dialects.postgresql import UUID
import uuid
import marshmallow as ma
from db import db

class Conversation(db.Model):
    __tablename__='conversation'
    conversation_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    conversation_name = db.Column(db.String(), nullable=False)

    def __init__(self, created_date, conversation_name):
        self.created_date = created_date
        self.conversation_name = conversation_name

class ConversationSchema(ma.Schema):
    class Meta:
        fields = ['conversation_id', 'conversation_name']

conversation_schema = ConversationSchema()
conversations_schema = ConversationSchema(many=True)