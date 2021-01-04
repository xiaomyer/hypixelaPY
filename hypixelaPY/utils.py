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
    "MODERATOR": "MOD",
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
    "MOD": int("00AA00", 16),
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
    int("1ABC9C", 16),
    int("607D8B", 16),
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
        return ratio
    if not bool(amount):
        amount = (math.trunc(ratio) + 1) - ratio
    needed = (ratio + amount) * negative_stat - positive_stat
    return round(needed)


def get_network_level(experience):
    # formula that i don't understand
    # thank you @littlemxantivirus
    return math.trunc(get_network_level_exact(experience))


def get_network_level_exact(experience):
    # formula that i don't understand
    # thank you @littlemxantivirus
    return (math.sqrt(experience + 15312.5) - 88.38834764831843) / 35.35533905932738


def get_level_percentage(level: float):
    # i wrote this months ago so idk but it's probably just math tho
    return round((level - math.trunc(level)) * 100, 2)


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
