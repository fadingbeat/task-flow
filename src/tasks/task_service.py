from tasks.task_factory import TaskFactory
from database.singleton_db import DatabaseConnection

class TaskService:
    def __init__(self):
        self.singleton_db = DatabaseConnection()
        self.task_factory = TaskFactory()

    def create_and_save_tasks(self, task_type, title, description, **kwargs):
        task = self.task_factory.create_task(task_type, title, description, **kwargs)
        self.singleton_db.insert_task(task_type, task.title, task.description)
        return task