import random


def quicksort(elements):
    """
    QuickSort is an efficient, divide-and-conquer, comparison-based sorting algorithm. 
    It works by selecting a 'pivot' element from the array and splitting the other elements 
    into two sub-arrays according to whether they are less than or greater than the pivot.

    elements - List of elements to be sorted
    """
    if len(elements) <= 1:
        return elements  # A list of zero or one elements is already sorted

    """
    I am selecting a random pivot index to efficiently sort a list by dividing it into smaller 
    sub-lists based on a pivot element. This approach is better, especially with large arrays, 
    reducing the risk of encountering the worst-case performance on already sorted or nearly sorted data.
    """
    # pivot_index = random.randint(0, len(elements) - 1)

    pivot_index = len(elements) // 2
    pivot = elements[pivot_index]

    low = []
    high = []

    # Partition the list into less than pivot and greater than pivot
    for i, value in enumerate(elements):
        if i != pivot_index:
            if value < pivot:
                low.append(value)
                print(f"{low} Less than Pivot {pivot}")
            else:
                high.append(value)
                print(f"{high} Greater than Pivot {pivot}")

    # Recursively sort and combine
    return quicksort(low) + [pivot] + quicksort(high)


def sort_array():
    array = [9, 1, 8, 2, 7, 3, 5, 6, 4]

    sorted_array = quicksort(array)

    print("Sorted array is:")
    print(sorted_array)


sort_array()
