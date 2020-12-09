// Advent Of Code #01.
var fs = require("fs");

var data = fs.readFileSync("input", "utf8");
data = data.toString().split("\n").map(Number);

// Part 1
function get_pair(data, target) {
  var lut = new Set();
  for (const a of data) {
    const b = target - a;
    if (lut.has(b)) {
      return { a, b };
    }
    lut.add(a);
  }
}

var pair = get_pair(data, 2020);
console.log("Part 1:", pair.a * pair.b);
console.assert(pair.a * pair.b == 997899);

// Part 2
function get_triplet(data, target) {
  for (const [i, a] of data.entries()) {
    var lut = new Set();
    for (const b of data.slice(i + 1)) {
      const c = target - a - b;
      if (lut.has(c)) {
        return { a, b, c };
      }
      lut.add(b);
    }
  }
}

var triplet = get_triplet(data, 2020);
console.log("Part 2:", triplet.a * triplet.b * triplet.c);
console.assert(triplet.a * triplet.b * triplet.c == 131248694);
