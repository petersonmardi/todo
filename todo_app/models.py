from .extensions import db
from datetime import datetime as dt


class Task(db.Model):
    __tablename__='task'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    date_time_ = db.Column(db.DateTime, nullable=False, default=dt.now)

    def __repr__(self):
        return f'Task: {self.text}'
