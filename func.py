"""
10 = T
紅心 = H
方塊 = D
黑桃 = S
梅花 = C

紅心10 = TH

雙方不同牌型
    player1: 對子
    plarer2: 葫蘆
    result: Player2 win

雙方相同牌型
    player1:  5H 5D 4S 4C 1C
    player2:  5S 5C 3H 3D 2D
    result: Player1 win the game with two pair 4S 4C

平手
    result: No winner
"""

poker_order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "1"]


def get_order(card):
    return poker_order.index(card)


class PokerGame():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def result(self):
        player1_list = self.player1.split(" ")  # ["1C", "2S"]  [Card("1C")]
        player2_list = self.player2.split(" ")
        player1_list_num = [get_order(x[0]) for x in player1_list]  # [0, 13]
        player2_list_num = [get_order(x[0]) for x in player2_list]
        player1_max = max(player1_list_num)
        player2_max = max(player2_list_num)

        player1_max_card_index = player1_list_num.index(player1_max)
        player2_max_card_index = player2_list_num.index(player2_max)

        if player1_max > player2_max:
            return f"Player1 win the game with nothing {player1_list[player1_max_card_index]}"
        elif player1_max < player2_max:
            return f"Player2 win the game with nothing {player2_list[player2_max_card_index]}"
        else:
            return "No winner"


class Card():
    def __init__(self, value):
        self.value = value
        self.num = get_order(value[0])

    def __eq__(self, other):
        return self.num == other.num

    def __gt__(self, other):
        return self.num > other.num

    def __lt__(self, other):
        return self.num < other.num

    def __ne__(self, other):
        return self.num != other.num

    def __ne__(self, other):
        return self.num != other.num

    def __ge__(self, other):
        return self.num >= other.num

    def __le__(self, other):
        return self.num <= other.num
