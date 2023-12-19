use std::fs::File;
use std::io::{self, BufRead};
//use std::collections::HashMap;

#[derive(Debug)]
struct MaxCounts {
    red: usize,
    green: usize,
    blue: usize,
}

fn main() -> io::Result<()> {
    let file = File::open("input")?;
    let games: Vec<String> = io::BufReader::new(file)
        .lines()
        .map(|line| line.unwrap())
        .collect();

    let mut possible_games_sum = 0;
    let mut power_sum = 0;

    for game in games.iter() {
        let (game_id_str, rounds) = game.split_once(": ").unwrap();
        let game_id = game_id_str[5..].parse::<usize>().unwrap();

        let maxes = process_game(rounds);

        if maxes.red <= 12 && maxes.green <= 13 && maxes.blue <= 14 {
            possible_games_sum += game_id;
        }

        power_sum += maxes.red * maxes.green * maxes.blue;
    }

    println!("Part 1: {}", possible_games_sum);
    assert!(possible_games_sum == 2156);
    println!("Part 2: {}", power_sum);
    assert!(power_sum == 66909);

    Ok(())
}

fn process_game(rounds: &str) -> MaxCounts {
    let mut maxes = MaxCounts { red: 0, green: 0, blue: 0 };

    for hand in rounds.split("; ").flat_map(|round| round.split(", ")) {
        let (count_str, color) = hand.split_once(" ").unwrap();
        let count = count_str.parse::<usize>().unwrap();

        match color {
            "red" => maxes.red = maxes.red.max(count),
            "green" => maxes.green = maxes.green.max(count),
            "blue" => maxes.blue = maxes.blue.max(count),
            _ => {}
        }
    }

    maxes
}
