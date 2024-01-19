def who_are_you_and_hello():
    name = input()
    while True:
        if name.isalpha() and name[0].isupper() and name[1:].islower():
            break
        else:
            name = input()
    print(f'Привет, {name}!')