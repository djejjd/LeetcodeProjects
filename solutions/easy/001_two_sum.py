"""
问题: Two Sum (LeetCode 1)
难度: Easy
链接: https://leetcode.com/problems/two-sum/

描述:
    给定一个整数数组 nums 和一个整数 target，
    返回两个数字的下标，使得它们加起来等于 target。
    
    你可以假设每个输入都恰好有一个解决方案，并且你不能使用相同的元素两次。

示例:
    输入: nums = [2,7,11,15], target = 9
    输出: [0,1]
    解释: nums[0] + nums[1] == 9，所以返回 [0, 1]

时间复杂度: O(n)
空间复杂度: O(n)

关键思想:
    - 使用哈希表存储已访问的数字
    - 对于每个数字，检查它的补数是否已在哈希表中
    - 避免了两层循环，大大提高效率
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        两数之和 - 哈希表方法
        
        思路:
        1. 创建一个字典来存储已见数字和它们的下标
        2. 遍历数组，对于每个数字：
           - 计算所需的补数 (target - num)
           - 如果补数在字典中，返回结果
           - 否则，将当前数字加入字典
        """
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # 如果补数已经在哈希表中，直接返回
            if complement in seen:
                return [seen[complement], i]
            
            # 将当前数字存入哈希表
            seen[num] = i
        
        # 如果没有找到，返回空列表（根据题意不会到这里）
        return []


# 测试用例
def test():
    sol = Solution()
    
    # 测试用例 1: 标准情况
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    print("✅ Test 1 passed: [2, 7, 11, 15] target=9 -> [0, 1]")
    
    # 测试用例 2: 负数
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]
    print("✅ Test 2 passed: [3, 2, 4] target=6 -> [1, 2]")
    
    # 测试用例 3: 数字相同
    assert sol.twoSum([3, 3], 6) == [0, 1]
    print("✅ Test 3 passed: [3, 3] target=6 -> [0, 1]")
    
    # 测试用例 4: 更长的数组
    assert sol.twoSum([1, 2, 3, 4, 5, 6, 7], 13) == [5, 6]
    print("✅ Test 4 passed: [1,2,3,4,5,6,7] target=13 -> [5, 6]")
    
    print("\n🎉 所有测试通过!")


if __name__ == "__main__":
    test()
