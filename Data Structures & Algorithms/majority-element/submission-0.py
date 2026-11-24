class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        res = 0
        major = 0
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
            if counts[n] > major:
                res = n
                major = counts[n]
        
        return res
        