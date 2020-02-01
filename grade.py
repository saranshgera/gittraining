#write a program to input marks of 5 subjects and then calculate total marks, percentage and grade of the student
sub1=int(input("enter the marks of subject 1:"))
sub2=int(input("enter the marks of subject 2:"))
sub3=int(input("enter the marks of subject 3:"))
sub4=int(input("enter the marks of subject 4:"))
sub5=int(input("enter the marks of subject 5:"))
total_marks=sub1+sub2+sub3+sub4+sub5
print("total marks achieved:",total_marks)
percentage=total_marks/5
print("percntage of marks secured=",percentage)
if percentage>=85:
    print("your grade:A")
elif percentage<85 and percentage>70:
    print("your grade:B")
elif percentage<70 and percentage>60:
    print("your grade:C")
else:
    print("your grade:D")
