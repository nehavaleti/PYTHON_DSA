"""
Question:

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

"""
# Method: 1 , Time Complexity is nlogn and space complexity is O(n)
class Solution:
    def sortedSqaures(self,nums:List[int]) -> List[int]:
        n=len(nums)
        new_array = [0]*n
        for i in range(n):
            new_array[i] = nums[i]**2
        new_array.sort()
        return new_array

# Method: 2, Time Complexity is O(n) and Space Complexity is O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i,j = 0,n-1
        new_array = [0]*n
        for k in reversed(range(n)):
            if nums[i]**2 > nums[j]**2:
                new_array[k] = nums[i]**2
                i+=1
            else:
                new_array[k] = nums[j]**2
                j-=1
        return new_array