class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 1, x // 2
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2
            sqr = mid * mid

            if sqr == x:
                return mid
            
            elif sqr < x:
                ans = mid
                left = mid + 1
            
            else:
                right = mid - 1
            

        return ans
        