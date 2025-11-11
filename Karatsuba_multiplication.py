def recintmult(x: int, y: int) -> int:

    '''
    Алгоритм рекурсивного умножения чисел длины n (n - степень числа 2)\n
    Algorithm for recursive multiplication of numbers of length n (n is the power of 2)

    Args:
        x (int): Число длины n / Number of Length n
        y (int): Число длины n / Number of Length n

    Returns:
        int: Произведение x и y / Multiplication of x and y
    
    Example:
        >>> recintmult(5678, 1234)
        '7006652'
    '''

    n = len(str(max(x, y)))

    if n == 1:
        return x * y
    else:
        if n % 2 != 0:
            n += 1
        
        x_str = str(x).zfill(n)
        y_str = str(y).zfill(n)

        a, b = int(x_str[:(n//2)]), int(x_str[(n//2):])
        c, d = int(y_str[:(n//2)]), int(y_str[(n//2):])

        ac = recintmult(a, c)
        ad = recintmult(a, d)
        bc = recintmult(b, c)
        bd = recintmult(b, d)

        return ac * (10**n) + (10**(n//2)) * (ad + bc) + bd



def karatsuba(x: int, y: int) -> int:

    '''
    Оптимизированная версия алгоритма recintmult\n
    An optimized version of the recintmult algorithm

    Args:
        x (int): Число длины n / Number of Length n
        y (int): Число длины n / Number of Length n

    Returns:
        int: Произведение x и y / Multiplication of x and y
    
    Example:
        >>> karatsuba(5678, 1234)
        '7006652'
    '''

    n = len(str(max(x, y)))
    
    if n == 1:
        return x * y
    

         
    else:
        if n % 2 != 0:
            n += 1
        
        x_str = str(x).zfill(n)
        y_str = str(y).zfill(n)

        a, b = int(x_str[:(n//2)]), int(x_str[(n//2):])
        c, d = int(y_str[:(n//2)]), int(y_str[(n//2):])
        
        p = a + b
        q = c + d

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        pq = karatsuba(p, q)

        adbc = pq - ac - bd

        return 10**n * ac + 10**(n//2) * adbc + bd