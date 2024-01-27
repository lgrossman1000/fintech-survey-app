from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes and methods.

@app.route('/submit-survey', methods=['POST'])
def submit_survey():
    data = request.json
    # Here you can validate and process the data
    print("Received data:", data)
    # Placeholder for data processing logic
    # TODO: Validate and store data, or send to ML model
    return jsonify({"message": "Survey data received"}), 201

@app.route('/')
def index():
    return 'The Flask app is running!'


if __name__ == '__main__':
    app.run(debug=True)
