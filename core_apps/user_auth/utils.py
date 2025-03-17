import random
import string
import secrets

def generate_otp(length: int = 6) -> str:
    return ''.join(random.choices(string.digits, k=length))


print(generate_otp(6))

def generate_secure_otp(length: int = 6) -> str:
    return ''.join(secrets.choice(string.digits) for _ in range(length))

print(generate_secure_otp())  # Cryptographically secure OTP
