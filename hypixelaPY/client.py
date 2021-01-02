from .exceptions import NoInputError, NoPlayerFoundError
from . import hypixel, mojang


class Hypixel:
    def __init__(self, api: str):
        self.api = api

    async def get(self, *, input_: str = "", uuid: str = "", name: str = ""):
        # input_ is taken to be a wildcard; could be a name or uuid
        # otherwise, it uses uuid first, then name if no uuid
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
        return await hypixel.get_player_by_uuid(uuid, self.api)

    async def get_player_by_name(self, name: str):
        uuid = (await mojang.get_player_by_name(name)).uuid
        return await hypixel.get_player_by_uuid(uuid, self.api)


class Mojang:
    async def get_player_by_name(self, name: str):
        return await mojang.get_player_by_name(name)

    async def get_player_name_history(self, uuid: str):
        return await mojang.get_player_name_history(uuid)
