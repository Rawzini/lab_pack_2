from flask import Blueprint

from controllers.main_controller import index, get_post_page, get_create_post_form, create_post, get_edit_post_form, edit_post, delete_post
from controllers.auth_controller import get_login_form, get_signup_form, login, signup, logout, get_profile_page
from controllers.test_controller import test_comments_model

routes = Blueprint('routes', __name__)

routes.route('/login', methods=['GET'])(get_login_form)
routes.route('/login', methods=['POST'])(login)
routes.route('/signup', methods=['GET'])(get_signup_form)
routes.route('/signup', methods=['POST'])(signup)
routes.route('/logout', methods=['GET'])(logout)
routes.route('/profile', methods=['GET'])(get_profile_page)

routes.route('/', methods=['GET'])(index)
routes.route('/<int:post_id>', methods=['GET'])(get_post_page)
routes.route('/create', methods=['GET'])(get_create_post_form)
routes.route('/create', methods=['POST'])(create_post)
routes.route('/<int:id>/edit', methods=['GET'])(get_edit_post_form)
routes.route('/<int:id>/edit', methods=['POST'])(edit_post)
routes.route('/<int:id>/delete', methods=['POST'])(delete_post)

routes.route('/comtest', methods=['GET'])(test_comments_model)