import random
import string

length=int(input("Enter the length of the password :"))
characters=string.ascii_letters+string.digits

password=''
for i in range(length):
    password+=random.choice(characters)

pass2=list(password)
random.shuffle(pass2)
password="".join(pass2)

print("Generated password :",password)