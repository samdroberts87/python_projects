import string

def cypher(word, shift):
    alphabet = string.ascii_lowercase
    encrypted_text = ""

    for i in word:
        if i == " ":
            encrypted_text += i
        else:
            index = alphabet.find(i)
            new_index = (index + shift) % len(alphabet)
            encrypted_text += alphabet[new_index]
    return encrypted_text

password = str(input("Type the password you want to cypher\n")).lower()
result = cypher(password, 3)

print(f"plain text: {password}\nencrypted text: {result}")