import inspect


def test_computer_player():
    from hangman.players import ComputerPlayer
    comp = ComputerPlayer()
    assert comp.changes_turns is False
    assert type(comp.quess_new_word()) is str


def test_human_player():
    from hangman.players import HumanPlayer
    result = HumanPlayer()
    assert result.changes_turns is True
    assert result._validate_word(None) is False
    assert result._validate_word(word='cat') is True
    assert result._validate_word(word='ЭЭЭ') is False


def test_selected():
    from hangman.players import HumanPlayer
    result = HumanPlayer()
    results = inspect.getsource(result.select_other_player)
    assert 'input(' in results
    assert 'except KeyError:' in results


def test_quest_new_word():
    from hangman.players import HumanPlayer
    result = HumanPlayer()
    results = inspect.getsource(result.quess_new_word())
    assert 'word = None' in results
