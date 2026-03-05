class CompensationStack:

    def __init__(self):
        self.stack = []

    def push(self, step):
        self.stack.append(step)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack = []