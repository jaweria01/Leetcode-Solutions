class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []
        
        # Step 1: collect valid elements
        for i in nums:
            if i != val:
                temp.append(i)
        
        # Step 2: copy back to nums
        for i in range(len(temp)):
            nums[i] = temp[i]
        
        # Step 3: return count
        return len(temp)