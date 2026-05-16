# Problem: Best Time to Buy and Sell Stock
# Find maximum profit
# [7,1,5,3,6,4] → buy at 1, sell at 6 → profit = 5

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

print(max_profit([7,1,5,3,6,4]))    # 5
print(max_profit([7,6,4,3,1]))      # 0 (no profit)
print(max_profit([1,2,3,4,5]))      # 4