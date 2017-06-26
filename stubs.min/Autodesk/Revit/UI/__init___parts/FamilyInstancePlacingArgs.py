class FamilyInstancePlacingArgs(object,IDisposable):
 """ The class is used to access necessary data during the placement of a FamilyInstance. """
 def Dispose(self):
  """ Dispose(self: FamilyInstancePlacingArgs) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FamilyInstancePlacingArgs,disposing: bool) """
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
 ActiveView=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The active view

Get: ActiveView(self: FamilyInstancePlacingArgs) -> View

"""

 IsBanned=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the cursor is banned or not.

Get: IsBanned(self: FamilyInstancePlacingArgs) -> bool

Set: IsBanned(self: FamilyInstancePlacingArgs)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FamilyInstancePlacingArgs) -> bool

"""

 StatusMessage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The message to be shown on the status bar

Get: StatusMessage(self: FamilyInstancePlacingArgs) -> str

Set: StatusMessage(self: FamilyInstancePlacingArgs)=value
"""

 TooltipMessage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The message to be shown via tooltip

Get: TooltipMessage(self: FamilyInstancePlacingArgs) -> str

Set: TooltipMessage(self: FamilyInstancePlacingArgs)=value
"""


