from extensions import db

class SurveyQuestion(db.Model):
    __tablename__ = 'survey_questions'
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(255), nullable=False)
    question_type = db.Column(db.String(50), nullable=False)
    answers = db.relationship('SurveyAnswer', backref='question', lazy=True)

    def __repr__(self):
        return f'<SurveyQuestion {self.question_text}>'

class SurveyAnswer(db.Model):
    __tablename__ = 'survey_answers'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('survey_questions.id'), nullable=False)
    answer_text = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<SurveyAnswer {self.answer_text}>'