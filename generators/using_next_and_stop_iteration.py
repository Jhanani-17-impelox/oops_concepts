def simple():
    yield "A"
    yield "B"

g = simple()

print(next(g))  # A
print(next(g))  # B
# print(next(g))  # Raises StopIteration



