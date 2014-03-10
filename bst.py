import random


class Node(object):
    """ This is a node."""
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BSTree(object):
    """This is a search tree"""
    def __init__(self, value):
        self.root = None
        self.size = 0

    def check_rl(self, value):
        pass

    def insert(self, value):
        """will insert the value val into the BST.  If val is already present,
        it will be ignored
        """
        if self.root is None:
            self.root = Node(value)
        else:
            if value > self.value:
                self.right = Node(value)
            if value < self.value:
                self.left = Node(value)
            else:
                break
        self.size += 1

    def contains(self, val):
        """will return True if val is in the BST, False if not"""
        pass

    def size(self):
        """will return the integer size of the BST (equal to the total number
            of values stored in the tree), 0 if the tree is empty."""
        return self.size

    def depth(self):
        """will return an integer representing the total number of levels in
        the tree"""
        pass

    def balance(self):
        """will return an integer, positive or negative that represents how
        well-balanced the tree is. Trees which are higher on the left than the
        right should return a positive value, trees which are higher on the
        right than the left should return a negative value.  An
        ideally-balanced tree should return 0.
        """
        pass

    # the below is all from Cris Ewing; required for this file.
    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" % ("" if self.data is None else (
            "\t%s;\n%s\n" % (
                self.data,
                "\n".join(self._get_dot())
            )
        ))

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        if self.left is not None:
            yield "\t%s -> %s;" % (self.data, self.left.data)
            for i in self.left._get_dot():
                yield i
        elif self.right is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.data, r)
        if self.right is not None:
            yield "\t%s -> %s;" % (self.data, self.right.data)
            for i in self.right._get_dot():
                yield i
        elif self.left is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.data, r)