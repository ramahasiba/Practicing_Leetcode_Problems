class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        longest_substring_length = 0
        start = 0
        
        for end, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1
            char_index_map[char] = end
            longest_substring_length = max(longest_substring_length, end - start + 1)
        
        return longest_substring_length
