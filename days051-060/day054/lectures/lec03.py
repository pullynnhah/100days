def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


def outer_function1():
    print("I'm outer 1")

    def nested_function():
        print("I'm inner 1")

    nested_function()


def outer_function2():
    print("I'm outer 2")

    def nested_function():
        print("I'm inner 2")

    return nested_function


result = calculate(add, 2, 3)
print(result)

result = calculate(sub, 2, 3)
print(result)

result = calculate(mul, 2, 3)
print(result)

result = calculate(div, 2, 3)
print(result)

outer_function1()
inner_function = outer_function2()
inner_function()

