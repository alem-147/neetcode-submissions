impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        nums.sort();

        let mut triplets: Vec<Vec<i32>> = Vec::new();

        for (i, val) in nums.iter().enumerate() {
            if *val > 0 {
                break;
            }
            
            if i > 0 && *val == nums[i-1] {
                continue;
            }

            let mut l: usize = i + 1;
            let mut r: usize = nums.len() - 1;
            while l < r {
                match (nums[i] + nums[l] + nums[r]).cmp(&0) {
                    Ordering::Less=>l+=1,
                    Ordering::Greater=>r-=1,
                    Ordering::Equal=> {
                        triplets.push(vec![nums[i], nums[l], nums[r]]);
                        l+=1;
                        r-=1;
                        while l < r && nums[l] == nums[l-1] {
                            l+=1
                        }
                    }
                }
            }
        }
        triplets
    }
}
