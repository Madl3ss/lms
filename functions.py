def palindrome(s):
    s = s.replace(" ", "")
    text = s.lower()
    re_text = s.lower()[::-1]
    if text == re_text:
        return 'Палиндром'
    return 'Не палиндром'