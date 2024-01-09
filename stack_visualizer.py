import traceback

def display_call_stack():
    stack = traceback.extract_stack()
    for entry in stack:
        print(f"Function: {entry.name}, Line: {entry.lineno}")

def foo():
    print("Entering foo()")
    display_call_stack()
    print("Exiting foo()")

def bar():
    print("Entering bar()")
    display_call_stack()
    foo()
    print("Exiting bar()")

bar()
