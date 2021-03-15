"""
MIT License

Copyright (c) 2020 Myer

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

import aiohttp

from .exceptions import InvalidAPIKeyError, NoPlayerFoundError, NoGuildFoundError
from .objects.guild import Guild
from .objects.leaderboards import Leaderboards
from .objects.objects import HypixelPlayer, APIKey

HYPIXEL_API = "https://api.hypixel.net"


async def get_api_stats(api: str) -> APIKey:
    async with aiohttp.request("GET", f"{HYPIXEL_API}/key?key={api}") as response:
        json = await response.json()
        if not json["success"]:
            raise InvalidAPIKeyError(api)
        return APIKey(json)


async def get_player_by_uuid(uuid: str, api: str) -> HypixelPlayer:
    async with aiohttp.request("GET", f"{HYPIXEL_API}/player?key={api}&uuid={uuid}") as response:
        json = await response.json()
        if not json["success"] or not json["player"]:  # hypixel apiTM; sometimes success is false sometimes player
            # is null
            raise NoPlayerFoundError(uuid)
        return HypixelPlayer(json)


async def get_leaderboards(api: str) -> Leaderboards:
    async with aiohttp.request("GET", f"{HYPIXEL_API}/leaderboards?key={api}") as response:
        json = await response.json()
    # theoretically this shouldn't error ever, there is no input to be invalid it should be static
        return Leaderboards(api, json)


async def get_guild_by_player_uuid(uuid: str, api: str) -> Guild:
    async with aiohttp.request("GET", f"{HYPIXEL_API}/guild?key={api}&player={uuid}") as response:
        json = await response.json()
        if not json["success"] or not json["guild"]:  # hypixel apiTM; sometimes success is false sometimes guild
            # is null
            raise NoGuildFoundError(uuid)
        return Guild(api, json)


async def get_guild_by_name(name: str, api: str) -> Guild:
    async with aiohttp.request("GET", f"{HYPIXEL_API}/guild?key={api}&name={name}") as response:
        json = await response.json()
        if not json["success"] or not json["guild"]:  # hypixel apiTM; sometimes success is false sometimes guild
            # is null
            raise NoGuildFoundError(name)
        return Guild(api, json)
