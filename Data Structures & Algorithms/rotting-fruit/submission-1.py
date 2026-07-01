class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY,FRESH,ROTTEN=0,1,2
        q=collections.deque()
        m,n=len(grid),len(grid[0])
        fresh_count=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==ROTTEN:
                    q.append((r,c))
                elif grid[r][c]==FRESH:
                    fresh_count+=1
        minutes=-1
        if fresh_count==0:
            return 0
        while q:
            qlen=len(q)
            minutes+=1
            for _ in range(qlen):
                i,j=q.popleft()
                for r,c in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=r<m and 0<=c<n and grid[r][c]==FRESH:
                        grid[r][c]=ROTTEN
                        fresh_count-=1
                        q.append((r,c))


        if fresh_count==0:
            return minutes
        else:
            return -1