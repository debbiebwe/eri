from func import PokerGame


def test_nothing_winner():
    game = PokerGame("1C 2H 6S 9S TD", "2C 4H 5S 8S 9D")
    assert game.result() == "Player1 win the game"


# 10 = T
# 紅心 = H
# 方塊 = D
# 黑桃 = S
# 梅花 = C
