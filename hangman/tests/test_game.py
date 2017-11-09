import inspect
from hangman.game import Game


def test_add_round():
    game = Game()
    result = inspect.getsource(game.add_round)
    assert 'won_rounds[winner.id] += 1' in result
    assert 'if' in result


def test_gets_winner():
    game = Game()
    assert game.get_winner() is None
    assert game.get_winner()

