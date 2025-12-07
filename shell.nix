{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "aoc";

  buildInputs = with pkgs; [
    pre-commit
    python3
    ruff
  ];
}
