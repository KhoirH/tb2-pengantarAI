from flask import request, session, make_response, render_template
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import AdminDto
from app.main.service.category_service import get_all_category
# from ..service.user_service import save_new_user, get_all_users, get_a_user
from typing import Dict, Tuple

api = AdminDto.api


@api.route('/category')
class CategoryView(Resource):
    @api.doc('admin page')
    @admin_token_required
    # @api.marshal_list_with(_user, envelope='data')
    def get(self):
        headers = {'Content-Type': 'text/html'}
        data = get_all_category()
        return make_response(render_template('admin/category.html', categories = data),200,headers)



