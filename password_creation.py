import random
import string
def password_generate():
    a = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
    print(a)
password_generate()
