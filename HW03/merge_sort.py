def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        # Merging

        left_index = 0
        right_index = 0
        k = 0

        while left_index < len(L) and right_index < len(R):
            if L[left_index] < R[right_index]:
                arr[k] = L[left_index]
                left_index += 1
            else:
                arr[k] = R[right_index]
                right_index += 1
            k += 1

        # Copy leftovers
        while left_index < len(L):
            arr[k] = L[left_index]
            left_index += 1
            k += 1

        while right_index < len(R):
            arr[k] = R[right_index]
            right_index += 1
            k += 1
