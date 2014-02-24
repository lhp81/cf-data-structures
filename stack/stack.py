class Stack(object):
    """An implementation of a stack that can pop (remove the first item and
    return it) and push (add an item to the top of the stack). As appropriate,
    informative error messages will be returned."""

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        """Prints the stack as a Python tuple literal.
        This code is recycled from my linked list."""
        to_print = ''
        start = self.head
        while start is not None:
            to_print += '(' + str(start.value) + ') '
            start = start.next
        return to_print

    def push(self, value):
        self.head = StackNode(value, self.head)
        return 'Added %r to stack.' % value

    def pop(self):
        try:
            old_head, self.head = self.head, self.head.next
            return str(old_head)  # the above made me feel clever-multiassign!
        except AttributeError:  # this made me feel very clever too.
            return 'There is nothing to pop()!'


class StackNode(object):
    """A StackNode is one of the items in the stack. It has a value and info
    on the value that comes after it, which by default is the current first
    item in the stack to which it is added.
    This cannot exist without a Stack, so prob. should be a subclass thereof?
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)