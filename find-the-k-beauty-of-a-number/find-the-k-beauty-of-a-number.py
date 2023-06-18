class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        k_beauty = 0 
        if k == 0: 
            return 0
        str_num = str(num)
        list_length = len(str_num) 
        for item_i in range(list_length - k + 1):
            sub_number = int(str_num[item_i: k + item_i])  
            if sub_number == 0:
                continue
            if num % sub_number == 0:  
                k_beauty = k_beauty + 1 
        return k_beauty
        