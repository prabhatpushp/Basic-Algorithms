# This is a program to implement insertion sort algorithm

def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


if __name__ == "__main__":
    # Input the array
    arr = [int(x) for x in input(
        "Please input elements of array separated by space\n").split()]
    # Call the insertion sort function
    insertion_sort(arr)
    # Print the sorted array
    print("the sorted array is:\n", arr)
