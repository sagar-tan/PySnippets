def counting_sort(arr):
    max_value = max(arr)
    counts = [0] * (max_value + 1)


    for num in arr:
        counts[num] += 1


    sorted_arr = []
    for i in range(len(counts)):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr


arr = input("Enter a list of numbers separated by spaces: ").split()
arr = [int(x) for x in arr]

sorted_arr = counting_sort(arr)
print("Original array:", arr)
print("Sorted array using counting sort:", sorted_arr)
