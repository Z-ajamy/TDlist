from flask import Flask
from presentation.api.views.task_view import task_bp, TaskAPI
from presentation.api.dependencies import container

def create_app() -> Flask:
    app = Flask(__name__)

    create_task_use_case = container.get_create_task_use_case()

    task_view = TaskAPI.as_view(
        "task_api", 
        create_task_use_case=create_task_use_case
    )

    task_bp.add_url_rule("/", view_func=task_view, methods=["POST"])

    app.register_blueprint(task_bp)


    return app
