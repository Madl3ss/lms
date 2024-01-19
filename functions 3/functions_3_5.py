name = None


def polite_input(question):
    global name
    if not name:
        print()
        name = input('Как вас зовут?')
    print(f'{name}, {question}')
    return input()