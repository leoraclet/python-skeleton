import string
import random


chars = string.ascii_letters + string.digits

for _ in range(10):
    
    password = ''.join([random.choice(chars) for _ in range(10)])
    print(password)
