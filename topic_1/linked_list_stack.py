"""
Program: linked_list_stack
Author: Daniel Meeker
Date: 10/11/2020
OS: Windows 10
IDE: PyCharm

This program demonstrates using a Stack data structure by
implementing it with a linked list. I kept the same driver as the original
stack lab so that I could do side-by-side comparison to make sure
it was working correctly. Python doesn't have a true built-in
linked list library but my reading online suggested that collections.deque
is an appropriate substitute.

Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or
unmodified. I have not given other fellow student(s) access
to my program.
"""
from collections import deque as l_list  # using this as my linked-list


class StackEmptyException(Exception):
    pass


class StackFullException(Exception):
    pass


class Stack:
    def __init__(self, max_size=5):
        self.top = -1  # represents the top of the stack. Gets incremented when items are pushed on the stack
        self.max_size = max_size  # represents how many items can be in the stack
        self.items = l_list()

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1
        # Shows it is full because the top will be at index
        # of 4 which is equal to a max size of 5 due to index
        # counts beginning at 0

    def push(self, item):
        if not self.is_full():
            self.top += 1
            self.items.append(item)  # linked_list method call
        else:
            raise StackFullException("Stack is full")

    def pop(self):
        try:
            self.peek()
            self.top -= 1
            return self.items.pop()  # linked_list method call
        except StackEmptyException:
            raise StackEmptyException("Stack is Empty")

    def peek(self):
        if not self.is_empty():  # If statement necessary otherwise it could not throw an exception
            return self.items[self.top]
        else:
            raise StackEmptyException("Stack is Empty")

    def size(self):
        return len(self.items)  # linked_list method call

    def print_stack_down(self):
        """
        creates a string containing all elements of the stack for printing
        :return: a string
        """
        if not self.is_empty():
            stack_str = ""
            for x in range(self.size())[::-1]:
                stack_str += str(self.items[x]) + "\n"
            return stack_str
        else:
            raise StackEmptyException("Stack is Empty")


if __name__ == '__main__':
    max_num_books = 3
    books = Stack(max_num_books)
    print(books.is_empty())
    try:
        print(books.peek())
    except StackEmptyException as ex:
        print(ex)
    books.push('Name of the Wind')
    books.push('Way of Kings')
    books.push('Red Rising')
    try:
        books.push('The Fifth Season')
    except StackFullException as ex:
        print(ex)
    print(books.peek())
    print(books.size())
    print(books.is_full())
    print(books.print_stack_down())
    print(books.pop())
    print(books.pop())
    print(books.size())
    print(books.pop())
    try:
        print(books.pop())
    except StackEmptyException as ex:
        print(ex)
    books.push('The Fifth Season')
    print(books.peek())
    input("Press Enter to Continue")
