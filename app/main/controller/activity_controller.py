from flask import request, session, make_response, render_template
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import AdminDto
from typing import Dict, Tuple

api = AdminDto.api


@api.route('/activity')
class UserList(Resource):
    @api.doc('admin page')
    @admin_token_required
    # @api.marshal_list_with(_user, envelope='data')
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('admin/activation.html'),200,headers)



