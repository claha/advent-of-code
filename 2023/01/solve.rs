use std::fs::File;
use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let file = File::open("input")?;
    let lines: Vec<String> = io::BufReader::new(file)
        .lines()
        .map(|l| l.unwrap())
        .collect();

    let mut sum = 0;

    for line in &lines {
        let first_num = find_first_num(line, false);
        let last_num = find_last_num(line, false);
        let combined = combine_numbers(&first_num, &last_num);
        sum += combined;
    }

    println!("Part 1: {}", sum);
    assert!(sum == 56042);

    let mut sum = 0;

    for line in &lines {
        let first_num = find_first_num(line, true);
        let last_num = find_last_num(line, true);
        let combined = combine_numbers(&first_num, &last_num);
        sum += combined;
    }

    println!("Part 2: {}", sum);
    assert!(sum == 55358);

    Ok(())
}

fn find_first_num(line: &str, spelled_out: bool) -> String {
    for (i, c) in line.chars().enumerate() {
        if c.is_digit(10) {
            return c.to_string();
        } else if spelled_out {
            for (j, n) in [
                "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
            ]
            .iter()
            .enumerate()
            {
                if i + n.len() < line.len() && &line[i..i + n.len()] == *n {
                    return (j + 1).to_string();
                }
            }
        }
    }
    "0".to_string()
}

fn find_last_num(line: &str, spelled_out: bool) -> String {
    let reversed_line: String = line.chars().rev().collect();
    for (i, c) in reversed_line.chars().enumerate() {
        if c.is_digit(10) {
            return c.to_string();
        } else if spelled_out {
            for (j, n) in [
                "eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "eni",
            ]
            .iter()
            .enumerate()
            {
                if i + n.len() < reversed_line.len() && &reversed_line[i..i + n.len()] == *n {
                    return (j + 1).to_string();
                }
            }
        }
    }
    "0".to_string()
}

fn combine_numbers(first_num: &str, last_num: &str) -> u32 {
    format!("{}{}", first_num, last_num).parse().unwrap_or(0)
}
