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