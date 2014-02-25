# a queue, by me for yueue!


class QueueNode(object):
    def __init__(self, value, after=None, before=None):
        self.value = value
        self.before = before
        self.after = after


class Queue(object):

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.length = 0

    def enqueue(self, value):
        if not self.head:
            self.head = QueueNode(value)
        else:
            old_tail = self.tail
            if self.tail:
                self.tail = QueueNode(value, before=old_tail)
                old_tail.after = self.tail
            else:
                self.tail = QueueNode(value, before=self.head)
                self.head.after = self.tail
        self.length += 1

    def size(self):
        return self.length

    def dequeue(self):
        if not self.head:
            raise DequeueException("There is nothing to dequeue!")
        if self.tail:
            dead_head = self.head
            self.head = self.head.after
            self.length -= 1
            return 'Dequeued %s' % dead_head.value
        else:
            dead_head = self.head
            self.head = None
            self.length -= 1
            return 'Dequeued %s' % dead_head.value


class DequeueException(Exception):
    """An empty class to pass useful exceptions."""
    pass
