def infinite_counter():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_counter()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
print(next(gen))  # 4
print(next(gen))  # 5
print(next(gen))  # 6
print(next(gen))  # 7
print(next(gen))  # 8
print(next(gen))  # 9
print(next(gen))  # 10
print(next(gen))  # 11
print(next(gen))  # 12
print(next(gen))  # 13
print(next(gen))  # 14
print(next(gen))  # 15  
print(next(gen))  # 16
print(next(gen))  # 17
print(next(gen))  # 18
print(next(gen))  # 19
print(next(gen))  # 20
print(next(gen))  # 21
