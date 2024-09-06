def insertion_sort(arr):
    n = len(arr)
    for  i in range(n):
        j = i
        while  j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -=1

    print("after imsertion _sort")
    print(" ".join(map(str, arr)))



if __name__ == "__main__":
    arr = [13,46,24,52,20,9]
    print("Before insertion sort")
    print(" ".join(map(str, arr)))

    insertion_sort(arr)