import random
letters="abcdefghijklmnopqrstuvwxyz"
numbers="1234567890"
special="@#$%&*/()"
chars=special+letters+numbers

print("Your password is:")
password=""
for x in range(16):
    password+=random.choice(chars)

print(password)

#OUTPUT MAY LOOK LIKE THIS:
Your password:
13k4mppx1)(ws&rl
Your Password:
yprdobwyg6*%/6v)
Your password is:
olm50mjp#l7l8ntb
