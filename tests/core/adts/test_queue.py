#
# Author: Rohtash Lakra
#
from core.adts.queue import Queue, PriorityQueue
from core.enums import Priority
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

    def test_PriorityQueue(self):
        print("test_PriorityQueue")
        pq = PriorityQueue()
        pq.enqueue(Priority.IMPORTANT, "Windshield wipers turned on")
        pq.enqueue(Priority.NEUTRAL, "Radio station tuned in")
        pq.enqueue(Priority.CRITICAL, "Brake pedal depressed")
        pq.enqueue(Priority.IMPORTANT, "Hazard lights turned on")
        print(f"pq={pq}")
        self.assertIsNotNone(pq)
        # self.assertEqual(4, len(pq))
        print()
        result = pq.dequeue()
        print(f"result={result}")
        # self.assertEqual("('CRITICAL', 'Brake pedal depressed')", str(result))
        self.assertEqual('Brake pedal depressed', result)
        print(pq.dequeue())
        print(pq.dequeue())
        print(pq.dequeue())
        # print items
        # for item in pq:
        #     print(item)
        print()


# Starting point
if __name__ == 'main':
    start(False)
