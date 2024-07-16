# caesar_cipher.py
def encrypt(text, shift):
    result = ""

    # transverse the plain text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# Driver code
if __name__ == "__main__":
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift number: "))
    encrypted_text = encrypt(text, shift)
    print(f"Encrypted Text: {encrypted_text}")

    decrypted_text = decrypt(encrypted_text, shift)
    print(f"Decrypted Text: {decrypted_text}")
