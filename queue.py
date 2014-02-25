# a queue, by me for yueue!


class QueueNode(object):
    def __init__(self, value, previous=None, next=None):
        self.value = value
        self.previous = previous
        self.next = next

class Queue(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.length = 0

    def enqueue(self, value):
        if self.head:
            old_tail = self.tail
            self.tail = QueueNode(value, old_tail, None)
        else:
            self.head = QueueNode(value, None, None)
        self.length += 1

    def dequeue(self, value):
        dead_head = self.head
        self.head = self.head.next
        self.length -= 1
        return dead_head

    def size(self):
        return self.length


class DequeueException(Exception):
    """An empty class to pass useful exceptions."""
    pass