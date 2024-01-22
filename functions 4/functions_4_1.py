i_know = []


def parrot(phrase):
    global i_know
    if phrase in i_know:
        print(phrase)
    i_know.append(phrase)