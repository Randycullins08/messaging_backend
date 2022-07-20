from sqlalchemy.dialects.postgresql import UUID
import uuid
import marshmallow as ma
from datetime import datetime
from db import db

class GroupMember(db.Model):
    __tablename__ = 'group_member'
    group_member_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    contact_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.contact_id'), default=uuid.uuid4, nullable=False)
    conversation_id = db.Column(UUID(as_uuid=True), db.ForeignKey('conversation.conversation_id'), nullable=False)
    created_date = db.Column(db.DateTime(), default=datetime.utcnow)

    def __init__(self, contact_id, conversation_id, created_date):
        self.contact_id = contact_id
        self.conversation_id = conversation_id
        self.created_date = created_date

class GroupMemberSchema(ma.Schema):
    class Meta:
        fields = ['contact_id', 'conversation_id', 'created_date']

group_member_schema = GroupMemberSchema()
group_members_schema = GroupMemberSchema(many=True)