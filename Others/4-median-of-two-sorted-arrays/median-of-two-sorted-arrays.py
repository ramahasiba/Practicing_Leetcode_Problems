import numpy as np

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        merged_len = nums1_len + nums2_len

        def add_zeros():
            for _ in range(nums2_len):
                nums1.append(0)

        add_zeros() 

        def merge_arrays(nums2_len, nums1_len):
            write_index = merged_len - 1
            while nums2_len >= 0:
                if nums1_len >= 0 and nums1[nums1_len] > nums2[nums2_len]:
                    nums1[write_index] = nums1[nums1_len]
                    nums1_len -= 1
                else:
                    nums1[write_index] = nums2[nums2_len]
                    nums2_len -= 1

                write_index -= 1

        merge_arrays(nums2_len - 1, nums1_len - 1) 
        if merged_len % 2 == 0:
            return (nums1[merged_len//2] + nums1[(merged_len // 2) - 1 ]) / 2.0

        return nums1[merged_len//2]  
        
            
        
        
        


        