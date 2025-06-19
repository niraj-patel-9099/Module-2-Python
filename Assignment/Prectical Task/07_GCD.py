number1=int(input("Please enter the number 1 :"))
number2=int(input("Please entr thre number 2 :"))

if number2>number1:
    mn = number1
else :
    mn = number2
for i in range(1, mn+1):
    if number1%i==0 and number2%i==0:
        mn=i
print(f"The GCD of {number1} and {number2} is : {mn}")