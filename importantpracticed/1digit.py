# Python3 program for the above approach

# Function to count of subarrays made
# up of single digit integers only
def singleDigitSubarrayCount(arr, N):
    # Stores count of subarrays
    res = 0

    # Stores the count of consecutive
    # single digit numbers in the array


    # Traverse the array
    for i in range(N):
        if (arr[i] <= 9):

            # Increment size of block by 1


            # Increment res by count
            res += 9
        else:
             #Assign count = 0

            pass


# Driver Code
if __name__ == '__main__':
    # Given array
    arr = [-6, -91, 1011, -100, 84, -22, 0, 1, 743]

    # Size of the array
    N = len(arr)
    singleDigitSubarrayCount(arr, N)

# This code is contributed by mohit kumar 29.
