class IManipulator:
 """ Provides the position of input that is needed to create a manipulation. """
 def GetPosition(self,relativeTo):
  """
  GetPosition(self: IManipulator,relativeTo: IInputElement) -> Point
  
   Returns the position of the System.Windows.Input.IManipulator object.
  
   relativeTo: The element to use as the frame of reference for calculating the position of 
    the System.Windows.Input.IManipulator.
  
   Returns: The position of the System.Windows.Input.IManipulator object.
  """
  pass
 def ManipulationEnded(self,cancel):
  """
  ManipulationEnded(self: IManipulator,cancel: bool)
   Called when the manipulation ends.
  
   cancel: true if the manipulation is canceled; otherwise,false.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a unique identifier for the object.

Get: Id(self: IManipulator) -> int

"""


 Updated=None

