use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut s_occs: HashMap<char, i32> = HashMap::new();
        let mut t_occs: HashMap<char, i32> = HashMap::new();
        
        if s.chars().count() != t.chars().count() {
            return false
        }
        for (s_let, t_let) in s.chars().zip(t.chars()) {
            *s_occs.entry(s_let).or_insert(0) += 1;
            *t_occs.entry(t_let).or_insert(0) += 1;
        }
        s_occs == t_occs
    }
}
