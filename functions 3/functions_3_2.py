old_message = ''
def print_without_duplicates(message):
    global old_message
    if old_message != message:
        print(message)
    old_message = message