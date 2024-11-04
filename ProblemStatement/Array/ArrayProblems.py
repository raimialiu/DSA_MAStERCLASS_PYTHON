"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
from typing import List


class ArrayProblems:
    def __init__(self):
        self.__author = "raimialiu428@gmail.com"

    def TwoSums(self, nums: List[int], target: int) -> List[int]:
        # [0,1,2,3,4] => 6
        def loopsum(list: List[int], popIndexValue):
            list_len = len(list)
            counter = 0
            while counter < list_len:
                current = list[counter]
                if counter + 1 >= list_len:
                    next_item = list[counter + 1]
                    if next_item is not None and (current + next_item == target):
                        return [counter, counter + 1]
                if current == target:
                    return [counter]
                if current + popIndexValue == target:
                    return [counter, popIndexValue]
                counter += 1
            return []

        def shiftArray(list: List[int], answer: List[int], popIndexValue):
            if len(list) == 0:
                return answer
            answer = loopsum(list,popIndexValue)
            if len(answer) == 0:
                pop_index = list.pop(0)
                original_index = nums.index(pop_index)
                shiftArray(list, answer, original_index)
            return answer

        answer = shiftArray(nums, [],0)
        return answer
