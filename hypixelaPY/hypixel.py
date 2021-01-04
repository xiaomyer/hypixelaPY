from .exceptions import NoPlayerFoundError
from .objects.objects import HypixelPlayer
from .objects.leaderboards import Leaderboards
import aiohttp

HYPIXEL_API = "https://api.hypixel.net"


async def get_player_by_uuid(uuid: str, api: str) -> HypixelPlayer:
    async with aiohttp.ClientSession() as session:
        json = await (await session.get(f"{HYPIXEL_API}/player?key={api}&uuid={uuid}")).json()
        if not json["success"] or not json["player"]:  # hypixel apiTM; sometimes success is false sometimes player
            # is null
            raise NoPlayerFoundError(uuid)
    return HypixelPlayer(json)


async def get_leaderboards(api: str) -> Leaderboards:
    async with aiohttp.ClientSession() as session:
        json = await (await session.get(f"{HYPIXEL_API}/leaderboards?key={api}")).json()
    # theoretically this shouldn't error ever, there is no input to be invalid it should be static
    return Leaderboards(api, json)
