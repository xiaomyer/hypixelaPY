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
        self.bow = Bow(data)
        self.classic = Classic(data)
        self.uhc = UHC(data)

    def __str__(self):
        return self.name


class Bow:
    def __init__(self, data):
        self.name = "Bow"
        self.games_played = data.get("bow_duel_rounds_played", 0)
        self.winstreak = data.get("player", {}).get("stats", {}).get("Duels", {}).get("current_bow_winstreak", 0)
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("bow_duel_kills", 0),
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("bow_duel_deaths", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("bow_duel_wins", 0),
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("bow_duel_losses", 0)
        )

    def __str__(self):
        return self.name


class Classic:
    def __init__(self, data):
        self.name = "Classic"
        self.games_played = data.get("classic_duel_rounds_played", 0)
        self.winstreak = data.get("player", {}).get("stats", {}).get("Duels", {}).get("current_classic_winstreak", 0)
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("classic_duel_kills", 0),
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("classic_duel_deaths", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("classic_duel_wins", 0),
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("classic_duel_losses", 0)
        )

    def __str__(self):
        return self.name


class UHC:
    def __init__(self, data):
        self.solo = SoloUHC(data)
        self.doubles = DoublesUHC(data)
        self.fours = FoursUHC(data)


class SoloUHC:
    def __init__(self, data):
        self.name = "UHC"
        self.games_played = data.get("uhc_duel_rounds_played", 0)
        self.winstreak = data.get("player", {}).get("stats", {}).get("Duels", {}).get("current_uhc_winstreak", 0)
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("uhc_duel_kills", 0),
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("uhc_duel_deaths", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("uhc_duel_wins", 0),
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("uhc_duel_losses", 0)
        )

    def __str__(self):
        return self.name


class DoublesUHC:
    def __init__(self, data):
        self.name = "UHC Doubles"
        self.games_played = data.get("uhc_doubles_rounds_played", 0)
        self.winstreak = data.get("player", {}).get("stats", {}).get("Duels", {}).get("current_uhc_doubles_winstreak", 0)
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("uhc_doubles_kills", 0),
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("uhc_doubles_deaths", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("uhc_doubles_wins", 0),
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("uhc_doubles_losses", 0)
        )

    def __str__(self):
        return self.name


class FoursUHC:
    def __init__(self, data):
        self.name = "UHC Fours"
        self.games_played = data.get("uhc_fours_rounds_played", 0)
        self.winstreak = data.get("player", {}).get("stats", {}).get("Duels", {}).get("current_uhc_fours_winstreak", 0)
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("uhc_fours_kills", 0),
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("uhc_fours_deaths", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("uhc_fours_wins", 0),
            data.get("player", {}).get("stats", {}).get("Duels", {}).get("uhc_fours_losses", 0)
        )

    def __str__(self):
        return self.name
