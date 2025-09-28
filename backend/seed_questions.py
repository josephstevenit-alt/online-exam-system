from app import create_app
from app.extensions import db
from app.models import Question

app = create_app()
with app.app_context():
    sample = [
        {
            "stem": "What is the output of 2 + 3 in Python?",
            "options": ["23", "5", "Error", "None"],
            "correct_index": 1,
            "mark": 1
        },
        {
            "stem": "Which data structure follows FIFO?",
            "options": ["Stack", "Queue", "Tree", "Graph"],
            "correct_index": 1,
            "mark": 1
        },
    ]
    for q in sample:
        if not Question.query.filter_by(stem=q['stem']).first():
            db.session.add(Question(stem=q['stem'], options=q['options'], correct_index=q['correct_index'], mark=q['mark']))
    db.session.commit()
    print("Seeded sample questions.")
