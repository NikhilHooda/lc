class MovingAverage:

    def __init__(self, size: int):
        self.queue = collections.deque()
        self.summ = 0
        self.q_size = 0
        self.size = size


    def next(self, val: int) -> float:
        self.queue.append(val)
        self.q_size += 1
        self.summ += val
        if self.q_size > self.size:
            value = self.queue.popleft()
            self.q_size -= 1
            self.summ -= value
            return self.summ / self.size
        else:
            return self.summ / self.q_size

