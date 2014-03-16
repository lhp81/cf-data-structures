import unittest
from queue import Queue, QueueNode, DequeueException


class QueueTest(unittest.TestCase):
    """Testing out my stack model."""

    def test_make_a_queue_and_enqueue_something(self):
        mq = Queue()
        mq.enqueue('cat')
        self.assertEqual(mq.size(), 1)

    def test_make_a_queue_and_enqueue_int(self):
        mq = Queue()
        mq.enqueue(1)
        self.assertEqual(mq.size(), 1)

    def test_make_a_queue_and_enqueue_float(self):
        mq = Queue()
        mq.enqueue(1.0)
        self.assertEqual(mq.size(), 1)

    def test_make_a_queue_and_dequeue(self):
        mq = Queue()
        mq.enqueue('dog')
        self.assertEqual(mq.dequeue(), 'dog')

    def test_size_method_works(self):
        mq = Queue()
        mq.enqueue('wallaby')
        mq.enqueue('fine linen')
        self.assertEqual(mq.size(), 2)

    def test_size_method_worsks_on_empty_queue(self):
        mq = Queue()
        self.assertEqual(mq.size(), 0)

    def test_dequeue_an_empty_stack(self):
        mq = Queue()
        self.assertRaises(DequeueException, lambda: mq.dequeue())


if __name__ == '__main__':
    unittest.main()
