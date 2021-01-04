from .. import utils


class Ratio:
    def __init__(self, positive_stat, negative_stat):
        self.positive_stat = positive_stat
        self.negative_stat = negative_stat
        self.ratio = utils.get_ratio(positive_stat, negative_stat)
        self.next = utils.get_ratio_next(self.ratio)

    def increase(self, *, amount: int = 0):
        return utils.get_increase(self.positive_stat, self.negative_stat, amount=amount)


class KillsDeaths:
    def __init__(self, kills, deaths):
        self.kills = kills
        self.deaths = deaths
        self.ratio = Ratio(self.kills, self.deaths)


class WinsLosses:
    def __init__(self, wins, losses):
        self.wins = wins
        self.losses = losses
        self.ratio = Ratio(self.wins, self.losses)


class FinalKillsDeaths:
    def __init__(self, kills, deaths):
        self.kills = kills
        self.deaths = deaths
        self.ratio = Ratio(self.kills, self.deaths)
