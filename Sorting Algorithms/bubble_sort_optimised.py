def optimised_bubble_sort(elements):
    """
    This optimisation improves the best-case time complexity from O(n^2) to O(n) 
    by adding a flag to check if any swaps are made in each iteration. If no swaps 
    are made, the list is already sorted, and the algorithm can terminate early.

    elements - List of elements to be sorted
    """
    n = len(elements)
    # Iterates through all elements in the list
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Iterate the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            # If this occurs in the first pass, it means the array is already sorted
            if i == 0:
                print("The array is already sorted.")
            break


def sort_array():
    array = [25, 99, 23, 41, 98, 56, 11, 64, 15, 16, 69, 43, 87, 62,
             12, 1, 27, 5, 10, 19, 84, 70, 92, 67, 75, 28, 97, 51, 95, 50]

    optimised_bubble_sort(array)

    print("Sorted array is:")
    print(array)


sort_array()
