class Stack:
    def __init__(self, bufsize=16):
        # Initialize the Stack object with a specified buffer size.
        self.bufsize = bufsize
        # Create a list to represent the stack with the given buffer size,
        # and set the initial stack size to 0.
        self.stackarr = [None] * self.bufsize
        self.stacksize = 0

    def push(self, element):
        # Push an element onto the stack.
        # Check if the stack is full, and raise an exception if it is.
        if self.stacksize == self.bufsize:
            raise Exception("Stack full")
        # Add the element to the stack and increment the stack size.
        self.stackarr[self.stacksize] = element
        self.stacksize += 1

    def pop(self):
        # Pop an element from the stack.
        # Check if the stack is empty, and raise an exception if it is.
        if not self.stacksize:
            raise Exception("Stack empty")
        # Decrement the stack size and return the popped element.
        self.stacksize -= 1
        return self.stackarr[self.stacksize]

    def empty(self):
        # Check if the stack is empty.
        return not self.stacksize


# Create an instance of the Stack class.
stack = Stack()

# Push elements [2, 3, 4, 5] onto the stack.
for i in [2, 3, 4, 5]:
    stack.push(i)

# Pop and print elements from the stack until it is empty.
while not stack.empty():
    print(stack.pop())
