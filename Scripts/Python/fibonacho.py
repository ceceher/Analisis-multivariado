fibonacho = [1, 1]
for i in range(2,9):
    fibonacho.append(fibonacho[i - 1] + fibonacho[i - 2])
print(fibonacho)

#List comprehention
[i for i in range(2, 9)]

