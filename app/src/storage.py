# Armazenamento na memória

tasks = []

def create_task(title):
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "done": False
    }
    tasks.append(task)
    return task

def list_tasks():
    return tasks

def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return task
    return None