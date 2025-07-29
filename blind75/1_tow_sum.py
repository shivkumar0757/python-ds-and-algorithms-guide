# LeetCode Problem #1
"""
Problem Statement:
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
Bassically, you are given the list of some numbers and a target number,
you need to give us the position(index) of the two numbers which add up to the target number.
example:
```
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```
"""
from typing import List

def tow_sum(nums: List[int], target:int) -> List[int]:
    # we need to return the indices, so we need to keep track of the indices
    # we can use a dictionary to store the indices of the numbers
    # if we need to return the element or number, we can use the set to store the numbers and find the
    # number theat will make current number sum equal to target
    num_to_index = dict()

    for index , num in enumerate(nums):
        # calculate the number that will make current numnber sum equal to target
        complement = target - num

        # if the complement is already in the dictionary, we have found the two numbers
        if complement in num_to_index:
            return [num_to_index[complement], index]

        # if not, we add the current number and its index to the dictionary
        num_to_index[num] = index

    # if we reach here, it means we didn't find any two numbers that add up to target
    return []


if __name__ == "__main__":
    # Test case 1: Basic example from problem description
    assert tow_sum([2, 7, 11, 15], 9) == [0, 1]
    print("Test case 1 passed")
    
    # Test case 2: Target sum with negative numbers
    assert tow_sum([-1, -2, -3, -4, -5], -8) == [2, 4]
    print("Test case 2 passed")
    
    # Test case 3: Target sum with duplicate values
    assert tow_sum([3, 3], 6) == [0, 1]
    print("Test case 3 passed")
    
    print("All test cases passed!")