# a queue, by me for yueue!


class QueueNode(object):
    """
    One of the things in a queue.
    It has a value, and can see what comes after it and what goes before it.
    """
    def __init__(self, value, after=None, before=None):
        self.value = value
        self.before = before
        self.after = after
        #  I found it way, way, way too confusing to do 'previous' and
        #  'next' with this, so changed the nomenclature to before/after. That
        #  makes it more analagous to a real queue, anyway.


class Queue(object):
    """
    This is a queue. It has a beginning and an end, when there are things in
    it.
    """
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.length = 0

    def enqueue(self, value):
        # the first thing queue objects do is look to go to the front of the
        # line. it's human nature.
        if not self.head:
            self.head = QueueNode(value)
        # If there is someone at the front of the line, then...
        else:
            if self.tail:
                old_tail = self.tail
                self.tail = QueueNode(value, before=old_tail)
                old_tail.after = self.tail
            else:
                self.tail = QueueNode(value, before=self.head)
                self.head.after = self.tail
        self.length += 1  # to keep count.

    def size(self):
        return self.length

    def dequeue(self):
        if not self.head:
            #  again, if there's nothing at the front of the line...
            raise DequeueException("There is nothing to dequeue!")
        else:
            dead_head = self.head
            self.head = self.head.after
            self.length -= 1
            return dead_head.value


class DequeueException(Exception):
    """An empty class to pass useful exceptions."""
    pass
