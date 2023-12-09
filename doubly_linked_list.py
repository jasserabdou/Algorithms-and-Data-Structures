class Node:
    """
    Represents a node in a doubly linked list.

    Attributes:
        data: The data stored in the node.
        prev: The reference to the previous node in the list.
        next: The reference to the next node in the list.
    """

    def __init__(self, data=None, prev=None, next=None):
        """
        Initializes a new node with the provided data and references.

        Args:
            data: The data to be stored in the node.
            prev: The reference to the previous node (optional).
            next: The reference to the next node (optional).
        """
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    """
    Implements a doubly linked list data structure.

    Attributes:
        start: The reference to the first node in the list.
        end: The reference to the last node in the list.
        _length: The cached length of the list (optional).
    """

    def __init__(self):
        """
        Initializes an empty doubly linked list.
        """
        self.start = None
        self.end = None
        self._length = None  # Cached length for faster access

    def nodes(self):
        """
        Iterates through all nodes in the list.

        Yields:
            Node: Each node in the list one by one.
        """
        point = self.start
        while point:
            yield point
            point = point.next

    def nodes_reverse(self):
        """
        Iterates through all nodes in the list in reverse order.

        Yields:
            Node: Each node in the list from the end to the beginning.
        """
        point = self.end
        while point:
            yield point
            point = point.prev

    def __repr__(self):
        """
        Provides a string representation of the list for debugging.

        Returns:
            str: A string with the data of each node in the list.
        """
        output = ""
        for node in self.nodes():
            output += f"{node.data}\n"
        return output

    def __str__(self):
        """
        Provides a string representation of the list.

        Returns:
            str: The same output as __repr__.
        """
        return self.__repr__()

    def length(self):
        """
        Calculates and returns the length of the list.

        Returns:
            int: The number of nodes in the list.
        """
        if self._length is not None:
            return self._length

        count = 0
        for _ in self.nodes():
            count += 1

        self._length = count
        return count

    def node_at(self, location):
        """
        Retrieves the node at a specific location in the list.

        Args:
            location: The index of the desired node (0-based).

        Returns:
            Node: The node at the specified location.

        Raises:
            Exception: If the location is outside the list bounds.
        """
        for n in self.nodes():
            if not location:
                return n
            location -= 1
        raise Exception("No entry in list")

    def data_at(self, location):
        """
        Retrieves the data stored in the node at a specific location in the list.

        Args:
            location: The index of the desired node (0-based).

        Returns:
            object: The data stored in the node at the specified location.

        Raises:
            Exception: If the location is outside the list bounds.
        """
        return self.node_at(location).data

    def insert_at(self, entry, location):
        """
        Inserts a new node with the given data at a specific location in the list.

        Args:
            entry: The data to be stored in the new node.
            location: The index where the new node should be inserted (0-based).

        Raises:
            Exception: If the location is outside the list bounds.
        """
        new_node = Node(data=entry)

        # Update start and end references if inserting at the beginning or end
        if not location:
            new_node.next = self.start
            new_node.prev = None

            if self.start:
                self.start
        # Update start and end references if inserting at the beginning or end
        if not location:
            new_node.next = self.start
            new_node.prev = None

            if self.start:
                self.start.prev = new_node
            else:
                self.end = new_node

            self.start = new_node
        else:
            # Traverse the list to find the insertion location
            point = self.start
            while location:
                if not point.next:
                    raise Exception("Index outside of list")
                location -= 1
                point = point.next

            # Insert the new node between point and its next node
            new_node.prev = point
            new_node.next = point.next
            point.next = new_node

            if new_node.next:
                new_node.next.prev = new_node

        # Update the cached length of the list
        if self._length is not None:
            self._length += 1

    def delete_at(self, location):
        """
        Deletes the node at a specific location in the list.

        Args:
            location: The index of the node to be deleted (0-based).

        Raises:
            Exception: If the location is outside the list bounds.
        """
        point = self.start

        # Traverse the list to find the node to be deleted
        while location and point:
            location -= 1
            point = point.next

        if not point:
            raise Exception("No such element")

        # Update references for deletion
        if point.prev:
            point.prev.next = point.next
        else:
            self.start = point.next

        if point.next:
            point.next.prev = point.prev
        else:
            self.end = point.prev

        # Update the cached length of the list
        self._length -= 1


# Create an instance of the DoublyLinkedList class.
doubly_linked_list = DoublyLinkedList()

# Insert elements [2, 3, 4, 5] into the doubly linked list.
for i in [2, 3, 4, 5]:
    doubly_linked_list.insert_at(i, 0)  # Insert at the beginning for this example

# Print the length of the doubly linked list.
print("Length:", doubly_linked_list.length())

# Print elements by iterating through the nodes in the doubly linked list.
print("Elements using nodes:")
for node in doubly_linked_list.nodes():
    print(node.data)

# Print elements in reverse order.
print("Elements in reverse order:")
for node in doubly_linked_list.nodes_reverse():
    print(node.data)

# Access and print data at a specific location.
location_to_access = 2
print(
    f"Data at location {location_to_access}: {doubly_linked_list.data_at(location_to_access)}"
)

# Delete an element at a specific location.
location_to_delete = 1
doubly_linked_list.delete_at(location_to_delete)
print(f"Doubly Linked List after deleting element at location {location_to_delete}:")

# Print the length of the doubly linked list after deletion.
print("Length after deletion:", doubly_linked_list.length())
