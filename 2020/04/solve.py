"""Advent Of Code #04."""


class Passport:
    """Class representing a passport."""

    DECIMAL = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    HEXADECIMAL = DECIMAL + ["a", "b", "c", "d", "e", "f"]

    def __init__(self, data):
        """Initialize the passport."""
        self._byr = None
        self._iyr = None
        self._eyr = None
        self._hgt = None
        self._hcl = None
        self._ecl = None
        self._pid = None
        self._cid = None

        for field in data.split(" "):
            key, value = field.split(":")

            if key == "byr":
                self._byr = value
            if key == "iyr":
                self._iyr = value
            if key == "eyr":
                self._eyr = value
            if key == "hgt":
                self._hgt = value
            if key == "hcl":
                self._hcl = value
            if key == "ecl":
                self._ecl = value
            if key == "pid":
                self._pid = value
            if key == "cid":
                self._cid = value

    def has_required_fields(self):
        """Check if passport has all required fields."""
        return (
            self._byr is not None
            and self._iyr is not None
            and self._eyr is not None
            and self._hgt is not None
            and self._hcl is not None
            and self._ecl is not None
            and self._pid is not None
        )

    def has_valid_fields(self):
        """Check if passport fields are valid."""
        if not self.has_required_fields():
            return False

        if not (1920 <= int(self._byr) <= 2002):
            return False
        if not (2010 <= int(self._iyr) <= 2020):
            return False
        if not (2020 <= int(self._eyr) <= 2030):
            return False

        if self._hgt.endswith("cm"):
            if not (150 <= int(self._hgt[:-2]) <= 193):
                return False
        elif self._hgt.endswith("in"):
            if not (59 <= int(self._hgt[:-2]) <= 76):
                return False
        else:
            return False

        if len(self._hcl) == 7:
            if not self._hcl[0] == "#":
                return False
            for i in range(1, 7):
                if not self._hcl[i] in Passport.HEXADECIMAL:
                    return False
        else:
            return False

        if self._ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False

        if len(self._pid) == 9:
            for i in range(9):
                if not self._pid[i] in Passport.DECIMAL:
                    return False
        else:
            return False

        return True


with open("input") as f:
    data = f.read().strip()
data = data.split("\n\n")
data = [d.replace("\n", " ") for d in data]
passports = [Passport(data[i]) for i in range(len(data))]

# Part 1
valid = 0
for passport in passports:
    if passport.has_required_fields():
        valid += 1
print("Part 1:", valid)
assert valid == 219

# Part 2
valid = 0
for passport in passports:
    if passport.has_valid_fields():
        valid += 1
print("Part 2:", valid)
assert valid == 127
