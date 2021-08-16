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

import math
import re

ranks = {
    "NONE": None,
    "VIP": "VIP",
    "VIP_PLUS": "VIP+",
    "MVP": "MVP",
    "MVP_PLUS": "MVP+",
    "SUPERSTAR": "MVP++",
    "YOUTUBER": "YOUTUBE",
    "PIG+++": "PIG+++",
    "BUILD TEAM": "BUILD TEAM",
    "HELPER": "HELPER",
    # "MODERATOR": "MOD",
    "GAME_MASTER": "GM",
    "ADMIN": "ADMIN",
    "SLOTH": "SLOTH",
    "OWNER": "OWNER"
}

rank_colors = {
    "VIP": int("55FF55", 16),
    "VIP+": int("55FF55", 16),
    "MVP": int("55FFFF", 16),
    "MVP+": int("55FFFF", 16),
    "MVP++": int("FFAA00", 16),
    "YOUTUBE": int("FF5555", 16),
    "PIG+++": int("FF69DC", 16),
    "BUILD TEAM": int("00AAAA", 16),
    "EVENTS": int("FFAA00", 16),
    "HELPER": int("5555FF", 16),
    # "MOD": int("00AA00", 16),
    "GM": int("00AA00", 16),
    "ADMIN": int("AA0000", 16),
    "SLOTH": int("AA0000", 16),
    "OWNER": int("AA0000", 16),
    None: int("607D8B", 16)
}

bedwars_prestiges = (
    "Stone",
    "Iron",
    "Gold",
    "Diamond",
    "Emerald",
    "Sapphire",
    "Ruby",
    "Crystal",
    "Opal",
    "Amethyst",
    "Rainbow",
    "Iron Prime",
    "Gold Prime",
    "Diamond Prime",
    "Emerald Prime",
    "Sapphire Prime",
    "Ruby Prime",
    "Crystal Prime",
    "Opal Prime",
    "Amethyst Prime",
    "Mirror",
    "Light",
    "Dawn",
    "Dusk",
    "Air",
    "Wind",
    "Nebula",
    "Thunder",
    "Earth",
    "Water",
    "Fire"
)

FIRST_FIVE_BEDWARS_LEVELS_TO_NEXT = {
    0: 500,
    1: 1000,
    2: 2000,
    3: 3500,
}

skywars_prestiges = (
    "Stone",
    "Iron",
    "Gold",
    "Diamond",
    "Emerald",
    "Sapphire",
    "Ruby",
    "Crystal",
    "Opal",
    "Amethyst",
    "Rainbow",
    "Mystic"
)

bedwars_prestige_colors = (
    int("607D8B", 16),  # stone
    int("95A5A6", 16),  # iron
    int("FFAC0F", 16),  # gold
    int("55FFFF", 16),  # diamond
    int("00AA00", 16),  # emerald
    int("00AAAA", 16),  # sapphire
    int("AA0000", 16),  # ruby
    int("FF69DC", 16),  # crystal
    int("2562E9", 16),  # opal
    int("AA00AA", 16),  # amethyst
    int("1ABC9C", 16),  # rainbow
    int("95A5A6", 16),
    int("FFAC0F", 16),
    int("55FFFF", 16),
    int("00AA00", 16),
    int("00AAAA", 16),
    int("AA0000", 16),
    int("FF69DC", 16),
    int("2562E9", 16),
    int("AA00AA", 16)  # i don't know the colors past this point yet
)

skywars_prestige_colors = (
    int("607D8B", 16),
    int("95A5A6", 16),
    int("FFAC0F", 16),
    int("55FFFF", 16),
    int("00AA00", 16),
    int("00AAAA", 16),
    int("AA0000", 16),
    int("FF69DC", 16),
    int("2562E9", 16),
    int("AA00AA", 16),
    int("AA00AA", 16),  # last two prestiges use the same color
)

guild_tag_colors = {
    "GRAY": int("607D8B", 16),
    "GOLD": int("FFAC0F", 16),
    "DARK_AQUA": int("00AAAA", 16),
    "DARK_GREEN": int("00AA00", 16),
    "YELLOW": int("FFFF55", 16)
}


def get_ratio(positive_stat, negative_stat):
    try:
        ratio = positive_stat / negative_stat
        return round(ratio, 2)
    except ZeroDivisionError:
        return float("inf") if positive_stat > 0 else 0


def get_ratio_next(ratio):
    if ratio == float("inf"):
        return ratio
    else:
        return math.trunc(ratio) + 1


def get_increase(positive_stat, negative_stat, *, amount: int = 0):
    ratio = get_ratio(positive_stat, negative_stat)
    if ratio == float("inf"):
        return 0
    if not bool(amount):
        amount = (math.trunc(ratio) + 1) - ratio
    needed = (ratio + amount) * negative_stat - positive_stat
    return round(needed)


