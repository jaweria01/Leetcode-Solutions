class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = sum(nums[:k])
        max_sum = cur_sum
        for i in range(k, len(nums)): # range(start,stop, step)
            cur_sum += nums[i] - nums[i-k] 
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum/k # average

# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         s=sum(nums[:k])
#         m=s
#         for i in range(k,len(nums)):
#             s=s+nums[i]-nums[i-k]
#             m=max(m,s)
#         return m/k

        