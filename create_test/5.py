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


a = input()
if is_correct_mobile_phone_number_ru(a):
    print("YES")
else:
    print('NO')
