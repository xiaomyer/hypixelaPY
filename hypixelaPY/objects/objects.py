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

from .bedwars import Bedwars
from .skywars import Skywars
from .blitz import Blitz
from .duels import Duels
import datetime
from .. import hypixel, utils


class APIKey:
    def __init__(self, data):
        self.key = data.get("record", {}).get("key")
        self.owner = data.get("record", {}).get("owner")
        self.limit = data.get("record", {}).get("limit")
        self.queries = APIKeyQueries(data)


class APIKeyQueries:
    def __init__(self, data):
        self.minute = data.get("record", {}).get("queriesInPastMin")
        self.all = data.get("record", {}).get("totalQueries")


class MojangPlayer:
    """
    The response from a call to the Mojang API
    Represents a player
    """
    def __init__(self, data):
        self.name = data["name"]
        self.uuid = data["id"]

    def __str__(self):
        return self.name


class NameHistory:
    """
    The response from a call to the Mojang namehistory API
    Represents a player's namehistory as an iterable
    """
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.data) - 1:
            raise StopIteration
        self.index += 1
        return NameHistoryEntry(self.data[self.index])


class NameHistoryEntry:
    """
    Represents a name in the namehistory of a player
    """
    def __init__(self, data):
        self.name = data["name"]
        self.time = datetime.datetime.fromtimestamp(data["changedToAt"] / 1000)

    def __str__(self):
        return self.name


class HypixelPlayer:
    """
    The response from a call to the Hypixel player endpoint
    Represents a player
    """
    def __init__(self, data):
        self.name = data.get("player", {}).get("displayname")
        self.uuid = data.get("player", {}).get("uuid")
        self.rank = Rank(data)
        self.display = utils.get_profile_display(self.name, self.rank)
        self.level = Level(data.get("player", {}).get("networkExp"))
        self.karma = data.get("player", {}).get("karma", 0)
        self.achievement_points = data.get("player", {}).get("achievementPoints", 0)
        self.logins = Logins(data)
        self.social = Social(data)
        self.bedwars = Bedwars(data)
        self.skywars = Skywars(data)
        self.blitz = Blitz(data)
        self.duels = Duels(data)

    def __str__(self):
        return self.name


class Logins:
    """
    The login times of a player
    """
    def __init__(self, data):
        self.first = datetime.datetime.fromtimestamp(data.get("player", {}).get("firstLogin", 0) / 1000)
        self.last = datetime.datetime.fromtimestamp(data.get("player", {}).get("lastLogin", 0) / 1000)


class Social:
    """
    The social media links of a player
    """
    def __init__(self, data):
        self.twitter = data.get("player", {}).get("socialMedia", {}).get("links", {}).get("TWITTER")
        self.youtube = data.get("player", {}).get("socialMedia", {}).get("links", {}).get("YOUTUBE")
        self.instagram = data.get("player", {}).get("socialMedia", {}).get("links", {}).get("INSTAGRAM")
        self.twitch = data.get("player", {}).get("socialMedia", {}).get("links", {}).get("TWITCH")
        self.discord = data.get("player", {}).get("socialMedia", {}).get("links", {}).get("DISCORD")
        self.hypixel_forums = data.get("player", {}).get("socialMedia", {}).get("links", {}).get("HYPIXEL")


class Rank:
    """
    The rank data of a player
    """
    def __init__(self, data):
        self.name = utils.get_rank(
            data.get("player", {}).get("rank"),
            data.get("player", {}).get("prefix"),
            data.get("player", {}).get("monthlyPackageRank"),
            data.get("player", {}).get("newPackageRank"),
            data.get("player", {}).get("packageRank"),
        )
        self.color = utils.get_rank_color(self.name)

    def __str__(self):
        return self.name

    def __bool__(self):
        return bool(self.name)


class Level:
    def __init__(self, experience):
        self.exact = utils.get_network_level_exact(experience)
        self.level = utils.get_network_level(experience)
        self.next = self.level + 1
        self.percentage = utils.get_level_percentage(self.exact)

    def __int__(self):
        return self.level
