"""Get Advent Of Code input automatically."""
import argparse
import datetime
import os
import pathlib
import urllib.request

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("year", type=int, nargs="?")
parser.add_argument("day", type=int, nargs="?")
args = parser.parse_args()

# Setup default value to today if not specified
today = datetime.datetime.now()
if args.year is None:
    args.year = today.year
if args.day is None:
    args.day = today.day

# Create url and filename from arguments
url = f"https://adventofcode.com/{args.year}/day/{args.day}/input"
filename = f"{args.year}/{args.day:02}/input"

# Read token from file and create cookies
with open(".token") as f:
    token = f.read().strip()
cookie = f"session={token}"

# Fetch and save to file
req = urllib.request.Request(url, headers={"Cookie": cookie.strip()})
os.makedirs(pathlib.Path(filename).parent, exist_ok=True)
with open(filename, "w") as f:
    f.write(urllib.request.urlopen(req).read().decode())
