import random

from structures.queue import TransactionQueue
from structures.stack import CompensationStack
from structures.failedTransactionsArray import FailedTransactionsArray


class TicketTransactionEngine:

    def __init__(self):

        self.queue = TransactionQueue()
        self.stack = CompensationStack()
        self.failedTransactions = FailedTransactionsArray()

        self.customer_id = 100

    def generatePurchaseRequest(self):

        self.customer_id += 1

        tickets = random.randint(1, 3)

        transaction = f"Customer {self.customer_id} - {tickets} tickets"

        self.queue.enqueue(transaction)

    def processTransaction(self):

        if self.queue.isEmpty():
            return "No transactions in queue"

        transaction = self.queue.dequeue()

        try:

            self.stack.push("reserve seats")
            self.stack.push("validate payment")
            self.stack.push("confirm purchase")

            if random.random() < 0.4:
                raise Exception("Payment failed")

            self.stack.clear()

            return f"SUCCESS: {transaction}"

        except:

            rollbackSteps = []

            while not self.stack.isEmpty():
                rollbackSteps.append(self.stack.pop())

            self.failedTransactions.addFailedTransaction(transaction)

            return f"FAILED: {transaction}"

    def getQueue(self):
        return self.queue.getQueue()

    def getFailedTransactions(self):
        return self.failedTransactions.getFailedTransactions()