import unittest
import stack


class StackTest(unittest.TestCase):
    """Testing out my stack model."""

    def make_a_stack_and_push_to_it(self):
        ms = Stack()
        ms.push('cat')
        ms.push(1337)
        ms.push(True)
        self.assertEqual(ms.__str__(), '(True) (1337) (cat)')

    def make_a_stack_and_pop(self):
        ms = Stack()
        ms.push('dog')
        ms.push(11235)
        self.assertEqual(ms.pop(), 11235)

if __name__ == '__main__':
    unittest.main()
