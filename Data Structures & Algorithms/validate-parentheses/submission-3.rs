impl Solution {
    pub fn is_valid(s: String) -> bool {
        /*
        case open - append to stack
        case close - if not stack or equiv open key, return false
        */
        let mut stack:  Vec<char> = vec![];
        let pairs: HashMap<char, char> = HashMap::from([
            (')', '('),
            (']', '['),
            ('}', '{'),
        ]);

        for c in s.chars() {
            match c {
                '(' | '{' | '[' => stack.push(c),

                ')' | ']' | '}' => {
                    if stack.pop() != pairs.get(&c).copied() {
                        return false
                    }
                }
                _ => {}
            }
        }
        stack.len() == 0
    }
}
