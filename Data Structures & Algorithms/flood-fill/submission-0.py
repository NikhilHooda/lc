class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    
        orig = image[sr][sc]  
        if orig == color:
            return image 
        ROWS, COLS = len(image), len(image[0])


        def dfs(r,c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or image[r][c] != orig:
               return
            
            if image[r][c] == orig:
                image[r][c] = color
            
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
            return 
        
        dfs(sr,sc)
        return image


            

        

        