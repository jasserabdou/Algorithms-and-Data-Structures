def multall(arr):
    # Recursive function to multiply all elements in a nested list.
    product = 1
    for factor in arr:
        # If the element is a list, recursively call the function to compute its product.
        if type(factor) == list:
            product *= multall(factor)
        # If the element is not a list, multiply it directly with the current product.
        else:
            product *= factor
    return product


# Example usage: Multiply all elements in the nested list [1, 5, 6, [2, 3, [5, 4]]].
print(multall([1, 5, 6, [2, 3, [5, 4]]]))
