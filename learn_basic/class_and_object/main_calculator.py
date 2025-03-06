##### None class example
def func_add(a, b):
    return a + b


def func_subtract(a, b):
    return a - b


#### Class
class Calculator:
    def __init__(self, a, b):
        self.num_1 = a
        self.num_2 = b

    def func_add(self):
        return self.num_1 + self.num_2

    def func_sub(self):
        return self.num_1 - self.num_2

    def complex_function(self):
        return self.func_add() + self.func_sub() * 2


def main():
    # Create a calculator
    cal = Calculator(3, 2)
    print(cal.func_add())
    print(cal.func_add())
    print(func_add(3, 2))


if __name__ == "__main__":
    main()
