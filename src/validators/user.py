from fastapi import HTTPException, status
import re

def validate_passwords(password: str, confirm_password: str):
    errors = []
    
    rules = [
        (r".{8,}", "Password must be at least 8 characters long."),
        (r"[A-Z]", "Password must contain at least one uppercase letter."),
        (r"[a-z]", "Password must contain at least one lowercase letter."),
        (r"[0-9]", "Password must contain at least one digit."),
        (r"[!@#$%^&*(),.?\":{}|<>]", "Password must contain at least one special character.")
    ]

    for pattern, message in rules:
        if not re.search(pattern, password):
            errors.append(message)
    
    if password != confirm_password:
        errors.append("Passwords do not match.")
    
    if errors:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="; ".join(errors)
        )

def validate_email_format(email: str):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    print("toto")
    if not re.match(email_regex, email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid email format."
        )
