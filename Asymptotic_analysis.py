# Анализ временной сложности / Time complexity analysis

# Пример 1 / Example 1
# Поиск в одном массиве / Search in one array
def search(array, n):
    for i in array:
        if i == n:
            return True
    return False

# Временная сложность - O(n) / Time complexity - O(n)


# Пример 2 / Example 2
# Поиск в двух массивах / Search in 2 arrays
def search(array1, array2, n):
    for i in array1:
        if i == n:
            return True

    for i in array2:
        if i == n:
            return True
        
    return False

# Временная сложность - O(n) / Time complexity - O(n)


# Пример 3 / Example 3
# Проверка на наличие общего элемента / Checking if an element exists in two arrays
def search(array1, array2, n):
    for i in array1:
        for j in array2:
            if i == j:
                return True
    return False

# Временная сложность - O(n^2) / Time complexity - O(n^2)


# Пример 4 / Example 4
# Проверка на дубликаты / Check for duplicates
def check(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                return True
    return False

# Временная сложность - O(n^2) / Time complexity - O(n^2)