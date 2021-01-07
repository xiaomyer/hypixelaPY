"""
MIT License

Copyright (c) 2020 myerfire

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

from .stats import WinsLosses, KillsDeaths


class Blitz:
    def __init__(self, data):
        self.name = "Blitz"
        self.coins = data.get("player", {}).get("stats", {}).get("HungerGames", {}).get("coins", 0)
        self.games_played = data.get("player", {}).get("stats", {}).get("HungerGames", {}).get("games_played", 0)
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("HungerGames", {}).get("kills", 0),
            data.get("player", {}).get("stats", {}).get("HungerGames", {}).get("deaths", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("HungerGames", {}).get("wins", 0),
            data.get("player", {}).get("stats", {}).get("HungerGames", {}).get("deaths", 0)
        )

    def __str__(self):
        return self.name
