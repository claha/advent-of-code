"""Get Advent Of Code input automatically."""
import argparse
import urllib.request

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("year", type=int)
parser.add_argument("day", type=int)
args = parser.parse_args()

# Create url and filename from arguments
url = f"https://adventofcode.com/{args.year}/day/{args.day}/input"
filename = f"{args.year}/{args.day:02}/input"

# Read token from file and create cookies
with open(".token", "r") as f:
    token = f.read().strip()
cookie = f"session={token}"

# Fetch and save to file
req = urllib.request.Request(url, headers={"Cookie": cookie.strip()})
with open(filename, "w") as f:
    f.write(urllib.request.urlopen(req).read().decode())
