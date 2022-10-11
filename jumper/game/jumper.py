class Jumper:

  def __init__(self):
    """ Constructs a new Jumper.
        
    Args:
        self (Jumper): an instance of Jumper
    """
      
    self._phases = [ 
    """ 
     ___  
    /___\ 
    \   / 
     \ /  
      0   
     /|\     
     / \  
      
   ^^^^^^^
    """ ,
    """ 
    /___\ 
    \   / 
     \ /  
      0   
     /|\  
     / \  
    
   ^^^^^^^
   """ ,
   """ 
     ___ 
    \   / 
     \ /  
      0   
     /|\     
     / \  
  
   ^^^^^^^
   """ ,
   """ 
    \   / 
     \ /  
      0   
     /|\    
     / \  
  
   ^^^^^^^
  """ ,
  """ 
     \ /  
      0   
     /|\    
     / \  
  
   ^^^^^^^
    """ ,
    """ 
      X   
     /|\    
     / \  
  
   ^^^^^^^
   """ ]

  def display_jumper(self, tries):
    """ Displays the jumper.

    Args:
    self (Jumper): an instance of Jumper
    """
    print(self._phases[tries])