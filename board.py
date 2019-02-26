


class Board:
    """
    This class will simulate the Matsermind game board
    """

    def __init__(self,columns,attempts):
        self.colors = ["red", "green", "blue", "yellow", "orange", "pink"]
        self.balls_per_row = columns
        self.attempts = attempts
        self.solution = []
        self.board = [[None] * columns] * attempts
        self.feedback =[]

    def check_guess(self, guess):
        """
        evaluates the guess solution of the player codebreaker
        :param guess: guess solution of the player
        :return: tuple (# of correct color/position, # of correct color and wrong positon)
        """
        pass

    def save_guess_feedback(self, guess):
        """
        saves the current guess into self.board
        saves the current feedback into self.feedback
        :param guess: guess solution of the player
        """
        pass

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

    def get_feedback(self):
        """
        :return: self.feedback historic
        """
        return self.feedback