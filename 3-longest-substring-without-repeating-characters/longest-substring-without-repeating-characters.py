class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        save strin characters in a dictionary with thier positions then check if the substring is greater than the current one then replace it 
        """
        #get the length of s
        s_length = len(s)

        #check if there is string
        if s_length == 0:
            return 0
        elif s_length == 1:
            return 1
        else:
            first_ptr, sec_ptr = 0, 1

            longest_substring_length = 1
            current_substring_length = 1 

            substring_chars = {
                s[0]: 0
            }
            
            while sec_ptr < s_length: 
                if s[sec_ptr] not in substring_chars:
                    substring_chars[s[sec_ptr]] = sec_ptr
                    sec_ptr += 1 
                else:
                    current_substring_length = len(substring_chars)

                    if current_substring_length > longest_substring_length:
                        longest_substring_length = current_substring_length 
                    
                    substring_chars = {
                        key: value for key, value in substring_chars.items() if value > substring_chars[s[sec_ptr]]
                    }

                    substring_chars[s[sec_ptr]] = sec_ptr
 
                    sec_ptr += 1  
                    
            current_substring_length = len(substring_chars)
            if current_substring_length > longest_substring_length:
                longest_substring_length = current_substring_length 
             
        return longest_substring_length
