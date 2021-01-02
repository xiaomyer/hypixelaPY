from exceptions import NoPlayerFoundError
from objects.objects import HypixelPlayer
import aiohttp

HYPIXEL_API = "https://api.hypixel.net"


async def get_player_by_uuid(uuid: str, api: str) -> HypixelPlayer:
    async with aiohttp.ClientSession() as session:
        json = await (await session.get(f"{HYPIXEL_API}/player?key={api}&uuid={uuid}")).json()
        if not json["success"] or not json["player"]:  # hypixel apiTM; sometimes success is false sometimes player
            # is null
            raise NoPlayerFoundError
    return HypixelPlayer(json)
