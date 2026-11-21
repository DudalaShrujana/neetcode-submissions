class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        left = 0
        max_f = 0
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_f = max(max_f, count[s[r]])
            
            if (r - left + 1) - max_f > k:
                count[s[left]] -= 1
                left += 1
                
     
            res = max(res, r - left + 1)
            
        return res
