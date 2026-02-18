# there's two methods to work with stack in python

# 1. List method
print('---------List Method------------')
stack = []
stack.append(10)
stack.append(20)
stack.append(30)

# print all element in stack
print(stack)  # 10 20 30

# to see the top of stack
# peek() method
print(stack[-1])  # 30

# delete top element
print(stack.pop())  # removes 30
print(stack)  # 10 20

# 1. build a stack class (better approche)


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


print("--------Class Method---------")
s = Stack()
s.push('A')
s.push('B')
s.push('C')

print(s.peek())
print(s.pop())
print(s.items)
