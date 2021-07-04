from flask import request, session, make_response, render_template, redirect
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import AdminDto
from app.main.service.employee_service import insert_employee, get_all_employee
from typing import Dict, Tuple

api = AdminDto.api

@api.route('/employee')
class EmployeeView(Resource):
    @api.doc('admin page')
    @admin_token_required
    # @api.marshal_list_with(_user, envelope='data')
    def get(self):
        headers = {'Content-Type': 'text/html'}
        data = get_all_employee()
        return make_response(render_template('admin/employee.html', employees = data),200,headers)

@api.route('/employee-create')
class EmployeeCreate(Resource):
    @api.doc('admin created')
    @admin_token_required
    def post(self):
        insert_employee(request)
        return redirect('employee')