# 1. Write a decorator which ensures that the first argument
# received by the function is a string.

def first_arg_string(fn):
    def wrapper(*args, **kwargs):
        if not args:
            raise ValueError('There should be at least one positional argument.')
        if not isinstance(args[0],str):
            raise ValueError('First argument should be a string.')
        return fn(*args, **kwargs)
    return wrapper

@first_arg_string
def func1(x,y,z):
    print(x,y,z)


func1()
func1(1,2,3)
func1('abcd',2,3)

# 2.  Write a decorator which ensures that the return
# value of a function is not zero.


def return_not_zero(fn):
    def wrapper(*args,**kwargs):
        result = fn(*args, **kwargs)
        if result == 0:
            raise ValueError('Return value cannot be zero.')
        return result
    return wrapper


@return_not_zero
def func1(x,y):
    return x+y


func1(1,-1)
func1(2,3)

# 3. Write a decorator that changes all the string arguments
# to lower case and all integer arguments to their absolute values.

def str_lower_int_abs(fn):
    def wrapper(*args, **kwargs):
        new_args=[]
        for value in args:
            if isinstance(value, str):
                new_args.append(value.lower())
            elif isinstance(value,int):
                new_args.append(abs(value))
            else:
                new_args.append(value)

        for key, value in kwargs.items():
            if isinstance(value,str):
                kwargs[key] = value.lower()
            elif isinstance(value, int):
                kwargs[key] = abs(value)
        return fn(*new_args,**kwargs)
    return wrapper


@str_lower_int_abs
def func1(a,b,c,d):
    print(a,b,c,d)


func1(-5,'ABCD',c=-10,d='jdhIHDAljaklJ')



# 4. Write a decorator that make a function accept only keyword arguments.
# Is there any other way of achieving this.

def kwargs_check(fn):
    def wrapper(*args,**kwargs):
        if args:
            raise ValueError('Positional arguments not allowed.')
        return fn(*args,**kwargs)
    return wrapper

@kwargs_check
def func1(x,y,z):
    print(x,y,z)


func1(1,2,3)
func1(x=1,y=2,z=3)


# Another way of enforcing kwargs is:

def func2(*,x,y,z):
    print(x,y,z)


func2(1,2,3)
func2(x=1,y=2,z=3)

# 5. Write a decorator that converts the return value from a list to
# a string that contains all the values of that list separated by commas.
#
# Write another decorator that converts the return value from a comma
# separated string of values to a list.

def list_to_string(fn):
    def wrapper(*args,**kwargs):
        result = fn(*args, **kwargs)
        result = [str(value) for value in result]
        result = ','.join(result)
        return result
    return wrapper


def string_to_list(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        result = result.split(',')
        return result
    return wrapper


@list_to_string
def func1():
    return [5.5,1,'abc','XYZ',2.56]

@string_to_list
def func2():
    return 'Joe,22.5,Ann, 10.56'

func1()
func2()

# 6. Write a decorator that appends a line to the docstring of a function.
# This will be a simple decorator that doesn't need to define any inner
# function. It should just modify the docstring and return the original
# function back.

def modify_doc(fn):
    if fn.__doc__:
        fn.__doc__ += ('\nThis is a new line.')
    else:
        fn.__doc__ = '\nThis is a new line.'
    return fn


@modify_doc
def func1():
    print('Hey hey')

@modify_doc
def func2():
    '''This is docstring for func2.'''
    print('Hey hey')


print(func1.__doc__)
print(func2.__doc__)


# 7. Write a decorator that adds a new attribute named author to any
# function that it decorates.

def add_att_author(fn):
    fn.__author__ = 'Joe Smith'
    return fn

@add_att_author
def func1():
    pass

print(dir(func1))


# 8. Write a decorator named timer to calculate the time taken by a
# function to execute. Apply this decorator to the built in sum function.


def timer(fn):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f'Execution time of {fn.__name__}: {end - start} seconds')
        return result
    return wrapper


sum = timer(sum)
x = sum([x for x in range(99999)])
print(x)

# 9. Write a decorator that executes the function after a delay of 5 seconds.

def delayed_execution(fn):
    def wrapper(*args, **kwargs):
        import time
        time.sleep(5)
        result = fn(*args, **kwargs)
        return result
    return wrapper


@delayed_execution
def func1():
    print("Executed")


func1()