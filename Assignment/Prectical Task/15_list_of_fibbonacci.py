num=int(input("Enter the number :"))
p1=0
p2=1
print("Fibonacci series: ",end=" ")
for i in range(num):
    print(p1,end=" ")
    p1,p2=p2 ,p1+p2



