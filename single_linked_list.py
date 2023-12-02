class Node:
    def __init__(self, data=None, next=None):
        # Initialize a node with data and a reference to the next node
        self.data = data
        self.next = next


class SingleLinkedList:
    def __init__(self):
        # Initialize an empty linked list with no starting node
        self.start = None

    def nodes(self):
        # Generator function to iterate through all nodes in the linked list
        point = self.start
        while point:
            yield point
            point = point.next

    def __repr__(self):
        # Representation of the linked list for debugging purposes
        for node in self.nodes():
            print(node.data)

    def __str__(self):
        # String representation of the linked list
        return self.__repr__()

    def length(self):
        # Calculate the length of the linked list
        count = 0
        for node in self.nodes():
            count += 1
        return count

    def node_at(self, location):
        # Get the node at a specific location in the linked list
        for n in self.nodes():
            if not location:
                return n
            location -= 1
        raise Exception("No entry in list")

    def data_at(self, location):
        # Get the data at a specific location in the linked list
        return self.node_at(location).data

    def insert_at(self, entry, location):
        # Insert a new node with data 'entry' at the specified location in the linked list
        new_node = Node(entry)
        new_node.next = self.start
        last = None
        while location:
            if not new_node.next:
                raise Exception("Index outside of list")
            location -= 1
            last = new_node.next
            new_node.next = new_node.next.next
        if last:
            last.next = new_node
            return

        # If 'last' is None, it means the new node is the new start of the linked list
        self.start = new_node

    def delete_at(self, location):
        # Delete the node at the specified location in the linked list
        point = self.start
        last = None
        while location and point:
            location -= 1
            last = point
            point = point.next
        if not point:
            raise Exception("No such element")
        if last:
            last.next = point.next
            return

        # If 'last' is None, it means the start of the linked list is being deleted
        self.start = self.start.next


# Create an instance of the SingleLinkedList class.
single_linked_list = SingleLinkedList()

# Insert elements [2, 3, 4, 5] into the linked list.
for i in [2, 3, 4, 5]:
    single_linked_list.insert_at(i, 0)  # Insert at the beginning for this example


# Print the length of the linked list.
print("Length:", single_linked_list.length())

# Print elements by iterating through the nodes in the linked list.
print("Elements using nodes:")
for node in single_linked_list.nodes():
    print(node.data)

# Access and print data at a specific location.
location_to_access = 2
print(
    f"Data at location {location_to_access}: {single_linked_list.data_at(location_to_access)}"
)

# Delete an element at a specific location.
location_to_delete = 1
single_linked_list.delete_at(location_to_delete)
print(f"Single Linked List after deleting element at location {location_to_delete}:")


# Print the length of the linked list after deletion.
print("Length after deletion:", single_linked_list.length())
