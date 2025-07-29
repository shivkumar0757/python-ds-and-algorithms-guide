# LeetCode Problem #2210
"""
Problem Statement:
You are given a 0-indexed integer array nums. An index i is part of a hill if the closest non-equal neighbors are smaller than nums[i]. 
Similarly, an index i is part of a valley if the closest non-equal neighbors are larger than nums[i].
Basically, you need to count how many hills and valleys are in the array.
example:
```
Input: nums = [2,4,1,1,6,5]
Output: 3
Explanation: Index 1 is a hill (4 > 2 and 4 > 1), index 2 is a valley (1 < 4 and 1 < 6), index 4 is a hill (6 > 1 and 6 > 5).
```
"""
from typing import List

def countHillValley(nums: List[int]) -> int:
    # we need to count hills and valleys in the array
    # a hill is when current element is greater than both neighbors
    # a valley is when current element is less than both neighbors
    # we need to skip consecutive equal elements
    
    if len(nums) < 3:
        return 0
    
    count = 0
    prev = nums[0]  # keep track of previous non-equal element
    n = len(nums)
    i = 1
    
    while i < n - 1:
        # skip consecutive equal elements
        if nums[i] == nums[i + 1]:
            i += 1
            continue
        
        # check if current element forms a hill or valley
        if (nums[i] > prev and nums[i] > nums[i + 1]) or (nums[i] < prev and nums[i] < nums[i + 1]):
            count += 1
        
        # update previous non-equal element
        prev = nums[i]
        i += 1
    
    # if we reach here, we have counted all hills and valleys
    return count


if __name__ == "__main__":
    # Test case 1: Basic example with hills and valleys
    assert countHillValley([2, 4, 1, 1, 6, 5]) == 3
    print("Test case 1 passed")
    
    # Test case 2: Array with no hills or valleys
    assert countHillValley([6, 6, 5, 5, 4, 1]) == 0
    print("Test case 2 passed")
    
    # Test case 3: Array with alternating values
    assert countHillValley([1, 2, 1, 3, 5, 4, 2, 1, 3]) == 4
    print("Test case 3 passed")
    
    print("All test cases passed!")