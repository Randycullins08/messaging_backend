from sqlalchemy.dialects.postgresql import UUID
import uuid
import marshmallow as ma
from datetime import datetime
from db import db
from models.user_model import UserSchema

class Conversation(db.Model):
    __tablename__='conversation'
    conversation_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    conversation_name = db.Column(db.String(), nullable=False)
    user_one = db.Column(UUID(as_uuid=True), db.ForeignKey('user.user_id'), nullable=False)
    user_two = db.Column(UUID(as_uuid=True), db.ForeignKey('user.user_id'), nullable=False)
    created_date = db.Column(db.DateTime(), default=datetime.utcnow)
    first_user = db.relationship('first_user', backref='first_user', lazy=True)
    second_user = db.relationship('second_user', backref='second_user', lazy=True)

    def __init__(self, created_date, conversation_name, user_one, user_two):
        self.created_date = created_date
        self.conversation_name = conversation_name
        self.user_one = user_one
        self.user_two = user_two

class ConversationSchema(ma.Schema):
    class Meta:
        fields = ['conversation_id', 'conversation_name', 'first_user', 'second_user']
    first_user = ma.fields.Nested(UserSchema(only=('first_name', 'last_name')))
    second_user = ma.fields.Nested(UserSchema(only=('first_name', 'last_name')))

conversation_schema = ConversationSchema()
conversations_schema = ConversationSchema(many=True)