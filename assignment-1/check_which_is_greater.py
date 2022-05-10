# 4. Take 3 values from the user and find the greatest among all
num_1 = int(input( "ENTER THE FIRST NUMBER OF YOUR CHOICE : "))
num_2 = int(input( "ENTER THE SECOND NUMBER OF YOUR CHOICE : "))
num_3 = int(input( "ENTER THE THIRD NUMBER OF YOUR CHOICE : "))
if num_1>num_2 and num_1>num_3:
    greatest_num= num_1
elif num_2>num_1 and num_2>num_3:
    greatest_num=num_2 
else:
    greatest_num=num_3
print("The Greatest Number out of the Numbers you entered",num_1,",",num_2,",",num_3," is",greatest_num )
print("Thank you")