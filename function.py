import re
import string
import random
def checkpasswordstrength(siu):    
    password=siu
    uppercase_pattern = re.compile(r"[A-Z]")
    lowercase_pattern = re.compile(r"[a-z]")
    digit_pattern = re.compile(r"\d")
    special_char_pattern = re.compile(r"[\W_]")

    has_uppercase = uppercase_pattern.search(password)
    has_lowercase = lowercase_pattern.search(password)
    has_digit = digit_pattern.search(password)
    has_special_char = special_char_pattern.search(password)

    password_score = 0

    if has_uppercase:
        password_score += 20
    if has_lowercase:
        password_score += 20
    if has_digit:
        password_score += 20
    if has_special_char:
        password_score += 20
    if len(password) >= 10:
        password_score += 20
    if len(password) <=3:
        password_score -= 10

    return password_score

def generatepassword(len):
    length=len
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for i in range(length))

    return password

