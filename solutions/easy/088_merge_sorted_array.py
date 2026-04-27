from typing import List

"""
问题: Merge Sorted Array (LeetCode 88)
难度: Easy
链接: https://leetcode.com/problems/merge-sorted-array/

描述:
    给你两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，
    使 nums1 成为一个有序数组。

时间复杂度: O(m + n)
空间复杂度: O(1)
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """官方标准解法：从尾部双指针原地合并。"""
        p = m - 1
        q = n - 1
        j = m + n - 1

        while j >= 0:
            if p == -1:
                nums1[j] = nums2[q]
                q -= 1
            elif q == -1:
                nums1[j] = nums1[p]
                p -= 1
            elif nums2[q] >= nums1[p]:
                nums1[j] = nums2[q]
                q -= 1
            else:
                nums1[j] = nums1[p]
                p -= 1
            j -= 1


class SolutionSort:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """简洁解法：直接将 nums2 放入 nums1 后排序。"""
        nums1[m:] = nums2[:n]
        nums1.sort()


class SolutionBuffer:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """辅助数组解法：先合并到临时数组再写回 nums1。"""
        merged = []
        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        if i < m:
            merged.extend(nums1[i:m])
        if j < n:
            merged.extend(nums2[j:n])

        nums1[:m+n] = merged


class SolutionHeap:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """Pythonic 解法：利用 heapq.merge 生成有序序列。"""
        import heapq

        nums1[:m+n] = list(heapq.merge(nums1[:m], nums2[:n]))


def _run_merge(merge_fn, test_cases):
    for nums1, m, nums2, n, expected in test_cases:
        arr = nums1.copy()
        merge_fn(arr, m, nums2.copy(), n)
        assert arr == expected, f"{arr} != {expected}"


def test():
    test_cases = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([0], 0, [1], 1, [1]),
        ([1], 1, [], 0, [1]),
        ([2, 0], 1, [1], 1, [1, 2]),
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
    ]

    _run_merge(Solution().merge, test_cases)
    _run_merge(SolutionSort().merge, test_cases)
    _run_merge(SolutionBuffer().merge, test_cases)
    _run_merge(SolutionHeap().merge, test_cases)

    print("✅ 088_merge_sorted_array: 所有解法测试通过")


if __name__ == "__main__":
    test()
