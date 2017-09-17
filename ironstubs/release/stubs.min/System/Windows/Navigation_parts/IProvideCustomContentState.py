class IProvideCustomContentState:
 """ Implemented by a class that needs to add custom state to the navigation history entry for content before the content is navigated away from. """
 def GetContentState(self):
  """
  GetContentState(self: IProvideCustomContentState) -> CustomContentState
  
   Returns an instance of a custom state class that is to be associated with 
    content in navigation history.
  
   Returns: An instance of a custom System.Windows.Navigation.CustomContentState class that 
    is to be associated with content in navigation history.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
