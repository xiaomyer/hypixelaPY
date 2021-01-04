from .stats import KillsDeaths, WinsLosses


class Duels:
    def __init__(self, data):
        self.name = "Duels"
        self.games_played = data.get("player", {}).get("stats", {}).get("Duels", {}).get("games_played_duels", 0)
        self.coins = data.get("player", {}).get("stats", {}).get("Duels", {}).get("coins", 0)
        self.winstreak = data.get("player", {}).get("stats", {}).get("Duels", {}).get("current_winstreak", 0)
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("kills", 0),
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("deaths", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("wins", 0),
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("losses", 0)
        )

    def __str__(self):
        return self.name
