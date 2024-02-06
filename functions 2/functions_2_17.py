def password_level(password):
    if len(password) < 6:
        return 'Недопустимый пароль'
    elif password.isdigit() or (password.islower() or password.isupper()):
        return 'Ненадежный пароль'
    elif password.istitle() or (password.islower() or password.isupper()) and password.isalnum():
        return 'Слабый пароль'
    

print(password_level("qwerty"))

print(password_level("123Qwerty"))

print(password_level("Qwerty"))