def get_level_percentage(level: float):
    # i wrote this months ago so idk but it's probably just math tho
    return round((level - math.trunc(level)) * 100, 2)


def get_network_level(experience):
    # formula that i don't understand
    # thank you @littlemxantivirus
    return math.trunc(get_network_level_exact(experience))


def get_network_level_exact(experience):
    # formula that i don't understand
    # thank you @littlemxantivirus
    return (math.sqrt(experience + 15312.5) - 88.38834764831843) / 35.35533905932738


def get_bedwars_prestige_name(star_index):
    if star_index > len(bedwars_prestiges) - 1:
        star_index = len(bedwars_prestiges) - 1
    return bedwars_prestiges[star_index]


def get_bedwars_prestige_color(star_index):
    if star_index > len(bedwars_prestige_colors) - 1:
        star_index = len(bedwars_prestige_colors) - 1
    return bedwars_prestige_colors[star_index]


def get_skywars_level(experience):
    return math.trunc(get_skywars_level_exact(experience))


def get_skywars_level_exact(experience):
    # another formula that I don't understand, thanks to @GamingGeeek and @littlemissantivirus
    total_xp = [20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
    level = 0
    if experience >= 15000:
        level = (experience - 15000) / 10000 + 12
    else:
        c = 0
        while experience >= 0 and c < len(total_xp):
            if experience - total_xp[c] >= 0:
                c += 1
            else:
                level = c + 1 + (experience - total_xp[c - 1]) / (total_xp[c] - total_xp[c - 1])
                break
    return level


def get_skywars_prestige_name(star_index):
    if star_index > len(skywars_prestiges) - 1:
        star_index = len(skywars_prestiges) - 1
    return skywars_prestiges[star_index]


def get_skywars_prestige_color(star_index):
    if star_index > len(skywars_prestige_colors) - 1:
        star_index = len(skywars_prestige_colors) - 1
    return skywars_prestige_colors[star_index]


def get_rank(rank, prefix_raw, monthly_package_rank, new_package_rank, package_rank):
    real_rank = None
    if prefix_raw:
        prefix = re.sub(r"§.", "", prefix_raw)[1:-1]
        # prefixes all start and end with brackets, and have minecraft color codes, this is to remove color codes and
        # brackets
        real_rank = ranks.get(prefix, prefix)
    elif rank and rank != "NORMAL" and not real_rank:
        real_rank = ranks.get(rank, rank)
    elif (monthly_package_rank and monthly_package_rank != "NONE") and not real_rank:
        # WHY DOES IT EXIST IF IT'S NONE HYPIXEL WHY
        real_rank = ranks.get(monthly_package_rank, monthly_package_rank)
    elif new_package_rank and not real_rank:
        real_rank = ranks.get(new_package_rank, new_package_rank)
    elif package_rank and not real_rank:
        real_rank = ranks.get(package_rank, package_rank)
    return real_rank


def get_rank_color(rank):
    return rank_colors[rank]


def get_profile_display(name, rank):
    # returns either "[rank] name" or "name" depending on whether the player has a rank
    if bool(rank):
        return f"[{rank}] {name}"
    else:
        return name


def get_guild_level(experience):
    return math.trunc(get_guild_level_exact(experience))


def get_guild_level_exact(experience):
    # credit for original formula to @Sk1er, translated into Kotlin by
    # @littlemxantivirus,
    # then translated into Python by @SirNapkin1334
    experience_below_14 = [
        100000,
        150000,
        250000,
        500000,
        750000,
        1000000,
        1250000,
        1500000,
        2000000,
        2500000,
        2500000,
        2500000,
        2500000,
        2500000
    ]
    c = 0.0
    for it in experience_below_14:
        if it > experience:
            level = c + round(experience / it * 100.0) / 100.0
        experience -= it
        c += 1

        increment = 3000000
    while experience > increment:
        c += 1
        experience -= increment
    level = c + (round(experience / increment * 100.0) / 100.0)
    return level


def get_guild_display(name, tag):
    if tag:
        return f"[{tag}] {name}"
    else:
        return name


def get_guild_tag_color(color):
    return guild_tag_colors.get(color, int("000000", 16))


def get_over_bedwars_prestige(level: int):
    return level - ((level // 100) * 100)


def get_bedwars_level(experience: int):
    level = 0
    while experience > 0:
        over_prestige = get_over_bedwars_prestige(level)
        if over_prestige in range(4):
            experience -= FIRST_FIVE_BEDWARS_LEVELS_TO_NEXT.get(over_prestige)
            level += 1
        elif experience > 5000:
            experience -= 5000
            level += 1
        else:
            break
    return level, experience
