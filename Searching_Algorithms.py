def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

def binary_search(arr: list[int], target:int):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def interpolation_search(arr: list[int], target:int):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:

        if arr[low] == arr[high]:
            if arr[low] == target:
                return low
            return -1

        guess = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[guess] == target:
            return guess
        elif arr[guess] < target:
            low = guess + 1
        else:
            high = guess - 1

    return -1

if __name__ == '__main__':
    import time
    
    initial = int(input('Enter initial element of array: '))
    final = int(input('Enter final element of array: '))
    step = int(input('Enter step between elements: '))

    array=[num for num in range(initial,final,step)]

    target = int(input('Enter element to look up: '))

    #Linear search
    initial_time = time.perf_counter_ns()

    linear_search(array, target)

    end_time = time.perf_counter_ns()
    time_taken = end_time - initial_time

    print(f"Linear search Time Taken: {time_taken} ns")

    #Binary search
    initial_time = time.perf_counter_ns()

    binary_search(array, target)

    end_time = time.perf_counter_ns()
    time_taken = end_time - initial_time

    print(f"Binary search Time Taken: {time_taken} ns")

    #Interpolation search
    initial_time = time.perf_counter_ns()

    interpolation_search(array, target)

    end_time = time.perf_counter_ns()
    time_taken = end_time - initial_time

    print(f"Interpolation search Time Taken: {time_taken} ns")
