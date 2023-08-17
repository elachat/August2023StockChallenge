def calculateMaxProfit(prices):
    
    minPrice = prices[0]
    profit = 0

    for price in prices:
        if price < minPrice:
            minPrice = price
        else:
            if price - minPrice > profit:
                profit = price - minPrice
    
    return profit