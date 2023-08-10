'''
Given an integer array nums,
rotate the array to the right by k steps, where k is non-negative.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''


def rotate(nums, k):
    n = len(nums)
    k %= n  # Calculate effective rotation steps
    nums[-int(k):] + nums[:-int(k)]
    return nums

rotate([6,5,4,3,3,2,1], 3)

'''
-> for value of k
-> slice the list for the k numbers from the end 
-> nums[::-k]

'''

#new solution 
def rotate_one(nums, k):
        n = len(nums)
        k %= n  # Calculate effective rotation steps
        
        # Extract the last k elements and place them at the beginning
        result = nums[:] = nums[-k:] + nums[:-k]
        print(nums[:])

        return result

rotate_one([1,2,3,4,5,6], 3)

