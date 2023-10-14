"""
CP1404 Practical 05: Game, Set, Match
Estimated Time: 30 minutes
Actual Time: 31 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    champion_to_win = {}
    countries_with_wins = set()
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            data = line.split(',')
            update_champions(champion_to_win, data)
            update_countries(countries_with_wins, data)
    print_report(champion_to_win, countries_with_wins)


def update_countries(countries_with_wins, data):
    countries_with_wins.add(data[1])


def update_champions(champion_to_win, data):
    try:
        champion_to_win[data[2]] += 1
    except KeyError:
        champion_to_win[data[2]] = 1


def print_report(champion_to_win: dict, countries_with_wins: set) -> None:
    print(f"Wimbledon Champions:")
    for champion in champion_to_win:
        print(f"{champion} {champion_to_win[champion]}")
    countries_with_wins = list(countries_with_wins)
    countries_with_wins.sort()
    print(f"\nThese {len(countries_with_wins)} have won Wimbledon:")
    print(", ".join(countries_with_wins))


main()
