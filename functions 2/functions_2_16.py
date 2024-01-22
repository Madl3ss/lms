def late(now, classes, bus):
    now = (int(now.split(':')[0]) * 60) + int(now.split(':')[1])
    classes = (int(classes.split(':')[0]) * 60) + int(classes.split(':')[1])
    ost = classes - now
    for time in bus[::-1]:
        if ((time >= 5) and (ost - 15 - time >= 0)):
            return f'Выйти через {time - 5} минут'
    return 'Опоздание'