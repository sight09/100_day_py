
#----------highest score-------------- 

score = input("input the list of the student ").split()

for n in range(0, len(score)):
    score[n] = int(score[n])
print(score)
highest_score = 0
for n in score:
    if n > highest_score:
        highest_score = n
print(f"the highest score is  {highest_score}")


