from flask import Blueprint

from controllers.main_controller import index, get_post_page, get_create_post_form, create_post, get_edit_post_form, edit_post, delete_post

post_bp = Blueprint('post_bp', __name__)

post_bp.route('/', methods=['GET'])(index)
post_bp.route('/<int:post_id>', methods=['GET'])(get_post_page)
post_bp.route('/create', methods=['GET'])(get_create_post_form)
post_bp.route('/create', methods=['POST'])(create_post)
post_bp.route('/<int:id>/edit', methods=['GET'])(get_edit_post_form)
post_bp.route('/<int:id>/edit', methods=['POST'])(edit_post)
post_bp.route('/<int:id>/delete', methods=['POST'])(delete_post)
