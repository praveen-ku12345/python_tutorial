def merge_sort(arr, inv_count):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        inv_count = merge_sort(left_half, inv_count)
        inv_count = merge_sort(right_half, inv_count)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                inv_count += len(left_half) - i  # Count inversions
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return inv_count
input_list = list(map(int, input("Enter space-separated numbers: ").split()))
inversions = 0
inversions_1 = merge_sort(input_list, inversions)
print("Sorted array:", input_list)
print("Inversion count:", inversions_1)
