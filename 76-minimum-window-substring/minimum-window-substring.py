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

