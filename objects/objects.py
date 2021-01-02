from .bedwars import Bedwars


class MojangPlayer:
    def __init__(self, data):
        self.name = data["name"]
        self.uuid = data["id"]


class HypixelPlayer:
    def __init__(self, data):
        self.name = data.get("player", {}).get("displayname")
        self.uuid = data.get("player", {}).get("uuid")
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
