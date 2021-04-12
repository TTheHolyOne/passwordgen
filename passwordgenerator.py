import string
from random import *


print('Welcome to TTheHolyOne password generator!')
input()
while True:
	cq = input('Press Q to quit or C to continue')
	if cq.lower() == 'q':
		break
	elif cq.lower() == 'c':
		pass
	a = int(input('Whats the minimum amount of length the password may have?(Recommended: 8)\n'))
	b = int(input('Whats the longest your password can be?(Recommended: 32)\n'))
	characters = string.ascii_letters + string.punctuation  + string.digits
	password =  "".join(choice(characters) for x in range(randint(a, b)))
	print(str(password))
	print(cq)

print('Shutting down..')