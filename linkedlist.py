"""
While writing this code I referred to the following sources to better
understand Linked Lists and to see how others had implemented them in
Python:

http://en.wikipedia.org/wiki/Linked_list#Singly_linked_list
http://www.openbookproject.net/thinkcs/python/english2e/ch18.html
http://www.brpreiss.com/books/opus7/html/page97.html
http://kkthegeek.wordpress.com/2010/05/06/linked-list-implementation-in-python/
http://alextrle.blogspot.com/2011/05/write-linked-list-in-python.html

Also helpful has been looking at the work of my classmates on github and
guidance and code review from Cris Ewing.

"""


class Node(object):
    """An individual node is one of the items in a Linked List.
       Each node contains a value and the key of the item to which it
       is linked."""
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class SingleLL(object):
    """A Single Linked List (SLL) is a collection of nodes."""
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        if self.head is not None:
            self.count = 1
        else:
            self.count = 0

    def __str__(self):  # works!
        """Prints the list as a Python tuple literal."""
        to_print = ''
        head = self.head  # this is the start of the LL
        tail = self.tail  # this is the end of the LL
        start = self.head
        while start is not None:
            to_print += '(' + str(start.value) + ',' + str(start.next) + ') '
            start = start.next
        return to_print

    def insert(self, val):  # works
        """inserts the value 'val' at the head of the list"""
        new_head = Node(val, self.head)
        self.head = new_head
        self.count += 1
        return str(self.head)

    def pop(self):  # works
        """Pops the first value off the head of the list & returns it."""
        to_return = str(self.head)
        self.head = self.head.next
        return to_return

    def size(self):  # works
        """Returns the length of the list."""
        # count = 0
        # to_count = self.head
        # while to_count:
        #     count += 1
        #     to_count = to_count.next
        return self.count

    def search(self, val):  # works!
        """returns the node containing 'val' if present. Else: None"""
        start = self.head
        found = None
        while start and not found:
            if start.value == val:
                found = (start.value, start.next)
            start = start.next
        return found

    def remove(self, target):  # works!
        """removes the given node from the list"""
        current = self.head
        previous = None
        while current:
            if current.value == target:
                if previous:
                    self.head = current.next
                else:
                    previous.next = current.next
                return target
            else:
                return 'Not Found.'



"""
My code for search and remove is indebted to my classmates Justin & Matt. I was
first exposed to these ways of solving the problem through our codereview of
their work.
"""
