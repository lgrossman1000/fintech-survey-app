from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from extensions import db  # Import the db instance

load_dotenv('credentials.env')

app = Flask(__name__)
CORS(app)

MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DB = os.getenv('MYSQL_DB')
MYSQL_HOST = os.getenv('MYSQL_HOST')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Initialize db with the Flask app

@app.route('/submit-survey', methods=['POST'])
def submit_survey():
    data = request.json
    print("Received data:", data)
    return jsonify({"message": "Survey data received"}), 201

@app.route('/')
def index():
    return 'The Flask app is running!'

if __name__ == '__main__':
    app.run(debug=True)
