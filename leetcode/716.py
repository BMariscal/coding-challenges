class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return max(self.stack)

    def popMax(self) -> int:
        max_int = self.peekMax()
        self.stack.reverse()

        del self.stack[self.stack.index(max_int)]
        self.stack.reverse()
        return max_int


        # Your MaxStack object will be instantiated and called as such:
        # obj = MaxStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.peekMax()
        # param_5 = obj.popMax()


from heapq import heappush, heappop

class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.hp = []
        self.id = 0
        self.stack_del = set()
        self.hp_del = set()

    def push(self, x: int) -> None:
        self.stack.append((self.id, x))
        heappush(self.hp, (-x, -self.id))
        self.id += 1

    def pop(self) -> int:
        top = self.top()
        id = self.stack[-1][0]
        self.hp_del.add(id)
        return self.stack.pop()[1]

    def top(self) -> int:
        while self.stack[-1][0] in self.stack_del:
            self.stack.pop()
        return self.stack[-1][1]

    def peekMax(self) -> int:
        while -self.hp[0][1] in self.hp_del:
            heappop(self.hp)
        return -self.hp[0][0]

    def popMax(self) -> int:
        val = self.peekMax()
        val, id = -self.hp[0][0], -self.hp[0][1]
        self.stack_del.add(id)
        return -heappop(self.hp)[0]


        # Your MaxStack object will be instantiated and called as such:
        # obj = MaxStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.peekMax()
        # param_5 = obj.popMax()