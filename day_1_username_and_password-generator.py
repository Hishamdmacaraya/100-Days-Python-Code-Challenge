print("Welcome to the 'Simple Username and Password Generator'")
print(' ')

fname = input("What's is your first name?\n")

print(' ')
lname = input("What's is your last name?\n")

print(' ')
dob = input("When is your birthday? Type in mm/dd/yyyy format.\n")
dob1 = dob[1]
dob2 = dob[6:-1]

print(' ')
soc = input("What is the last 4 digits of your social security number?\n")

import random
import string
characters = string.ascii_letters + string.digits + string.punctuation
random = ''.join(random.choice(characters) for i in range(4))


print(' ')
print("Your Username is: " + fname[0] + "" + lname[0:5] + soc)
print("Your unique password is: " + dob1 + fname[1::2] + "" + dob2 + random)
