import random
import string
password_length=10
charValues= string.ascii_letters +string.punctuation+string.digits
password=" "
for i in range(password_length):
           password+=(random.choice(charValues))

print("my random generated password: ",password)        
# 
# #list comprehension   
result="".join([random.choice(charValues) for i in range(password_length)])
print("random password through list: ",result)