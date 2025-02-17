import re

# Expanded list of common weak passwords
COMMON_PASSWORDS = {
    'password', '123456', '12345678', 'qwerty', 'abc123', 'letmein', 'monkey',
    'football', 'iloveyou', 'admin', 'welcome', 'sunshine', 'password1', '123123',
    '123456789', 'qwerty123', 'dragon', 'baseball', 'superman', 'trustno1'
}


def check_password_strength(password):
    """Evaluates the strength of a given password based on security best practices."""

    strength = {
        'length': len(password) >= 12,
        'lower': bool(re.search(r'[a-z]', password)),
        'upper': bool(re.search(r'[A-Z]', password)),
        'digit': bool(re.search(r'[0-9]', password)),
        'special': bool(re.search(r'[^A-Za-z0-9]', password)),
        'common': password.lower() not in COMMON_PASSWORDS
    }

    # Calculate password score
    score = (
            (2 if strength['length'] else 0) +
            sum(1 for key in ['lower', 'upper', 'digit', 'special'] if strength[key])
    )

    # Determine strength level and provide feedback
    if score >= 7 and strength['common']:
        return "Strong", "Your password is strong. Good job!"
    elif score >= 4:
        suggestions = []
        if not strength['length']:
            suggestions.append("Use at least 12 characters.")
        if not strength['special']:
            suggestions.append("Include a special character (!@#$%^&*).")
        if not strength['digit']:
            suggestions.append("Add at least one number.")
        return "Medium", "Your password is decent, but could be stronger. " + " ".join(suggestions)
    else:
        return "Weak", "Your password is weak. Use a longer password with uppercase, lowercase, numbers, and special characters."


def main():
    print("Password Strength Checker")
    print("-------------------------")
    print("WARNING: This tool is for educational purposes only.")
    print("Do not use it to secure sensitive accounts.\n")

    while True:
        password = input("Enter password (or 'q' to quit): ").strip()
        if password.lower() == 'q':
            print("Exiting program.")
            break

        rating, feedback = check_password_strength(password)
        print(f"\nStrength: {rating}")
        print(f"Feedback: {feedback}\n")


if __name__ == "__main__":
    main()
