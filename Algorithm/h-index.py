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