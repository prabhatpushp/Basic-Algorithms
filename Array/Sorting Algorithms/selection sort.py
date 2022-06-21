# This is a program to implement selection sort algorithm

def selection_sort(arr: list) -> list:
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


if __name__ == "__main__":
    # Input the array
    arr = [int(x) for x in input(
        "Please input elements of array separated by space\n").split()]
    # Call the selection sort function
    selection_sort(arr)
    # Print the sorted array
    print("the sorted array is:\n", arr)
