struct MinStack {
    prefix_min_stk: Vec<i32>,
    stk: Vec<i32>,
}

impl MinStack {
    pub fn new() -> Self {
        Self {
            prefix_min_stk: Vec::new(),
            stk: Vec::new(),
        }
    }

    pub fn push(&mut self, val: i32) {
        match self.prefix_min_stk.last() {
            Some(x) => {
                self.prefix_min_stk.push((*x).min(val))
            }
            None => {
                self.prefix_min_stk.push(val)
            }
        }
        self.stk.push(val)
    }

    pub fn pop(&mut self) {
        self.prefix_min_stk.pop();
        self.stk.pop();
    }

    pub fn top(&self) -> i32 {
        *self.stk.last().unwrap()
    }

    pub fn get_min(&self) -> i32 {
        *self.prefix_min_stk.last().unwrap()
    }
}
