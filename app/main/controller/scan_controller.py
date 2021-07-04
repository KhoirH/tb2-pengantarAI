from flask import request, render_template, make_response, Response
from flask_restx import Resource
from app.main.service.scan_service import generate_frames
from app.main.service.employee_service import get_all_employee
from ..util.dto import ScanDto

api = ScanDto.api


@api.route('/')
class ScanView(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('videostream.html'),200,headers)



@api.route('/video')
class VideoView(Resource):
    def get(self): 
        data = get_all_employee()
        return Response(generate_frames(data), mimetype='multipart/x-mixed-replace; boundary=frame')

