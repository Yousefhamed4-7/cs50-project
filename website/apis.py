from flask import Blueprint,jsonify,request,session
from .utilities.database import Database

db = Database()

api = Blueprint("api",__name__)


@api.route("/iscorrect",methods=["POST"])
def iscorrect():
    choice  = db.get_choice(request.json.get("choice_id"))
    question = db.get_question(request.json.get("question_id"),session["user_id"])
    if not choice or not question:
        return jsonify(
            {
                "message": "No Data Found"
            }
        ,);
    if choice.correct == 1:
        question.Solved = 1
        db.update()
        return jsonify(
            {
            "correct": 1
            }
        )
    question.Solved = 0
    db.update()
    return jsonify({
        "incorrect": 0
    })