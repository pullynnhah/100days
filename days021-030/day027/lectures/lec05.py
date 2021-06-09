def function(*args):
    print(args[0], args[1])
    print(args)
    print(type(args))
    for n in args:
        print(n, end=' ')
    print()


def add(*args):
    return sum(args)


function(3, 5, 6)

print(add(3, 5, 6))
print(add(3, 5, 6, 2, 1, 7, 4, 3))
