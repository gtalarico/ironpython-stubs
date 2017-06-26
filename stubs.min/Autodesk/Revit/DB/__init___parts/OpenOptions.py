class OpenOptions(object,IDisposable):
 """
 This class contains options available for opening a document from disk.
 
 OpenOptions()
 """
 def Dispose(self):
  """ Dispose(self: OpenOptions) """
  pass
 def GetOpenWorksetsConfiguration(self):
  """
  GetOpenWorksetsConfiguration(self: OpenOptions) -> WorksetConfiguration
  
   Gets the object used to configure the worksets to open when the model is opened.
   Returns: The options.  If ll,all user-created worksets will be opened.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: OpenOptions,disposing: bool) """
  pass
 def SetOpenWorksetsConfiguration(self,openConfiguration):
  """
  SetOpenWorksetsConfiguration(self: OpenOptions,openConfiguration: WorksetConfiguration)
   Sets the object used to configure the worksets to open when the model is opened.
  
   openConfiguration: The options.  If ll,all user-created worksets will be opened.
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
 AllowOpeningLocalByWrongUser=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether a local file is allowed to be opened as read-only by a user other than its owner.

Get: AllowOpeningLocalByWrongUser(self: OpenOptions) -> bool

Set: AllowOpeningLocalByWrongUser(self: OpenOptions)=value
"""

 Audit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether to expand all elements in order to check for corruption.

Get: Audit(self: OpenOptions) -> bool

Set: Audit(self: OpenOptions)=value
"""

 DetachFromCentralOption=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """An option that specifies whether or not a workset-enabled document is detached from its central document.

Get: DetachFromCentralOption(self: OpenOptions) -> DetachFromCentralOption

Set: DetachFromCentralOption(self: OpenOptions)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: OpenOptions) -> bool

"""


