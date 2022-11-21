class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_element = 10**4 # used to store the minimum element of the list found so far.
        profit = 0
        for element in prices:
            if element < minimum_element:
                minimum_element = element
            profit = max(element - minimum_element, profit)
        return profit
