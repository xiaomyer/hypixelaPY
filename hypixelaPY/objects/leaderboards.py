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

from .. import hypixel


class Leaderboards:
    def __init__(self, api, data):
        self.api = api  # leaderboards class needs to also use data it gets to make more queries
        self.uhc = UHC(self.api, data["leaderboards"]["UHC"])
        self.bedwars = Bedwars(self.api, data["leaderboards"]["BEDWARS"])


class Leaderboard:
    def __init__(self, api, data):
        self.api = api
        self.path = data["path"]
        self.prefix = data["prefix"]
        self.title = data["title"]
        self.location = data["location"]
        self.count = data["count"]
        self.players = data["leaders"]
        self.name = f"{self.prefix} {self.title}"

    def __str__(self):
        return self.name

    async def get_players(self):
        """
        Gets all the players on this leaderboard. This is a separate action because it is expensive
        :return: List of HypixelPlayer based on self.players
        """
        players = [await hypixel.get_player_by_uuid(player, self.api) for player in self.players]
        return players


class UHC:
    def __init__(self, api, data):
        self.api = api
        self.overall_kills = Leaderboard(self.api, data[0])


class Bedwars:
    def __init__(self, api, data):
        self.api = api
        self.stars = Leaderboard(self.api, data[0])
        self.wins = BedwarsWins(self.api, data)
        self.finals = BedwarsFinalKills(self.api, data)


class BedwarsWins:
    def __init__(self, api, data):
        self.api = api
        self.overall = Leaderboard(self.api, data[1])
        self.weekly = Leaderboard(self.api, data[2])


class BedwarsFinalKills:
    def __init__(self, api, data):
        self.api = api
        self.overall = Leaderboard(self.api, data[3])
        self.weekly = Leaderboard(self.api, data[4])
