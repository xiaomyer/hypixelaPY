from .. import utils
from .stats import KillsDeaths, WinsLosses


class Skywars:
    def __init__(self, data):
        self.name = "Skywars"
        self.prestige = Prestige(data)
        self.games_played = data.get("player", {}).get("stats", {}).get("SkyWars", {}).get("games_played_skywars", 0)
        self.coins = data.get("player", {}).get("stats", {}).get("SkyWars", {}).get("coins", 0)
        self.tokens = data.get("player", {}).get("stats", {}).get("SkyWars", {}).get("cosmetic_tokens", 0)
        self.souls = data.get("player", {}).get("stats", {}).get("SkyWars", {}).get("souls", 0)
        self.winstreak = data.get("player", {}).get("stats", {}).get("SkyWars", {}).get("winstreak", 0)
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("SkyWars", {}).get("kills", 0),
            data.get("player", {}).get("stats", {}).get("SkyWars", {}).get("deaths", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("SkyWars", {}).get("wins", 0),
            data.get("player", {}).get("stats", {}).get("SkyWars", {}).get("losses", 0)
        )

    def __str__(self):
        return self.name


class Prestige:
    def __init__(self, data):
        self.exact = utils.get_skywars_level_exact(data.get("player", {}).get("stats", {}).get("SkyWars", {}).get("skywars_experience", 0))
        self.star = utils.get_skywars_level(data.get("player", {}).get("stats", {}).get("SkyWars", {}).get("skywars_experience", 0))
        self.next = self.star + 1
        self.star_index = self.star // 5
        self.percentage = utils.get_level_percentage(self.exact)
        self.color = utils.get_skywars_prestige_color(self.star_index)
