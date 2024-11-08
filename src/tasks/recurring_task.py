from .base_task import BaseTask

class RecurringTask(BaseTask):
    def __init__(self, title: str, description: str, frequency: str):
        super().__init__(title, description)
        self.frequency = frequency

    def execute(self):
        return f"Recurring Task: {self.title} every {self.frequency} - {self.description}"
