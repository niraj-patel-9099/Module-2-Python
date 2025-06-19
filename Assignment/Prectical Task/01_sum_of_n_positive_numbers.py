n=input("Please enter the positive intiger :")
if n.isdigit():     #checked here if input is digit or not. 
    n=int(n)    #converted string input into intiger.
    if n<=0:    
        print("plese entre the positive intiger greater than 0.")
    else:
        total=0
        for i in range(1,n+1):      #used loop to go through ecesry intiger from i to n.
            total+=i 
        print(f"The sum of first {n} positive intiger is :{total} ")
else:
    print("Invelid input, please enter positive intiger.")      #If input is not positive intiger then user needs to enter positive intiger.

'''
sample input/output
input :
positive intiger : 5

output :
0+1+2+3+4+5 = 15

'''