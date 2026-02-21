import random
import string

def password_creation(n):
    if  n<5:
        return  manual_password_creation(7)
    else:
         return manual_password_creation(n)
def manual_password_creation(n):
        word=string.ascii_letters+string.digits+string.punctuation
        password="".join(random.choice(word) for _ in range(n))
        return password
   

n=int(input("Enter the length of the password:"))
output=password_creation(n)
print("Generated password:", output)