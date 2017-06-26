class IOnLocalLinkSharedCoordinatesSavedCallback:
 """
 A callback for notifying an IExternalResourceServer that
    shared coordinates changes have been saved back to one
    of the Revit links provided by that server.
 """
 def OnLocalLinkSharedCoordinatesSaved(self,changedResource):
  """
  OnLocalLinkSharedCoordinatesSaved(self: IOnLocalLinkSharedCoordinatesSavedCallback,changedResource: ExternalResourceReference)
   Revit will call this method whenever shared coordinates
     changes are saved 
    to a linked document provided by an
     IExternalResourceServer. This call is a 
    notification
     to the server provider that one of their Revit links has
     
    changed locally,and they should upload the new version
     back to their 
    server.
  
  
   changedResource: The ExternalResourceReference whose shared coordinates have been saved.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
