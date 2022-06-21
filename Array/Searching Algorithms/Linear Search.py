# This is a program to implement linear search algorithm

def linear_search(arr: list, target: int) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


if __name__ == '__main__':
    # Input the array
    arr = [int(x) for x in input(
        "Please input elements of array separated by space\n").split()]
    # Input the element to be searched
    elem = int(input("Please input element to be searched\n"))
    # Call the linear search function
    search_index = linear_search(arr, elem)
    # Print the index of the element
    if search_index == -1:
        print("Element not found")
    else:
        print("Element found at index", search_index)
