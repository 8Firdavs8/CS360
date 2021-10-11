#!/usr/bin/env python3
"""Binary Heap implementation"""


<<<<<<< HEAD
from heapq import heappop
=======
from typing import Any
>>>>>>> c648aa77121700ab02735dc28bbec4270eace7ae


class BinaryHeapMax:
    """Heap class implementation"""

    def __init__(self):
        """Initializer"""
        self._heap = []
        self._size = 0

<<<<<<< HEAD
    def _perc_up(self, cur_idx):

        """Move a node up"""
        while cur_idx // 2 > 0:
            if self._heap[cur_idx] < self._heap[cur_idx // 2]:
                tmp = self._heap[cur_idx // 2]
                self._heap[cur_idx // 2] = self._heap[cur_idx]
                self._heap[cur_idx] = tmp
            cur_idx = cur_idx // 2
        return cur_idx
=======
    def _perc_up(self, cur_idx: int) -> None:
        """Move a node up"""
        # TODO: Implement this function
        ...
>>>>>>> c648aa77121700ab02735dc28bbec4270eace7ae

    def _perc_down(self, cur_idx: int) -> None:
        """Move a node down"""
<<<<<<< HEAD
        
    def insert(self, item):
        """Add a new item. Optional for this exercise"""
        pass
=======
        # TODO: Implement this function
        ...

    def add(self, item: Any) -> None:
        """Add a new item"""
        # TODO: Implement this function
        ...
>>>>>>> c648aa77121700ab02735dc28bbec4270eace7ae

    def remove(self) -> Any:
        """Remove an item from the heap"""
        # TODO: Implement this function
        ...

    def heapify(self, not_a_heap: list) -> None:
        """Turn a list into a heap"""
        # TODO: Implement this function
        ...

<<<<<<< HEAD
    def get_max_child(self, parent_idx):
        """Get the greater child"""
        negMax = heappop(parent_idx)
        maxItem = (-negMax[0], -negMax[1])
        return maxItem
=======
    def _get_max_child(self, parent_idx: int) -> int:
        """Get index of the greater child"""
        # TODO: Implement this function
        ...
>>>>>>> c648aa77121700ab02735dc28bbec4270eace7ae

    def __len__(self) -> int:
        """Get heap size"""
        return self._size

    def __str__(self) -> str:
        """Heap as a string """
        return str(self._heap)
