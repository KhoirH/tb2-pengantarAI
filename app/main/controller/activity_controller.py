from flask import request, session, make_response, render_template
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import AdminDto
from typing import Dict, Tuple
from app.main.service.activity_service import get_all_activity
api = AdminDto.api


@api.route('/activity')
class ActivityView(Resource):
    @api.doc('admin page')
    @admin_token_required
    # @api.marshal_list_with(_user, envelope='data')
    def get(self):
        headers = {'Content-Type': 'text/html'}
        data = get_all_activity()
        return make_response(render_template('admin/activation.html', activities = data),200,headers)



