from flask_restx import Namespace, fields


class AdminDto:
    api = Namespace('admin', description='admin page')

class ScanDto:
    api = Namespace('scan', description='scan page')
