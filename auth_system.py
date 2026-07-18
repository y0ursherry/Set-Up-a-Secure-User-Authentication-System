import hashlib
import os
import pyotp

# Simple database (in-memory)
users_db = {}

def register_user(username, password):
    if username in users_db:
        print("\n Username already exists!")
        return
    
    # Password hashing with Salt (Security Best Practice)
    salt = os.urandom(16)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    
    # 2FA Secret Key generation
    totp_secret = pyotp.random_base32()
    
    # Store in our local "database"
    users_db[username] = {
        'salt': salt,
        'password': hashed_password,
        'totp_secret': totp_secret
    }
    
    print(f"\n User '{username}' successfully registered!")
    print(f" Your 2FA Secret Key is: {totp_secret}")
    print(" Add this key to an authenticator app (like Google Authenticator) or save it.")

def login_user(username, password):
    if username not in users_db:
        print("\n Username not found!")
        return False
    
    # Verify Password
    user_data = users_db[username]
    salt = user_data['salt']
    stored_password = user_data['password']
    
    input_hashed = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    
    if input_hashed != stored_password:
        print("\n Incorrect password!")
        return False
    
    print("\n Password verified! 2FA authentication required.")
    
    # 2FA Verification
    totp = pyotp.TOTP(user_data['totp_secret'])
    # For testing, we print the current valid OTP so it's easy to demonstrate
    print(f" (Testing Tip): Current valid OTP is: {totp.now()}")
    
    user_otp = input(" Enter the 6-digit OTP from your app: ")
    
    if totp.verify(user_otp, valid_window=1):
        print("\n Access Granted! Welcome to the secure system.")
        return True
    else:
        print("\n Invalid OTP! Access Denied.")
        return False

# Main Menu Loop
while True:
    print("\n--- SECURE AUTHENTICATION SYSTEM ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Select an option (1-3): ")
    
    if choice == '1':
        uname = input("Enter new username: ")
        pword = input("Enter new password: ")
        register_user(uname, pword)
    elif choice == '2':
        uname = input("Enter username: ")
        pword = input("Enter password: ")
        login_user(uname, pword)
    elif choice == '3':
        print("\nGoodbye!")
        break
    else:
        print("\n Invalid choice, please try again.")