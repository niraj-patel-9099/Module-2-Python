def factorial(n):
   if n==1 or n==0:
     return 1
   return n*factorial(n-1)
   
n=int(input("please enter the number: "))
print(f"factorial of {n} : ",factorial(n))