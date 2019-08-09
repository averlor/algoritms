def min_index(arr):
    smaller = arr[0]
    smaller_index = 0

    for i in range(1, len(arr)):
        if (arr[i] < smaller):
            smaller = arr[i]
            smaller_index = i

    return smaller_index

def sort_selection(arr):

    newArr = []
    for i in range(len(arr)):
        smallest = min_index(arr)
        newArr.append(arr.pop(smallest))

    return newArr

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


def main(arr, item):

    arr = sort_selection(arr)
    print(binary_search(arr, item))


if __name__ == '__main__':

    item = int(input('Введите число: '))
    arr = [1, 25, 2, 145, 3, 11, 4, 78, 85, 46, 4512, 64564]

    main(arr, item)