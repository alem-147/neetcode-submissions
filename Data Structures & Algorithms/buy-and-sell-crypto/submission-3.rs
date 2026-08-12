impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut profit = 0;
        let mut buy_price = prices[0];

        for i in 1..prices.len() {
            let sell = prices[i];
            profit = profit.max(sell - buy_price);
            buy_price = buy_price.min(sell);
        }
        profit
    }
}
