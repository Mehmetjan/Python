def hello_decorator(func):
    def inner1():
        print("hello, this is my function execution: ")

        func()

        print("this is after fucntion execution:")
    return inner1



def function_to_be_used():
        print("this is inside the function!!")

function_to_be_used = hello_decorator(function_to_be_used )
function_to_be_used()

time. clock()