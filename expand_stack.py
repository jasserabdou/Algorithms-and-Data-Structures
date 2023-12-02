from stack import Stack


class Expand_Stack(Stack):
    def __init__(self, bufsize=4):
        # Initialize the Expand_Stack object, inheriting from the Stack class.
        # Set the buffer size and initialize the stack using the parent class constructor.
        Stack.__init__(self, bufsize)

    def push(self, element):
        # Override the push method to expand the stack if it's full.
        if self.stacksize == self.bufsize:
            # Double the buffer size and create a new array with the updated size.
            self.bufsize *= 2
            new_arr = [None] * self.bufsize

            # Copy existing elements to the new array.
            for i in range(self.stacksize):
                new_arr[i] = self.stackarr[i]
            self.stackarr = new_arr

        # Add the element to the stack and increment the stack size.
        self.stackarr[self.stacksize] = element
        self.stacksize += 1

    def empty(self):
        # Override the empty method for clarity.
        return not self.stacksize

    def peek(self):
        # Get the top element of the stack without removing it.
        # Raise an exception if the stack is empty.
        if self.empty():
            raise Exception("Peek: stack empty")
        return self.stackarr[self.stacksize - 1]

    def __repr__(self):
        # Override the __repr__ method to provide a string representation of the stack.
        # Display elements separated by "|".
        return "|".join("%s" % str(s) for s in self.stackarr)


# Create an instance of the Expand_Stack class.
expandstack = Expand_Stack()

# Push elements [0, 1, ..., 9] onto the expandable stack and print the stack after each push.
for i in range(10):
    expandstack.push(i)
    print("push", i, ":", expandstack)
