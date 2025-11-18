def complete_enumeration(array: list) -> int:
    '''
    Алгоритм для подсчёта количества инверсий в массиве методом полного перебора\n
    An algorithm for counting the number of inversions in an array using the exhaustive search method

    Args:
        array (list): массив из n разных целых чисел / an array of n different integers

    Returns:
        int: количество инверсий в массиве / number of inversions in the array

    Example:
        >>> complete_enumeration([1,2,4,3,5,6])
        >>> 1
    '''
    numInv = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                numInv += 1
    return numInv


def Sort_and_countInv(array: list) -> int:
    '''
    Алгоритм для подсчёта количества инверсий методом "Разделяй и властвуй"\n
    An Algorithm for calculating the Number of Inversions Using the Divide and Conquer Method

    Args:
        array (list): массив из n разных целых чисел / an array of n different integers

    Returns:
        int: количество инверсий в массиве / number of inversions in the array
    '''

    n = len(array)

    if n == 0 or n == 1:
        return (array, 0)
    
    else:
        (C, left_inv) = Sort_and_countInv(array[:n//2])
        (D, right_inv) = Sort_and_countInv(array[n//2:])
        (B, split_inv) = Merge_and_countInv(C, D)

        return (B, left_inv + right_inv + split_inv)
    
def Merge_and_countInv(array1, array2):
    '''
    Подпрограмма для сортировки массивов и подсчёта инверсий\n
    A routine for sorting arrays and counting inversions
    '''

    i = 0
    j = 0
    split_inv = 0
    B = []
    n = len(array1)

    while i != len(array1)  or j != len(array2):
        if i >= len(array1):
            B.append(array2[j])
            j += 1

        elif j >= len(array2):
            B.append(array1[i])
            i += 1

        else:
            if array1[i] < array2[j]:
                B.append(array1[i])
                i += 1

            else:
                B.append(array2[j])
                j += 1
                split_inv += ((n//2) - i + 1)

    return (B, split_inv)