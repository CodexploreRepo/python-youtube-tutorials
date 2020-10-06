# Required Parameter & Default Parameter
def print_name(name, greeting="Welcome Cac Ban"):
    print(f'{name}, {greeting} ')

def codexplore(a, b, c):
    print(a, b, c)

# Variable-length parameters (*args and **kwargs)

# If you mark a parameter with one asterisk (*),
# you can pass any number of positional arguments to your function (Typically called *args)
# If you mark a parameter with two asterisks (**),
# you can pass any number of keyword arguments to this function (Typically called **kwargs).

def varibleLengthArgExample(a, b, *args, **initkwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key, value in initkwargs.items():
        print(key, value)


def main():
    # Positional Arguments
    # codexplore(3, 2, 1)

    # Keyword arguments
    # codexplore(a="Hello World", c="C value", b=2)

    # *args:
    # varibleLengthArgExample('a', 'b', "Hello World", 1, 2, 3)
    # **kwargs:
    varibleLengthArgExample('a', 2, size="Up Size", age="NG")


if __name__ == "__main__":
    main()
