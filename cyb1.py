def caesar_cipher(text, shift):
    """
    Encrypts or decrypts the given text using the Caesar Cipher algorithm.
    :param text: The input text (string).
    :param shift: The shift value (integer).
    :return: The encrypted or decrypted text.
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Determine whether to shift left or right based on the shift value
            shift_direction = 1 if shift >= 0 else -1
            # Convert the character to uppercase for consistency
            char = char.upper()
            # Calculate the new character position
            new_pos = (ord(char) - ord('A') + shift) % 26
            # Convert back to the corresponding letter
            new_char = chr(ord('A') + new_pos)
            # Apply the shift direction
            result += new_char if shift_direction == 1 else new_char.lower()
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    return result

def main():
    try:
        message = input("Enter your message: ")
        shift_value = int(input("Enter the shift value (positive for encryption, negative for decryption): "))
        encrypted_message = caesar_cipher(message, shift_value)
        print(f"Encrypted/Decrypted message: {encrypted_message}")
    except ValueError:
        print("Invalid input. Please enter a valid shift value (integer).")

if __name__ == "__main__":
    main()
