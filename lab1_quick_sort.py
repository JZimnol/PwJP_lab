import random
import time


def partition(arr: list, low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1


def quick_sort(arr: list, low: int, high: int):
    if low < high:
        # because arr is being changed "in place",
        # it's pased by reference and can be changed
        # inside a function
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def average(sorting_function, no_iterations, no_elements):
    ret = 0
    for _ in range(no_iterations):
        random_list = random.sample(range(0, no_elements), no_elements)
        start = time.time()
        sorting_function(random_list, 0, no_elements - 1)
        end = time.time()
        ret += end - start
    return ret / no_iterations


if __name__ == '__main__':
    random_list = random.sample(range(0, 100), 10)
    print(random_list)
    quick_sort(random_list, 0, len(random_list) - 1)
    print(random_list)

    number_of_iterations = 100000
    number_of_elements = 100
    print(f"Average of {number_of_iterations} iterations and {number_of_elements} elements:")
    print(average(quick_sort, number_of_iterations, number_of_elements))

    number_of_iterations = 10000
    number_of_elements = 100
    print(f"Average of {number_of_iterations} iterations and {number_of_elements} elements:")
    print(average(quick_sort, number_of_iterations, number_of_elements))


#               A is assigned to B
#                     (B = A)
#                    /      \
#                   /        \
#       Something else      B is mofied
#      is assigned to B       in place
#        (B = 'Hello')      (B.append(2))
#             |                   |
#             |                   |
#       A does not change    A also changes
