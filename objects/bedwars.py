import utils


class Bedwars:
    def __init__(self, data):
        self.prestige = Prestige(data.get("player", {}).get("achievements", {}).get("bedwars_level", 0))
        self.coins = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("coins_bedwars", 0)
        self.games_played = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("games_played_bedwars", 0)
        self.beds = BedsBrokenLost(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("beds_broken_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("beds_lost_bedwars", 0)
        )
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("deaths_bedwars", 0)
        )
        self.finals = FinalKillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("final_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("final_deaths_bedwars", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("wins_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("losses_bedwars", 0)
        )
        self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("winstreak", 0)
        self.solo = Solo(data)
        self.doubles = Doubles(data)
        self.threes = Threes(data)
        self.fours = Fours(data)
        self.four_v_four = FourVFour(data)
        self.dreams = Dreams(data)


class Prestige:
    def __init__(self, star):
        self.star = star
        self.star_index = star // 100
        self.name = utils.get_bedwars_prestige_name(self.star_index)
        self.color = utils.get_bedwars_prestige_color(self.star_index)


# every mode is going to have one of these
class BedsBrokenLost:
    def __init__(self, broken, lost):
        self.broken = broken
        self.lost = lost
        self.ratio = utils.get_ratio(broken, lost)

    def increase(self, *, amount: int = 0):
        return utils.get_increase(self.broken, self.lost, amount=amount)


class KillsDeaths:
    def __init__(self, kills, deaths):
        self.kills = kills
        self.deaths = deaths
        self.ratio = utils.get_ratio(kills, deaths)

    def increase(self, *, amount: int = 0):
        return utils.get_increase(self.kills, self.deaths, amount=amount)


class FinalKillsDeaths:
    def __init__(self, kills, deaths):
        self.kills = kills
        self.deaths = deaths
        self.ratio = utils.get_ratio(kills, deaths)

    def increase(self, *, amount: int = 0):
        return utils.get_increase(self.kills, self.deaths, amount=amount)


class WinsLosses:
    def __init__(self, wins, losses):
        self.wins = wins
        self.losses = losses
        self.ratio = utils.get_ratio(wins, losses)

    def increase(self, *, amount: int = 0):
        return utils.get_increase(self.wins, self.losses, amount=amount)


# regular modes
class Solo:
    def __init__(self, data):
        self.games_played = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get(
            "eight_one_games_played_bedwars", 0)
        self.beds = BedsBrokenLost(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_beds_broken_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_beds_lost_bedwars", 0)
        )
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_deaths_bedwars", 0)
        )
        self.finals = FinalKillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_final_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_final_deaths_bedwars", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_wins_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_losses_bedwars", 0)
        )
        self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_winstreak", 0)


class Doubles:
    def __init__(self, data):
        self.games_played = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get(
            "eight_two_games_played_bedwars", 0)
        self.beds = BedsBrokenLost(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_beds_broken_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_beds_lost_bedwars", 0)
        )
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_deaths_bedwars", 0)
        )
        self.finals = FinalKillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_final_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_final_deaths_bedwars", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_wins_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_losses_bedwars", 0)
        )
        self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_winstreak", 0)


class Threes:
    def __init__(self, data):
        self.games_played = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get(
            "four_three_games_played_bedwars", 0)
        self.beds = BedsBrokenLost(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_beds_broken_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_beds_lost_bedwars", 0)
        )
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_deaths_bedwars", 0)
        )
        self.finals = FinalKillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_final_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_final_deaths_bedwars", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_wins_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_losses_bedwars", 0)
        )
        self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_winstreak", 0)


class Fours:
    def __init__(self, data):
        self.games_played = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get(
            "four_four_games_played_bedwars", 0)
        self.beds = BedsBrokenLost(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_beds_broken_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_beds_lost_bedwars", 0)
        )
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_deaths_bedwars", 0)
        )
        self.finals = FinalKillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_final_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_final_deaths_bedwars", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_wins_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_losses_bedwars", 0)
        )
        self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_winstreak", 0)


