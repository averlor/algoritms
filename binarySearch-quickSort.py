import random

def quick_sort(arr):

    '''quick sort of array'''
    if (len(arr)) < 2:
        return arr
    else:
        pivot = random.choice(arr)                                  # опорный элемент, выбранный случайно из массива
        less = [i for i in arr if i < pivot]                    #подмассив меньше опорного элемента
        greater = [i for i in arr if i > pivot]                 # подмассив больше опорного элемента

        return quick_sort(less) + [pivot] + quick_sort(greater)     # собираем массив, рекурсивно пробегая по less и greater


def binary_search(arr, item):

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = round((low + high) / 2)
        guess = arr[mid]

        if (guess == item):
            return mid
        elif (guess > item):
            high = mid - 1
        else:
            low = mid + 1

    return None


if __name__ == '__main__':

    item = int(input('Введите число: '))
    arr = [1, 25, 2, 145, 3, 11, 4, 78, 85, 46, 4512, 64564]
    arr = quick_sort(arr)
    print(binary_search(arr, item))