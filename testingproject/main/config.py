import random
EMAIL = 'example@gmail.com'
PASSWORD = 'password'
def generate_unique_code():
    code = ''.join(random.choice('0123456789') for _ in range(6))
    return code