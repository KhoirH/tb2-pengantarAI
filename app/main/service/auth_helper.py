from app.main.model.admin import Admin
from ..service.blacklist_service import save_token
from typing import Dict, Tuple


class Auth:

    @staticmethod
    def login_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        try:
            # fetch the user data
            user = Admin.query.filter_by(username=data.get('username')).first()
            print(user)
            if user and user.check_password(data.get('password')):
                auth_token = Admin.encode_auth_token(user.id_admin)
                if auth_token:
                    return auth_token
            else:
                return 'error'

        except Exception as e:
            return 'error'

    @staticmethod
    def logout_user(data: str) -> Tuple[Dict[str, str], int]:
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = Admin.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_user(token):
        # get the auth token
        auth_token = token
        if auth_token:
            resp = Admin.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = Admin.query.filter_by(id_admin=resp).first()

                response_object =  {
                    'user_id': user.id_admin,
                    'username': user.username
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401
