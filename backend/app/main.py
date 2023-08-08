from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

@app.route('/')
def index():
    return 'Hello, Flask with SQLAlchemy and PostgreSQL!'

if __name__ == '__main__':
    app.run(debug=True)
