class Number:
    def __init__(self, a_number):
        self.a_number = a_number

    def is_even(self):
        return self.a_number % 2 == 0


class SpecialNumber(Number):
    def double_if_even(self):
        if self.is_even():
            return self.a_number * 2
        else:
            return self.a_number
        
    def reset(self,new_number):
        self.a_number = new_number


# Sample Test
n = SpecialNumber(4)
print(n.double_if_even())  
n.reset(50)
print(n.double_if_even())  

n.reset(5)
print(n.double_if_even())  

