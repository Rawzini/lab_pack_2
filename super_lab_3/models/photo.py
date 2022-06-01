from sqlalchemy.sql import func

from models.basic import db


class Photo(db.Model):
    __tablename__ = 'photos'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime(timezone=True),
                        server_default=func.now())
    filename = db.Column(db.Text, nullable=False)
    path = db.Column(db.Text, nullable=False)

def db_create_photo(photo):
    photo = Photo(filename=photo['filename'],
                  path=photo['path'])
    db.session.add(photo)
    db.session.commit()
    db.session.refresh(photo)

    return photo.id


def get_photo(id):
    return Photo.query.filter_by(id=id).first()
