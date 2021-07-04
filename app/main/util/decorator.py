from functools import wraps

from flask import request, session, redirect

from app.main.service.auth_helper import Auth
from typing import Callable


def token_required(f) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        return f(*args, **kwargs)

    return decorated


def admin_token_required(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        
        token_session = session.get('token')
        data, status = Auth.get_logged_in_user(token_session)
        token = data
        
        if not token:
            return redirect('admin/login')

        admin = token.get('username')
        if not admin:
            return redirect('admin/login')

        return f(*args, **kwargs)

    return decorated
