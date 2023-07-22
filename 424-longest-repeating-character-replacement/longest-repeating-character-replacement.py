
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_length = len(s)
        if s_length == 0:
            return 0
        elif k >= s_length:
            return s_length
        else:
            max_length = 0
            max_count = 0
            left_ptr, right_ptr = 0, 0
            char_count = [0] * 26

            while right_ptr < s_length:
                char_count[ord(s[right_ptr]) - ord('A')] += 1
                max_count = max(max_count, char_count[ord(s[right_ptr]) - ord('A')])
                if (right_ptr - left_ptr + 1) - max_count > k:
                    char_count[ord(s[left_ptr]) - ord('A')] -= 1
                    left_ptr += 1
                max_length = max(max_length, right_ptr - left_ptr + 1)
                right_ptr += 1

            return max_length
