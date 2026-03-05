class TransactionQueue:

    def __init__(self):
        self.queue = []

    def enqueue(self, transaction):
        self.queue.append(transaction)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def getQueue(self):
        return self.queue
    
