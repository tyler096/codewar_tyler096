fn bonus_time(salary: u64, bonus: bool) -> String {
    if bonus {
        "¥".to_owned()+&(salary*10).to_string()
    }
    else {
        "¥".to_owned()+&salary.to_string()
    }
}

/*
fn bonus_time(salary: u64, bonus: bool) -> String {
  format!("¥{}", salary * if bonus {10} else {1})
}
*/