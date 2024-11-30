#!/usr/bin/env python
"""Get Advent Of Code input automatically."""

import argparse
import datetime
import pathlib
import urllib.request
from pathlib import Path

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("day", type=int, nargs="?")
parser.add_argument("year", type=int, nargs="?")
args = parser.parse_args()

# Setup default value to today if not specified
today = datetime.datetime.now(tz=datetime.UTC)
if args.year is None:
    args.year = today.year
if args.day is None:
    args.day = today.day

# Create url and filename from arguments
url = f"https://adventofcode.com/{args.year}/day/{args.day}/input"
filename = f"{args.year}/{args.day:02}/input"

# Read token from file and create cookies
with Path.open(".token") as f:
    token = f.read().strip()
cookie = f"session={token}"

# Fetch and save to file
req = urllib.request.Request(url, headers={"Cookie": cookie.strip()})  # noqa: S310
Path.mkdir(pathlib.Path(filename).parent, parents=True, exist_ok=True)
with Path.open(filename, "w") as f:
    f.write(urllib.request.urlopen(req).read().decode())  # noqa: S310
