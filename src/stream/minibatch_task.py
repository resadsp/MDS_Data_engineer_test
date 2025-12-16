from core.task import Task

class MiniBatchTask(Task):
    def __init__(self, batch):
        self.batch = batch
        self.messages = batch.messages

    def execute(self):
        print(f"[MiniBatchTask] Processing batch of {len(self.batch)} messages")

    def __repr__(self):
        return f"MiniBatchTask({len(self.batch)} messages)"
