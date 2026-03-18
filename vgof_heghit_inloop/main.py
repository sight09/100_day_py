#------avg of heghit in loop------------ 

student_heghit = input("enter the list of the student heghit ").split()
a = 0
for n in range(0, len (student_heghit)):
    student_heghit[n] = int (student_heghit[n])
print(student_heghit)
for m in student_heghit:
    a += m
print(a/len(student_heghit))


