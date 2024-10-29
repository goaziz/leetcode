class Logger:

    def __init__(self):
        self.hash_table = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        if message not in self.hash_table:
            self.hash_table[message] = timestamp
            return True

        last_time = self.hash_table[message]
        if last_time + 10 <= timestamp:
            self.hash_table[message] = timestamp
            return True
        else:
            return False


logger = Logger()
logger.shouldPrintMessage(1, "foo")
logger.shouldPrintMessage(2, "bar")
logger.shouldPrintMessage(3, "foo")
logger.shouldPrintMessage(8, "bar")
logger.shouldPrintMessage(10, "foo")
logger.shouldPrintMessage(11, "foo")
