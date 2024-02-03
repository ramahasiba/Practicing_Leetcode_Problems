class Solution:
    def intToRoman(self, num: int) -> str:
        symbol_values = {
            1: 'I', 
            5: 'V', 
            10:'X',   
            50: 'L', 
            100:'C', 
            500: 'D', 
            1000: 'M', 
            4: 'IV', 
            9: 'IX',
            40: 'XL',
            90: 'XC',
            400: 'CD',
            900: 'CM'    
        } 
        roman=''
        for key, val in sorted(symbol_values.items(), reverse=True): 
            # while num >= key:
            #     roman+=val
            #     num-=key 
            while num // key:
                roman+=val
                num-=key 
        return roman



