impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut res = 0;
        let mut buy_price = prices[0];

        for &price in &prices {
            res = res.max(price - buy_price);
            buy_price = buy_price.min(price);
        }
        res
    }
}
