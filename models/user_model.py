from sqlalchemy.dialects.postgresql import UUID
import uuid
import marshmallow as ma
from datetime import datetime
from db import db

class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    active = db.Column(db.Boolean(), nullable=False, default=True)

    def __init__(self, first_name, last_name, create_date, active=True):
        self.first_name = first_name
        self.last_name = last_name
        self.create_date = create_date
        self.active = active

class UserSchema(ma.Schema):
    class Meta:
        fields = ['user_id', 'first_name', 'last_name', 'create_date', 'active']

user_schema = UserSchema()
users_schema = UserSchema(many=True)