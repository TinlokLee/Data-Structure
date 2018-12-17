import heapq

class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item(object):
    def __init__(self, name):
        self.name = name 

    def __repr__(self):
        return "Item: {!r}".format(self.name)

if __name__ == "__mian__":
    q = PriorityQueue()
    q.push(Item('foo'), 5)
    q.push(Item('bar'), 1)
    q.push(Item('spam'), 3)
    q.push(Item('gork'), 4)
    for i in range(4):
        print(q._queue)
        print(q.pop())
        