# LeetCode Solutions

每日LeetCode刷题记录，按难度分类存储解题代码。

## 📁 项目结构

```
LeetcodeProjects/
├── README.md                 # 项目说明文档
├── solutions/                # 所有题目的最终解答
│   ├── easy/                # 简单题（Easy）
│   ├── medium/              # 中等题（Medium）
│   └── hard/                # 困难题（Hard）
├── daily/                   # 每日刷题记录
│   ├── 2026-04/            # 按月份组织
│   │   ├── 2026-04-25.md   # 日期记录（包括思路、总结）
│   │   └── ...
│   └── ...
├── utils/                   # 辅助工具和测试
│   ├── test_helper.py      # 测试辅助函数
│   └── template.py         # 解题模板
└── venv/                    # Python虚拟环境（Git忽略）
```

## 🚀 快速开始

### 1. 激活虚拟环境
```bash
source venv/bin/activate
```

### 2. 创建新题目解答

**在 `solutions/easy/` 中创建文件：**
```
solutions/easy/001_two_sum.py
```

**文件格式示例：**
```python
"""
问题: Two Sum (LeetCode 1)
难度: Easy
链接: https://leetcode.com/problems/two-sum/

描述:
    给定一个整数数组 nums 和一个目标值 target，
    返回数组中和为目标值的两个数的下标。
    
时间复杂度: O(n)
空间复杂度: O(n)
"""

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    """
    使用哈希表来存储已见过的数字和它们的下标
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# 测试用例
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))  # [0, 1]
```

### 3. 记录每日进度

**在 `daily/2026-04/` 中创建日期文件：**
```markdown
# 2026-04-25 刷题记录

## 完成题目
- [x] 1. Two Sum (Easy)

## 今日总结
- 学会了哈希表的使用
- 时间复杂度优化从O(n²)到O(n)

## 困难点
- 理解两数之和的最优解法

## 明天计划
- 完成 Add Two Numbers
```

## 📊 刷题统计

| 难度 | 已完成 | 计划 |
|------|--------|------|
| Easy | 0 | 50 |
| Medium | 0 | 40 |
| Hard | 0 | 20 |

## 💡 解题建议

1. **先理解问题** - 清楚理解题目要求
2. **分析复杂度** - 考虑时间和空间复杂度
3. **多种解法** - 尝试不同的方法
4. **测试用例** - 包括边界情况
5. **总结反思** - 记录关键要点

## 🔗 有用资源

- [LeetCode](https://leetcode.com/)
- [Python类型提示](https://docs.python.org/3/library/typing.html)
- [算法复杂度分析](https://en.wikipedia.org/wiki/Big_O_notation)

## 📝 提交规范

```bash
git add .
git commit -m "Add: Problem 001 Two Sum (Easy)"
# 或
git commit -m "Update: Daily record for 2026-04-25"
git push
```

---
**开始你的LeetCode之旅吧！🎯**
