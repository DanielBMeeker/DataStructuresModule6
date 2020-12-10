"""
Program: linked_list_queue.py
Author: Daniel Meeker
Date: 10/11/2020

This program demonstrates creating a queue in Python with a linked list

I am using the same driver as the Queue lab so that I can do a side by side
comparison and make sure that it is working as expected.

Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or
unmodified. I have not given other fellow student(s) access
to my program.
"""
from collections import deque as l_list  # using this as my linked-list


class QueueEmptyException(Exception):
    pass


class QueueFullException(Exception):
    pass


class Queue:
    def __init__(self, max_size=5):
        self.head = 0
        self.queue_size = 0
        self.max_size = max_size  # used to limit size of Queue. Defaults to 5.
        self.items = l_list(maxlen=self.max_size)

    def is_empty(self):
        """
        If there are no elements in the queue this will return true,
        otherwise it will return false
        :return: boolean
        """
        return self.size() == 0

    def is_full(self):
        """
        If the number of elements in the queue are equal to its self.max_size
        this will return true, otherwise it will return false.
        :return:
        """
        return self.size() == self.max_size

    def enqueue(self, item):
        """
        This function will take an item and add it to the end of the queue
        :param item: required
        :return: void
        """
        if not self.is_full():
            self.items.append(item)  # linked_list method call
        else:
            raise QueueFullException("Queue is Full")

    def dequeue(self):
        """
        This function will remove and return the item from the front of the queue
        :return: first item of whatever data type is in the list
        """
        try:
            self.peek()
            return self.items.popleft()  # linked_list method call
        except QueueEmptyException:
            raise QueueEmptyException("Queue is Empty")

    def peek(self):
        if not self.is_empty():
            item_str = self.items[self.head]
            return item_str
        else:
            raise QueueEmptyException("Queue is Empty")

    def size(self):
        self.queue_size = len(self.items)  # deque supports len(object)
        return self.queue_size

    def print_queue(self):
        if not self.is_empty():
            stack_str = ""
            for x in range(self.size()):
                stack_str += str(self.items[x]) + "\n"
            return stack_str
        else:
            raise QueueEmptyException("Queue is Empty")


if __name__ == '__main__':
    max_size = 3
    queue = Queue(max_size)
    queue.enqueue("Sam")
    queue.enqueue("Jacen")
    queue.enqueue("Daniel")
    print(queue.print_queue())
    try:
        queue.enqueue("Michelle")
    except QueueFullException as qf:
        print(qf)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    try:
        print(queue.print_queue())
    except QueueEmptyException as qe:
        print(qe)
    queue.enqueue("Michelle")
    print(queue.print_queue())
    print(queue.is_empty())
    print(queue.dequeue())
    print(queue.is_empty())
    try:
        print(queue.dequeue())
    except QueueEmptyException as qe:
        print(qe)
    input("Press Enter to End")
