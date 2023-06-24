def remove_backspace(s:str) -> str:
    counter = 0
    for index, char_ in enumerate(s):
        if char_ == '#' and (index - counter) != 0:
            s = s[: index - (1 + counter)] + s[(index + 1) - counter: ]
            counter = counter + 2

        elif char_ == '#' and (index - counter) == 0:
            s = s[1: ]
            counter = counter + 1
    return s
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        equals = False
        s = remove_backspace(s)
        t = remove_backspace(t)
        # s_counter = 0
        # s_length = len(s)
        # for index, char in enumerate(s):
        #     if index < s_length - 1:
        #         if s[index + 1 - s_counter] == '#':
        #             s = s[: index - s_counter] + s[index + 2 - s_counter: ]
        #             s_counter = s_counter + 2   

        # t_counter = 0
        # t_length = len(t)
        # for index, char in enumerate(t):
        #     if index < t_length - 1:
        #         if t[index + 1 - t_counter] == '#':
        #             t = t[: index - t_counter] + t[index + 2 - t_counter: ]
        #             t_counter = t_counter + 2 

        if t == s:
            equals = True


        return equals