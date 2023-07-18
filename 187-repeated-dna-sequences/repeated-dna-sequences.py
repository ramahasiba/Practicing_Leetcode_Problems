class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        s_length = len(s)

        if s_length < 10: 
            return []
        else:
            sequence_frequency = {}
            sequences = set()
            left_ptr, right_ptr = 0, 10
            while right_ptr <= s_length:
                sequence = s[left_ptr: right_ptr]
                if sequence in sequence_frequency:
                    sequences.add(sequence)
                else:
                    sequence_frequency[sequence] = 1
                    
                right_ptr += 1
                left_ptr += 1
        return sequences

