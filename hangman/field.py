
class HangmanField(object):
    states = [
        """
        ______
        |     |
        |
        |
        |
        |
        |
        """,
        """
        ______
        |     |
        |     0
        |
        |
        |
        |
        """,
        """
        ______
        |    |
        |    0 |
        | 
        |
        |
        |
        """,
        """
        ______
        |     |
        |     0 |
        |     | 
        | 
        |
        |
        """,
        """
        _______
        |     |
        |     0 |
        |     |
        |    |
        |
        |
        """,
        """
        _______
        |     |
        |     0 |
        |     |
        |    | |
        |
        |
        """

    ]

    def draw(self, wrong_tries: int)->None:
        print(self.states[wrong_tries])
