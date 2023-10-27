#This is a Calculator to calculate Total Marks, Percentage and SGPA/CGPA for students

n=int(input('Enter the number of Subjects: '))
sgpa1=int(input("Enter the SGPA of Previous Semester to Calculate CGPA (If in 1st Semester Press 0): "))
semester=int(input("Enter the Current Semester you Are in (Please Press 1 to 8): "))
lst1=[]
lst2=[]
for i in range(1,n+1):
    a=int(input(f"Enter the Credit Points of Subject {(i)} in a Sequence same as VTU Marks Card: "))
    lst1.append(a)
print("\n")

for i in range(1,n+1):
    b=float(input(f"Enter the Marks of Subject {(i)} in same order as above Credit Points: "))
    lst2.append(b)

print("\n")
print(f"Grade Points: {lst1}")
print(f"Marks: {lst2}")

print("\n")
total_marks_obtained=sum(lst2)
percentage=(total_marks_obtained/(n*100))*100
print(f"Total Marks: {total_marks_obtained}")
print(f"Percentage: {percentage}\n")

total_obt=0
total_points=0
for j in range(n):
    lst2[j]=lst2[j]//10
    lst2[j]=lst2[j]+1
    if lst2[j] == 11:
        lst2[j]=11-1
    total_obt+=lst1[j]*lst2[j]
    total_points+=lst1[j]*(10)

sgpa=(total_obt/total_points)*10
print(f"Total Points Obtained for {n} Subjects: {total_obt}")
print(f"Total Points of {n} Subjects: {total_points}\n")
print(f"SGPA for the {semester} Semester: {sgpa}\n")

cgpa=(sgpa1+sgpa)/semester
print(f"The CGPA of the Course: {cgpa}")






    