class FourVFour:
    def __init__(self, data):
        self.games_played = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get(
            "two_four_games_played_bedwars", 0)
        self.beds = BedsBrokenLost(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("two_four_beds_broken_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("two_four_beds_lost_bedwars", 0)
        )
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("two_four_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("two_four_deaths_bedwars", 0)
        )
        self.finals = FinalKillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("two_four_final_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("two_four_final_deaths_bedwars", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("two_four_wins_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("two_four_losses_bedwars", 0)
        )
        self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("two_four_winstreak", 0)


# dreams modes
class Dreams:
    def __init__(self, data):
        self.armed = Armed(data)
        self.castle = Castle(data)
        self.lucky = LuckyBlocks(data)


class Armed:
    def __init__(self, data):
        self.doubles = ArmedDoubles(data)
        self.fours = ArmedFours(data)


class ArmedDoubles:
    def __init__(self, data):
        self.games_played = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get(
            "eight_two_armed_games_played_bedwars", 0)
        self.beds = BedsBrokenLost(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_armed_beds_broken_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_armed_beds_lost_bedwars", 0)
        )
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_armed_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_armed_deaths_bedwars", 0)
        )
        self.finals = FinalKillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_armed_final_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_armed_final_deaths_bedwars", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_armed_wins_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_armed_losses_bedwars", 0)
        )
        self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_armed_winstreak", 0)


class ArmedFours:
    def __init__(self, data):
        self.games_played = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get(
            "four_four_armed_games_played_bedwars", 0)
        self.beds = BedsBrokenLost(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_armed_beds_broken_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_armed_beds_lost_bedwars", 0)
        )
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_armed_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_armed_deaths_bedwars", 0)
        )
        self.finals = FinalKillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_armed_final_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_armed_final_deaths_bedwars", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_armed_wins_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_armed_losses_bedwars", 0)
        )
        self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_armed_winstreak", 0)


class Castle:
    def __init__(self, data):
        self.games_played = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get(
            "castle_games_played_bedwars", 0)
        self.beds = BedsBrokenLost(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("castle_beds_broken_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("castle_beds_lost_bedwars", 0)
        )
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("castle_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("castle_deaths_bedwars", 0)
        )
        self.finals = FinalKillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("castle_final_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("castle_final_deaths_bedwars", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("castle_wins_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("castle_losses_bedwars", 0)
        )
        self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("castle_winstreak", 0)


class LuckyBlocks:
    def __init__(self, data):
        self.doubles = LuckyBlocksDoubles(data)
        self.fours = LuckyBlocksFours(data)


class LuckyBlocksDoubles:
    def __init__(self, data):
        self.games_played = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get(
            "eight_two_lucky_games_played_bedwars", 0)
        self.beds = BedsBrokenLost(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_lucky_beds_broken_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_lucky_beds_lost_bedwars", 0)
        )
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_lucky_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_lucky_deaths_bedwars", 0)
        )
        self.finals = FinalKillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_lucky_final_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_lucky_final_deaths_bedwars", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_lucky_wins_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_lucky_losses_bedwars", 0)
        )
        self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_lucky_winstreak", 0)


class LuckyBlocksFours:
    def __init__(self, data):
        self.games_played = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get(
            "four_four_lucky_games_played_bedwars", 0)
        self.beds = BedsBrokenLost(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_lucky_beds_broken_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_lucky_beds_lost_bedwars", 0)
        )
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_lucky_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_lucky_deaths_bedwars", 0)
        )
        self.finals = FinalKillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_lucky_final_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_lucky_final_deaths_bedwars", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_lucky_wins_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_lucky_losses_bedwars", 0)
        )
        self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_lucky_winstreak", 0)


class Rush:
    def __init__(self, data):
        self.solo = RushSolo(data)
        self.doubles = RushDoubles(data)
        self.fours = RushFours(data)


class RushSolo:
    def __init__(self, data):
        self.games_played = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get(
            "eight_one_rush_games_played_bedwars", 0)
        self.beds = BedsBrokenLost(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_rush_beds_broken_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_rush_beds_lost_bedwars", 0)
        )
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_rush_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_rush_deaths_bedwars", 0)
        )
        self.finals = FinalKillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_rush_final_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_rush_final_deaths_bedwars", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_rush_wins_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_rush_losses_bedwars", 0)
        )
        self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_rush_winstreak", 0)


