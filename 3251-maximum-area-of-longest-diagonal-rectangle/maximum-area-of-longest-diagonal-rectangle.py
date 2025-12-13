class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        
        maxDiagonal = 0
        maxArea = 0

        for l , w in dimensions :
            diagonal = l*l + w*w
            area = l*w

            if diagonal > maxDiagonal :
                maxDiagonal = diagonal
                maxArea = area

            elif diagonal == maxDiagonal :
                maxArea = max(maxArea , area)

        return maxArea