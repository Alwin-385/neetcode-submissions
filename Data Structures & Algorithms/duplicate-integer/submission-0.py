class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         for x in range(0,len(nums)):
            for y in range(x+1,len(nums)):
               if nums[x]==nums[y]:
                   return True
         return False   
