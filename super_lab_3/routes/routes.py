from flask import Blueprint

from controllers.main_controller import index, get_post_page, get_create_post_form, create_post, get_edit_post_form, edit_post, delete_post
from controllers.test_controller import test_comments_model

routes = Blueprint('routes', __name__)

routes.route('/', methods=['GET'])(index)
routes.route('/<int:post_id>', methods=['GET'])(get_post_page)
routes.route('/create', methods=['GET'])(get_create_post_form)
routes.route('/create', methods=['POST'])(create_post)
routes.route('/<int:id>/edit', methods=['GET'])(get_edit_post_form)
routes.route('/<int:id>/edit', methods=['POST'])(edit_post)
routes.route('/<int:id>/delete', methods=['POST'])(delete_post)

routes.route('/comtest', methods=['GET'])(test_comments_model)