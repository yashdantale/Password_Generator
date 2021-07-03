#Password Generator
import string
from secrets import choice

#Initialize all the elements i.e characters with punctuation marks, digits, alphabets
elements = string.digits + string.ascii_letters + string.punctuation
#print all the used characters
print(elements)
#generating password
n = int(input("Enter length of Password\n"))
password = "".join(choice(elements)for x in range(0,n))
print(password)





