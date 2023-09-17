class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_len, nums2_len, write_index = m-1, n-1, m + n - 1
        while nums2_len >= 0:
            if nums1_len >= 0 and nums1[nums1_len] > nums2[nums2_len]:
                nums1[write_index] = nums1[nums1_len]
                nums1_len -= 1
            else:
                nums1[write_index] = nums2[nums2_len]
                nums2_len -= 1

            write_index -= 1