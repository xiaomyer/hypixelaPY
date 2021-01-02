from .bedwars import Bedwars
import datetime
from .. import utils


class MojangPlayer:
    def __init__(self, data):
        self.name = data["name"]
        self.uuid = data["id"]

    def __str__(self):
        return self.name

    def __int__(self):
        return self.uuid


class NameHistory:
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
    def __init__(self, data):
        self.name = data["name"]
        self.time = datetime.date.fromtimestamp(data["changedToAt"] / 1000)


class HypixelPlayer:
    def __init__(self, data):
        self.name = data.get("player", {}).get("displayname")
        self.uuid = data.get("player", {}).get("uuid")
        self.rank = Rank(data)
        self.karma = data.get("player", {}).get("karma", 0)
        self.achievement_points = data.get("player", {}).get("achievementPoints", 0)
        self.logins = LoginTimes(data)
        self.social_media = SocialMedia(data)
        self.bedwars = Bedwars(data)


class LoginTimes:
    def __init__(self, data):
        self.first = data.get("player", {}).get("firstLogin", 0)
        self.last = data.get("player", {}).get("lastLogin", 0)


class SocialMedia:
    def __init__(self, data):
        self.twitter = data.get("player", {}).get("socialMedia", {}).get("links", {}).get("TWITTER")
        self.youtube = data.get("player", {}).get("socialMedia", {}).get("links", {}).get("YOUTUBE")
        self.instagram = data.get("player", {}).get("socialMedia", {}).get("links", {}).get("INSTAGRAM")
        self.twitch = data.get("player", {}).get("socialMedia", {}).get("links", {}).get("TWITCH")
        self.discord = data.get("player", {}).get("socialMedia", {}).get("links", {}).get("DISCORD")
        self.hypixel_forums = data.get("player", {}).get("socialMedia", {}).get("links", {}).get("HYPIXEL")


class Rank:
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