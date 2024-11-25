# password_reset_script.py

import re

def authenticate_user():
    print("\nWelcome to the Password Reset Tool!")
    username = input("Enter your username: ")
    if username.strip():
        print("User authenticated successfully.")
        return True
    else:
        print("Invalid username. Please try again.")
        return False

def validate_security_question():
    security_answer = input("What is the name of your first pet? ")
    if security_answer.lower() == "fluffy":
        print("Security question answered correctly.")
        return True
    else:
        print("Incorrect answer. Please try again.")
        return False

def validate_password(password):
    password_regex = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if re.match(password_regex, password):
        return True
    return False

def reset_password():
    while True:
        new_password = input("Enter your new password: ")
        if validate_password(new_password):
            confirm_password = input("Confirm your new password: ")
            if new_password == confirm_password:
                print("Password reset successfully!")
                break
            else:
                print("Passwords do not match. Please try again.")
        else:
            print("Password does not meet complexity requirements.")
            print("Requirements: Minimum 8 characters, at least one letter, one number, and one special character.")

def main():
    if authenticate_user():
        if validate_security_question():
            reset_password()
        else:
            print("Security question validation failed. Exiting tool.")
    else:
        print("Authentication failed. Exiting tool.")

if __name__ == "__main__":
    main()
