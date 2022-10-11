from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.puzzle import Puzzle

class Director:
    """ A person who directs the game.

    The responsibility of a Director is to control the sequence of play.
   
    Attributes:
        jumper (Jumper): The game's jumper.
        is_playing (boolean): Whether or not to keep playing.
        puzzle (Puzzle): The game's random word.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """ Constructs a new Director.
        
        Args:
            self (Director): an instance of Director
        """
        self._jumper = Jumper()
        self._puzzle = Puzzle()
        self._terminal_service = TerminalService()
        self._is_playing = True
     
    def start_game(self):
        """ Starts the game by running the main game loop. 
        
        Args:
            self (Director): an instance of Director
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """ Displays the secret word, character, and gets the guess guess_letter from the player.
        Args:
            self (Director): an instance of Director
        """
        self._puzzle.draw_word_guess()
        self._puzzle.display_jumper()
        self.guess_letter = self._terminal_service.read_text("Guess a letter [a-z]: ")
        
    def _do_updates(self):
        """The puzzle is actualized.
        Args:
            self (Director): An instance of Director.
        """
        self._puzzle.process_guess(self.guess_letter)

    def _do_outputs(self):
        """ Determines when the game is over.
        Args:
            self (Director): an instance of Director
        """
        if self._puzzle.can_keep_guessing():
            self._puzzle.draw_word_guess()
            self._puzzle.display_jumper()
            self._is_playing = False 
        
     