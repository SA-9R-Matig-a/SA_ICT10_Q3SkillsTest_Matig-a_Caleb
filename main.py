# Skills Test 3rd Quarter
from pyscript import display, document


def username_verification(e):
    document.getElementById('output').innerHTML = ' '

    username = document.getElementById('username').value
    #creates variable to count the number of characters
    username_length = len(username)

    if username_length < 7:
        #if username is too short, subtracts 7 by the length of the username to determine how many more characters are needed
        display(f'Your username is too short. Add at least {7 - username_length} more character/s to proceed.', target='output')
    else:
        return(True)


def password_verification(e):
    document.getElementById('output').innerHTML = ' '

    password = document.getElementById('password').value
    password_length = len(password)
    password_has_number = any(char.isdigit() for char in password)
    password_has_letter = any(char.isalpha() for char in password)

    if password_length < 10:
        #if password is too short, subtracts 10 by the length of the password to determine how many more characters are needed
        display(f'Your password is too short. Add at least {10 - password_length} more character/s to proceed.', target='output')
    elif not password_has_letter:
        display(f'Password must contain at least one letter.', target='output')
    elif not password_has_number:
        display(f'Password must contain at least one number.', target='output')
    else:
        return(True)


def account_creation(e):
    document.getElementById('output').innerHTML = ' '

    if username_verification(e) == True and password_verification(e) == True:
        display(f'Account created. You may now log in using your credentials.', target='output')
    else:
        display(f'Try again', target='output')

def compute_average(event):
    # Get the input values and convert to float
    score1 = float(document.getElementById("score1").value)
    score2 = float(document.getElementById("score2").value)
    score3 = float(document.getElementById("score3").value)
    score4 = float(document.getElementById("score4").value)

    # Compute average
    average = (score1 + score2 + score3 +score4) / 4

    # Determine pass/fail
    if average >= 95:
        result = "Eligible. Input this in the regiment selector to join the M.P."
    else:
        result = "Not Eligible for Military Police"

    # Displays results, rounds off to 2 decimal points, and converts answer into a string
    document.getElementById("average").innerText = str(round(average, 2))
    document.getElementById("result").innerText = result
