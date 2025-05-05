class UserInput:
    def process(self, name=None, age=None):
        if name and age:
            print(f"User {name} is {age} years old.")
        elif name:
            print(f"User's name is {name}.")
        elif age:
            print(f"User's age is {age}.")
        else:
            print("No information provided.")

user = UserInput()
user.process("John", 30)  
user.process("John")      
user.process(age=25)      
user.process()            #
