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

from .stats import KillsDeaths


class Quake:
    def __init__(self, data):
        self.name = "Quake"
        self.coins = data.get("player", {}).get("stats", {}).get("Quake", {}).get("coins", 0)
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Quake", {}).get("kills", 0),
            data.get("player", {}).get("stats", {}).get("Quake", {}).get("deaths", 0)
        )
        self.wins = data.get("player", {}).get("stats", {}).get("Quake", {}).get("wins", 0)
        self.headshots = data.get("player", {}).get("stats", {}).get("Quake", {}).get("headshots", 0)
        self.killstreaks = Killstreaks(data)
        self.shots_fired = data.get("player", {}).get("stats", {}).get("Quake", {}).get("shots_fired", 0)

    def __str__(self):
        return self.name


class Killstreaks:
    def __init__(self, data):
        self.name = "Killstreaks"
        self.killstreaks = self.amount = self.total = data.get("player", {}).get("stats", {}).get("Quake", {}).get("killstreaks", 0)
        self.highest = data.get("player", {}).get("stats", {}).get("Quake", {}).get("highest_killstreak", 0)