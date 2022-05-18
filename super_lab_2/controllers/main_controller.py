from flask import render_template, url_for, request, flash, redirect, abort

from models.posts import get_post, get_all_posts

# Этот импорт надо будет удалить
from models.basic_functions import get_db_connection


def index():
    posts = get_all_posts()
    return render_template('index.html', posts=posts)


def get_post_page(post_id):
    post = get_post(post_id)
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
    else:
        # Этот код нужно перенести в модель posts, создать для него функцию create_post
        conn = get_db_connection()
        conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                     (title, content))
        conn.commit()
        conn.close()
        # конец переносимого куска
        return redirect(url_for('.index'))


def get_edit_post_form(id):
    post = get_post(id)
    if post is None:
        abort(404)

    return render_template('edit.html', post=post)


def edit_post(id):
    title = request.form['title']
    content = request.form['content']

    if not title:
        flash('Необходим заголовок!')
    else:
        # Этот код нужно перенести в модель posts, создать для него функцию update_post
        conn = get_db_connection()
        conn.execute('UPDATE posts SET title = ?, content = ?'
                     ' WHERE id = ?',
                     (title, content, id))
        conn.commit()
        conn.close()
        # конец переносимого куска
        return redirect(url_for('.index'))


def delete_post(id):
    post = get_post(id)
    if post is None:
        abort(404)

    # Этот код нужно перенести в модель posts, создать для него функцию delete_post
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    # конец переносимого куска
    flash('"{}" был успешно удален!'.format(post['title']))

    return redirect(url_for('.index'))
