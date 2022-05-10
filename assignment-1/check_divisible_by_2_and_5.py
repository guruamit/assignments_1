# 3. Take input from the user and check whether that value is divisible by 2 and 5
num = int (input("Enter the number you want to check : "))
if num % 5==0 and  num % 2==0 :
    print("The number you entered is ",num,".","It is divisible by 2 and 5.")
else:
    print("The number you entered is ",num,".","It is not divisible by both 2 and 5")

print("Thank You") 