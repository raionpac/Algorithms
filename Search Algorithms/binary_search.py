import os
# Clear the terminal before running the code
os.system('cls' if os.name == 'nt' else 'clear')


def binary_search(elements, target, ascending=True):
    """
    Binary search is an efficient algorithm for finding an item from a sorted list of items. 
    It works by repeatedly dividing in half the portion of the list that could contain the item 
    until you've narrowed the possible locations to just one.

    The time complexity of the binary search algorithm is O(log n). 
    The algorithm divides the search interval in half with each step. As a result, 
    the time it takes to search for an element grows logarithmically with the size of the list, 
    making it very efficient for large datasets.

    elements -  Sorted list of elements to search through
    target - The element to search for
    return - The index of the target if found, otherwise -1
    """
    left = 0
    right = len(elements) - 1

    while left <= right:
        mid = (left + right) // 2  # Find the middle

        # Check if the middle element is the target
        if elements[mid] == target:
            return mid

        # Decide which side to continue the search on
        if elements[mid] < target:
            left = mid + 1  # Continue on the right side
        else:
            right = mid - 1  # Continue on the left side

    return -1  # Target not found


def find_element():
    sorted_elements = [4, 22, 28, 38, 39, 40, 53, 57,
                       61, 67, 68, 70, 76, 77, 78, 86, 87, 89, 93, 100]

    target = 61

    result = binary_search(sorted_elements, target)

    if result != -1:
        print(f"Element is present at index {result}\n")
    else:
        print("Element is not present in list\n")


find_element()
