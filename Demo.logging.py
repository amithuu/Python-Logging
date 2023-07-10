

class DemoLogging1:
    def add_numbers(self, a, b):
        return a + b
    
    def multiply_numbers(self, a, b):
        return a * b


dl = DemoLogging1()
sum = dl.add_numbers(3, 5)
print(f"the addition is :{sum}")
multi = dl.multiply_numbers(3, 5)
print(f"the multiply is :{multi}")
