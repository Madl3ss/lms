def print_document(pages):
    isSecret = False
    for page in pages:
        if page.split(' ')[0] != 'Секретно':
            print(page)

        if page.split(' ')[0] == 'Секретно' and isSecret == False:
            isSecret = True
        
    if isSecret:
        print('Дальнейшие материалы засекречены')
    else:
        print('Напечатано без купюр')