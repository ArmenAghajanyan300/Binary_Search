def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2 
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1  
        else:
            high = mid - 1
    
    return -1


# Example usage
array = [10, 20, 30, 40, 50, 60, 70]
target = int(input("Enter the number to search: "))

index = binary_search(array, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")
