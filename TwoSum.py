class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, number in enumerate (nums):
            diff = target - number
            if diff in map:
                return [map[diff], i]
            map[number] = i
