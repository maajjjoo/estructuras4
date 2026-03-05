class FailedTransactionsArray:

    def __init__(self, size=5):
        self.size = size
        self.transactions = []

    def addFailedTransaction(self, transaction):

        if len(self.transactions) >= self.size:
            self.transactions.pop(0)

        self.transactions.append(transaction)

    def getFailedTransactions(self):
        return self.transactions