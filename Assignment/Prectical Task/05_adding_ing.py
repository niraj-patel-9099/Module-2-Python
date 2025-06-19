string=input("Please enter the string (lenth should be more than 3) :")
if len(string) >3: 
    if string.endswith("ing"):
        string = string[:-3] + "ly" #Removed ing and added "ly"
    else :
        string = string + "ing"     #adding ing after all conditions matched.
    print(string)
else:
    print(string)   #stirng will be print as it is beacuse its cantiants 3 or less than 3 cahrecters. 
