scores = [45, 92, 78, 61, 88, 34, 95, 72, 55, 83]

# First step the average grade

sum_marks = 0 
for num in scores:
    sum_marks += num

average_score = sum_marks / len(scores)

print(average_score)

# Second step the lowest and highest grades

# scores.sort()
# print(f"The lowest grade is {scores[0]}\n\nThe highest one is {scores[-1]}")

# Third step new list with only scores above average

average_list = []

for num in scores:
    if num >= average_score:
        average_list.append(num)
    
print("List of the grades above avarage --->", average_list)

# Step 4: bubble algorithm which sorts a list of grades above the average

n = len(average_list)

for i in range(n-1):
    for j in range(n-i-1):
        if average_list[j] > average_list[j+1]:
            average_list[j], average_list[j+1] = average_list[j+1], average_list[j]

print(f"Sorted average list: {average_list}")