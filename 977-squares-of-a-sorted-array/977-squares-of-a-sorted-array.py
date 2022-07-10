class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = sorted(nums, key=abs) # 절대값 순으로 정렬
        for i in range(len(nums)):
            answer[i]=answer[i]*answer[i]
        return answer
                