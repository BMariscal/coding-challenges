class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # {message, timestamp}
        self.log = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        logged = self.log.get(message, None)
        if logged == None:
            self.log[message] = timestamp
            return True
        elif logged != None and timestamp >= (logged + 10):
            self.log[message] = timestamp
            return True
        return False




        # Your Logger object will be instantiated and called as such:
        # obj = Logger()
        # param_1 = obj.shouldPrintMessage(timestamp,message)