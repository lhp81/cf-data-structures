import random  # for the eventual if 'name' == __main__ hypotheticals.
import time
from queue import Queue


class BSTree(object):
    """This is a search tree"""
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, value):
        """will insert the value val into the BST.  If val is already present,
        it will be ignored
        """
        if self.value is None:
            self.value = value
        else:
            if value > self.value:
                if self.right is None:
                    self.right = BSTree(value)
                else:
                    self.right.insert(value)
            if value < self.value:
                if self.left is None:
                    self.left = BSTree(value)
                else:
                    self.left.insert(value)
            else:
                return

    def contains(self, val):
        """will return True if val is in the BST, False if not"""
        try:
            if val == self.value:
                return True
            elif val > self.value:
                return self.right.contains(val)
            elif val < self.value:
                return self.left.contains(val)
        except AttributeError:
            return False

    def size(self):
        """will return the integer size of the BST (equal to the total number
            of values stored in the tree), 0 if the tree is empty."""
        total = 0
        if not self.value:
            return total
        else:
            total += 1
        if self.left:
            total += self.left.size()
        if self.right:
            total += self.right.size()
        return total
        # this is from Stephen's code; refactored my original work to it.

    def depth(self):
        """will return an integer representing the total number of levels in
        the tree"""
        total = 0
        if not self.value:
            return total
        else:
            left_total = self.left.depth() if self.left else 0
            right_total = self.right.depth() if self.right else 0
            return max(left_total, right_total) + 1
            # this comes from our in-class code breakdown.

    def balance(self):
        """Will return an positive or negative integer that represents how
           well-balanced the tree is. Positive value means the tree is right-
           heavy; negative means it is left-heavy. Balanced tree = 0."""
        if not self.value:
            return 0
        else:
            return self.right.depth() - self.left.depth()

    def in_order(self):
        '''returns a generator that will return the values in the tree using
        in-order traversal, one at a time.
        In-order means left, middle, right.'''
        if self.left:
            for value in self.left.in_order():
                yield value
        yield self.value
        if self.right:
            for value in self.right.in_order():
                yield value

    def pre_order(self):
        '''returns a generator that will return the values in the tree using
        pre-order traversal, one at a time.
        Pre-order means middle, left, right.'''
        if not self.value:
            return
        else:
            yield self.value
            if self.left:
                for val in self.left.pre_order():
                    yield val
            if self.right:
                for val in self.right.pre_order():
                    yield val

    def post_order(self):
        '''returns a generator that will return the values in the tree using
        post_order traversal, one at a time.
        Post-order means right, middle, left.'''
        if not self.value:
            return
        else:
            if self.left:
                for val in self.left.post_order():
                    yield val
            if self.right:
                for val in self.right.post_order():
                    yield val
            yield self.value

    def breadth_first(self):
        '''returns a generator that will return the values in the tree using
        breadth-first traversal, one at a time.'''
        # set up a queue and add the root to it.
        # a queue is FIFA, so we want to add from the top and then go left-to-
        # right across the tree, level by level.
        number_queue = Queue()
        if self.value:
            number_queue.enqueue(self)
        #  now start traversing the tree, inserting each level's nodes into the
        #  queue.
        while number_queue.size():
            to_yield = number_queue.dequeue()
            if to_yield.value is not None:
                yield to_yield.value
            if to_yield.left is not None:
                number_queue.enqueue(to_yield.left)
            if to_yield.right is not None:
                number_queue.enqueue(to_yield.right)
        # this is based off of looking at Mark & Matt's code, and hammering my
        # head against the wall. I wasn't getting that I needed to use
        # enqueue(self).


    def delete(self, value):
        """remove val from the tree if present; if not present, this method is
        a no-op. Return None in all cases"""
        if not self.value:
            return None  # for empty trees.
        # if it's a leaf (no self.left or self.right)
        if self.value == value:
            if not self.left.value and not self.right.value:
                self.value = None
                return None
            # if it's got self.left.
            elif self.left and not self.right:
                return None
            # if it's got self.right.
            elif self.right and not self.left:
                return None
        # if it's got self.right and self.left.
        if (self.self) and (self.right):
            self.delete_when_its_complicated(self.value)

    def delete_when_its_complicated(self, value):
        return None

    # the below is all from Cris Ewing; required for this file.

    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" % ("" if self.value is None else (
            "\t%s;\n%s\n" % (
                self.value,
                "\n".join(self._get_dot())
            )
        ))

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        if self.left is not None:
            yield "\t%s -> %s;" % (self.value, self.left.value)
            for i in self.left._get_dot():
                yield i
        elif self.right is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)
        if self.right is not None:
            yield "\t%s -> %s;" % (self.value, self.right.value)
            for i in self.right._get_dot():
                yield i
        elif self.left is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)

if __name__ == '__main__':
    ordered_tree = BSTree()
    random_tree = BSTree()
    for num in range(900):
        ordered_tree.insert(num)
        random_tree.insert(random.choice(range(2000)))
    first_time = time.time()
    ramdom_has = random_tree.contains(900)
    second_time = time.time()
    ordered_has = ordered_tree.contains(900)
    third_time = time.time()
    print 'Random: %r sec.' % (second_time-first_time)
    print 'Ordered: %r sec.' % (third_time-second_time)
