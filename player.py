import collections


class Player():
    """
    This class will simulate the codebreaker game player
    """

    def __init__(self, board):
        self.colors = {"r" : "red", "g" : "green", "b" : "blue", "y" : "yellow", "o" : "orange", "p" : "pink"}
        self.board = board



    def generate_pattern(self):
        """
        CodeMaker generates a valid pattern which is going to be the solution to find by the codebraker.
        """
        good_pattern = False
        while not good_pattern:
            guess = self.ask_for_pattern_codebraker()

            # If len os the user's input is not 4. The pattern given is not accepted.
            if len(guess) != self.board.balls_per_row:
                continue
            pattern = collections.Counter(guess)
            for element in pattern:
                # The pattern given is not accepted. User's input uses non-accepted colors.
                if element not in self.colors:
                    good_pattern = False
                    break
                else:
                    good_pattern = True
        self.board.set_solution(guess)
        self.board.counted_solution = pattern


    def ask_for_pattern_codebraker(self):
        guess = raw_input(
            "CODE MAKER, please choose a pattern [r for 'red', g 'green', b for 'blue', y for 'yellow', "
            "o for 'orange', p for'pink'] of length 4 :\n")
        return guess

    def ask_for_attempt_codebreaker(self):
        attempt = raw_input(
            "CODE BREAKER, please try to guess the pattern [r for 'red', g 'green', b for 'blue', y for 'yellow', "
            "o for 'orange', p for'pink'] of length 4 : \n")
        return attempt

    def make_attempt(self):
        """
        Tries guees, if not correct solution decreases attempts. Returns feedback.
        :return: feedhack
        """
        attempt = self.ask_for_attempt_codebreaker()

        #If the user's input is 'historic' retrun the game historic and ask for a solution again.
        while attempt == "historic":
            self.board.print_historic()
            attempt = self.ask_for_attempt_codebreaker()

        #If len of the user's input is not 4. The solution given is not accepted.
        if len(attempt) != 4:
            print("Please insert 4 colors")
            return None,None
        counted_attempt = collections.Counter(attempt)
        for element in counted_attempt:
            # The solution given is not accepted. User's input uses non-accepted colors.
            if element not in self.colors:
                print("You did not choose a valid color")
                return None,None
        return counted_attempt,attempt





if __name__ == "__main__":
    import doctest
    doctest.testmod()