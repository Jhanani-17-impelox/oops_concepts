def custom():
    value = yield "Start"
    print("Got:", value)

gen = custom()
print(next(gen))       # Start
print(next(gen))       # Start
print(next(gen))       # Start

print(gen.send(42))    # Got: 42 → raises StopIteration after this
