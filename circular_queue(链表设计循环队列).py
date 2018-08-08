# coding：utf-8


class Empty(Exception):
    pass

class LinkedStack:
    """ LIFO Stack implementation using a singly linked list for storage"""

    # -------------nested _Node class ______________

    class _Node:
        """ Lightweight, nopublic class for storing a singly linked node"""

        __slots__ = '_element', '_next'  # streamlinge memory usage

        def __init__(self, element, next):
            self._element = element

            self._next = next
    # -----------stack methods-----------------

    def __init__(self):

        """ Create an empty stack """
        self._head = None
        self._size = 0

    def __len__(self):
        """ Return the number of elements in the stack"""
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        #node  = self._Node(e, self._head)
        #node._next = self._head
        #self._head = node
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


if __name__ == '__main__':
    s = LinkedStack()
    s.push('kang ff ')
    s.push('fffff')
    print(s.pop())
    print(s.top())










