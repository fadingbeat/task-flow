from .base_task import BaseTask


class ReminderTask(BaseTask):
    def __init__(self, title: str, description: str, remind_time: str ):
        super().__init__(title, description)
        self.remind_time = remind_time

    def execute(self):
        return f"Reminder: {self.title} at {self.remind_time} - {self.description}"
