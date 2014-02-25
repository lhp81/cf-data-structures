import unittest
from queue import Queue, QueueNode, DequeueException


class QueueTest(unittest.TestCase):
    """Testing out my stack model."""

    def test_make_a_queue_and_enqueue_something(self):
        mq = Queue()
        mq.enqueue('cat')
        # self.assertEqual(ms.__str__(), '(True) (1337) (cat) ')

    def test_make_a_queue_and_dequeue(self):
        mq = Queue()
        mq.enqueue('dog')
        # self.assertEqual(mq.pop(), '11235')

    def test_pop_an_empty_stack(self):
        mq = Stack()
        # self.assertRaises(PopException, lambda: ms.pop())

    def test_queue_size(self):
        pass

    def test_empty_queue_size(self):
        pass

if __name__ == '__main__':
    unittest.main()
