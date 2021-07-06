from flask import  Blueprint,request, render_template, abort, make_response, redirect, session
from flask_restx import Resource
from jinja2 import TemplateNotFound

from app.main.service.auth_helper import Auth
from ..util.dto import AdminDto
from typing import Dict, Tuple

api = AdminDto.api
# user_auth = AdminDto.user_auth


@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    def get(self):
        headers = {'Content-Type': 'text/html'}
        if session.get('token') :
            return redirect('activity')

        return make_response(render_template('admin/login.html'),200,headers)

    # @api.expect(user_auth, validate=True)
    def post(self) -> Tuple[Dict[str, str], int]:
        # get the post data
        post_data = request.form
        
        token = Auth.login_user(data=post_data)
        if token != 'error' :
            print(token)
            session['token'] = token; 

        return redirect('login')


@api.route('/logout')
class Logout(Resource):
    """
    Logout Resource
    """
    # @api.doc('logout a user')
    def get(self):
        session.pop('token', None)
        return redirect('/admin/login')
