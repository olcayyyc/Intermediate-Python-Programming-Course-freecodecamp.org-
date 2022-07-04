#Fonksiyon decorators ve class decorators olarak ikiye ayrılıyor.


#@mydecorator
def dosomething():
    pass


def start_end_decorator(func):
    
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

#Eğer @start_end_decorator olmasaydı start ve end komutu için aşağıdaki koda ihtiyacımız olurdu.
#print_name = start_end_decorator(print_name)
@start_end_decorator
def print_name():
    print("Alex")

print_name()


def add5(x):
    return x + 5

#Bir decoratorun genel yapısı.

import functools
def start_end_decorator(func):
    
    @functools.wraps(func)
    def wrapper(*args, kwargs):
        #Bir şeyler yaptır.
        result = func(*args, **kwargs)
        #Bir şeyler yaptır.
        return result
    return wrapper



import functools
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')

greet('Alex')





import functools
def start_end_decorator(func):
    
    def wrapper():
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k} = {v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper


#decoratorleri stackleyebilirsin. İlk olarak debug sonra start olan çalışır.
@debug
@start_end_decorator
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

say_hello('Alex')


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)

cc = CountCalls(None)

@CountCalls
def say_hello():
    print('Hello')

say_hello()
say_hello()
say_hello()