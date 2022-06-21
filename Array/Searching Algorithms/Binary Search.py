# This is a program to implement binary search algorithm

def binary_search(arr: list, target: int) -> int:
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


if __name__ == "__main__":
    # Input the array
    arr = [int(x) for x in input(
        "Please input elements of array separated by space\n").split()]
    # Input the element to be searched
    elem = int(input("Please input element to be searched\n"))
    # Call the binary search function
    search_index = binary_search(arr, elem)
    # Print the index of the element
    if search_index == -1:
        print("Element not found")
    else:
        print("Element found at index", search_index)
