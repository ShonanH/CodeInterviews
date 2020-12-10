# You are given an integer n. An array nums of length n + 1 is generated in the following way:

# nums[0] = 0
# nums[1] = 1
# nums[2 * i] = nums[i] when 2 <= 2 * i <= n
# nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
# Return the maximum integer in the array nums​​​.


# input : n = 7
# output: 3
# How does this  algorithm work?
# nums[0] = 0
# nums[1] = 1
# nums[2] = [2 * i] = nums[i] = nums[1] = 1                                                      ...............(i.e even number 2 = 2i, therefore i = 1)
# nums[3] = [2 * i + 1] = nums[i] + nums[i + 1] = nums[1] + nums[2] = 2                          ...............(i.e odd number 3 = 2i + 1, therefore i = 1)
# nums[4] = [2  *  i] = nums[i] = nums[2] = 1                                                    ...............(i.e even number 4 = 2i, therfore i = 2)
# nums[5] = [2 * i + 1] = nums[i] + nums[i + 1] = nums[2] + nums[3] = 3                          ...............(i.e odd number 5 = 2i + 1, therefore i = 2)
# nums[6] = [2 * i] = nums[i] = nums[3] = 2                                                      ...............(i.e even number 6 = 2i, therefore i = 3)
# nums[7] = [2 * i + 1] = nums[i] + nums[i + 1] = nums[3] + nums[4] = 3                          ...............(i.e odd number 7 = 2i + 1, therefore i = 3)



class Solution:
    
    def getMaximumGenerated(n):
        if (n == 0):
            return 0
        else:
            nums = []
            nums.extend([0,1])
            max_val = 0
            for i in range(2,n+1):
                k = i % 2
                if k == 0:
                    nums.append(nums[i // 2])
                else:
                    nums.append(nums[i // 2] + nums[i // 2 + 1])
                max_val = max(nums)
            print(max(nums))
        return max_val
    getMaximumGenerated(7)






