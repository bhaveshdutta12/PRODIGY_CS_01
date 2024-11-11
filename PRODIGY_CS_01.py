# Function to apply Caesar Cipher encryption
def encrypt_message(message, shift_value):
    encrypted_text = ""

    # Iterate over each character in the message
    for letter in message:
        if letter.isalpha():
            # Determine if the character is uppercase or lowercase
            base = ord('A') if letter.isupper() else ord('a')
            # Shift the character and wrap around using modulo
            encrypted_text += chr((ord(letter) - base + shift_value) % 26 + base)
        else:
            # Keep non-letter characters unchanged
            encrypted_text += letter

    return encrypted_text

# Function to decrypt the text
def decrypt_message(message, shift_value):
    return encrypt_message(message, -shift_value)

# Entry point of the program
if __name__ == "__main__":
    msg = input("Enter your text: ")
    shift_value = int(input("Enter the shift amount: "))

    encrypted_text = encrypt_message(msg, shift_value)
    print(f"Encrypted Text: {encrypted_text}")

    decrypted_text = decrypt_message(encrypted_text, shift_value)
    print(f"Decrypted Text: {decrypted_text}")
