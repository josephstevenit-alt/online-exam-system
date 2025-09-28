from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models import Question, ExamResult
from flask_jwt_extended import jwt_required, get_jwt_identity

exam_bp = Blueprint('exams', __name__)

@exam_bp.route('/start', methods=['GET'])
@jwt_required(optional=True)
def start_exam():
    # Return N random questions (without answer)
    from random import sample
    n = int(request.args.get('n', 10))
    qs = Question.query.all()
    selected = sample(qs, min(n,len(qs)))
    out = [{"id": q.id, "stem": q.stem, "options": q.options, "mark": q.mark} for q in selected]
    return jsonify({"questions": out})

@exam_bp.route('/submit', methods=['POST'])
@jwt_required()
def submit_exam():
    data = request.get_json() or {}
    user_id = int(get_jwt_identity())  # cast back to int

    answers = data.get('answers')  # list of {question_id, selected_index}
    if not answers:
        return jsonify({"msg":"no answers sent"}),400
    total = 0; score = 0; details = []
    for ans in answers:
        q = Question.query.get(ans.get('question_id'))
        if not q:
            continue
        total += q.mark
        correct = (q.correct_index == ans.get('selected_index'))
        if correct: score += q.mark
        details.append({
            "question_id": q.id,
            "selected_index": ans.get('selected_index'),
            "correct_index": q.correct_index,
            "correct": correct,
            "mark": q.mark
        })
    res = ExamResult(user_id=user_id, score=score, total=total, details=details)
    db.session.add(res); db.session.commit()
    return jsonify({"score": score, "total": total, "result_id": res.id, "details": details}),200
