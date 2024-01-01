def linear_search(elements, target):
    """
    Linear search algorithm is a simple method to find a specific element in a list or an array. 
    It works sequentially and checks each list component until the desired element is found or the list ends.
    Performs linear search for a target in an array.

     elements - List of elements to search through
     target - The element to search for
     return - The index of the target if found, otherwise -1
    """
    for i in range(len(elements)):
        if elements[i] == target:
            return i  # Target found, return its index
    return -1  # Target not found


def find_element():

    array = [5, 3, 8, 6, 7, 2, 1, 4, 9, 10, 61, 67,
             68, 70, 76, 77, 78, 86, 87, 89, 93, 100]
    target = 4

    index = linear_search(array, target)

    if index != -1:
        print(f"Element found at index {index}")
    else:
        print("Element not found")


find_element()
