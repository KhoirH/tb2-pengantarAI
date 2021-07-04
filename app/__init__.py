from flask_restx import Api
from flask import Blueprint

from .main.controller.auth_controller import api as auth_ns
from .main.controller.category_controller import api as category_ns
from .main.controller.daliy_activation_controller import api as daliy_activation_ns
from .main.controller.employee_controller import api as employee_ns
from .main.controller.activity_controller import api as activity_ns

blueprint = Blueprint('web', __name__)
staticBlueprint = Blueprint('css', __name__, static_folder='static', static_url_path='/static')

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    blueprint,
    title='FLASK RESTPLUS(RESTX) API BOILER-PLATE WITH JWT',
    version='1.0',
    description='a boilerplate for flask restplus (restx) web service',
    authorizations=authorizations,
    security='apikey'
)

api.add_namespace(auth_ns)
api.add_namespace(activity_ns)
api.add_namespace(daliy_activation_ns)
api.add_namespace(employee_ns)
api.add_namespace(category_ns)

