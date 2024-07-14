import random
import string

def generate_random_password(length=12):
    # Define characters to use in the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation  

    # Combine all characters
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# Example usage:
password = generate_random_password()
print("Generated Password:", password)
