from flask import jsonify, request, render_template
from storage import create_task, list_tasks, complete_task
from metrics import REQUEST_COUNT
from prometheus_client import generate_latest

import time

def register_routes(app):

    @app.before_request
    def before_request():
        REQUEST_COUNT.inc()

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    @app.route("/tasks", methods=["POST"])
    def create():
        data = request.json
        if not data or "title" not in data:
            return jsonify({"error": "Title is required"}), 400

        task = create_task(data["title"])
        return jsonify(task), 201

    @app.route("/tasks", methods=["GET"])
    def list_all():
        return jsonify(list_tasks()), 200

    @app.route("/tasks/<int:task_id>", methods=["PUT"])
    def complete(task_id):
        task = complete_task(task_id)
        if not task:
            return jsonify({"error": "Task not found"}), 404
        return jsonify(task), 200

    # endpoint pra simular erro
    @app.route("/fail")
    def fail():
        return jsonify({"error": "simulated failure"}), 500

    # latência
    @app.route("/slow")
    def slow():
        time.sleep(3)
        return jsonify({"message": "slow response"}), 200

    # métricas
    @app.route("/metrics")
    def metrics():
        return generate_latest(), 200

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Route not found"}), 404