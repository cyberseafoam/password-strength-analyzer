def check_length(password):
    """
    Check if a password has at least 12 characters.
    """
    return len(password) >= 12


def check_uppercase(password):
    """
    Check if a password contains an uppercase letter.
    """
    for character in password:
        if character.isupper():
            return True
    return False


def check_lowercase(password):
    """
    Check if a password contains a lowercase letter.
    """
    for character in password:
        if character.islower():
            return True
    return False


def check_number(password):
    """
    Check if a password contains a number.
    """
    for character in password:
        if character.isdigit():
            return True
    return False


def check_special(password):
    """
    Check if a password contains a special character.
    """
    special_characters = '!@#$%^&*()-_+=?'
    for character in password:
        if character in special_characters:
            return True
    return False


def check_common(password):
    """
    Check if a password is a common password.
    """
    common_passwords = ['password','password123','123456','12345678','qwerty','admin','letmein','welcome']
    return password.lower() in common_passwords


def calculate_score(password):
    """
    Calculate a password strength score.
    """
    if check_common(password):
        return 0
    score = 0
    if len(password) >= 8:
        score += 20
    if check_length(password):
        score += 20
    if len(password) >= 16:
        score += 20
    if check_uppercase(password):
        score += 10
    if check_lowercase(password):
        score += 10
    if check_number(password):
        score += 10
    if check_special(password):
        score += 10
    return score


def get_rating(score):
    """
    Return the strength rating based on the score.
    """
    if score < 40:
        return 'Weak'
    elif score < 80:
        return 'Moderate'
    else:
        return 'Strong'


def get_suggestions(password):
    """
    Return a list of suggestions to improve a password.
    """
    suggestions = []
    if check_common(password):
        suggestions.append('Avoid common passwords.')
    if not check_length(password):
        suggestions.append('Use at least 12 characters.')
    if not check_uppercase(password):
        suggestions.append('Add an uppercase letter.')
    if not check_lowercase(password):
        suggestions.append('Add a lowercase letter.')
    if not check_number(password):
        suggestions.append('Add a number.')
    if not check_special(password):
        suggestions.append('Add a special character.')
    if len(password) < 16:
        suggestions.append('Consider using 16 or more characters.')
    return suggestions


def analyze_password(password):
    """
    Display the password strength analysis.
    """
    score = calculate_score(password)
    rating = get_rating(score)
    suggestions = get_suggestions(password)
    print()
    print('Password Strength Analysis')
    print('--------------------------')
    print('Score:', score, '/ 100')
    print('Rating', rating)
    print()
    print('Suggestions:')
    if len(suggestions) == 0:
        print('Your password meets all the basic checks!')
    else:
        for suggestion in suggestions:
            print('-', suggestion)
    print()
    print('Note: This is only a basic password strength estimate.')


def main():
    """
    Run the Password Strength Analyzer :)
    """
    print("===============================")
    print("    PASSWORD STRENGTH ANALYZER")
    print("===============================")
    running = True
    while running:
        print()
        print('1. Analyze a password')
        print('2. Exit')
        choice = input('Choose an option (1-2): ')
        if choice == '1':
            password = input('Enter a sample password: ')
            analyze_password(password)
        elif choice == '2':
            print('Thanks for using Password Strength Analyzer! :D')
            running = False
        else:
            print('Invalid choice. Please enter 1 or 2.')


if __name__ == '__main__':
    main()