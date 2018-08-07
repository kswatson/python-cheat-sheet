from functools import wraps
# https://docs.python.org/2/library/functools.html

def basic_decorator(func):
    def wrapper(*args, **kwargs):
        print('Called before func!')
        func(*args, **kwargs)
        print('Called after func!')

    return wrapper


@basic_decorator
def basic_decorated_func():
    print('foo')


def advanced_decorator(arg):
    print('Run without call! arg is: {}'.format(arg))
    stored_arg = arg

    def decorator(func):
        def wrapper(*args, **kwargs):
            print('Can hold args: {}'.format(stored_arg))
            func(*args, **kwargs)

        return wrapper

    return decorator


@advanced_decorator(arg='val1')
def advanced_decorated_func():
    print('bar')


def decorator_factory_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Still called before func!')
        return func(*args, **kwargs)

    return wrapper


@decorator_factory_decorator
def wraps_decorated_func():
    return 'foobar'


if __name__ == '__main__':
    basic_decorated_func()
    advanced_decorated_func()

    print('Problem! Decorator __name__ and __doc__ are found instead of decorated method.')
    print('basic_decorated_func.__name__: {}'.format(basic_decorated_func.__name__))

    print('Use @wraps to preserve the original function references.')
    print('wraps_decorated_func.__name__: {}'.format(wraps_decorated_func.__name__))

    print('Still works the same')
    print(wraps_decorated_func())
