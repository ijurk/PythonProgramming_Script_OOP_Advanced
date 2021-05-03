# 1. Modify the add_to_docstring decorator that you had
# created in the last exercise so that it can add different
# strings to docstrings of different functions.

def add_to_docstring(string):
    def actual_decorator(fn):
        if fn.__doc__:
            fn.__doc__ += string
        else:
            fn.__doc__ = string
        return fn
    return actual_decorator


@add_to_docstring('This is the new docstring.')
def func1():
    print('Hey hey')

@add_to_docstring('\nThis is an additional line.')
def func2():
    '''This is docstring for func2.'''
    print('Hey hey')


print(func1.__doc__)
print(func2.__doc__)


# 2. Modify the decorator delay_execution that you had created
# in the last exercise, such that it delays execution for a
# specified number of seconds.

def delayed_execution(n):
    def actual_decorator(fn):
        def wrapper(*args, **kwargs):
            import time
            print(f'Delaying execution by {n} seconds.')
            time.sleep(n)
            result = fn(*args, **kwargs)
            return result
        return wrapper
    return actual_decorator


@delayed_execution(5)
def func1():
    print("Executed")

@delayed_execution(10)
def func2():
    print("Executed")


func1()
func2()

# 3. Write a decorator factory that takes variable number of positional arguments.
# These arguments denote the allowed values for the first argument of the function
# that is to be decorated.
from functools import wraps

def allowed_first_arg(*outer_args):
    def actual_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if not args:
                raise ValueError('There should be at least one positional argument')
            if args[0] not in outer_args:
                raise ValueError(f'First argument must be one of these values {outer_args}')
            return fn(*args, **kwargs)
        return wrapper
    return actual_decorator


@allowed_first_arg(1,2,3)
def func1(x,y,z):
    print(x,y,z)


func1(3,5,6)
func1(x=2,y=5,z=6)
func1(6,9,8)


@allowed_first_arg('abc','def')
def func2(x, y):
    print(x, y)


func2('abc','jkoh')
func2('nji','abc')

# 4. Modify this decorator such that it takes as argument the file to which the
# information is written. The default value for the parameter should be log.txt.
from functools import wraps

def logger(filename='log.txt'):
    def actual_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            from time import ctime
            with open(filename,'a') as fout:
                fout.write(f'{fn.__name__} called at {ctime()}\n')
            return fn(*args, **kwargs)
        return wrapper
    return actual_decorator


@logger()
def func1(x,y):
    print(x,y)


@logger('log2.txt')
def func2(x,y):
    print(x,y)

func1(2,3)
func2(5,6)

# 5.  In the previous exercise(Q 7) we had written a decorator
# that adds a new attribute named author to a function. Now write a
# decorator that can add any number of new attributes to a function.

def add_attribute(**kwargs):
    def actual_decorator(fn):
        for key, value in kwargs.items():
            setattr(fn,key, value)
        return fn
    return actual_decorator


@add_attribute(author='Iva', location='London')
def func1():
    pass

print(dir(func1))


# 6. Modify this timer decorator so that it can be enabled or disabled.
from functools import wraps

def timer(enable=True):
    def actual_decorator(fn):
        if enable is True:
            @wraps(fn)
            def wrapper(*args, **kwargs):
                from time import time
                start = time()
                result = fn(*args, **kwargs)
                end = time()
                print(f'{fn.__name__} took {end - start} seconds')
                return result
            return wrapper
        else:
            return fn
    return actual_decorator

@timer(enable=False)
def func1():
    x = sum([x for x in range(99999)])
    print(x)


@timer()
def func2():
    x = sum([x for x in range(99999)])
    print(x)


func1()
func2()


# 7. Write a decorator that restricts the return value of a function to a few types.

@returns(int, float)  # function can return an int or float only
def func1():
    return 1.2


@returns(list, tuple)  # function can return a list or tuple only
def func2():
    return [1, 3]


@returns(str)  # function can return a string only
def func3():
    return 'abc'

@returns(str)  # function can return a string only
def func4():
    return 5.5


def returns(*outer_args):
    def actual_decorator(fn):
        def wrapper(*args,**kwargs):
            result = fn(*args, **kwargs)
            if not isinstance(result, outer_args):
                raise ValueError(f'Return value can only be: {outer_args}')
            return result
        return wrapper
    return actual_decorator

func1()
func2()
func3()
func4()