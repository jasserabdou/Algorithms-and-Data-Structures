class Queue:
    def __init__(self, bufsize=8):
        # Initialize a Queue object with a specified buffer size.
        self.bufsize = bufsize
        # Set initial queue size, start index, and create a list to represent the queue.
        self.queuesize = 0
        self.queuestart = 0
        self.queuearr = [None] * bufsize

    def empty(self):
        # Check if the queue is empty.
        return not self.queuesize

    def enqueue(self, item):
        # Add an item to the back of the queue.
        if self.queuesize >= self.bufsize:
            raise Exception("Queue full")

        # Calculate the new index for the item, considering circular wrapping.
        new_index = (self.queuestart + self.queuesize) % self.bufsize
        self.queuearr[new_index] = item
        self.queuesize += 1

    def dequeue(self):
        # Remove and return the item from the front of the queue.
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
