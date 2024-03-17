import re

def assess_password_strength(password):
    length_score = len(password) // 8

    uppercase_score = 1 if re.search(r"[A-Z]", password) else 0
    lowercase_score = 1 if re.search(r"[a-z]", password) else 0
    digit_score = 1 if re.search(r"\d", password) else 0
    special_char_score = 1 if re.search(r"[!@#$%^&*()_+=\-[\]{};:'\"|,.<>?\\]", password) else 0

    total_score = length_score + uppercase_score + lowercase_score + digit_score + special_char_score

    if total_score <= 2:
        strength = "Weak"
    elif total_score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    feedback = (
        f"Length: {'Good' if length_score else 'Poor'}\n"
        f"Uppercase: {'Good' if uppercase_score else 'Poor'}\n"
        f"Lowercase: {'Good' if lowercase_score else 'Poor'}\n"
        f"Digits: {'Good' if digit_score else 'Poor'}\n"
        f"Special Characters: {'Good' if special_char_score else 'Poor'}\n"
    )

    return strength, feedback

def main():
    password = input("Enter your password: ")

    strength, feedback = assess_password_strength(password)

    print(f"Password Strength: {strength}")
    print("Feedback:")
    print(feedback)

if __name__ == "__main__":
    main()
