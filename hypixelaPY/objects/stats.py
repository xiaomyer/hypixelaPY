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
