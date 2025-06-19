import random
import string

'''
Problem Statement: 


password Generator :-

input from user:
User ID
Name

Input 2 words  witch should not be less than 2 words.

Add Numbers and Special Charectors 

Lenth of password shout be 8 or more than 8.

Use user Class and store each user details as a tuple.

'''

class user:
    def __init__(self,user_id,name,password):
        self.details=(user_id,name,password)

    def get_details(self):
        return self.details

def generate_password(user_input):
    
        if not user_input or not user_input.strip():
             print("Input can't be empty.")
             return None
        
        words=user_input.split()
        if len(words)<2:
            print("Enter at least 2 words.")
            return None 
        selected_words=random.sample(words,min(3,len(words)))
        base_password=''.join(selected_words)

        number=''.join(random.choices(string.digits,k=2))
        special=''.join(random.choices('!@$#%&*^()',k=2))

        base_password=base_password.capitalize() + number + special

        while len(base_password)<=8:
            base_password+=random.choice(string.digits+'!@#$%^&*()')

        return base_password

    


def main():
    user_id=input("Please Enter Your user ID: ")
    name=input("Please Enter your Name: ")
    user_input=input("Please enter 2 words(separated by space): ")

    password=generate_password(user_input)
    if password:
        new_user = user(user_id,name,password)
        print("user details created successfully!!")
        print("User detrials : ",new_user.get_details())
    
    else:
        print("Failed to creat a strong password.")

main()
