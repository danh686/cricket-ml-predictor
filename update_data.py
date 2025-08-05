import argparse
import pandas as pd
import os
from src.input.loaders.cricsheet_loader import parse_cricsheet

LEAGUE_OPTIONS = {"1": "IPL", "2": "BBL", "3": "T20 Blast"}


def choose_league():
    print("Choose a league:")
    for key, league in LEAGUE_OPTIONS.items():
        print(f"{key}. {league}")

    choice = input("Enter the number corresponding to the league: ").strip()
    if choice in LEAGUE_OPTIONS:
        return LEAGUE_OPTIONS[choice]
    else:
        print("Invalid choice.")
        exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Update match data from Cricsheet JSON files."
    )
    parser.add_argument(
        "folder", type=str, help="Path to folder containing Cricsheet JSON files."
    )
    args = parser.parse_args()

    league = choose_league()
    output_path = f"data/{league.lower().replace(" ", "")}_matches.csv"

    print(f"Loading data from {args.folder}...")
    df = parse_cricsheet(args.folder)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Match data saved to {output_path}")


if __name__ == "__main__":
    main()
