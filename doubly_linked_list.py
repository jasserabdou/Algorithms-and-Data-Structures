class Node:
    def __init__(self, data=None, prev=None, next=None):
        # Initialize a node with data, previous, and next references
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        # Initialize an empty doubly linked list with no starting and ending nodes
        self.start = None
        self.end = None
        self._length = None  # Cache for storing the length of the linked list

    def nodes(self):
        # Generator function to iterate through all nodes in the doubly linked list
        point = self.start
        while point:
            yield point
            point = point.next

    def nodes_reverse(self):
        # Generator function to iterate through all nodes in the doubly linked list in reverse order
        point = self.end
        while point:
            yield point
            point = point.prev

    def __repr__(self):
        # Representation of the doubly linked list for debugging purposes
        for node in self.nodes():
            print(node.data)

    def __str__(self):
        # String representation of the doubly linked list
        return self.__repr__()

    def length(self):
        # Calculate the length of the doubly linked list
        if self._length is not None:
            return self._length
        count = 0
        for _ in self.nodes():
            count += 1
        self._length = count
        return count

    def node_at(self, location):
        # Get the node at a specific location in the doubly linked list
        for n in self.nodes():
            if not location:
                return n
            location -= 1
        raise Exception("No entry in list")

    def data_at(self, location):
        # Get the data at a specific location in the doubly linked list
        return self.node_at(location).data

    def insert_at(self, entry, location):
        # Insert a new node with data 'entry' at the specified location in the doubly linked list
        new_node = Node(data=entry)
        new_node.next = self.start
        new_node.prev = None

        while location:
            if not new_node.next:
                raise Exception("Index outside of list")
            location -= 1
            new_node.prev = new_node.next
            new_node.next = new_node.next.next

        # Increment the length of the linked list
        if self._length is not None:
            self._length += 1
        else:
            self._length = 1

        # Fix predecessor nodes
        if new_node.prev:
            new_node.prev.next = new_node
        else:
            self.start = new_node

        # Fix successor nodes
        if new_node.next:
            new_node.next.prev = new_node
        else:
            self.end = new_node

    def delete_at(self, location):
        # Delete the node at the specified location in the doubly linked list
        point = self.start

        while location and point:
            location -= 1
            point = point.next

        if not point:
            raise Exception("No such element")

        # Decrement the length of the linked list
        self._length -= 1

        # Fix predecessor nodes
        if point.prev:
            point.prev.next = point.next
        else:
            self.start = point.next

        # Fix successor nodes
        if point.next:
            point.next.prev = point.prev
        else:
            self.end = point.prev


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
