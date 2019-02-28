


class Board():
    """
    This class will simulate the Matsermind game board
    """

    def __init__(self,columns=4,attempts=13):
        self.colors = ["red", "green", "blue", "yellow", "orange", "pink"]
        self.balls_per_row = columns
        self.rows = attempts
        self.attempts = attempts
        self.solution = None
        self.counted_solution = None
        self.board = [None] * attempts
        self.feedback =[None] * attempts

    def check_guess(self, counted_attempt,attempt):
        """
        evaluates the guess solution of the player codebreaker
        :param guess: guess solution of the player
        :return: tuple (# of correct color/position, # of correct color and wrong positon)

        >>> import collections
        >>> board = Board()
        >>> board.solution = "rrrb"
        >>> board.counted_solution = collections.Counter(board.solution)
        >>> attempt = "rbgr"
        >>> counted_attempt = collections.Counter(attempt)
        >>> board.check_guess(counted_attempt, attempt)
        (2, 1)
        """
        close = sum(min(self.counted_solution[i], counted_attempt[i]) for i in self.counted_solution)
        exact = sum(a == b for a, b in zip(self.solution, attempt))
        close -= exact
        self.save_guess_feedback((close, exact))
        self.save_attempt(attempt)
        return close, exact


    def set_solution(self,solution):
        """
        sets a solution fo the board
        :param solution: pattern given by the player codemaker
        """
        self.solution = solution

    def get_solution(self):
        """
        :return: self.solution at that moment
        """
        return self.solution

    def get_board(self):
        """
        :return: self.board historic
        """
        return self.board

    def restart_board(self):
        """
        restart board to None
        restart attempts to 13

        >>> board = Board()
        >>> board.restart_board()
        [None, None, None, None, None, None, None, None, None, None, None, None, None]
        >>> board.attempts
        13
        """
        self.board = [None]  * self.attempts
        self.attempts = self.rows
        return self.board

    def get_feedback(self):
        """
        :return: self.feedback historic
        """
        return self.feedback

    def restart_feedback(self):
        """
        restart feedback to None

        >>> board = Board()
        >>> board.restart_feedback()
        [None, None, None, None, None, None, None, None, None, None, None, None, None]
        """
        self.feedback = [None] * self.attempts
        return self.feedback


    def save_attempt(self,attempt):
        """
        Saves attempt into board and decreasses self.attempts by 1
        :param attempt: list of colors
        :return: number of attempts

        >>> board = Board()
        >>> board.save_attempt("rbrb")
        12
        """
        if len(attempt) != self.balls_per_row:
            raise ValueError("Number of balls is not valid")
        postion = self.rows- self.attempts
        self.board[postion] = attempt
        self.attempts -= 1
        return self.attempts

    def save_guess_feedback(self, feedback):
        """
        saves the current feedback into self.feedback
        :param guess: guess solution of the player

        >>> feedback = (3,1)
        >>> board = Board()
        >>> board.save_guess_feedback(feedback)
        [(3, 1), None, None, None, None, None, None, None, None, None, None, None, None]
        """
        positon = self.rows- self.attempts
        self.feedback[positon] = feedback
        return self.feedback


if __name__ == "__main__":
    import doctest
    doctest.testmod()
