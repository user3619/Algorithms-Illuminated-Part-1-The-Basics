def MergeSort(array: list) -> list:
    '''
    Алгоритм сортировки слиянием / Merge sort algorithm

    Args:
        array (list): массив из n разных целых чисел / An array of n different integers

    Returns:
        array: Отсортированный массив чисел / Sorted array of numbers

    Example:
        >>> MergeSort([5, 4, 1, 8, 7, 2, 6, 3])
        >>> [1, 2, 3, 4, 5, 6, 7, 8]
    '''
    if 0 <= len(array) <= 1:
        return array
    
    else:
        C = MergeSort(array[:len(array)//2])
        D = MergeSort(array[len(array)//2:])

        return Merge(C, D)



def Merge(array1, array2):
    '''
    Подпрограмма для сортировки массивов / Subroutine for sorting arrays
    '''
    i = 0
    j = 0
    B = []

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

    return B