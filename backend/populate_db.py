import json
from app import db
from models import SurveyQuestion, SurveyAnswer
from app import app
from flask_sqlalchemy import SQLAlchemy


def populate_db():
    # Load your questions and answers from the JSON file
    with open('survey_questions.json', 'r') as file:
        questions_data = json.load(file)

    # Insert questions and answers into the database
    for question_data in questions_data:
        question = SurveyQuestion(
            question_text=question_data['text'],
            question_type=question_data['type']
        )
        db.session.add(question)
        db.session.commit()  # Commit to get the question ID

        # Insert the answers for the question
        for answer_text in question_data['answers']:
            answer = SurveyAnswer(question_id=question.id, answer_text=answer_text)
            db.session.add(answer)

    db.session.commit()  # Commit all the new answers to the database

if __name__ == '__main__':
    with app.app_context():
        populate_db()
        print("Database populated with survey questions and answers.")
