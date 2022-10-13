#leetcode question - https://leetcode.com/problems/two-sum/submissions/
#Used try and except to avoid checking if the element is present in the map everytime.
def twoSum( nums, target):
    map = {}
    for i in range(len(nums)):
        try:
            v = map[nums[i]]
            return [i, v]
        except:
            map[target - nums[i]] = i

if __name__ == "__main__":
    twoSum([2,7,8,15], 9)

    
#solution that i looked up
def twoSum(nums, target):
    map_of_numbers = {}
    for i, value in enumerate(nums):
        if target - value in map_of_numbers:
            return [i, map_of_numbers[target - value]]
        map_of_numbers[value] = i
