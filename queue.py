def push(stack: list,value):
    stack.append(value)

def pop(stack:list):
    return stack.pop()

def peek(stack:list):
    return stack[-1]


def is_empty(stack:list):
    return len(stack)==0

my_stack = []
push(my_stack, 10)
push(my_stack, 14)
push(my_stack, 15)
push(my_stack, 1)
push(my_stack, 2)
push(my_stack, 55)  
pop(my_stack)
peek(my_stack)
print(is_empty(my_stack))