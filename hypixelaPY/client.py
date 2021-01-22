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

from .exceptions import NoInputError, NoPlayerFoundError, NoGuildFoundError
from . import hypixel, mojang


class Hypixel:
    """
    Main client object of the library. This saves the API key provided and creates separate objects for the other
    Hypixel API methods
    """

    def __init__(self, api: str):
        self.api = api
        self.key = hypixel.get_api_stats(self.api)
        # this could error with InvalidAPIKeyError
        # this acts as a check to see if the API key provided was valid and also will contain the stats of the key
        self.player = Player(self.api)
        self.guild = Guild(self.api)
        self.leaderboards = Leaderboards(self.api)


class Player:
    """
    Wrapper on the /player method of the Hypixel API
    """

    def __init__(self, api: str):
        self.api = api

    async def get(self, *, uuid: str = "", name: str = "", input_: str = ""):
        """
        Takes various inputs and tries to get a user
        This prioritizes UUID, then name, then an input wildcard that could be either name or UUID

        :param uuid: A Minecraft account UUID
        :param name: A Minecraft account's name that will be converted to a
        UUID with the Mojang API
        :param input_: A wildcard that could be either a UUID or a name. The library will
        try to interpret this as a uuid first, and will fallback to interpreting as a name
        """
        if bool(uuid):
            return await self.get_by_uuid(uuid)
        elif bool(name):
            return await self.get_by_name(name)
        elif bool(input_):
            try:
                return await self.get_by_uuid(input_)
            except NoPlayerFoundError:
                return await self.get_by_name(input_)  # has the possibly of erroring with NoPlayerFoundError
        else:
            raise NoInputError

    async def get_by_uuid(self, uuid: str):
        """
        Directly queries Hypixel with a provided UUID

        :param uuid: A Minecraft account UUID
        """
        return await hypixel.get_player_by_uuid(uuid, self.api)

    async def get_by_name(self, name: str):
        """
        Queries Mojang for the UUID of the player name provided, then queries Hypixel with the newly obtained UUID

        :param name: A Minecraft account's name
        """
        uuid = (await mojang.get_player_by_name(name)).uuid
        return await hypixel.get_player_by_uuid(uuid, self.api)


class Leaderboards:
    def __init__(self, api):
        self.api = api

    async def get(self):
        return await hypixel.get_leaderboards(self.api)


class Guild:
    def __init__(self, api):
        self.api = api

    async def get(self, *, name: str = "", uuid: str = "", input_: str = ""):
        if bool(name):
            return await self.get_by_name(name)
        elif bool(uuid):
            return await self.get_by_uuid(uuid)
        elif bool(input_):
            try:
                return await self.get_by_name(input_)
            except NoGuildFoundError:
                return await self.get_by_uuid(input_)  # has the possibility of erroring with NoGuildFoundError
        else:
            raise NoInputError

    async def get_by_uuid(self, uuid: str):
        """
        Gets a guild from a player UUID

        :param uuid: A player's uuid
        :param name: A guild name
        :return: Guild
        """
        return await hypixel.get_guild_by_player_uuid(uuid, self.api)

    async def get_by_name(self, name: str):
        """
        Gets a guild from a guild name

        :param uuid: A player's uuid
        :param name: A guild name
        :return: Guild
        """
        return await hypixel.get_guild_by_name(name, self.api)


class Mojang:
    async def get(self, *, uuid: str = "", name: str = "", input_: str = ""):
        """
        Takes various inputs and tries to get a user
        This prioritizes UUID, then name, then an input wildcard that could be either name or UUID

        :param uuid: A Minecraft account UUID
        :param name: A Minecraft account's name that will be converted to a
        UUID with the Mojang API
        :param input_: A wildcard that could be either a UUID or a name. The library will
        try to interpret this as a uuid first, and will fallback to interpreting as a name
        """
        if bool(uuid):
            return await self.get_by_uuid(uuid)
        elif bool(name):
            return await self.get_by_name(name)
        elif bool(input_):
            try:
                return await self.get_by_uuid(input_)
            except NoPlayerFoundError:
                return await self.get_by_name(input_)  # has the possibility of erroring with NoPlayerFoundError
        else:
            raise NoInputError

    @staticmethod
    async def get_by_name(name: str):
        """
        Gets the UUID of a player from a name

        :param name: A Minecraft account's name
        :return: MojangPlayer
        """
        return await mojang.get_player_by_name(name)

    @staticmethod
    async def get_by_uuid(uuid: str):
        """
        Gets the UUID of a player from a name

        :param uuid: A Minecraft account's UUID
        :return: MojangPlayer
        """
        return await mojang.get_player_by_uuid(uuid)

    @staticmethod
    async def get_name_history(uuid: str):
        """
        Gets the name history of a Minecraft account from a UUID

        :param uuid: A Minecraft account's UUID
        :return: NameHistory
        """
        return await mojang.get_player_name_history(uuid)
