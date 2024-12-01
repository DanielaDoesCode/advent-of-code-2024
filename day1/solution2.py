#We have to pair the lowest numbers from the right with the lowest numbers from the left and organize them.
#We can do this by sorting the list and then pairing the numbers.
numbers_left = []
numbers_right = []

with open("input1.txt") as f:
    for line in f:
        left, right = map(int, line.split())
        numbers_left.append(left)
        numbers_right.append(right)

#sort both lists
numbers_left.sort()
numbers_right.sort()

#find the total distance between them
times_appeared = []
#initialize the list with zeros
for i in range(len(numbers_left)):
    times_appeared.append(0)

#find how many times each appears
for i in range(len(numbers_left)):
    for j in range(len(numbers_right)):
        if numbers_left[i] == numbers_right[j]:
            times_appeared[i] += 1

for i in range(len(numbers_left)):
    print(numbers_left[i], "appeared", times_appeared[i], "times")
    numbers_left[i] = (numbers_left[i] * times_appeared[i])

print("Total similarity score: ", sum(numbers_left))