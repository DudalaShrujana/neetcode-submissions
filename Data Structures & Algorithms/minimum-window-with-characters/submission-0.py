from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""
        target_counts = Counter(t)
        window_counts = {}

        have, need = 0, len(target_counts)
        res_len = float("inf")
        res_bounds = (-1, -1)

        left = 0
        for right, char in enumerate(s):

            window_counts[char] = window_counts.get(char, 0) + 1

            if char in target_counts and window_counts[char] == target_counts[char]:
                have += 1

                while have == need:
                    current_len = right - left + 1
                    if current_len <res_len:
                        res_len = current_len
                        res_bounds = (left, right)

                    left_char = s[left]
                    window_counts[left_char] -= 1

                    if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                        have -= 1
                    left += 1
                

        l, r = res_bounds
        return s[l : r + 1] if res_len != float("inf") else ""
        