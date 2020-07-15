"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# QUEUE IMPLEMENTATION WITH PYTHON LISTS
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.append(None)

        # shift all of the storage:
        for i in range(len(self.storage)-1, 0, -1):
            self.storage[i] = self.storage[i-1]

        self.storage[0] = value
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            return_value = self.storage[-1]
            del self.storage[-1]
            self.size -= 1
            return return_value


# QUEUE IMPLEMENTATION WITH SINGLY LINKED LIST
# import sys
# sys.path.append("..")

# from singly_linked_list.singly_linked_list import LinkedList


# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.add_to_tail(value)
#         self.size += 1

#     def dequeue(self):
#         return_value = self.storage.remove_head()
#         if return_value != None:
#             self.size -= 1
#         return return_value


# QUEUE IMPLEMENTATION WITH 2 STACK
import sys
sys.path.append("..")
from stack.stack import Stack

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = Stack()
        self.temp_storage = Stack()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.push(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None

        for i in range(self.size-1):
            self.temp_storage.push(self.storage.pop())
        
        return_value = self.storage.pop()
        
        for i in range(self.size-1):
            self.storage.push(self.temp_storage.pop())

        self.size -= 1
        
        return return_value
