"""     **** Capgemini ****

7. Problem Statement - Raj wants to know the maximum marks scored by him in each semester. 
The mark should be between 0 to 100, if it goes beyond the range display "You have entered 
invalid mark."

Sample Input 1:
○ Enter no of semester:
  3
○ Enter no of subjects in 1 semester:
  3
○ Enter no of subjects in 2 semester:
  4
○ Enter no of subjects in 3 semester:
  2
○ Marks obtained in semester 1:
  50
  60
  70
○ Marks obtained in semester 2:
  90
  98
  76
  67
○ Marks obtained in semester 3:
  89
  76

Sample Output 1:
○ Maximum mark in 1 semester: 70
○ Maximum mark in 2 semester  98
○ Maximum mark in 3 semester: 89
"""


sem = int(input("Enter the number of semesters: "))
sub = []

for x in range(sem):
    num_sub = int(input(f"\n Enter the number of subjects in Semester {x+1}: "))
    sub.append(num_sub)

marks = []

for x in range(sem):
    sem_marks = []
    print(f"\n Marks obtained in Semester {x+1}: ")

    for y in range(sub[x]):
        mark = int(input())

        if mark < 0 or mark > 100:
            print("You have entered an invalid mark.")
            exit()
        sem_marks.append(mark)
    marks.append(sem_marks)

print("\n Maximum Marks Obtained: ")

for x in range(sem):
    maxMarks = max(marks[x])
    print(f"Maximum marks in Semester {x+1}: {maxMarks}")
