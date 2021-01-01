"""Python serial number generator."""

    """Machine to create unique incrementing serial numbers.
    
    >>>serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
  """Make a new generator, starting at start."""
class SerialGenerator:
  def __init__(self, start = 0):
  self.start = self.next = start
      
def__repr__(self):
  """Show representation."""
  return f"<SerialGenerator start={self.start} next={self.next}>"


 
