# 2225. Find Players With Zero or One Losses

class Solution:
    def findWinners(self, matches: list) -> list:
        losses = dict()

        for match in matches:
            winner, loser = match

            losses[winner] = losses.get(winner, 0) + 0

            losses[loser] = losses.get(loser, 0) + 1

        no_losers, losers_of_1 = [], list()

        for players in list(losses.items()):
            if (losses[players[0]] == 0): # if a player hasn't LOST any matches
                no_losers += [players[0]]
            elif (losses[players[0]] == 1): # if a player has lost ONE match
                losers_of_1.append(players[0])

        return [sorted(no_losers), sorted(losers_of_1)]
