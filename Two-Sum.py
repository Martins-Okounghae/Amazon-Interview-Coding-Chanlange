# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.


class SolutionsTwoSums(object):
    def twoSum(self, nums, target):
        complementMap = dict()

        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if num in complementMap:
                return complementMap[num], i
            else:
                complementMap[complement] = i



testSolTwoSums = SolutionsTwoSums()


prtestSolTwoSums = testSolTwoSums.twoSum([2, 7, 9, 5, 6], 11)

print(prtestSolTwoSums)










