def merge_sort(arr):
    """
    Sorts an array of elements using the merge sort algorithm.

    Args:
        arr: The array of elements to be sorted.
    """

    # Check if the array has more than one element
    if len(arr) > 1:
        # Split the array into two halves
        mid_index = len(arr) // 2
        left_arr = arr[:mid_index]
        right_arr = arr[mid_index:]

        # Recursively apply merge_sort to both halves
        merge_sort(left_arr)
        merge_sort(right_arr)

        # Initialize counters for left, right, and merged array
        i = 0  # Index for left array
        j = 0  # Index for right array
        k = 0  # Index for merged array

        # Merge the two halves into the original array
        while i < len(left_arr) and j < len(right_arr):
            # Compare elements from both halves and merge in ascending order
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # Check if there are remaining elements in the left half
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # Check if there are remaining elements in the right half
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


# Example usage:
arr_test = [2, 8, 5, 3, 9, 4, 1, 7]

# Apply merge_sort to the example array
merge_sort(arr_test)

print(arr_test)
