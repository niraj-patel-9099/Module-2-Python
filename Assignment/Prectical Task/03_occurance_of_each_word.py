#Aske the user to entre the sentence
user=input("Enter a sentence : ")

#split sentance into words (separated by space)
words=user.split()
#created empty dictionary to store word count
word_count={}
#loop through each word in the list
for i in words:
    #if word is already in dictionary, increase it's count by 1
    if i in word_count:
        word_count[i]+=1
    #if word is not in dictionary, add it with count 1
    else:
        word_count[i]=1
#loop through the dictionary items (owrd and count) and print
for word, count in word_count.items():
    print(f"{word}:{count}")

'''
semple input/output :

input : Python is easy language and Python is fun to use.

output:
Python:2
is:2
easy:1
language:1
and:1
fun:1
to:1
use:1

'''