import random
from game.jumper import Jumper
from game.terminal_service import TerminalService

class Puzzle:
    """The puzzle that the player will try to solve.

    The responsibility of Puzzle is to process the player input and display letters.
    
    Attributes:
        _word_list (list): A list of words.
        _word_selected (string): A random word selected from the words list.
        _word_guess (list): Displays the secret word.
        _tries (int): The number of tries that the player has to guess the word.
        _jumper (Jumper): The game's jumper class.
        _terminal_service (TerminalService): The game's terminal service class.
   
    """
    def __init__(self):
        """ Constructs a new Puzzle.
        
        Args:
            self (Puzzle): an instance of Puzzle.
        """
        self._word_list = ["history", "short" , "tiger", "paint"]  
        self._word_selected = random.choice(self._word_list)
        self._word_guess = ["_ "] * len(self._word_selected)
        self._tries = 0
        self._jumper = Jumper()
        self._terminal_service = TerminalService()

    def draw_word_guess(self):
        """ Displays the puzzle.
        
        Args: 
            self (Puzzle): An instance of Puzzle.
        """
        print( ' '.join(self._word_guess))
        
    def display_jumper(self):
        """ Displays the jumper.
        
        Args:
            self (Puzzle): An instance of Puzzle.
        """
        self._jumper.display_jumper(self._tries) 

    def process_guess(self, guess_letter):
        """ Determine whether the guessed letter is in the word, and based on that, decide how to act.
        
        Args:
            self (Puzzle): An instance of Puzzle.
        """
        if guess_letter in self._word_selected:
            self._word_guess[self._word_selected.index(guess_letter)] = guess_letter

        if guess_letter in self._word_selected:
            return guess_letter
        else:
            self._tries += 1
           
    def can_keep_guessing(self):
        """ Determine when the player can keep playing.
        
        Args:
            self (Puzzle): An instance of Puzzle.
        """
        
        if ''.join(self._word_guess) == self._word_selected:
            return True
        
        if  self._tries == 5:
            return True
   

      

    