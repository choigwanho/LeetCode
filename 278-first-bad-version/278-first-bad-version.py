# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        for i in range(1,n+1):
            start, end = 1, n
            
            while start<end:
                mid=int((start+end)/2) # 확인할 중간
                if isBadVersion(mid):
                    end=mid # 참이면 시작부터 중간까지 탐색
                else:
                    start=mid+1 # 거짓이면 중간 이후부터 끝까지 탐색
            return start # start<end 에서 멈추면 start 값 출력
        
