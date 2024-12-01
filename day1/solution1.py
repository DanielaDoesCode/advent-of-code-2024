#We have to pair the lowest numbers from the right with the lowest numbers from the left and organize them.
#We can do this by sorting the list and then pairing the numbers.

numbers_left = []
numbers_right = []

with open("day1/input1.txt") as f:
    for line in f:
        left, right = map(int, line.split())
        numbers_left.append(left)
        numbers_right.append(right)

#sort both lists
numbers_left.sort()
numbers_right.sort()

#find the total distance between them

total_distance = 0
for i in range(len(numbers_left)):
    total_distance += abs(numbers_left[i] - numbers_right[i])

print("Total distance of locations: ", total_distance)