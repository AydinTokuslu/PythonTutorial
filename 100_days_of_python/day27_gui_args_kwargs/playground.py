def add(*args):  # arguments
    print(args[1])  # tipi tuple dır

    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 5, 6, 2, 1, 7, 4, 3))

def calculate(n, **kwargs):  # key word arguments
    print(kwargs)  # tipi dictionarydir.
    # for key, values in kwargs.items():
    #     print(key)
    #     print(values)
    n += kwargs["add"]
    n += kwargs["multiply"]
    print(n)

calculate(2, add =3, multiply=5)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)
