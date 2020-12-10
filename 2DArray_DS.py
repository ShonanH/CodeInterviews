def hourglass(arr):
    rows = len(arr)
    columns = len(arr[0])

    max_hourglass = -63

    for i in range(rows-2):
        for j in range(columns-2):
            current_val = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            max_hourglass = max(max_hourglass, current_val)
    
    return max_hourglass
hourglass([[1, 1, 1, 0, 0, 0], 
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0], 
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]])
        
arr = [[1, 1, 1, 0, 0, 0], 
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0], 
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]

print(len(arr[0]))
