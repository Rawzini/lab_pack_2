from flask import render_template

# from models.comment import Comment

def test_comments_model():
    comments = []
    #comments = Comment.query.all()
    return render_template('test.html', comments=comments)