impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut l: usize = 0;
        let mut r: usize = numbers.len() -1;

        let mut added: i32 = numbers[l] + numbers[r];
        while l < r {
            match (numbers[l] + numbers[r]).cmp(&target) {
                Ordering::Equal => return vec![(l+1) as i32, (r+1) as i32],
                Ordering::Greater => r -= 1,
                Ordering::Less => l += 1,
            }
        }
        unreachable!("Can't get here")
    }
}
