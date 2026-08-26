class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numbers_and_indexes=dict()

        for i in range (0, len(nums)):
            if(target - nums[i]) in  numbers_and_indexes:
                return [numbers_and_indexes[target - nums[i]],i]
            else:
                numbers_and_indexes[nums[i]]=i
