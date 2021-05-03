# 1. Create a decorator named singleton. When applied to a class this
# decorator should make sure that only one instance of that class exists.

def singleton(cls):
    instance = None
    def wrapper(*args, **kwargs):
        nonlocal instance
        if instance == None:
            instance = cls(*args, **kwargs)
        return instance
    return wrapper

class X:
    pass

@singleton
class Y:
    pass


x1 = X()
x2 = X()
x3 = X()

y1 = Y()
y2 = Y()
y3 = Y()

print(id(x1), id(x2), id(x3))
print(id(y1), id(y2), id(y3))

# 2. We had made this decorator function to count the number of calls.
# Instead of this create a decorator class.

def counter(fn):
    def wrapper():
        wrapper.number_of_calls += 1
        return fn()
    wrapper.number_of_calls = 0
    return wrapper

# Answer:
from functools import update_wrapper


class CountNumberOfCalls:
    def __init__(self,fn):
        update_wrapper(self, fn)
        self.func = fn
        self.number_of_calls = 0

    def __call__(self, *args, **kwargs):
        self.number_of_calls += 1
        return self.func(*args, **kwargs)


@CountNumberOfCalls
def func1():
    print('Hey hey')


func1()
func1.number_of_calls
func1()
func1.number_of_calls
func1()
func1.number_of_calls

# 3. In a class decorator, how will you copy the metadata of the original function using the wraps decorator.

# In dunder init method add following line

wraps(fn) (self)


# 4. Write a decorator class named Logger that logs a function call to a file.
# Take a class variable named log_file and give it the value 'log.txt'.

class Logger:
    log_file = 'log_class.txt'

    def __init__(self,fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        from time import ctime
        with open(Logger.log_file,'a') as fout:
            fout.write(f'{self.fn.__name__} called at {ctime()}\n')
        return self.fn(*args,**kwargs)

@Logger
def func1(x,y):
    print(x,y)

func1(2,3)
func1(5,6)

Logger.log_file = 'log_class2.txt'

func1(7,8)

# 5. Change the class decorator Logger such that it takes the name of the log file as argument.


class Logger:
    def __init__(self,log_file):
        self.log_file = log_file

    def __call__(self, fn):
        def wrapper(*args, **kwargs):
            from time import ctime
            with open(self.log_file,'a') as fout:
                fout.write(f'{fn.__name__} called at {ctime()}\n')
            return fn(*args,**kwargs)
        return wrapper


@Logger('log_class3.txt')
def func1(x,y):
    print(x,y)


func1(1,2)


# 6. Change the Logger class made in the previous question so that it can be disabled or enabled.

class Logger:
    enable = True

    def __init__(self,log_file):
        self.log_file = log_file

    def __call__(self, fn):
        if Logger.enable is True:
            def wrapper(*args, **kwargs):
                from time import ctime
                with open(self.log_file,'a') as fout:
                    fout.write(f'{fn.__name__} called at {ctime()}\n')
                return fn(*args,**kwargs)
            return wrapper
        else:
            return fn

@Logger('log_class4.txt')
def func1(x,y):
    print(x,y)

func1(1,2)

Logger.enable = False

@Logger('log_class5.txt')
def func2(x,y):
    print(x,y)

func2(2,3)


# 7. Write a class decorator named Accepts that takes arguments, these arguments specify the types
# of the arguments that the decorated function can take.


class Accepts:
    def __init__(self, *other_args):
        self.other_args = other_args

    def __call__(self,fn):
        def wrapper(*args, **kwargs):
            if kwargs:
                print('Keyword arguments not allowed')

            for argument, type in zip(args, self.other_args):
                if not isinstance(argument, type):
                    raise ValueError('Invalid argument type')
            return fn(*args)
        return wrapper


@Accepts(str,int)
def func(x,y):
    print(x,y)


func('abc',5)
func(4,'abc')

