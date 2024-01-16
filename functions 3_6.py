friends = dict()


def add_friends(name_of_person, list_of_friends):
    if name_of_person in friends:
        friends[name_of_person].extend(list_of_friends)
    else:
        friends[name_of_person] = list_of_friends


def are_friends(name_of_person1, name_of_person2):
    return name_of_person2 in friends[name_of_person1]


def print_friends(name_of_person):
    print(*sorted(friends[name_of_person]))