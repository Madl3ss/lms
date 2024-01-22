def take_large_banknotes(banknotes):
    up_banknotes = []
    for banknote in banknotes:
        if banknote > 10:
            up_banknotes.append(banknote)
    return up_banknotes