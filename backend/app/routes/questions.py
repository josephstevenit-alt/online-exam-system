from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models import Question
from flask_jwt_extended import jwt_required

q_bp = Blueprint('questions', __name__)

@q_bp.route('/', methods=['POST'])
@jwt_required()
def create_question():
    data = request.get_json() or {}
    stem = data.get('stem'); options = data.get('options'); correct_index = data.get('correct_index'); mark = data.get('mark',1)
    if not stem or not options or correct_index is None:
        return jsonify({"msg":"missing fields"}),400
    q = Question(stem=stem, options=options, correct_index=correct_index, mark=mark)
    db.session.add(q); db.session.commit()
    return jsonify({"id": q.id}),201

@q_bp.route('/list', methods=['GET'])
def list_questions():
    qs = Question.query.all()
    out = [{"id": q.id, "stem": q.stem, "options": q.options, "mark": q.mark} for q in qs]
    return jsonify(out)

@q_bp.route('/random', methods=['GET'])
def random_questions():
    import random
    n = int(request.args.get('n',10))
    qs = Question.query.all()
    selected = random.sample(qs, min(n, len(qs)))
    out = [{"id": q.id, "stem": q.stem, "options": q.options, "mark": q.mark} for q in selected]
    return jsonify(out)
