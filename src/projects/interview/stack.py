#!/usr/bin/env python3
"""
`stack` implementation

@authors: Roman Yasinovskyy
@version: 2021.11
"""

import heapq
from typing import Any


class StackError(Exception):
    """Stack errors"""

    def __init__(self, *args, **kwargs):
        """Initializer"""
        Exception.__init__(self, *args, **kwargs)


class Stack:
    """
    LIFO data structure

    Items are added and removed at the same end of the collection
    """

    def __init__(self):
        """Initialize a stack using heapq"""
        # NOTE: Do not modify this method
        self.items = []
    
    def siftdown(heap, startpos, pos):
        newitem = heap[pos]
        # Follow the path to the root, moving parents down until finding a place
        # newitem fits.
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = heap[parentpos]
            if newitem < parent:
                heap[pos] = parent
                pos = parentpos
                continue
            break
        heap[pos] = newitem

    def siftup(heap, pos):
        endpos = len(heap)
        startpos = pos
        newitem = heap[pos]
       
        childpos = 2*pos + 1    
        while childpos < endpos:
            
            rightpos = childpos + 1
            if rightpos < endpos and not heap[childpos] < heap[rightpos]:
                childpos = rightpos
           
            heap[pos] = heap[childpos]
            pos = childpos
            childpos = 2*pos + 1
        
        heap[pos] = newitem
        heap.siftdown( startpos, pos)

    def push(self, item: Any) -> None:
        """
        Add a new item to stack

        :param item: a new item to push onto the stack
        """
        # TODO: Implement this method
        self.items.append(item)
        self.siftdown( 0, len(self.items)-1)


    def pop(self) -> Any:
        """
        Remove an item from the stack

        :return: the top element of the stack
        :raise StackError is the stack is empty
        """
        # TODO: Implement this method
        self.items.pop()
        """Pop the smallest item off the heap, maintaining the heap invariant."""
        heap = self.items
        lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
        if heap:
            returnitem = heap[0]
            heap[0] = lastelt
            self.siftup( 0)
            return returnitem
        return lastelt


    def peek(self) -> Any:
        """
        Look at the top item without removing it

        :return: the top element of the stack
        :raise StackError is the stack is empty
        """
        # TODO: Implement this method
        return self.items[0]


    def __bool__(self) -> bool:
        """
        Evaluate the stack

        :return: False if the stack is empty, True otherwise
        """
        # TODO: Implement this method
        value = True
        if len(self.items)==0:
            value = False
        return value


    def __len__(self) -> int:
        """
        Return the number of items in the stack

        :return: number of items in the stack (0 if the stack is empty)
        """
        # TODO: Implement this method
        return len(self.items)==0

