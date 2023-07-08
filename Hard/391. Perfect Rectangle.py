class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        corner = set()
        for x1, y1, x2, y2 in rectangles:
            area += (x2 - x1) * (y2 - y1)
            for i in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if i in corner:
                    corner.remove(i)
                else:
                    corner.add(i)
        
        if len(corner) != 4:
            return False
        
        X1, Y1 = float('inf'), float('inf')
        X2, Y2 = float('-inf'), float('-inf')
        for x, y in corner:
            X1 = min(X1, x)
            Y1 = min(Y1, y)
            X2 = max(X2, x)
            Y2 = max(Y2, y)
        return area == (X2 - X1) * (Y2 - Y1)
