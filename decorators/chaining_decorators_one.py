def deco1(func):
    def wrapper():
        print("Layer 1: deco1")
        func()
    return wrapper

def deco2(func):
    def wrapper():
        print("Layer 2: deco2")
        func()
    return wrapper

def deco3(func):
    def wrapper():
        print("Layer 3: deco3")
        func()
    return wrapper

def deco4(func):
    def wrapper():
        print("Layer 4: deco4")
        func()
    return wrapper

@deco1
@deco2
@deco3
@deco4
def core_function():
    print(">>> Core Logic <<<")

core_function()



# ---visual tree:----
"""
core_function()
└── deco1 wrapper
    └── deco2 wrapper
        └── deco3 wrapper
            └── deco4 wrapper
                └── original core_function()

"""
