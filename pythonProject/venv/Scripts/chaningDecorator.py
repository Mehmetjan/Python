def decor1(func):
    def inner():
        x = funx()
        return x*x
    return inner

def decor(func):
    def inner():
        x =func()
        return 2*x
    return inner


@decor1
@decor

def dnum():
    return 10

print(num())
