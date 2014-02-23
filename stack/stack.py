class Stack(object):
    """An implementation of a stack that can pop (remove the first item and
    return it) and push (add an item to the top of the stack). As appropriate,
    informative error messages will be returned."""
    def __init__(self, my_stack):
        self.my_stack = my_stack

    def __str__(self):
        print self.my_stack

    def pop(self):
        pop, my_stack = self.my_stack.split(',', 1)
        return pop

    def push(self, num):
        self.my_stack = num + ',', self.my_stack
