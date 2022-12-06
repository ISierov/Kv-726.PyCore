def greet(name):
    """
    Greeting function
    :param name: name of someone
    :return: Nothing
    """
    print(f'Hello, {name}. How are you?')
    return


def factor(n):
    if n == 1:
        return 1
    else:
        return n * factor(n-1)

