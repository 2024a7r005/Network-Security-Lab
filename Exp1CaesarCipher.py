text = input("Enter the text: ").upper()
key = int(input("Enter the key: "))

def encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            new = (ord(char) - ord("A") + key) % 26
            result += chr(ord("A") + new)
        else:
            result += char

    return result


def decrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            new = (ord(char) - ord("A") - key) % 26
            result += chr(ord("A") + new)
        else:
            result += char

    return result


encrypted = encrypt(text, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypt(encrypted, key))