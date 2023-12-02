import math


class MaxHeap:
    def __init__(self, array):
        # Initialize a MaxHeap object with the given array and set the heap size.
        self.array = array
        self.heapsize = len(array)

    def left(self, i):
        # Get the left child index of the element at index 'i'.
        return 2 * i

    def right(self, i):
        # Get the right child index of the element at index 'i'.
        return 2 * i + 1

    def heapify(self, i):
        # Maintain the max-heap property starting from the given index 'i'.
        l = self.left(i)
        r = self.right(i)

        # Find the index of the largest element among the element at 'i', its left, and right children.
        if l <= self.heapsize and self.array[l - 1] > self.array[i - 1]:
            largest = l
        else:
            largest = i
        if r <= self.heapsize and self.array[r - 1] > self.array[largest - 1]:
            largest = r

        # If the largest element is not at index 'i', swap elements and recursively heapify the affected subtree.
        if largest != i:
            self.array[i - 1], self.array[largest - 1] = (
                self.array[largest - 1],
                self.array[i - 1],
            )
            self.heapify(largest)

    def build_heap(self):
        # Build a max heap from the given array.
        for i in range(math.floor(self.heapsize // 2), 0, -1):
            self.heapify(i)

    def heapsort(self):
        # Sort the array using the heapsort algorithm.
        self.build_heap()
        for i in range(self.heapsize - 1, 0, -1):
            self.array[0], self.array[i] = self.array[i], self.array[0]
            self.heapsize -= 1
            self.heapify(1)

    def heappop(self):
        # Pop the maximum element from the heap (root of the max heap).
        if len(self.array) < 1:
            raise Exception("No elements in heap")
        the_top = self.array[0]
        self.array[0] = self.array[len(self.array) - 1]
        del self.array[len(self.array) - 1]
        self.heapify(1)
        return the_top


# Example usage: Create a MaxHeap, perform heapsort, and print the sorted array.
arr = [4, 10, 3, 5, 1]
max_heap = MaxHeap(arr)
max_heap.heapsort()
print("Sorted Array:", max_heap.array)
