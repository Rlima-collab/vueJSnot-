from .app import app, db
from .models import Questionnaire, Question
from flask import request, jsonify, abort


@app.route("/questionnaires", methods=["GET"])
def get_questionnaires():
    questionnaires = Questionnaire.query.all()
    return jsonify({"questionnaires": [q.to_json() for q in questionnaires]})

@app.route("/questions", methods=["GET"])
def get_all_questions():
    questions = Question.query.all()
    return jsonify([q.to_json() for q in questions])

@app.route("/questionnaires", methods=["POST"])
def create_questionnaire():
    if not request.json or "name" not in request.json:
        abort(400)

    questionnaire = Questionnaire(name=request.json["name"])
    db.session.add(questionnaire)
    db.session.commit()
    return jsonify(questionnaire.to_json())

@app.route("/questionnaires/<int:questionnaire_id>", methods=["GET"])
def get_questionnaire_par_id(questionnaire_id):
    questionnaire = Questionnaire.query.get(questionnaire_id)
    return jsonify(questionnaire.to_json())

@app.route("/questionnaires/<int:questionnaire_id>/questions/<int:question_id>", methods=["GET"])
def get_question_par_id(questionnaire_id, question_id):
    question = Question.query.filter_by(id=question_id, questionnaire_id=questionnaire_id).first() # Il faut absolument mettre le first !!!!!!!! sinon AttributeError: 'Query' object has no attribute 'to_json'
    return jsonify(question.to_json())

@app.route("/questionnaires/<int:questionnaire_id>/questions", methods=["GET"])
def get_question_par_questionnaire(questionnaire_id):
    question = Question.query.filter_by(questionnaire_id=questionnaire_id).all()
    return jsonify({"questions": [q.to_json() for q in question]})

@app.route("/questionnaires/<int:questionnaire_id>/questions", methods=["POST"])
def create_question(questionnaire_id):
    if not request.json or "title" not in request.json or "question_type" not in request.json:
        abort(400)
    
    new_question = Question(
        title=request.json["title"],
        question_type=request.json["question_type"],
        questionnaire_id=questionnaire_id
    )
    
    db.session.add(new_question)
    db.session.commit()
    
    return jsonify(new_question.to_json()), 201

@app.route("/questionnaires/<int:questionnaire_id>/questions/<int:id_question>", methods=["PUT"])
def update_question(questionnaire_id, id_question):
    question = Question.query.filter_by(id=id_question, questionnaire_id=questionnaire_id).first()
    if "title" in request.json:
        question.title = request.json["title"]
    if "question_type" in request.json:
        question.question_type = request.json["question_type"]
    
    db.session.commit()
    return jsonify(question.to_json())

@app.route("/questionnaires/<int:questionnaire_id>", methods=["DELETE"])
def delete_questionnaire(questionnaire_id):
    questionnaire = Questionnaire.query.get(questionnaire_id)
    db.session.delete(questionnaire)
    db.session.commit()
    return jsonify({"result": True})


@app.route("/questionnaires/<int:questionnaire_id>/questions/<int:id_question>", methods=["DELETE"])
def delete_question(questionnaire_id, id_question):
    question = Question.query.filter_by(id=id_question, questionnaire_id=questionnaire_id).first()
    db.session.delete(question)
    db.session.commit()
    return jsonify({"result": True})

@app.route("/questionnaires/<int:questionnaire_id>", methods=["PUT"])
def update_questionnaire(questionnaire_id):
    questionnaire = Questionnaire.query.get(questionnaire_id)
    if "name" in request.json:
        questionnaire.name = request.json["name"]
    db.session.commit()
    return jsonify(questionnaire.to_json())