impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut l: usize = 0;
        let mut r: usize = numbers.len() -1;

        let mut added: i32 = numbers[l] + numbers[r];
        while added != target {
            if added < target {
                l += 1;
            }
            if added > target {
                r -= 1;
            }
            added = numbers[l] + numbers[r]
        }
        vec![l as i32+1, r as i32+1]
    }
}
