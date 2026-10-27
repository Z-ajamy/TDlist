# src/presentation/api/views/task_view.py
from flask import Blueprint, request, jsonify
from flask.views import MethodView
from pydantic import ValidationError

from application.task.create_task import CreateTaskUseCase
from presentation.api.schemas.task.create_task import CreateTaskSchema

task_bp = Blueprint("tasks", __name__, url_prefix="/api/v1/tasks")

class TaskAPI(MethodView):
    def __init__(self, create_task_use_case: CreateTaskUseCase):
        self.create_use_case = create_task_use_case

    def post(self):
        json_data = request.get_json()
        if not json_data:
            return jsonify({"error": "Missing JSON payload"}), 400

        try:
            schema = CreateTaskSchema.model_validate(json_data)
            
            dto = schema.to_dto()
            task_id = self.create_use_case.execute(dto)
            
            return jsonify({
                "message": "Task created successfully",
                "data": {"task_id": task_id}
            }), 201
            
        except ValidationError as e:
            return jsonify({
                "error": "Validation failed",
                "details": e.errors()
            }), 422
