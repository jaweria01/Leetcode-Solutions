class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # brute force
        # Two pointers
        l = 0
        r = len(numbers)-1
        while l<r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return l+1, r+1
            elif sum > target:
                r -= 1
            elif sum< target:
                l +=1

        


















        
        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]   # 1-based indexing
# # Two pointer approch 

#         l = 0
#         r = len(numbers)-1
#         while l<r :
#             if numbers[l] + numbers[r] == target:
#                 return [l+1 , r+1]
#             elif numbers[l] + numbers[r] > target:
#                 r -=1 # move right pointer left
#             else:
                #l+=1 # move left pointer left
               # r+=1 # move left pointer left still its giving answer correct even I'm moving right pointer 
# Since r already starts at the end (len(numbers)-1), increasing it will eventually make r == len(numbers) (which is out of range). When you later do numbers[r], Python crashes with IndexError: list index out of range.
                

# Brute Force approch




        