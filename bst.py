import random


class BSTree(object):
    """This is a search tree"""
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None

    def check_rl(self, value):
        pass

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
                pass

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
            total += self.value
            if self.right:
                total += self.right.size()
            if self.left:
                total += self.left.size()
        return total

    def depth(self):
        """will return an integer representing the total number of levels in
        the tree"""
        depth = 0
        if not self.value:
            return depth
        else:
            depth += 1
            if (self.right and not self.left) or (self.right and :

    def balance(self):
        """Will return an integer, positive or negative that represents how
           well-balanced the tree is.
        Trees which are higher on the left than the right should return a
           positive value, trees which are higher on the right than the left
           should return a negative value.
        An ideally-balanced tree should return 0.
        """
        balance = 0
        if not self.value:
            return balance
        else:
            

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