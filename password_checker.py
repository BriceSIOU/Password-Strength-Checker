import string

def check_password_strength(password):
    #Criteria
    min_length = 8
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # the length
    if len(password) < min_length:
        return "Weak password, it must be longer than 8 characters"
    
    # check each character
    for char in password:
        if char in string.ascii_uppercase:
            has_upper = True
        elif  char in string.ascii_lowercase:
            has_lower = True
        elif char in string.digits:
            has_digit = True
        elif char in special_chars:
            has_special = True

    # Evaluation of the strength
    if has_special and has_digit and has_lower and has_upper:
        return  "You enter a strong password"
    else:
        missing = []
        if not has_digit:
            missing.append("Add at least one digit in your password")
        if not has_lower:
            missing.append("Add at least one lowercase in your password")                       
        if not has_upper:
            missing.append("Add at least one upercase in your password")   
        if not has_special:
            missing.append("Add at least one special in your password")   
        return f"Recommandation for a good password: {', '.join(missing)}." 

#User input and password test

password = input("Enter a password to check its strength: ")
result = check_password_strength(password)
print(result)           