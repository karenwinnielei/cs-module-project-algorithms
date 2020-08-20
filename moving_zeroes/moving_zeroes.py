'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    count = 0 # count of non-zero elements

    # traverse arr
    # if element is non zero, replace element at arr[count] with this element
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1 # increment count

    # all non-zero elements have been shifted to the front and count is set as index of first 0
    # make all elements 0 from count to end
    while count < len(arr):
        arr[count] = 0
        count += 1
    
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")