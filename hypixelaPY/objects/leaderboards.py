from .. import hypixel
import asyncio


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
        self.name = f"UHC {self.prefix} {self.title}"

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
