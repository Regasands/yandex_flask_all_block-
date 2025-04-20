def is_prime(n):
    try:
        n = int(n)
    except (ValueError, TypeError):
        return False
    
    if n <= 1:
        return False
    
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


a = input()
if is_prime(a):
    print('YES')
else:
    print('NO')
