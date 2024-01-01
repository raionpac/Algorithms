def bubble_sort(elements):
    """
    Bubble Sort is a simple sorting algorithm that repeatedly iterate through the list, 
    compares adjacent elements, and swaps them if they are in the wrong order. 
    The iteration is repeated until the list is sorted. 

    This algorithm has a time complexity of O(n^2 ) in the worst-case scenarios, 
    where n is the number of elements in the list arising this quadratic complexity because
      Bubble Sort involves two nested loops over the list.

    elements - List of elements to be sorted
    """
    n = len(elements)

    # Iterates through all elements in the list
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Iterate the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]


def sort_array():
    array = [64, 34, 25, 12, 22, 11, 90]

    bubble_sort(array)

    print("Sorted array is:")
    print(array)


sort_array()
