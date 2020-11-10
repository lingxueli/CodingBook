# https://leetcode.com/problems/contiguous-array/
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # corner case
        if nums is None or len(nums) == 0:
            return 0
        
        countIndexMap = {}
        countIndexMap[0] = -1
        count = 0
        res = 0
        
        for i in range(0, len(nums)):
            if nums[i] == 0:
                count-=1
            else:
                count+=1
            
            if count not in countIndexMap:
                countIndexMap[count] = i
            else:
                res = max(res, i - countIndexMap[count])
                
        return res