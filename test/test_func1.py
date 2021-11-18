from func import PokerGame


def test_nothing_winner():
    game = PokerGame("1C 2H 6S 9S TD", "2C 4H 5S 8S 9D")
    assert game.result() == "Player1 win the game with nothing 1C"


def test_nothing_winner_jqk_1():
    game = PokerGame("QC 2H 6S 9S TD", "2C 4H JS 8S 9D")
    assert game.result() == "Player1 win the game with nothing QC"


def test_nothing_winner_jqk_2():
    game = PokerGame("JC 2H 6S 9S TD", "2C 4H KS 8S 9D")
    assert game.result() == "Player2 win the game with nothing KS"


def test_nothing_winner_jqk_3():
    game = PokerGame("KC QH 6S 9S TD", "2C JH KS 8S 9D")
    assert game.result() == "Player1 win the game with nothing QH"


def test_nothing_no_winner():
    game = PokerGame("1C 2H 6S 8S KD", "2C 1H KS 8D 6D")
    assert game.result() == "No winner"


def test_onepair_nothing_1():
    game = PokerGame("1C 1H 3S 6S KD", "2C 1H KS 8D 6D")
    assert game.result() == "Player1 win the game"

# 10 = T
# 紅心 = H
# 方塊 = D
# 黑桃 = S
# 梅花 = C
