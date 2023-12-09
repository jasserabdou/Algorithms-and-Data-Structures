import math


class MaxHeap:
    """
    Implements a MaxHeap data structure for efficient sorting and retrieval of maximum elements.

    Attributes:
        array: The array containing the heap elements.
        heapsize: The current size of the heap (number of elements).
    """

    def __init__(self, array):
        """
        Initializes a new MaxHeap object with the given array and sets the heap size.

        Args:
            array: The array of elements to be stored in the heap.
        """
        self.array = array
        self.heapsize = len(array)

    def parent(self, i):
        """
        Returns the index of the parent element for the element at index 'i'.

        Args:
            i: The index of the element whose parent index is needed.

        Returns:
            int: The index of the parent element.
        """
        return i // 2

    def left(self, i):
        """
        Returns the index of the left child element for the element at index 'i'.

        Args:
            i: The index of the element whose left child index is needed.

        Returns:
            int: The index of the left child element, or None if out of bounds.
        """
        left_index = 2 * i
        if left_index > self.heapsize:
            return None
        return left_index

    def right(self, i):
        """
        Returns the index of the right child element for the element at index 'i'.

        Args:
            i: The index of the element whose right child index is needed.

        Returns:
            int: The index of the right child element, or None if out of bounds.
        """
        right_index = 2 * i + 1
        if right_index > self.heapsize:
            return None
        return right_index

    def heapify(self, i):
        """
        Maintains the max-heap property by recursively comparing and swapping elements starting from index 'i'.

        Args:
            i: The index of the element to start heapifying from.
        """
        left_index = self.left(i)
        right_index = self.right(i)

        # Find the largest element among the element at 'i', its left and right children.
        largest = i
        if left_index and self.array[left_index - 1] > self.array[i - 1]:
            largest = left_index
        if right_index and self.array[right_index - 1] > self.array[largest - 1]:
            largest = right_index

        # If the largest element is not at index 'i', swap elements and recursively heapify the affected subtree.
        if largest != i:
            self.array[i - 1], self.array[largest - 1] = (
                self.array[largest - 1],
                self.array[i - 1],
            )
            self.heapify(largest)

    def build_heap(self):
        """
        Builds a max-heap from the existing array.
        """
        start_index = math.floor(self.heapsize // 2) - 1
        for i in range(start_index, -1, -1):
            self.heapify(i)

    def heapsort(self):
        """
        Sorts the elements in the array using the heapsort algorithm.
        """
        self.build_heap()
        for i in range(self.heapsize - 1, 0, -1):
            self.array[0], self.array[i] = self.array[i], self.array[0]
            self.heapsize -= 1
            self.heapify(1)

    def heappop(self):
        """
        Extracts and returns the maximum element (root) from the heap.

        Raises:
            Exception: If the heap is empty.

        Returns:
            object: The maximum element from the heap.
        """
        if len(self.array) < 1:
            raise Exception("No elements in heap")
        the_top = self.array[0]
        self.array[0] = self.array[len(self.array) - 1]
        del self.array[len(self.array) - 1]
        self.heapsize -= 1
        self.heapify(1)
        return the_top


# Example usage: Create a MaxHeap, perform heapsort, and print the sorted array.
arr = [4, 10, 3, 5, 1]
max_heap = MaxHeap(arr)
max_heap.heapsort()
print("Sorted Array:", max_heap.array)
