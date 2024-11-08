from .base_task import BaseTask


class LimitTask(BaseTask):
    def __init__(self, title: str, description: str, limit: str):
        super().__init__(title, description)
        self.limit = limit

    def execute(self):
        return f"The limit execution for {self.title} is {self.limit} - {self.description} "