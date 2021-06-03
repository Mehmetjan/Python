def hello_decorator(func):
    def inner(*args, **kwargs):
        print ("before execution")

        returned_value = func(*args, **kwargs)
        print("after executeion")

        return returned_value

    return inner1

@hello_decorator
def sum_two_numbers(a,b):
    print("inside the fucntion")
    return a + b
a, b=1,2

print("Sum = ", sum_two_numbers(a,b))