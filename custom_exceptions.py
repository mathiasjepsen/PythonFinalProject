class WrongUsernameException(Exception):
   def __init__(self, arg):
      self.args = arg

class InvalidTokenException(Exception):
   def __init__(self, arg):
      self.args = arg