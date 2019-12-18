def array2D(arr):

    # want to find the maximum hourglass sum
    # minimum hourglass sum = -9 * 7 = -63
    maxSum = -63
    
    for i in range(4):
        for j in range(4):
        
            # sum of top 3 elements
            top = sum(arr[i][j:j+3])
            
            # sum of the mid element
            mid = arr[i+1][j+1]
            
            # sum of bottom 3 elements
            bottom = sum(arr[i+2][j:j+3])
            
            hourglass = top + mid + bottom
            
            if hourglass > maxSum:
                maxSum = hourglass
                
    return maxSum

arr = [ [-9, -9, -9,  1, 1, 1],
        [0, -9,  0,  4, 3, 2],
        [-9, -9, -9,  1, 2, 3],
        [0,  0,  8,  6, 6, 0],
        [0,  0,  0, -2, 0, 0],
        [0,  0,  1,  2, 4, 0]]

print("Max Sum {}".format(array2D(arr)))