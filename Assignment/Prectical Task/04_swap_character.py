str1, str2=('hello world').split()
str1_swapped=str2[:2] + str1[2:]
str2_swapped=str1[:2] + str2[2:]

result= str1_swapped + " " + str2_swapped
print("result: ",result)
