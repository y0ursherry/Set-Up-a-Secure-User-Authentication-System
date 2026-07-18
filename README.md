# Set-Up-a-Secure-User-Authentication-System
# Task 3: Secure User Authentication System with 2FA

A Python-based secure authentication system developed as part of my Cybersecurity Internship at Internee.pk.

## 🛡️ Security Features Covered
* **Password Hashing:** Implemented secure password hashing using `PBKDF2` with `SHA-256` to prevent plain-text credential leaks.
* **Salting:** Generated a unique 16-byte cryptographic salt per user to defend against rainbow table attacks.
* **Two-Factor Authentication (2FA):** Integrated Time-based One-Time Passwords (TOTP) using `pyotp` for secondary verification.

## 🚀 Technologies Used
* Python 3
* `hashlib` & `os` (Built-in standard libraries)
* `pyotp` (TOTP library)
* `cryptography` (Cryptographic recipes)

## 📋 How to Run
1. Install dependencies:
   ```bash
   pip install pyotp cryptography
