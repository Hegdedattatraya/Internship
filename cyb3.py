def check_password_strength(password):
    """
    Checks the strength of a password based on specified criteria.
    :param password: The input password (string).
    :return: A feedback message indicating the strength.
    """
    # Check length
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."

    # Check for uppercase and lowercase letters
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return "Weak: Password should contain both uppercase and lowercase letters."

    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        return "Weak: Password should include at least one digit."

    # Check for special characters
    special_chars = "!@#$%^&*()-+"
    if not any(char in special_chars for char in password):
        return "Weak: Password should have at least one special character."

    return "Strong: Password meets all criteria!"

def main():
    try:
        user_password = input("Enter your password: ")
        strength_feedback = check_password_strength(user_password)
        print(strength_feedback)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
