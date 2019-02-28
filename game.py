import collections
from board import Board
from player import Player


class Game():

    """
    Game class for mastermind
    """

    def __init__(self,columns=4,attempts=13):
        self.colors = {"r" : "red", "g" : "green", "b" : "blue", "y" : "yellow", "o" : "orange", "p" : "pink"}
        self.board = Board(columns,attempts)
        self.player = Player(self.board)


    def start_game_guess(self):
        """
        Start the game until the player solves the game or is out of attempts
        """
        self.player.generate_pattern()

        print("The game is about to start, if you want to check the game historic at any moment please write "
              "'historic'.\n")
        while self.board.attempts > 0:
            counted_attempt,attempt = self.player.make_attempt()
            if counted_attempt is not None:
                close, exact = self.board.check_guess(counted_attempt,attempt)
                if exact == self.board.balls_per_row:
                    break
                print("Attempts: %d . Feedback: CLOSE -> %d EXACT -> %d .\n" %(self.board.attempts, close,exact))
            else:
                print("This guess is not valid. The colors available are %s . This attempt does not count" % (
                    self.colors))


        # When the player has solved the game
        if exact == self.board.balls_per_row:
            print("Good job!! Game solved. You used %d attempts" %(self.board.rows - self.board.attempts))

        # Out of attempts
        else:
            print("Game OVER!! The solution was %s" % (self.board.solution))

        self.board.print_historic()






if __name__ == "__main__":
    game = Game()
    game.start_game_guess()







