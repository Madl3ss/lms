def ask_password():
    password = 'password'
    
    for _ in range(3):
        input_password = input()
        if input_password == password:
            print('Пароль принят')
            break
    else:
        print('В доступе отказано')