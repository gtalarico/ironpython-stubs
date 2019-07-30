class ICloneable:
 """ Supports cloning,which creates a new instance of a class with the same value as an existing instance. """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ICloneable()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Clone(self):
  """
  Clone(self: ICloneable) -> object
  
   Creates a new object that is a copy of the current instance.
   Returns: A new object that is a copy of this instance.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
