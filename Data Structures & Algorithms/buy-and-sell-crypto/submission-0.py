class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Tracking variables
        total_prices: int = len(prices)
        optimal_profit: int = 0  # No transactions edgecase
        l: int = 0  # buy ptr
        r: int = 1  # sell ptr

        # Iterate through all prices (cannot buy on last day)
        while r < total_prices:
            # Check if current trade would be profitable
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                optimal_profit = max(optimal_profit, profit)
            else:
                l = r  # New lowest price found
            r += 1  # Move sell window forward

        # Return optimal profit
        return optimal_profit