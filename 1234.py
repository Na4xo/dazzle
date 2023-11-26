#Задача A

a = set(input())
b = -1
for i in a:
    b += 1
print(b)

#Задача B

a = [10, 6, 15]
b = [20, 2, 15,10,33]

for i in a:
    for j in b:
        if i == j:
            print(i, j)

#Задача C

a = [234,235,213,12,46,67,123,23,11,5,65]
b = [23,12,42,543,667,87,979,34,67,65]

for i in a:
    for j in b:
        if i == j:
            print(i, j)

#Задача F

with open('text.txt') as f:
    tex = str(f.readlines())

print(len(set(tex.split())))