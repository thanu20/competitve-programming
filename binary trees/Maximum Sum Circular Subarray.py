class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #for circular sum array use total sum of original array and next subtract it from the minimum of the array
        def kadane(nums):
            if not nums:
                return 0

            max_sum = current_sum = nums[0]
            for num in nums[1:]:
                current_sum = max(num, current_sum + num)
                max_sum = max(max_sum, current_sum)
            return max_sum

        n = len(nums)
        if n == 1:
            return nums[0]

        max_sum_within_circular = kadane(nums)
        max_sum_total = sum(nums) + kadane([-num for num in nums[1:n-1]])
        return max(max_sum_within_circular, max_sum_total)
