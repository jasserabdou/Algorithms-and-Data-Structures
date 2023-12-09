class Queue:
    """
    Implements a basic queue data structure.

    Attributes:
        bufsize: The maximum number of elements the queue can hold.
        queuesize: The current number of elements in the queue.
        queuestart: The index of the first element in the queue.
        queuearr: A list of elements representing the queue.
    """

    def __init__(self, bufsize=8):
        """
        Initializes a new Queue object with the specified buffer size.

        Args:
            bufsize: The maximum number of elements the queue can hold (default: 8).
        """
        self.bufsize = bufsize
        self.queuesize = 0
        self.queuestart = 0
        self.queuearr = [None] * bufsize

    def empty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return not self.queuesize

    def enqueue(self, item):
        """
        Adds an item to the back of the queue.

        Raises:
            Exception: If the queue is already full.

        Args:
            item: The element to be added to the queue.
        """
        if self.queuesize >= self.bufsize:
            raise Exception("Queue full")

        # Calculate the new index for the item, considering circular wrapping.
        new_index = (self.queuestart + self.queuesize) % self.bufsize
        self.queuearr[new_index] = item
        self.queuesize += 1

    def dequeue(self):
        """
        Removes and returns the item from the front of the queue.

        Raises:
            Exception: If the queue is already empty.

        Returns:
            object: The element removed from the queue.
        """
        if not self.queuesize:
            raise Exception("Queue empty")

        # Get the item from the start index, update the start index, and decrement the queue size.
        item = self.queuearr[self.queuestart]
        self.queuestart = (self.queuestart + 1) % self.bufsize
        self.queuesize -= 1
        return item


# Example usage: Create a queue with a buffer size of 5, enqueue elements, and dequeue elements until the queue is empty.
queue = Queue(5)

# Enqueue elements [2, 3, 4, 5]
for i in range(2, 6):
    queue.enqueue(i)

# Dequeue and print elements until the queue is empty
while not queue.empty():
    print(queue.dequeue())
