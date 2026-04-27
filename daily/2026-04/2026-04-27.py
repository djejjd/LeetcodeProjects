class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m - 1
        q = n - 1
        j = m + n - 1P


        while j >= 0 :
            if p == -1:
                nums1[j] = nums2[q]
                q -= 1
            elif q == -1:
                nums1[j] = nums1[p]
                p -= 1
            elif nums2[q] >= nums1[p]:
                nums1[j] = nums2[q]
                q -= 1
            elif nums1[p] > nums2[q]:
                nums1[j] = nums1[p]
                p -= 1
            j -= 1
