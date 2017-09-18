class LinkLoadContent(ExternalResourceLoadContent,IDisposable):
 """
 This class is used by IExternalResourceServers to return Link data to Revit when their

    LoadResource method is invoked.  It also contains additional information used by

    IExternalResourceUIServers to display link load status results to the user.
 """
 def Dispose(self):
  """ Dispose(self: ExternalResourceLoadContent,A_0: bool) """
  pass
 def GetLinkDataPath(self):
  """
  GetLinkDataPath(self: LinkLoadContent) -> ModelPath

  

   Returns the Link data path owned by this LinkLoadContent object.

   Returns: The Links data path owned by this LinkLoadContent object.
  """
  pass
 def GetLinkLoadResult(self):
  """
  GetLinkLoadResult(self: LinkLoadContent) -> RevitLinkLoadResult

  

   Retrieves the LinkLoadResult of the attempt to load or reload a Revit link.

   Returns: A LinkLoadObject containing the status and other information about an attempt 

    by Revit

     to load a Revit link.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ExternalResourceLoadContent,disposing: bool) """
  pass
 def SetLinkDataPath(self,linkPath):
  """
  SetLinkDataPath(self: LinkLoadContent,linkPath: ModelPath)

   Sets the Link data path owned by this LinkLoadContent object.

  

   linkPath: The Links data path set for this LinkLoadContent object.
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
