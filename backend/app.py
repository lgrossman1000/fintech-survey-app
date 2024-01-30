from flask import Flask, request, jsonify
from models import db, SurveyQuestion, SurveyAnswer, UserResponse
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv('credentials.env')

app = Flask(__name__)
CORS(app)

# Configure the SQLAlchemy part
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{os.getenv("MYSQL_USER")}:{os.getenv("MYSQL_PASSWORD")}@{os.getenv("MYSQL_HOST")}/{os.getenv("MYSQL_DB")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Retrieve all questions
@app.route('/questions', methods=['GET'])
def get_questions():
    questions = SurveyQuestion.query.all()
    return jsonify([{'id': q.id, 'text': q.question_text, 'type': q.question_type} for q in questions])

# Create a new question
@app.route('/questions', methods=['POST'])
def create_question():
    data = request.get_json()
    new_question = SurveyQuestion(question_text=data['text'], question_type=data['type'])
    db.session.add(new_question)
    db.session.commit()
    return jsonify({'id': new_question.id, 'text': new_question.question_text, 'type': new_question.question_type}), 201

# Retrieve a single question by ID
@app.route('/questions/<int:id>', methods=['GET'])
def get_question(id):
    question = SurveyQuestion.query.get_or_404(id)
    return jsonify({'id': question.id, 'text': question.question_text, 'type': question.question_type})

# Update a question by ID
@app.route('/questions/<int:id>', methods=['PUT'])
def update_question(id):
    question = SurveyQuestion.query.get_or_404(id)
    data = request.get_json()
    question.question_text = data['text']
    question.question_type = data['type']
    db.session.commit()
    return jsonify({'id': question.id, 'text': question.question_text, 'type': question.question_type})

# Delete a question by ID
@app.route('/questions/<int:id>', methods=['DELETE'])
def delete_question(id):
    question = SurveyQuestion.query.get_or_404(id)
    db.session.delete(question)
    db.session.commit()
    return jsonify({'message': 'Question deleted successfully'}), 200

# Store user's answers
@app.route('/answers', methods=['POST'])
def store_answer():
    data = request.get_json()
    new_response = UserResponse(question_id=data['question_id'], answer_id=data['answer_id'])
    db.session.add(new_response)
    db.session.commit()
    return jsonify({'message': 'Answer saved successfully'}), 201

# Determine and send the next question
@app.route('/next-question/<int:user_id>', methods=['GET'])
def get_next_question(user_id):
    # Placeholder for your decision tree logic to determine the next question
    # For now, we will just return the next question in order
    last_response = UserResponse.query.filter_by(user_id=user_id).order_by(UserResponse.id.desc()).first()
    if last_response:
        next_question = SurveyQuestion.query.filter(SurveyQuestion.id > last_response.question_id).first()
    else:
        next_question = SurveyQuestion.query.first()
    
    if next_question:
        return jsonify({'id': next_question.id, 'text': next_question.question_text, 'type': next_question.question_type})
    else:
        return jsonify({'message': 'No more questions available'}), 404

if __name__ == '__main__':
    app.run(debug=True)
