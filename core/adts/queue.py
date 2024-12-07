#
# Author: Rohtash Lakra
#
from collections import deque
from heapq import heappop, heappush
from typing import Any

from core.enums import Priority


class Queue:
    """
    https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics)
    https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
    """

    def __init__(self, items: list[Any] = None):
        self._items = deque(items) if items else deque()

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item

    def enqueue(self, item: Any):
        self._items.append(item)

    def dequeue(self):
        return self._items.popleft()


class Deque(Queue):
    pass


class PriorityQueue:

    def __init__(self):
        self._items = []

    def enqueue(self, priority: Priority, item):
        heappush(self._items, (-priority.value, item))

    def dequeue(self):
        return heappop(self._items)[1]
