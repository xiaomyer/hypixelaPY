from exceptions import NoPlayerFoundError
from objects.objects import MojangPlayer
import aiohttp

MOJANG_API = "https://api.mojang.com"
MOJANG_SESSION_SERVER = "https://sessionserver.mojang.com"


async def get_player_by_name(name: str) -> MojangPlayer:
    async with aiohttp.ClientSession() as session:
        response = await session.get(f"{MOJANG_API}/users/profiles/minecraft/{name}")
        if response.status == 400:
            raise NoPlayerFoundError
    return MojangPlayer(await response.json())
