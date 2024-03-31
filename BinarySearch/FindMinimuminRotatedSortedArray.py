#Problem 153 :  https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        if(nums[right] > nums[left]):
            return nums[0]
        while left < right:
            mid = (left + right ) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] > nums[0]:
                left = mid + 1
            if nums[mid] < nums[0]:
                right = mid - 1 

        return -5001

        #better implementation
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left=mid + 1
            else:
                right = mid

        return nums[left]
