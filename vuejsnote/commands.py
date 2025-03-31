from todo.app import db, app
from todo.models import Question, Questionnaire
with app.app_context():
    db.create_all() 
    questionnaire1 = Questionnaire(name="Mathématiques")
    questionnaire2 = Questionnaire(name="Informatique")

    db.session.add(questionnaire1)
    db.session.add(questionnaire2)
    db.session.commit()

    question1 = Question("Quelle est la valeur de π ?", "QCM", questionnaire1.id)
    question2 = Question("What is Java?", "Ouverte", questionnaire2.id)

    db.session.add(question1)
    db.session.add(question2)
    db.session.commit()