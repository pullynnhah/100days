# Create the logging_decorator() function 👇
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        function = func.__name__
        positional_arguments = [str(arg) for arg in args]
        keyword_arguments = [f'{key}={value}' for key, value in kwargs.items()
                             ]
        arguments = ', '.join(positional_arguments + keyword_arguments)
        print(f'You called {function}({arguments})')
        print(f'It returned: {func(*args, **kwargs)}')

    return wrapper


# Use the decorator 👇
@logging_decorator
def add(*args, **kwargs):
    return sum(args + tuple(kwargs.values()))


add(1, 2, 3, x=4, y=5)
