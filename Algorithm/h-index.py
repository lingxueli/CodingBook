# https://leetcode.com/problems/h-index/
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 0:
            return 0
        
        citations.sort(reverse=True)
        
        for i in range(len(citations)):
            # You'll encouter this case first
            # if A[i] > i + 1:
            #    continue;
            if citations[i] <= i + 1:
                if citations[i] == i + 1:
                    return citations[i]
                else:
                    return i
                
        #[100,99,98] h-index = 3        
        return len(citations)

# time complexity: O(nlgn)
# space complexity: constant

s = Solution()
print(s.hIndex([100,99,98])) # 3

print(s.hIndex([3,0,6,1,5])) # 3

print(s.hIndex([6,5,4,1,0])) # 3

print(s.hIndex([6,4,1,0])) # 2
