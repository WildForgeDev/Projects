class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        print(f"{val} has been pushed to the top of the stack.")
        self.stack.insert(0, val)

    def peek(self):
        p = self.stack[0]
        print(f"{p} is at the top of the stack.")

    def pop(self):
        if len(self.stack) <= 0:
            print("Stack is empty")
        else:
            print(self.stack[0], "was popped from the top of the stack.")
            self.stack.pop(0)
    
    def size(self):
            print("There are", len(self.stack), "items in the stack.")
    
    def show_stack(self):
        if len(self.stack) <= 0:
            print("Stack is empty")
        else:
            t = self.stack[0]
            b = self.stack[-1]
            print("The current stack contains " '[%s]' % ', '.join(map(str, self.stack)))
            print(f"{t} is at the top of the stack.")
            print(f"{b} is at the bottom of the stack.")


retail_products = Stack()
retail_products.size()
retail_products.show_stack()
retail_products.push("LCD")
retail_products.push("LED")
retail_products.push("Mobile")
retail_products.push("Charger")
retail_products.push("Speaker")
retail_products.push("Mouse")
retail_products.push("Keyboard")
retail_products.push("Laptop")
retail_products.size()
retail_products.peek()
retail_products.show_stack()
retail_products.pop()
retail_products.pop()
retail_products.pop()
retail_products.size()
retail_products.show_stack()