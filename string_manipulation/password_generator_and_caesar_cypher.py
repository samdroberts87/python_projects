import random
import string


def password_generator(length):
    pool = string.ascii_letters + string.digits + string.punctuation
    selection = "".join(random.choice(pool) for i in range(password_length))
    return selection


while True:
    password_length = int(
        input("How many characters should the password be in length?\n")
    )

    if password_length == 0:
        print("Password can't have 0 length. Please enter a valid number.")
    else:
        break
password_result = password_generator(password_length)


def cypher(word, shift):
    alphabet = string.ascii_lowercase
    encrypted_text = ""

    for i in word:
        if i == " " or i in string.digits or i in string.punctuation:
            encrypted_text += i
        else:
            index = alphabet.find(i)
            new_index = (index + shift) % len(alphabet)
            encrypted_text += alphabet[new_index]
    return encrypted_text


password = str(password_result.lower())
final_result = cypher(password, 3)

print(f"plain text: {password}\nencrypted text: {final_result}")
