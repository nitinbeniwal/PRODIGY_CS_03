import re

def assess_password_strength(password):
    length_check = len(password) >= 8
    uppercase_check = re.search(r'[A-Z]', password) is not None
    lowercase_check = re.search(r'[a-z]', password) is not None
    digit_check = re.search(r'\d', password) is not None
    special_char_check = re.search(r'[@$!%*?&]', password) is not None

    criteria_met = sum([length_check, uppercase_check, lowercase_check, digit_check, special_char_check])
    
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    feedback = {
        "Strength": strength,
        "Length Check": length_check,
        "Uppercase Check": uppercase_check,
        "Lowercase Check": lowercase_check,
        "Digit Check": digit_check,
        "Special Character Check": special_char_check
    }

    return feedback

user_password = input("Enter a password to check its strength: ")
result = assess_password_strength(user_password)


print("\nPassword Strength Assessment:")
print(f"Strength: {result['Strength']}")
print(f"Meets Length Requirement (8 or more characters): {result['Length Check']}")
print(f"Contains Uppercase Letter: {result['Uppercase Check']}")
print(f"Contains Lowercase Letter: {result['Lowercase Check']}")
print(f"Contains Digit: {result['Digit Check']}")
print(f"Contains Special Character: {result['Special Character Check']}")
