def test_isset_states():
    from hangman.field import HangmanField
    result = HangmanField.states
    assert len(result) > 0


def test_draw():
    from hangman.field import HangmanField
    game = HangmanField()
    assert game.draw(5) is None
