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


### List Methods
numbers = [ 2,3,4,9,7,5,10,8 ]

numbers.append(6)
print(numbers)

numbers.insert(2,15) # deals with index.
print(numbers)

numbers.remove(5)
print(numbers)

numbers.pop()  # remove last number in list
print(numbers)

numbers.clear() # remove content in list
print(numbers)

####
numbers = [ 2,3,4,9,7,5,10,8,5 ]

print(numbers.index(4))
# print(numbers.index(11)) value error exit with code 1

print(11 in numbers)  # provide boolean output
print(10 in numbers)


print(numbers.count(5)) # count num of characters in that list

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
numbers.append(11)
print(numbers)
print(numbers2)

#### To remove duplicates in list

numbers = [ 2,3,4,2,9,7,5,10,8,5 ]

uniques = []

for num in numbers:
    if num not in uniques:
        uniques.append(num)
print(uniques)








