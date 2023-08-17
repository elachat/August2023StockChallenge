

def calculateMaxProfit(prices):
    if len(prices) <= 1:
        return 0
    elif len(prices) == 2:
        if prices[0] >= prices [1]:
            return 0
        else:
            prices = prices.sort(reversed = True)
            return prices[0] - prices[1]

    else:
        profit = 0
        for n in range(len(prices)):
            #something
        return profit
