from sqlalchemy import ForeignKey
from sqlalchemy.sql import func

from global_objects import db
from models.photo import Photo
from models.helpers.photos import get_path_to_photo


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime(timezone=True),
                        server_default=func.now())
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    photo_id = db.Column(db.Integer, ForeignKey("photos.id"))


def db_get_post_with_photo_src(id):
    query = db.session.query(Post, Photo)
    query = query.outerjoin(Photo, Post.photo_id == Photo.id)
    post_with_photo = query.filter(Post.id == id).first()

    if post_with_photo is None:
        return

    post, photo = post_with_photo

    if photo is None:
        return post

    if photo.path is not None:
        post.photo_src = get_path_to_photo(photo.path)
    else:
        post.photo_src = None

    return post


def db_get_post(id):
    return Post.query.filter_by(id=id).first()


def db_get_all_posts_with_photo_srcs():
    query = db.session.query(Post, Photo)
    query = query.outerjoin(Photo, Post.photo_id == Photo.id)
    posts_with_photos = query.all()

    posts = []
    for pair in posts_with_photos:
        post, photo = pair

        if photo is None:
            posts.append(post)
            continue

        if photo.path is not None:
            post.photo_src = get_path_to_photo(photo.path)
        else:
            post.photo_src = None

        posts.append(post)

    return posts


def db_get_all_posts():
    return Post.query.all()


def db_create_post(post_fields):
    post = Post(title=post_fields['title'],
                content=post_fields['content'],
                photo_id=post_fields['photo_id'])
    db.session.add(post)
    db.session.commit()


def db_update_post(id, post_fields):
    post = Post.query.filter_by(id=id).first()
    post.title = post_fields['title']
    post.content = post_fields['content']

    db.session.add(post)
    db.session.commit()


def db_delete_post(id):
    post = Post.query.filter_by(id=id).first()
    db.session.delete(post)
    db.session.commit()
