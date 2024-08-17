class Caculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        if self.num1 > self.num2:
            return self.num1 / self.num2
        else:
            print("num1 should be greater and equal than num2")

calculate = Caculator(34,45)
print(calculate.add())
print(calculate.subtract())
print(calculate.multiply())
print(calculate.divide())

    