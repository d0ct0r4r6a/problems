/**
 * https://leetcode.com/submissions/detail/689632685/
 * 145 ms, faster than 16.65%
 * 52 MB, less than 35.67%
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let smallestPrice = prices[0];
  let biggestPriceDifference = 0;
  for (let price of prices) {
    if (price < smallestPrice) {
      smallestPrice = price;
    }
    if (price - smallestPrice > biggestPriceDifference) {
      biggestPriceDifference = price - smallestPrice;
    }
  }
  return biggestPriceDifference
};

let prices = [7,6,4,3,1]
console.log(maxProfit(prices))