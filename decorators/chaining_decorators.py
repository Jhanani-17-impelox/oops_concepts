def shout(func):
    def wrapper():
        print("Before shouting!")
        func()
    return wrapper

def smile(func):
    def wrapper():
        print("Smiling first!")
        func()
    return wrapper

@shout
@smile
def talk():
    print("I am talking!")

talk()



"""

Output:

Before shouting!      ← from shout
Smiling first!        ← from smile
I am talking!         ← from original talk()
"""


"""
talk()
└── shout wrapper        # From @shout
    └── smile wrapper    # From @smile
        └── original talk()
"""
