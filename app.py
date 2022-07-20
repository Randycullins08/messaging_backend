from flask import Flask
from flask_marshmallow import Marshmallow
from db import db, init_db, query

app = Flask(__name__)

database_host = "127.0.01:5432"
database_name = "messaging"
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{database_host}/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app, db)
ma = Marshmallow(app)

def create_all():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    create_all()
    app.run()