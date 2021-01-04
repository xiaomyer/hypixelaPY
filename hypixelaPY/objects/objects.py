from .bedwars import Bedwars
from .skywars import Skywars
from .duels import Duels
import datetime
from .. import utils


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

    def __int__(self):
        return self.uuid


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
        self.level = Level(data)
        self.karma = data.get("player", {}).get("karma", 0)
        self.achievement_points = data.get("player", {}).get("achievementPoints", 0)
        self.logins = Logins(data)
        self.social = Social(data)
        self.bedwars = Bedwars(data)
        self.skywars = Skywars(data)
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
    def __init__(self, data):
        self.exact = utils.get_network_level_exact(data.get("player", {}).get("networkExp"))
        self.level = utils.get_network_level(data.get("player", {}).get("networkExp"))
        self.next = self.level + 1
        self.percentage = utils.get_level_percentage(self.exact)
