import pytest
import StockChallenge

prices = []

def testPricesWith1Value():
    prices = [4]
    profit = StockChallenge.calculateMaxProfit(prices)
    assert profit == 0

def testPricesWith2Values():
    prices = [3, 2]
    profit = StockChallenge.calculateMaxProfit(prices)
    assert profit == 0

    prices = [10, 10]
    profit = StockChallenge.calculateMaxProfit(prices)
    assert profit == 0

    prices = [1, 3]
    profit = StockChallenge.calculateMaxProfit(prices)
    assert profit == 2

def testPricesExample1():
    prices = [7,1,5,3,6,4]
    profit = StockChallenge.calculateMaxProfit(prices)
    assert profit == 5

def testPricesExample2():
    prices = [7,6,4,3,1]
    profit = StockChallenge.calculateMaxProfit(prices)
    assert profit == 0