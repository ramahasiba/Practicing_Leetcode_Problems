# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:

#         s_length = len(s)

#         if s_length == 0:
#             return 0

#         elif k >= s_length:
#             return s_length

#         else:
#             left_ptr, right_ptr = 0, k + 1

#             longest_substring_length = k
             
#             while right_ptr < s_length: 

#                 current_substig_length = 1

#                 while s[left_ptr] == s[left_ptr + 1] and left_ptr < s_length - 2:

#                     current_substig_length += 1

#                     left_ptr += 1
#                     right_ptr += 1
                
#                 if right_ptr < s_length:
#                     if s[right_ptr] == s[left_ptr]: 

#                         current_substig_length += (k + 1) 

#                         while right_ptr <= s_length - 2 and s[right_ptr] == s[right_ptr + 1] :
#                             # if right_ptr + 1 == s_length - 1:
#                             #     current_substig_length += 1 
#                             #     right_ptr += 1  

#                             current_substig_length += 1 
#                             right_ptr += 1      
#                         else: 
#                             left_ptr += 1
#                             right_ptr += 1

#                     else:
#                         current_substig_length += (k)
#                         left_ptr += 1
#                         right_ptr += 1

#                 if current_substig_length > longest_substring_length:
#                     longest_substring_length = current_substig_length

#         if longest_substring_length > s_length:
#             return s_length 
#         else: 
#             return longest_substring_length





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
