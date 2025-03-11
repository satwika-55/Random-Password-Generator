import random 
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()"

len = int(input("Enter the length of the password"))

a = "".join(random.sample(password,len))

print("Your password is",a)

