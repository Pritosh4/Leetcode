class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        array = []
                    
        for interval in intervals:
            if not array or array[-1][1] < interval[0]:
                array.append(interval)
            else:
                array[-1][1] = max(array[-1][1], interval[1])
        return array
        
