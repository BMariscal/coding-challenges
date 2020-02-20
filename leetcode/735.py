class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].update({timestamp: value})
        else:
            self.store[key] = {timestamp: value}

    def get(self, key: str, timestamp: int) -> str:
        storage_values = self.store.get(key)
        if storage_values:
            while timestamp > 0:
                if timestamp in storage_values:
                    return storage_values[timestamp]
                timestamp -= 1
        return ""




        # Your TimeMap object will be instantiated and called as such:
        # obj = TimeMap()
        # obj.set(key,value,timestamp)
        # param_2 = obj.get(key,timestamp)