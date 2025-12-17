from core.task import Task

class MiniBatchTask(Task):
    def __init__(self, batch):
        self.batch = batch
        self.messages = batch.messages

    def execute(self):
        pass
