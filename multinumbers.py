from rich import print

a = [ [ [], [], [ [] ] ] ]

print(a)

b = [[] for _ in range(4)]
print(b)

a.extend(b)

print(a)
