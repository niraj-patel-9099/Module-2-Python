user=int(input("Please enter elemetns: "))
lst_num=[]

for i in range(user):
    items=input(f"entr the number{i+1}: ")
    lst_num.append(items)
print(lst_num)

unique_lst=[]
for i in lst_num:
   if i not in unique_lst:
       unique_lst.append(i)
       
print("The unique value:", unique_lst)
