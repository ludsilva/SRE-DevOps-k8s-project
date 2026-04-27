# storage.py

import redis
import os
import json

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

TASKS_KEY = "tasks"
TASK_ID_KEY = "task_id"


def create_task(title):
    task_id = r.incr(TASK_ID_KEY)

    task = {
        "id": task_id,
        "title": title,
        "done": False
    }

    r.hset(TASKS_KEY, task_id, json.dumps(task))
    return task


def list_tasks():
    tasks = r.hgetall(TASKS_KEY)
    return [json.loads(task) for task in tasks.values()]


def complete_task(task_id):
    task = r.hget(TASKS_KEY, task_id)

    if not task:
        return None

    task = json.loads(task)
    task["done"] = True

    r.hset(TASKS_KEY, task_id, json.dumps(task))
    return task