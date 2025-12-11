{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "aoc";

  buildInputs = with pkgs; [
    pre-commit
    python313
    ruff
    python313Packages.shapely
    python313Packages.pulp
  ];
}
