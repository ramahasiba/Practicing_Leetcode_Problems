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
        if t == s:
            equals = True
        return equals