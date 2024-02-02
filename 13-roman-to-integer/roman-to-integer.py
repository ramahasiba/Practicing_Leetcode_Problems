class Solution:
    def romanToInt(self, s: str) -> int:
        symobol_values = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000, 
            'IV': 4, 
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900 
        }         
        s_len = len(s)  
        track, total = 0, 0

        while track < s_len:
            if track<s_len-1 and symobol_values[s[track]] < symobol_values[s[track + 1]]:
                    total += symobol_values[s[track: track+2]]
                    track += 2
                    continue 
            total += symobol_values[s[track]]      
            track += 1 
        return total         



        