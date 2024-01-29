from app import app
from extensions import db
from models import SurveyQuestion, SurveyAnswer

with app.app_context():
    db.create_all()
