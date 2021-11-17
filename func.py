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
    player1:  55441
    player2:  55332
    result: Player1 win the game with two pair 44

平手
    result: No winner
"""


class PokerGame():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def result(self):
        player1_list = self.player1.split(" ")
        player2_list = self.player2.split(" ")
