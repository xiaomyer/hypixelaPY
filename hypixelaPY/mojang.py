from .exceptions import NoPlayerFoundError
from .objects.objects import MojangPlayer, NameHistory
import aiohttp

MOJANG_API = "https://api.mojang.com"
MOJANG_SESSION_SERVER = "https://sessionserver.mojang.com"


async def get_player_by_name(name: str) -> MojangPlayer:
    async with aiohttp.ClientSession() as session:
        response = await session.get(f"{MOJANG_API}/users/profiles/minecraft/{name}")
        if response.status != 200:
            raise NoPlayerFoundError(name)
    return MojangPlayer(await response.json())


async def get_player_by_uuid(uuid: str) -> MojangPlayer:
    async with aiohttp.ClientSession() as session:
        response = await session.get(f"{MOJANG_SESSION_SERVER}/session/minecraft/profile/{uuid.replace('-', '')}")
        if response.status != 200:
            raise NoPlayerFoundError(uuid)
    return MojangPlayer(await response.json())


async def get_player_name_history(uuid: str) -> NameHistory:
    async with aiohttp.ClientSession() as session:
        response = await session.get(f"{MOJANG_API}/user/profiles/{uuid}/names")
        if response.status != 200:
            raise NoPlayerFoundError(uuid)
    return NameHistory(await response.json())
