class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hashmap = {}
        ans = []
        for i in range(len(groupSizes)):
            if groupSizes[i] in hashmap:
                hashmap[groupSizes[i]].append(i)
            else:
                hashmap[groupSizes[i]] = [i]
            if len(hashmap[groupSizes[i]]) == groupSizes[i]:
                ans.append(hashmap[groupSizes[i]])
                del hashmap[groupSizes[i]] 
        return ans
