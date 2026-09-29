import string

print("--- Password Checker ---")
print("Requirements: 8+ characters, 1 uppercase, 1 lowercase, 1 number, and 1 special character.")

while True:
    password = input("\nEnter a password (or type 'exit' to quit): ")

    if password.lower() == 'exit':
        print("Exiting program.")
        break


    char_count = 0
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False


    for char in password:
        char_count += 1

        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_special = True


    if char_count < 8:
        print("Error: Password must be at least 8 characters long.")

    elif not has_upper:
        print("Error: Password must contain at least one uppercase letter (A-Z).")

    elif not has_lower:
        print("Error: Password must contain at least one lowercase letter (a-z).")

    elif not has_digit:
        print("Error: Password must contain at least one number (0-9).")

    elif not has_special:
        print("Error: Password must contain at least one special character (e.g., ! @ # $ %).")

    else:
        print("Success! Your password meets all security requirements.")
        break