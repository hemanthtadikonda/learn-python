names = ["Jhon","Bob","Hem","Ram","Baji"]

print(names[-1])
print(names[3])
print(names[2:])
print(names[1:4])
print(names)

numbers = [3,4,1,5,7,11,8,2]

max = numbers[0]

for value in numbers:
    if value > max:
        max = value
    # print(max)
print(max)


## 2D lists

matrix = [
    [1,2,3] ,
    [4,5,6] ,
    [7,8,9]
]

print(matrix[1][2])
matrix[0][0] = 20
print(matrix[0][0])

for row in matrix:
    for item in row:
        print(item)

