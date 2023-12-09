class Stack:
    """
    Implements a basic stack data structure.

    Attributes:
        bufsize (int): The maximum number of elements the stack can hold.
        stackarr (list): A list representing the stack.
        stacksize (int): The current number of elements in the stack.
    """

    def __init__(self, bufsize=16):
        """
        Initializes a new Stack object with the specified buffer size.

        Args:
            bufsize (int): The maximum number of elements the stack can hold (default: 16).
        """
        self.bufsize = bufsize
        self.stackarr = [None] * self.bufsize
        self.stacksize = 0

    def push(self, element):
        """
        Pushes an element onto the stack.

        Raises:
            Exception: If the stack is already full.

        Args:
            element: The element to be pushed onto the stack.
        """
        if self.stacksize == self.bufsize:
            raise Exception("Stack full")
        self.stackarr[self.stacksize] = element
        self.stacksize += 1

    def pop(self):
        """
        Pops and returns the top element from the stack.

        Raises:
            Exception: If the stack is already empty.

        Returns:
            object: The popped element.
        """
        if not self.stacksize:
            raise Exception("Stack empty")
        self.stacksize -= 1
        return self.stackarr[self.stacksize]

    def empty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return not self.stacksize


# Create an instance of the Stack class.
stack = Stack()

# Push elements [2, 3, 4, 5] onto the stack.
for i in [2, 3, 4, 5]:
    stack.push(i)

# Pop and print elements from the stack until it is empty.
while not stack.empty():
    print(stack.pop())
