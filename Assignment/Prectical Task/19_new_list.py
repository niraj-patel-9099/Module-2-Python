def new_list(lst):
    unique_num_lst=[]
    for i in lst:
        if i not in unique_num_lst:
            unique_num_lst.append(i)
    return unique_num_lst

lst=[1,1,2,2,2,3,4,4,5,5]
print("The unique list is: ",new_list(lst))
