import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_len = len(nums1)
        nums2_len = len(nums2)

        def add_zeros():
            for _ in range(nums2_len):
                nums1.append(0)
        add_zeros() 

        def merge_arrays(nums2_len, nums1_len):
            write_index = nums1_len + nums2_len + 1
            while nums2_len >= 0:
                if nums1_len >= 0 and nums1[nums1_len] > nums2[nums2_len]:
                    nums1[write_index] = nums1[nums1_len]
                    nums1_len -= 1
                else:
                    nums1[write_index] = nums2[nums2_len]
                    nums2_len -= 1

                write_index -= 1

        merge_arrays(nums2_len - 1, nums1_len - 1)
 
        return np.median(nums1)
        


        