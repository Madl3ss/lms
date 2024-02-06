def check_pin(pinCode):
    a, b, c = pinCode.split('-')
    isSimple = True
    isPalindrome = False
    isQw = False
    a = int(a)
    c = int(c)
    
    if a == 1:
        isSimple = False
    for i in range(2, a):
        if a % i == 0:
            isSimple = False
            break

    if int(a) % 2 != 0:
        isSimple = True
    
    if b == b[::-1]:
        isPalindrome = True

    if int(c) & (int(c) - 1) != int(c):
        isQw = True

    if isSimple and isPalindrome and isQw:
        return 'Корректен'
    return 'Некорректен'