def function1(**kwargs):
    print(kwargs)
    print(type(kwargs))


def function2(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


def function3(**kwargs):
    print(kwargs['add'])
    print(kwargs['mul'])


def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['mul']
    print(f'n is {n}')


function1(add='Addition', mul='Multiplication')
print()

function2(add='Addition', mul='Multiplication')
print()

function3(add='Addition', mul='Multiplication')
print()

calculate(2, add=3, mul=5)
