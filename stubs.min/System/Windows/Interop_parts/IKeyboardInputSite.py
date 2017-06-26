class IKeyboardInputSite:
 """ Manages keyboard focus within the container.  This interface implements keyboard message management in WPF-Win32 interoperation scenarios. """
 def OnNoMoreTabStops(self,request):
  """
  OnNoMoreTabStops(self: IKeyboardInputSite,request: TraversalRequest) -> bool
  
   Called by a contained component when it has reached its last tab stop and has 
    no further items to tab to.
  
  
   request: Specifies whether focus should be set to the first or the last tab stop.
   Returns: If this method returns true,the site has shifted focus to another component. 
    If this method returns false,focus is still within the calling component. The 
    component should "wrap around" and set focus to its first contained tab stop.
  """
  pass
 def Unregister(self):
  """
  Unregister(self: IKeyboardInputSite)
   Unregisters a child keyboard input sink from this site.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Sink=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the keyboard sink associated with this site.

Get: Sink(self: IKeyboardInputSite) -> IKeyboardInputSink

"""


