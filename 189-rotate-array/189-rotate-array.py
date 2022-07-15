class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n= len(nums)
        k = k % n # K가 nums의 길이보다 클 때, nums의 길이만큼은 회전할 필요가 없기 때문에 나머지로 반복을 없앤다.
        nums[:]= nums[n-k:]+nums[:n-k]