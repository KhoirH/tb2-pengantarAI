from flask import request, render_template, make_response, Response, flash, redirect
from flask_restx import Resource
from app.main.service.scan_service import generate_frames
from app.main.service.employee_service import get_all_employee
from app.main.service.activity_service import insert_activity
from app.main.service.category_service import status_category
from ..util.dto import ScanDto

api = ScanDto.api


@api.route('/')
class ScanView(Resource):
    def get(self):
        print(status_category())
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('videostream.html'),200,headers)

@api.route('/video')
class VideoView(Resource):
    def get(self): 
        employee = get_all_employee()
        a = generate_frames(employee)
        return Response(a, mimetype='multipart/x-mixed-replace; boundary=frame')
        

@api.route('/process-scan')
class BeforeScanView(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        status = insert_activity(request)
        message = "anda berhasil melakukan " + status
        if status == 'late':
            message = "Anda telat"
        return make_response(render_template('starting.html', message = message ),200,headers)
