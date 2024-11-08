from .reminder_task import ReminderTask
from .limit_task import LimitTask
from .recurring_task import RecurringTask

class TaskFactory:
    @staticmethod
    def create_task(task_type: str, title: str, description: str, **kwargs):
        if task_type == "reminder":
            return ReminderTask(title, description, kwargs.get('remind_time'))
        elif task_type == "limit":
            return LimitTask(title, description, kwargs.get('limit'))
        elif task_type == "recurring":
            return RecurringTask(title, description, kwargs.get('frequency'))
        else:
            raise ValueError(f"Unknown task type: {task_type}")
