def multall(arr):
    """
    This function takes a nested list and returns the product of all numbers in the list.
    """
    product = 1
    for factor in arr:
        if type(factor) == list:
            product *= multall(factor)
        else:
            product *= factor
    return product


def sumall(arr):
    """
    This function takes a nested list and returns the sum of all numbers in the list.
    """
    total = 0
    for num in arr:
        if type(num) == list:
            total += sumall(num)
        else:
            total += num
    return total


def minall(arr):
    """
    This function takes a nested list and returns the smallest number in the list.
    """
    min_val = float("inf")
    for num in arr:
        if type(num) == list:
            min_val = min(min_val, minall(num))
        else:
            min_val = min(min_val, num)
    return min_val


def maxall(arr):
    """
    This function takes a nested list and returns the largest number in the list.
    """
    max_val = float("-inf")
    for num in arr:
        if type(num) == list:
            max_val = max(max_val, maxall(num))
        else:
            max_val = max(max_val, num)
    return max_val


def countall(arr):
    """
    This function takes a nested list and returns the count of all numbers in the list.
    """
    count = 0
    for num in arr:
        if type(num) == list:
            count += countall(num)
        else:
            count += 1
    return count


def flatten(arr):
    """
    This function takes a nested list and returns a flattened list.
    """
    result = []
    for num in arr:
        if type(num) == list:
            result.extend(flatten(num))
        else:
            result.append(num)
    return result


# Test array
test_arr = [1, 5, 6, [2, 3, [5, 4]]]

# Function calls
print(
    f"The product of all numbers in the array is: {multall(test_arr)}"
)  # Output: The product of all numbers in the array is: 3600
print(
    f"The sum of all numbers in the array is: {sumall(test_arr)}"
)  # Output: The sum of all numbers in the array is: 26
print(
    f"The smallest number in the array is: {minall(test_arr)}"
)  # Output: The smallest number in the array is: 1
print(
    f"The largest number in the array is: {maxall(test_arr)}"
)  # Output: The largest number in the array is: 6
print(
    f"The count of all numbers in the array is: {countall(test_arr)}"
)  # Output: The count of all numbers in the array is: 7
print(
    f"The flattened array is: {flatten(test_arr)}"
)  # Output: The flattened array is: [1, 5, 6, 2, 3, 5, 4]
