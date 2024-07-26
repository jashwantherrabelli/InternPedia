# Password Generator

import secrets
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    """Generate a secure random password."""
    character_pool = ''
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation
    
    if not character_pool:
        raise ValueError("At least one character type must be selected")
    
    password = ''.join(secrets.choice(character_pool) for _ in range(length))
    return password

def get_user_input():
    """Get user input for password generation settings."""
    try:
        length = int(input("Enter the password length: "))
        if length <= 0:
            raise ValueError("Password length must be a positive integer")
        
        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
        
        return length, use_uppercase, use_lowercase, use_digits, use_symbols
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

def main():
    """Main function to run the password generator application."""
    user_input = get_user_input()
    if user_input:
        length, use_uppercase, use_lowercase, use_digits, use_symbols = user_input
        try:
            password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
            print(f"Generated Password: {password}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Failed to get valid input. Exiting the program.")

if __name__ == "__main__":
    main()
