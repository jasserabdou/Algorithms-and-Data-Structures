from stack import Stack


class Expand_Stack(Stack):
    """
    Extends the Stack class to automatically expand its capacity when it becomes full.
    """

    def __init__(self, bufsize=4):
        """
        Initializes the Expand_Stack object.

        Args:
            bufsize: Initial buffer size of the stack.
        """
        super().__init__(
            bufsize
        )  # Initialize parent Stack class with the given buffer size.

    def push(self, element):
        """
        Pushes an element onto the stack, expanding the capacity if necessary.

        Args:
            element: The element to be pushed.
        """
        if self.stacksize == self.bufsize:
            # Double the buffer size.
            self.bufsize *= 2
            # Create a new array with the updated size.
            new_arr = [None] * self.bufsize
            # Copy existing elements to the new array.
            for i in range(self.stacksize):
                new_arr[i] = self.stackarr[i]
            # Update the stack array with the new one.
            self.stackarr = new_arr

        # Add the element to the stack and increment the size.
        self.stackarr[self.stacksize] = element
        self.stacksize += 1

    def empty(self):
        """
        Returns True if the stack is empty, False otherwise.
        """
        return not self.stacksize

    def peek(self):
        """
        Returns the top element of the stack without removing it.

        Raises:
            Exception: If the stack is empty.
        """
        if self.empty():
            raise Exception("Peek: stack empty")
        return self.stackarr[self.stacksize - 1]

    def __repr__(self):
        """
        Returns a string representation of the stack elements separated by "|".
        """
        return "|".join("%s" % str(s) for s in self.stackarr)


# Create an instance of the Expand_Stack class.
expandstack = Expand_Stack()

# Push elements [0, 1, ..., 9] onto the expandable stack and print the stack after each push.
for i in range(10):
    expandstack.push(i)
    print("push", i, ":", expandstack)
