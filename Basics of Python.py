#List of tuples
a = [(1, 2, 3), (4, 5, 6)]
b = []

for i in a:
    d = sum(i)
    b.append(d)

print(b)

#Dictionary
d = {'A': ['a', 'b', 'c'], 'B': ['d', 'e', 'f']}
for i in d['A']:
    for j in d['B']:
        print(i + j)

#List
a = [1, 2, 3]
for i in a:
    for j in a:
        print(str(i) + str(j))