class RushDoubles:
    def __init__(self, data):
        self.games_played = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get(
            "eight_two_rush_games_played_bedwars", 0)
        self.beds = BedsBrokenLost(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_rush_beds_broken_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_rush_beds_lost_bedwars", 0)
        )
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_rush_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_rush_deaths_bedwars", 0)
        )
        self.finals = FinalKillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_rush_final_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_rush_final_deaths_bedwars", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_rush_wins_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_rush_losses_bedwars", 0)
        )
        self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_rush_winstreak", 0)


class RushFours:
    def __init__(self, data):
        self.games_played = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get(
            "four_four_rush_games_played_bedwars", 0)
        self.beds = BedsBrokenLost(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_rush_beds_broken_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_rush_beds_lost_bedwars", 0)
        )
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_rush_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_rush_deaths_bedwars", 0)
        )
        self.finals = FinalKillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_rush_final_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_rush_final_deaths_bedwars", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_rush_wins_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_rush_losses_bedwars", 0)
        )
        self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_rush_winstreak", 0)
        
        
class Ultimate:
    def __init__(self, data):
        self.solo = UltimateSolo(data)
        self.doubles = UltimateDoubles(data)
        self.fours = UltimateFours(data)


class UltimateSolo:
    def __init__(self, data):
        self.games_played = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get(
            "eight_one_ultimate_games_played_bedwars", 0)
        self.beds = BedsBrokenLost(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_ultimate_beds_broken_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_ultimate_beds_lost_bedwars", 0)
        )
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_ultimate_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_ultimate_deaths_bedwars", 0)
        )
        self.finals = FinalKillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_ultimate_final_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_ultimate_final_deaths_bedwars", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_ultimate_wins_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_ultimate_losses_bedwars", 0)
        )
        self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_ultimate_winstreak", 0)


class UltimateDoubles:
    def __init__(self, data):
        self.games_played = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get(
            "eight_two_ultimate_games_played_bedwars", 0)
        self.beds = BedsBrokenLost(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_ultimate_beds_broken_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_ultimate_beds_lost_bedwars", 0)
        )
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_ultimate_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_ultimate_deaths_bedwars", 0)
        )
        self.finals = FinalKillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_ultimate_final_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_ultimate_final_deaths_bedwars", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_ultimate_wins_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_ultimate_losses_bedwars", 0)
        )
        self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_ultimate_winstreak", 0)


class UltimateFours:
    def __init__(self, data):
        self.games_played = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get(
            "four_four_ultimate_games_played_bedwars", 0)
        self.beds = BedsBrokenLost(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_ultimate_beds_broken_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_ultimate_beds_lost_bedwars", 0)
        )
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_ultimate_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_ultimate_deaths_bedwars", 0)
        )
        self.finals = FinalKillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_ultimate_final_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_ultimate_final_deaths_bedwars", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_ultimate_wins_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_ultimate_losses_bedwars", 0)
        )
        self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_ultimate_winstreak", 0)
        
        
class Voidless:
    def __init__(self, data):
        self.doubles = VoidlessDoubles(data)
        self.fours = VoidlessFours(data)


class VoidlessDoubles:
    def __init__(self, data):
        self.games_played = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get(
            "eight_two_voidless_games_played_bedwars", 0)
        self.beds = BedsBrokenLost(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_voidless_beds_broken_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_voidless_beds_lost_bedwars", 0)
        )
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_voidless_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_voidless_deaths_bedwars", 0)
        )
        self.finals = FinalKillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_voidless_final_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_voidless_final_deaths_bedwars", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_voidless_wins_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_voidless_losses_bedwars", 0)
        )
        self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_voidless_winstreak", 0)


class VoidlessFours:
    def __init__(self, data):
        self.games_played = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get(
            "four_four_voidless_games_played_bedwars", 0)
        self.beds = BedsBrokenLost(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_voidless_beds_broken_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_voidless_beds_lost_bedwars", 0)
        )
        self.kills = KillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_voidless_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_voidless_deaths_bedwars", 0)
        )
        self.finals = FinalKillsDeaths(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_voidless_final_kills_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_voidless_final_deaths_bedwars", 0)
        )
        self.wins = WinsLosses(
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_voidless_wins_bedwars", 0),
            data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_voidless_losses_bedwars", 0)
        )
        self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_voidless_winstreak", 0)