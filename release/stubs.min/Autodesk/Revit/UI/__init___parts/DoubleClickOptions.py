class DoubleClickOptions(object,IDisposable):
 """ Provides access to settings that control what happens when the current user double-clicks on an element. """
 def Dispose(self):
  """ Dispose(self: DoubleClickOptions) """
  pass
 def GetAction(self,target):
  """
  GetAction(self: DoubleClickOptions,target: DoubleClickTarget) -> DoubleClickAction

  

   Returns the active user's desired action for a particular double-click target.

  

   target: The target to check.

   Returns: The user's desired action for the specified target.
  """
  pass
 @staticmethod
 def GetDoubleClickOptions():
  """
  GetDoubleClickOptions() -> DoubleClickOptions

  

   Returns the current user's DoubleClickOptions.

   Returns: The DoubleClickOptions for the current user.
  """
  pass
 def IsSupportedAction(self,target,action):
  """
  IsSupportedAction(self: DoubleClickOptions,target: DoubleClickTarget,action: DoubleClickAction) -> bool

  

   Checks whether the specified double-click target supports the specified action.

  

   target: The double-click target to check.

   action: The desired double-click action.

   Returns: True if the target supports the specified action,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: DoubleClickOptions,disposing: bool) """
  pass
 def SetAction(self,target,action):
  """
  SetAction(self: DoubleClickOptions,target: DoubleClickTarget,action: DoubleClickAction)

   Changes the double-click action associated with a specified target.

  

   target: The double-click target whose action will be changed.

   action: The action to assign to the target.
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



Get: IsValidObject(self: DoubleClickOptions) -> bool



"""


