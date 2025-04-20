def is_palindrome(arg):
    return arg == arg[::-1]


def is_prime(n):
    if type(n) is not int:
        raise TypeError
    if n in [0, 1]:
        raise ValueError
    for divisor in range(2, int(n ** 0.5) + 1): 
        if n % divisor == 0: 
            return False 
    return True


def is_correct_mobile_phone_number_ru(arg):
    try:
        arg = str(arg)
    except TypeError:
        return False

    if arg.startswith('+7'):
        arg = arg[2:]
    elif arg.startswith('8'):
        arg = arg[1:]
    else:
        return False
        
    last_symbol = arg[0]
    sp = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', ' ', ')', '(']
    for elem in arg[1:]:
        if elem == last_symbol:
            if elem == ' ':
                return False
            elif elem == '-':
                return False
        if elem not in sp:
            return False
        last_symbol = elem

    arg = arg.replace(' ', '')
    arg = arg.replace('-', '')
    
    if arg[0] == '(' and arg[4] == ')':
        arg = arg[1:4] + arg[5:]
    if arg.count('(') != 0 or arg.count(')') != 0:
        return False

    if len(arg) != 10:
        return False
    return True


def strip_punctuation_ru(arg):
    punctuations = '''!()—[]{};:'",<>./?@#$%^&*_~'''
    str_ = ''
    try:
        for elem in arg:
            if elem not in punctuations:
                str_ += elem
        str_ = str_.replace(' - ', ' ')
        str_ = str_.strip()
        last_arg = str_[0]
        end_str = last_arg
        for e in str_[1:]:
            if e == last_arg and e in ['\t', ' ', '\n']:
                continue
            end_str += e
            last_arg = e
        return end_str
    except Exception:
        return ''
