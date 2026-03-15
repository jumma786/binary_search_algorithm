def binary_search_recursive(arr, target, left, right):

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)

    else:
        return binary_search_recursive(arr, target, mid + 1, right)


numbers = [3, 7, 12, 18, 25, 31, 42, 56]

target = int(input("Enter number to search: "))

result = binary_search_recursive(numbers, target, 0, len(numbers) - 1)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")