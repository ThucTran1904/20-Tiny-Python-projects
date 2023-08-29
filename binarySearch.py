def searchBinary(arr, targetNumber):
    left = 0
    right = len(arr)
    mid = 0
    print('')
    print('The array: ', arr)
    while left <= right:

        mid = left + (right - left) // 2
       

        # Check if targetNumber is present at mid
        if arr[mid] == targetNumber:
            print('')
            print(f"Element {targetNumber} is present at index", mid)
            quit()

        # If targetNumber is greater, ignore left half
        elif arr[mid] < targetNumber:
            left = mid + 1
        elif arr[mid] > targetNumber: 
            right = mid - 1
        # If targetNumber is smaller, ignore right half
        elif arr[mid] != targetNumber:
            print(f"Element {targetNumber} is not present in this array")
            

    # If we reach here, then the element
    # was not present
tg = 9
thuk = [1,2,3,4,5,6,7,8,9,10,11,12]
searchBinary(thuk, tg)