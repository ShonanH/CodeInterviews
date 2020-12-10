#Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#Return the running sum of nums.


#Example
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]


class Solution:
    def runningSum(nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        print (nums)
        return nums
    
    runningSum([1,2,3,4])
        