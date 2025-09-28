from app import create_app
from app.extensions import db
from app.models import User, Question, ExamResult

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Question": Question, "ExamResult": ExamResult}
