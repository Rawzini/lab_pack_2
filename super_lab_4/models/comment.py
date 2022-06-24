from sqlalchemy.sql import func

from global_objects import db


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    created = db.Column(db.DateTime(timezone=True),
                        server_default=func.now())
    post_id = db.Column(db.Integer)
    comment = db.Column(db.Text, nullable=False)
