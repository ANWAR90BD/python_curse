
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):

    try:
        return a / b
    except ZeroDivisionError as a:
        print(a)

if __name__ == '__main__':
    print("This is my program...")

    result = add(20, 30)
    print(result)
