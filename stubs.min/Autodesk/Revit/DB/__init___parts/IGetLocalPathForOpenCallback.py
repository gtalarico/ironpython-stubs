class IGetLocalPathForOpenCallback:
 """ The interface used to provide custom support for the "Open (and Unload)" command for Revit Links obtained as external resources. """
 def GetLocalPathForOpen(self,desiredResource):
  """
  GetLocalPathForOpen(self: IGetLocalPathForOpenCallback,desiredResource: ExternalResourceReference) -> str
  
   Implement this method to specify the local path from where a copy of a Revit 
    link external resource can be opened
     for modification without interfering 
    with its use as a link in other open documents.
  
  
   desiredResource: The ExternalResourceReference that needs to be opened for modification by Revit.
   Returns: The local path from where Revit can open the linked file as its own top-level 
    document.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
