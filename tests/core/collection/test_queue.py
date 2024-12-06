#
# Author: Rohtash Lakra
#
from core.collection.queue import Queue
from tests.core._abstract import AbstractTest, start


class QueueTest(AbstractTest):
    """Unit-tests for Queue"""

    def test_queue_enqueue(self):
        print("test_queue_enqueue")
        queue = Queue()
        queue.enqueue("Python")
        queue.enqueue("Java")
        queue.enqueue("Script")
        queue.enqueue("Shell")

        print()
        print(f"queue={queue}, size={len(queue)}")
        self.assertIsNotNone(queue)
        self.assertEqual(4, len(queue))
        # print items
        for item in queue:
            print(item)
        print()

    def test_queue_dequeue(self):
        print("test_queue_dequeue")
        queue = Queue()
        queue.enqueue("Python")
        queue.enqueue("Java")
        queue.enqueue("Script")
        queue.enqueue("Shell")
        #
        self.assertIsNotNone(queue)
        self.assertEqual(4, len(queue))
        print()

        # remove element
        print(queue.dequeue())
        print(f"queue={queue}, size={len(queue)}")
        self.assertIsNotNone(queue)
        self.assertEqual(3, len(queue))

        # remove element
        print(queue.dequeue())
        print(f"queue={queue}, size={len(queue)}")
        self.assertIsNotNone(queue)
        self.assertEqual(2, len(queue))

        # remove element
        print(queue.dequeue())
        print(f"queue={queue}, size={len(queue)}")
        self.assertIsNotNone(queue)
        self.assertEqual(1, len(queue))

        # remove element
        print(queue.dequeue())
        print(f"queue={queue}, size={len(queue)}")
        self.assertIsNotNone(queue)
        self.assertEqual(0, len(queue))
        print()

    def test_queue_iterator(self):
        print("test_queue_iterator")
        queue = Queue()
        queue.enqueue("Python")
        queue.enqueue("Java")
        queue.enqueue("Script")
        queue.enqueue("Shell")
        self.assertIsNotNone(queue)
        self.assertEqual(4, len(queue))
        # print items
        for item in queue:
            print(item)
        print()


# Starting point
if __name__ == 'main':
    start(False)
