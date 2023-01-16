a = {'milk', 'bread', 'jam', 'milk', 'potatoes', 'potatoes', 'pasta'}
fs = frozenset(a)
print(fs)
print(type(a))

b = frozenset([1, 2, 3])
print(b)

c = frozenset('hi my name is')
print(c)