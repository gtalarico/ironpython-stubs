class RevitLinkOperations(object,IDisposable):
 """
 This class is used to extend the IExternalResourceServer interface with methods to support operations

    specifically related to Revit links.
 """
 def Dispose(self):
  """ Dispose(self: RevitLinkOperations) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: RevitLinkOperations,disposing: bool) """
  pass
 def SetGetLocalPathForOpenCallback(self,makeLocalCopyForOpen):
  """
  SetGetLocalPathForOpenCallback(self: RevitLinkOperations,makeLocalCopyForOpen: IGetLocalPathForOpenCallback)

   Sets the IGetLocalPathForOpenCallback that will support the "Open (and Unload)" 

    command for Revit links

     obtained from an IExternalResourceServer.

  

  

   makeLocalCopyForOpen: The IGetLocalPathForOpenCallback that will support the "Open (and Unload)" 

    command.
  """
  pass
 def SetOnLocalLinkSharedCoordinatesSavedCallback(self,onLocalLinkSharedCoordinatesSaved):
  """
  SetOnLocalLinkSharedCoordinatesSavedCallback(self: RevitLinkOperations,onLocalLinkSharedCoordinatesSaved: IOnLocalLinkSharedCoordinatesSavedCallback)

   Sets the callback that will be called when the Revit user saves new shared 

    coordinate

     settings to a linked document obtained from an 

    IExternalResourceServer.

  

  

   onLocalLinkSharedCoordinatesSaved: An IOnLocalLinkSharedCoordinatesSavedCallback object that can respond when the 

    user

     saves new shared coordinates to a Revit link document obtained from 

    IExternalResourceServer.
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: RevitLinkOperations) -> bool



"""


