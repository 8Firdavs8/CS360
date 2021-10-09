#!/usr/bin/env python3
"""Binary Heap implementation"""


from heapq import heappop


class BinaryHeapMax:
    """Heap class implementation"""

    def __init__(self):
        """Initializer"""
        self._heap = []
        self._size = 0

    def _perc_up(self, cur_idx):

        """Move a node up"""
        while cur_idx // 2 > 0:
            if self._heap[cur_idx] < self._heap[cur_idx // 2]:
                tmp = self._heap[cur_idx // 2]
                self._heap[cur_idx // 2] = self._heap[cur_idx]
                self._heap[cur_idx] = tmp
            cur_idx = cur_idx // 2
        return cur_idx

    def _perc_down(self, cur_idx):
        """Move a node down"""
        
    def insert(self, item):
        """Add a new item. Optional for this exercise"""
        pass

    def delete(self):
        """Remove an item from the heap. Optional for this exercise"""
        pass

    def heapify(self, not_a_heap):
        """Turn a list into a heap"""
        raise NotImplementedError

    def get_max_child(self, parent_idx):
        """Get the greater child"""
        negMax = heappop(parent_idx)
        maxItem = (-negMax[0], -negMax[1])
        return maxItem

    def __len__(self):
        """Get heap size"""
        return self._size

    def __str__(self):
        """Heap as a string """
        return str(self._heap)
