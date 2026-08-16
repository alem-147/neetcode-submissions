impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut low = 0;
        let mut high = nums.len();

        while low < high {
            let idx = low + (high - low) / 2;
            match nums[idx].cmp(&target) {
                Ordering::Greater=> high = idx,
                Ordering::Less => low = idx + 1,
                Ordering::Equal =>return idx as i32,
            }
        }
        -1
    }
}
