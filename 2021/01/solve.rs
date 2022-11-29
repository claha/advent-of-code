// Advent Of Code #01.
use std::fs;

fn read_input() -> Vec<i32> {
    let input = fs::read_to_string("input").expect("Failed to read input");
    let data: Vec<i32> = input
        .lines()
        .map(|d| d.parse().expect("Failed to parse"))
        .collect();
    return data;
}

fn solve_part_1(data: Vec<i32>) {
    let mut count = 0;
    for i in 1..data.len() {
        if data[i] > data[i - 1] {
            count += 1;
        }
    }
    println!("Part 1: {count}");
    assert!(count == 1298)
}

fn solve_part_2(data: Vec<i32>) {
    let mut count = 0;
    for i in 3..data.len() {
        if data[i] > data[i - 3] {
            count += 1;
        }
    }
    println!("Part 2: {count}");
    assert!(count == 1248)
}

fn main() {
    let data = read_input();
    solve_part_1(data.clone());
    solve_part_2(data.clone());
}
