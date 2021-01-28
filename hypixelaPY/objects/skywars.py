"""
MIT License

Copyright (c) 2020 Myer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from .stats import KillsDeaths, WinsLosses
from .. import utils


class Skywars:
    def __init__(self, data):
        self.name = "Skywars"
        self.prestige = Prestige(data.get("player", {}).get("stats", {}).get("SkyWars", {}).get("skywars_experience", 0))
        self.games_played = data.get("player", {}).get("stats", {}).get("SkyWars", {}).get("games_played_skywars", 0)
        self.coins = data.get("player", {}).get("stats", {}).get("SkyWars", {}).get("coins", 0)
        self.tokens = data.get("player", {}).get("stats", {}).get("SkyWars", {}).get("cosmetic_tokens", 0)
        self.souls = data.get("player", {}).get("stats", {}).get("SkyWars", {}).get("souls", 0)
        self.winstreak = data.get("player", {}).get("stats", {}).get("SkyWars", {}).get("win_streak", 0)
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
    def __init__(self, experience):
        self.exact = utils.get_skywars_level_exact(experience)
        self.star = utils.get_skywars_level(experience)
        self.star_index = self.star // 5
        self.name = utils.get_skywars_prestige_name(self.star_index)
        self.next = self.star + 1
        self.percentage = utils.get_level_percentage(self.exact)
        self.color = utils.get_skywars_prestige_color(self.star_index)
