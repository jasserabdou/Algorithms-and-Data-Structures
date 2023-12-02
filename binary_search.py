def find(item, arr, bot, top):
    # Base case: If the range between 'bot' and 'top' is just one element,
    # check if the item is equal to the element at 'bot' position.
    # If true, return the index 'bot'; otherwise, return None.
    if (top - bot) == 1:
        if arr[bot] == item:
            return bot
        else:
            return None

    # Calculate the middle index of the current range.
    mid = (bot + top) // 2

    # If the element at the middle index minus one is equal to the item,
    # recursively search in the lower half of the current range (bot to mid).
    if arr[mid - 1] == item:
        return find(item, arr, bot, mid)
    # If not, recursively search in the upper half of the current range (mid to top).
    else:
        return find(item, arr, mid, top)


# Example usage: Find the index of the item 60 in the sorted array.
print(find(60, [1, 2, 5, 19, 27, 42, 60, 101], 0, 8))
