# 5. Take marks for English, Maths and Science subject and find the total value, percentage and grade on the bases of it
English_marks = int(input( "ENTER THE MARKS YOU HAVE RECEIVED OUT OF 100 IN ENGLISH : "))
Science_marks = int(input( "ENTER THE MARKS YOU HAVE RECEIVED OUT OF 100 IN SCIENCE : "))
Mathemathics_marks = int(input( "ENTER THE MARKS YOU HAVE RECEIVED OUT OF 100 IN MATHS : "))
Total_marks= English_marks +Science_marks +Mathemathics_marks
Percentage= Total_marks/3
print("English Marks", English_marks)
print("Science Marks", Science_marks)
print("Mathematics Marks", Mathemathics_marks)
print("Total Marks Obtained out of 300 is ", Total_marks)
print("Percentage scored is ", Percentage)
if Percentage>=90 and Percentage<=100:
    print("Grade scored by you is A")
if Percentage>=80 and Percentage<90:
    print("Grade scored by you is B")
if Percentage>=70 and Percentage<80:
    print("Grade scored by you is C")
if Percentage>=60 and Percentage<70:
    print("Grade scored by you is D")
if Percentage>=50 and Percentage<60:
    print("Grade scored by you is E")
if Percentage>=40 and Percentage<50:
    print("Grade scored by you is F")
if Percentage>=33 and Percentage<40:
    print("Grade scored by you is E")
if Percentage>=1 and Percentage<33:
    print("Grade scored by you is F")
    print("You are fail.")

print("Thank You")    
    
