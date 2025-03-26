from .app import db

class Questionnaire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return "<Questionnaire (%d) %r>" % (self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Question(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    question_type = db.Column(db.String(120))
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'))
    questionnaire = db.relationship('Questionnaire', backref=db.backref('questions', lazy='dynamic'))

    def __init__(self, title, question_type, questionnaire_id):
        self.title = title
        self.question_type = question_type
        self.questionnaire_id = questionnaire_id
    
    def __repr__(self):
        return "<Question (%d) %r>" % (self.id, self.title)
    
    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'question_type': self.question_type,
            'questionnaire_id': self.questionnaire_id
        }