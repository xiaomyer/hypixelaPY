from .exceptions import NoInputError, NoPlayerFoundError
from . import hypixel, mojang


class Hypixel:
    """
    Main client object of the library. This saves the API key provided and creates separate objects for the other
    Hypixel API methods
    """

    def __init__(self, api: str):
        self.api = api
        self.player = Player(self.api)
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
            return await self.get_player_by_uuid(uuid)
        elif bool(name):
            return await self.get_player_by_name(name)
        elif bool(input_):
            try:
                return await self.get_player_by_uuid(input_)
            except NoPlayerFoundError:
                return await self.get_player_by_name(input_)  # has the possibly of erroring with NoPlayerFoundError
        else:
            raise NoInputError

    async def get_player_by_uuid(self, uuid: str):
        """
        Directly queries Hypixel with a provided UUID

        :param uuid: A Minecraft account UUID
        """
        return await hypixel.get_player_by_uuid(uuid, self.api)

    async def get_player_by_name(self, name: str):
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
            return await self.get_player_by_uuid(uuid)
        elif bool(name):
            return await self.get_player_by_name(name)
        elif bool(input_):
            try:
                return await self.get_player_by_uuid(input_)
            except NoPlayerFoundError:
                return await self.get_player_by_name(input_)  # has the possibly of erroring with NoPlayerFoundError
        else:
            raise NoInputError

    async def get_player_by_name(self, name: str):
        """
        Gets the UUID of a player from a name

        :param name: A Minecraft account's name
        :return: MojangPlayer
        """
        return await mojang.get_player_by_name(name)

    async def get_player_by_uuid(self, uuid: str):
        """
        Gets the UUID of a player from a name

        :param uuid: A Minecraft account's UUID
        :return: MojangPlayer
        """
        return await mojang.get_player_by_uuid(uuid)

    async def get_player_name_history(self, uuid: str):
        """
        Gets the name history of a Minecraft account from a UUID

        :param uuid: A Minecraft account's UUID
        :return: NameHistory
        """
        return await mojang.get_player_name_history(uuid)
