# This program is to implement bubble sort algorithm

def bubble_sort(arr: list) -> list:
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    # Input the array
    arr = [int(x) for x in input(
        "Please input elements of array separated by space\n").split()]
    # Call the bubble sort function
    bubble_sort(arr)
    # Print the sorted array
    print("the sorted array is:\n", arr)
