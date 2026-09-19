class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = collections.deque() #cap at length size
        self.summ = 0
        self.queue_size = 0  

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.summ += val
        self.queue_size += 1
        if len(self.queue) > self.size:
            value = self.queue.popleft()
            self.summ -= value
            return self.summ / self.size
        else:
            return self.summ / self.queue_size
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
