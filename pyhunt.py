__author__ = 'slyfocks'
import numpy as np

reputation_list = []
num_players = []
num_hunts = []
decision_counts = []


def hunt_choices(round_number, current_food, current_reputation, m,  player_reputations):
    # The main routine that plays each individual round.
    hunt_decisions = []
    player_count = len(player_reputations)
    #number of decisions made in each round by all of the players combined
    decision_count = float(player_count*(player_count - 1))
    if round_number == 1:
        hunt_decisions = ['h'*player_count]
    else:
        average_rep = sum(player_reputations)/player_count
        average_last_rep = float(sum(reputation_list[-1])/num_players[-1])
        percent_hunt = float(num_hunts[-1])/decision_counts[-1]
        if num_players[-1] > len(player_reputations):
            #number of players eliminated between rounds
            num_elim = num_players[-1] - len(player_reputations)
            #average reputation if eliminated are included
            rep_with_elim = ((round_number - 1)*average_last_rep + percent_hunt)/round_number
            #from this, calculate average reputation of the eliminated
            #this will be used to "pity" those who are deemed to be closer to elimination
            elim_rep_avg = (num_players[-1]*rep_with_elim - average_rep*player_count)/num_elim
            #make probability of hunting for those close to elimination 1 and decrease outwards
            #this takes advantage of naive players close to 1 and refuses to help the lazy
            #make the probability for average = percent_hunt so we can closely mimic the previous round's activity
            slope = abs((1-percent_hunt)/(elim_rep_avg - average_rep))
            for player_rep in player_reputations:
                if np.random.random_sample() < (1 - slope*abs(player_rep - elim_rep_avg)):
                    hunt_decisions.append('h')
                else:
                    hunt_decisions.append('s')
        #else we take an adapted tit-for-tat approach where the
        else:
            slope = -abs((1 - percent_hunt)/(average_rep - percent_hunt))
            for player_rep in player_reputations:
                if np.random.random_sample() < (1 - slope*abs(player_rep - average_rep)):
                    hunt_decisions.append('h')
                else:
                    hunt_decisions.append('s')
    reputation_list.append(player_reputations)
    num_players.append(player_count)
    decision_counts.append(decision_count)
    return hunt_decisions


def hunt_outcomes(food_earnings):
    # hunt_outcomes is called after all hunts for the round are complete.

    # Add any code you wish to modify your variables based on the outcome of the last round.

    # The variable passed in to hunt_outcomes for your use is:
    #     food_earnings: list of integers, the amount of food earned from the last round's hunts.
    #                    The entries can be negative as it is possible to lose food from a hunt.
    #                    The amount of food you have for the next round will be current_food
    #                    + sum of all entries of food_earnings + award from round_end.
    #                    The list will be in the same order as the decisions you made in that round.

    pass


def round_end(award, m, number_hunters):
    # round_end is called after all hunts for the round are complete.
    num_hunts.append(number_hunters)
    # award - the total amount of food you received due to cooperation in the round.
    # Can be zero if the threshold m was not reached.

    # Add any code you wish to modify your variables based on the cooperation that occurred in
    # the last round.

    # The variables passed in to round_end for your use are:
    #     award: integer, total food bonus (can be zero) you received due to players cooperating
    #            during the last round. The amount of food you have for the next round will be
    #            current_food (including food_earnings from hunt_outcomes this round) + award.
    #     number_hunters: integer, number of times players chose to hunt in the last round.

    pass
