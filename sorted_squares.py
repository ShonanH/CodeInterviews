# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

#Example 1:
#Input: [-4,-1,0,3,10]
#Output: [0,1,9,16,100]

class Solution:
    def sortedSquares(A):
        new_array = []
        for i in range(len(A)):
            x = A[i] * A[i]
            new_array.append(x)
        new_array.sort()
        print(new_array)
        return new_array
    
    sortedSquares([-4,-1,0,3,10])