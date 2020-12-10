# Given an array A of positive integers, let S be the sum of the digits of the minimal element of A.

# Return 0 if S is odd, otherwise return 1.

#Example
# Input: [99,77,33,66,55]
# Output: 1
# Explanation: 
# The minimal element is 33, and the sum of those digits is S = 3 + 3 = 6 which is even, so the answer is 1.

class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        low = min(A)
        new_array = [int(x) for x in str(low)]
        for i in range(0, len(new_array)):
            if len(new_array) < 2:
                s = new_array[i]
            else:
                s = new_array[i] + new_array[i+1]
        
            if (s % 2 == 0):
                return 1
            else:
                return 0
    
    sumOfDigits([34,23,1,24,75,33,54,8])