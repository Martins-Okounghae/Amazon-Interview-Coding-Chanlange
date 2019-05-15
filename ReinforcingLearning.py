class solutionsTwoSum(object):

    def twoSumSol(self, nums, target):

        complementMap = {}

        for i in range(len(nums)):

            num = nums[i]
            complement = target - num

            if num in complementMap:
                print(num)
                #print(i)
                print(complement)
                return complementMap[num],  i
            else:
                complementMap[complement] = i
                print(complementMap)


test = solutionsTwoSum()

test2 = test.twoSumSol([95,90,70,80,100,101,102,103], 180)

print(test2)











