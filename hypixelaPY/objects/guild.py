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

import datetime

from .. import hypixel, utils


class Guild:
    def __init__(self, api, data):
        self.api = api
        self.name = data.get("guild", {}).get("name")
        self.id = data.get("guild", {}).get("_id")
        self.tag = Tag(data)
        self.display = utils.get_guild_display(self.name, self.tag.tag)
        self.members = GuildMembers(self.api, data.get("guild", {}).get("members"))
        self.created = datetime.datetime.fromtimestamp(data.get("guild", {}).get("created", 0) / 1000)
        self.level = self.experience = self.xp = self.exp = Level(data.get("guild", {}).get("exp", 0))

    def __str__(self):
        return self.name


class Tag:
    def __init__(self, data):
        self.tag = data.get("guild", {}).get("tag")
        self.color = utils.get_guild_tag_color(data.get("guild", {}).get("tagColor"))


class Level:
    def __init__(self, experience):
        self.exact = utils.get_guild_level_exact(experience)
        self.level = utils.get_guild_level(experience)
        self.next = self.level + 1
        self.percentage = utils.get_level_percentage(self.exact)

    def __int__(self):
        return self.level


class GuildMembers:
    def __init__(self, api, data):
        self.api = api
        self.data = data
        self.count = len(data)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.data) - 1:
            raise StopIteration
        self.index += 1
        return GuildMember(self.api, self.data[self.index])


class GuildMember:
    def __init__(self, api, data):
        self.api = api
        self.uuid = data.get("uuid")
        self.rank = data.get("rank")
        self.joined = datetime.datetime.fromtimestamp(data.get("joined") / 1000)
        self.experience = self.xp = self.exp = self.exp_history = data.get("expHistory")

    async def get(self):  # get HypixelPlayer object of guild member
        return await hypixel.get_player_by_uuid(self.uuid, self.api)
