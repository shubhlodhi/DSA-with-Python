def is_valid_expression(expression):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    
    
    # print(brackets)
    
    for char in expression:
        if char in brackets.keys():
            stack.append(char)
            print("s",stack)
        elif char in brackets.values():
            print("b",char)
            if not stack:
                return False
            top = stack.pop()
            print("t",top)
            if brackets[top] != char:
                print("BT" ,brackets[top])
                print("c",char)
                return False
    
    return len(stack) == 0

# Test cases:
# expression1 = "[(a+b)]"
expression2 = "{(a+b}"
# expression3 = "{[(a+b)*2]/3}"
# expression4 = "{[a+b}*2]/3}"

# print(is_valid_expression(expression1))  # True
print(is_valid_expression(expression2))  # True
# print(is_valid_expression(expression3))  # True
# print(is_valid_expression(expression4))  # False
# In this example, the is_valid_expression function uses a stack to keep track of the opening brackets encountered. It matches each closing bracket with the corresponding opening bracket from the stack. If all brackets are balanced and properly nested, the stack will be empty at the end.

# You can use this function to check the validity of expressions with different types of brackets. Just replace the expression1, expression2, etc., with the expressions you want to test.





