def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break



def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    for val in arr:
        index = int(n * val)
        buckets[index].append(val)

    for bucket in buckets:
        bucket.sort()

    k = 0
    for bucket in buckets:
        for val in bucket:
            arr[k] = val
            k += 1


def count_sort(arr):
    max_val = max(arr)
    freq = [0] * (max_val + 1)

    for val in arr:
        freq[val] += 1

    for i in range(1, len(freq)):
        freq[i] += freq[i - 1]

    output = [0] * len(arr)
    for val in reversed(arr):
        freq[val] -= 1
        output[freq[val]] = val

    for i in range(len(arr)):
        arr[i] = output[i]



def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current



def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1




def quick_sort(arr):
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def sort(low, high):
        if low < high:
            pi = partition(low, high)
            sort(low, pi - 1)
            sort(pi + 1, high)

    sort(0, len(arr) - 1)




def counting_sort_for_radix(arr, pos):
    n = len(arr)
    count = [0] * 10
    output = [0] * n

    for num in arr:
        index = (num // pos) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in reversed(range(n)):
        index = (arr[i] // pos) % 10
        count[index] -= 1
        output[count[index]] = arr[i]

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    pos = 1
    while max_val // pos > 0:
        counting_sort_for_radix(arr, pos)
        pos *= 10



def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

