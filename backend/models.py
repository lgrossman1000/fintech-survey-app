from app import db

class SurveyQuestion(db.Model):
    __tablename__ = 'survey_questions'
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(255), nullable=False)
    question_type = db.Column(db.String(50), nullable=False)
    
    # Define a relationship if you have a separate Answers table
    answers = db.relationship('SurveyAnswer', backref='question', lazy=True, foreign_keys='SurveyAnswer.question_id')

    def __repr__(self):
        return f'<SurveyQuestion {self.question_text}>'

class SurveyAnswer(db.Model):
    __tablename__ = 'survey_answers'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('survey_questions.id'), nullable=False)
    answer_text = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f'<SurveyAnswer {self.answer_text}>'

class UserResponse(db.Model):
    __tablename__ = 'user_responses'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('survey_questions.id'), nullable=False)
    answer_id = db.Column(db.Integer, db.ForeignKey('survey_answers.id'), nullable=False)
    # Add a user_id field if you are tracking individual users
    
    def __repr__(self):
        return f'<UserResponse question_id={self.question_id} answer_id={self.answer_id}>'

if __name__ == '__main__':
    db.create_all()
