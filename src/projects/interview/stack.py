
#!/usr/bin/env python3
"""
stack implementation

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
   
   
    def push(self, item: Any) -> None:
        count = 0
        """
        Add a new item to stack

        :param item: a new item to push onto the stack
        """
        heapq.heappush(self.items,(count,item))
        count = count + 1

    def pop(self) -> Any:
        """
        Remove an item from the stack

        :return: the top element of the stack
        :raise StackError is the stack is empty
        """
        return heapq.heappop(self.items)

    def peek(self) -> Any:
        """
        Look at the top item without removing it

        :return: the top element of the stack
        :raise StackError is the stack is empty
        """
        
        
        element = self.items[0]
        return element


    def __bool__(self) -> bool:
        """
        Evaluate the stack

        :return: False if the stack is empty, True otherwise
        """
        value = True
        if len(self.items)==0:
            value = False
        return value

    def __len__(self) -> int:
        """
        Return the number of items in the stack

        :return: number of items in the stack (0 if the stack is empty)
        """
        return len(self.items)==1