# Leetcode 1 - Two Sum


# Naive Solution
def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                continue
            if nums[i] + nums[j] == target:
                print(i, j)


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 11
findPairs(myList, target)


# 2. Optimal Solution
def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in seen:
            return [seen[complement], i]

        seen[nums[i]] = i
