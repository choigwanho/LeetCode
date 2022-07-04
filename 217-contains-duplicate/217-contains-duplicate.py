class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        answer = True
        
        if len(set(nums))==len(nums):
            answer=False
        
        return answer
        