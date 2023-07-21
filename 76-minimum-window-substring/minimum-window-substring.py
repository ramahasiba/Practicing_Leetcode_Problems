class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_length, t_length = len(s), len(t) 

        if t_length > s_length:
            return "" 
        elif t == s:
            return s
        elif t_length == 1:
            try:
                s.index(t)
                return t
            except:
                return ""

        ans=""
        t_frequency = collections.Counter(t)
        track = dict()

        def test():
            for key, val in t_frequency.items():
                if val > track[key]:
                    return False
            return True

        #init
        for k in t_frequency.keys():
            track.update(
                {k : 0}
                )

        #first look
        left_ptr = 0
        right_ptr = 0
        for i in range(s_length): 
            if s[i] in t_frequency.keys():
                left_ptr = i
                break
        
        for i in range(left_ptr, s_length):
            
            #move right
            right_ptr = i
            if s[i] in t_frequency.keys():
                track.update({s[i]: track[s[i]] + 1})
                while test():
                    w=s[left_ptr: right_ptr + 1]
                    if ans=="" or len(w)<len(ans):
                        ans=w

                    #move left
                    track.update({s[left_ptr]: track[s[left_ptr]] - 1}) 
                    for j in range(left_ptr + 1, right_ptr + 1):
                        if s[j] in t_frequency.keys():
                            left_ptr = j
                            break

        if (test()):
            if ans == "" or len(w) < len(ans):
                ans = w

        return ans


#         t_set = set(t)
#         t_set_length = len(t_set)

#         left_ptr, right_ptr = 0, s_length - 1

#         while left_ptr < s_length and s[left_ptr] not in t_set:
#             left_ptr += 1
        
#         while right_ptr >= 0 and s[right_ptr] not in t_set:
#             right_ptr -= 1 

#         string_list = []

#         list_right = right_ptr + 1
 
#         min_length = 10000000
#         start_ptr, end_ptr = 0, 0

#         #####################
#         while left_ptr < right_ptr:
#             if s[left_ptr] in t_set:
#                 t_dict = {}
#                 for char in t_set:
#                     t_dict[char] = False 
                    
#                     indices_list = []

#                     contains_all_chars = True
#                     current_set = set()
#                     for t_char in t_dict:
#                         try:
#                             t_dict[t_char] = True
#                             indices_list.append(
#                                 s[left_ptr:].index(t_char) + left_ptr
#                                 )
#                             current_set.add(t_char)
#                         except: 
#                             # contains_all_chars = False 
#                             pass

#                     if len(indices_list) > 0 and t_set_length == len(current_set):
#                         print(contains_all_chars, indices_list)
#                         max_index = max(indices_list)
#                         min_index = min(indices_list) 
#                         size = max_index - min_index 

#                         if size <= min_length:
#                             min_length = size
#                             start_ptr, end_ptr = min_index, max_index + 1 
 
#             left_ptr += 1 
#         #####################

#         # for element in string_list:
#             # counter = 0
#             # for char in element:
#             #     if char in t_set:
#             #         counter += 1
            
#             # if counter >= t_set_length:
#             #     return element
            
#             for bool_char in t_dict:
#                 if t_dict[bool_char]:
#                     continue
#                 else:
#                     return ""

#         return s[start_ptr: end_ptr]

