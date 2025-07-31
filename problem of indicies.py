

nums = [2,7,11,15]
target = 9



for i, num in enumerate(nums):
    print(i, num)
            
class Solution(object):
    def twoSum(self, nums, target):
        my_hash = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in my_hash:
                return [my_hash[complement], i]
            my_hash[num] = i




x = Solution()
print(x.twoSum(nums, target))