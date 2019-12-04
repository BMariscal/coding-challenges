from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()  # use ordereddict to implement a queue/FIFO

    @property
    def is_at_capacity(self):
        return len(self.cache) > self.capacity

    def get(self, key: int) -> int:
        try:
            self.cache.move_to_end(key)  # move item to end
        except KeyError:
            return -1
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)  # move new item to end

        if self.is_at_capacity:
            self.cache.popitem(last=False)  # pop first item in dict