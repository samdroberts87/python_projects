import random
import string

def password_generator(length):
    pool = string.ascii_letters + string.digits + string.punctuation
    selection = "".join(random.choice(pool) for i in range(password_length))
    return selection

password_length = int(input("How many characters should the password be in length?\n"))
final_result = password_generator(password_length)

print(f"\nyour plain text password is:\n\n{final_result}\n")