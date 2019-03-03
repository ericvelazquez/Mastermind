import collections
from board import Board
from player import Player


class Game():

    """
    Game class for mastermind

    """

    def __init__(self,columns=4,attempts=13):
        self.colors = {"r" : "red", "g" : "green", "b" : "blue", "y" : "yellow", "o" : "orange", "p" : "pink"}
        self.board = Board(columns,attempts,self.colors)
        self.player = Player(self.board, self.colors)


    def start_game_guess(self):
        """
        Start the game until the player solves the game or is out of attempts
        """
        # Let the codemaker choose the pattern
        self.player.generate_pattern()

        print("The game is about to start, if you want to check the game historic at any moment please write "
              "'historic'.\n")
        print("Write 'hint' at any time and we will provide you one hint. Just one per game.\n")
        # While the codebreaker still has attempts
        while self.board.attempts > 0:
            # Ask the codebreaker to make an attempt
            counted_attempt,attempt = self.player.make_attempt()
            # Check if the attempt is valid
            if counted_attempt is not None:
                # Get the close/exact result
                close, exact = self.board.check_guess(counted_attempt,attempt)
                # If all the balls are placed correctly then finish the game
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

        # Print the historic at the end of the game
        self.board.print_historic()



if __name__ == "__main__":
    game = Game()
    game.start_game_guess()







