from flask import render_template, url_for, request, flash, redirect, abort

from models.photo import db_create_photo
from models.post import db_get_post, db_get_all_posts_with_photo_srcs, db_create_post, db_update_post, db_delete_post, \
    db_get_post_with_photo_src
from models.helpers.photos import is_allowed_extention, ALLOWED_EXTENSIONS, save_photo_to_disk


def index():
    posts = db_get_all_posts_with_photo_srcs()
    return render_template('index.html', posts=posts)


def get_post_page(post_id):
    post = db_get_post_with_photo_src(post_id)
    if post is None:
        abort(404)

    return render_template('post.html', post=post)


def get_create_post_form():
    return render_template('create.html')


def create_post():
    title = request.form['title']
    content = request.form['content']

    if not title:
        flash('Необходим заголовок!')
        return redirect(url_for('.create_post'))
    if 'file' not in request.files:
        flash('Ошибка при загрузке фото!')
        return redirect(url_for('.create_post'))

    photo = request.files['file']

    if photo.filename == '':
        flash('Необходимо загрузить фотографию!')
        return redirect(url_for('.create_post'))

    if not is_allowed_extention(photo.filename):
        flash('Разрешены только следующие расширения: ' + str(ALLOWED_EXTENSIONS))
        return redirect(url_for('.create_post'))

    photo_path = save_photo_to_disk(photo)
    photo_id = db_create_photo({
        'filename': photo.filename,
        'path': photo_path
    })

    db_create_post({
        'title': title,
        'content': content,
        'photo_id': photo_id
    })

    return redirect(url_for('.index'))


def get_edit_post_form(id):
    post = db_get_post(id)
    if post is None:
        abort(404)

    return render_template('edit.html', post=post)


def edit_post(id):
    title = request.form['title']
    content = request.form['content']

    if not title:
        flash('Необходим заголовок!')
    else:
        db_update_post(id, {
            'title': title,
            'content': content
        })
        return redirect(url_for('.index'))


def delete_post(id):
    post = db_get_post(id)
    if post is None:
        abort(404)

    db_delete_post(id)
    flash('"{}" был успешно удален!'.format(post.title))

    return redirect(url_for('.index'))
