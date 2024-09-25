import random
import string


def password_generator(length):
    pool = string.ascii_letters + string.digits + string.punctuation
    selection = "".join(random.choice(pool) for i in range(length))
    return selection


while True:
    password_length = int(
        input("How many characters should the password be in length?\n")
    )

    if password_length == 0:
        print("Password can't have 0 length. Please enter a valid number.")
    else:
        break

final_result = password_generator(password_length)

print(f"\nYour plain text password is:\n\n{final_result}\n")
