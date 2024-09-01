student_scores= [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 86]

# Sum all the numbers in list
sum= 0
for score in student_scores:
    sum += score

print(sum)

# Find the maximum number in list
max_score= 0
for score in student_scores:
    if score > max_score:
        max_score= score

print(max_score)