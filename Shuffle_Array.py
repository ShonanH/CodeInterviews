""" 
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].


Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7]. """

def shuffle_array(nums, n):
    new_arr = []
    for i in range(n):
        new_arr.append(nums[i])
        new_arr.append(nums[i+n])
    print (new_arr)
shuffle_array([2,5,1,3,4,7], 3)
