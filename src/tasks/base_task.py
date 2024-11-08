class BaseTask:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description

    def execute(self):
        raise NotImplementedError("Subclasses must implement this method")