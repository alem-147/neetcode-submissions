use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }

        let mut count = [0i32; 26];
        for (s_b, t_b) in s.bytes().zip(t.bytes()) {
            count[(s_b - b'a') as usize] += 1;
            count[(t_b - b'a') as usize] -= 1;
        }

        count.iter().all(|&v| v == 0)
    }
}
