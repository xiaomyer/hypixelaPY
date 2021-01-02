import hypixel
import mojang


class Hypixel:
    def __init__(self, api: str):
        self.api = api

    async def get_player_by_uuid(self, uuid: str):
        return await hypixel.get_player_by_uuid(uuid, self.api)

    async def get_player_by_name(self, name: str):
        uuid = (await mojang.get_player_by_name(name)).uuid
        return await hypixel.get_player_by_uuid(uuid, self.api)


class Mojang:
    async def get_player_by_name(self, name: str):
        return await mojang.get_player_by_name(name)