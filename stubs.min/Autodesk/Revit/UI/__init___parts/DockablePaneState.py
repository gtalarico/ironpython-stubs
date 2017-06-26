class DockablePaneState(object,IDisposable):
 """
 Describes where a dockable pane window should appear in the Revit user interface.
 
 DockablePaneState(other: DockablePaneState)
 DockablePaneState()
 """
 def Dispose(self):
  """ Dispose(self: DockablePaneState) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: DockablePaneState,disposing: bool) """
  pass
 def SetFloatingRectangle(self,rect):
  """
  SetFloatingRectangle(self: DockablePaneState,rect: Rectangle)
   When %dockPosition% is Floating,sets the rectangle used to determine the size 
    and position of the pane when %dockPosition% is Floating.  Coordinates are 
    relative to the upper-left-hand corner of the main Revit window.
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
 @staticmethod
 def __new__(self,other=None):
  """
  __new__(cls: type,other: DockablePaneState)
  __new__(cls: type)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 DockPosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Which part of the Revit application frame the pane should dock to.

Get: DockPosition(self: DockablePaneState) -> DockPosition

Set: DockPosition(self: DockablePaneState)=value
"""

 FloatingRectangle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When %dockPosition% is Floating,this rectangle determines the size and position of the pane.  Coordinates are relative to the upper-left-hand corner of the main Revit window.
   Note: the returned Rectangle is a copy. In order to change the pane state,you must call SetFloatingRectangle with a modified rectangle.

Get: FloatingRectangle(self: DockablePaneState) -> Rectangle

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: DockablePaneState) -> bool

"""

 TabBehind=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Ignored unless %dockPosition% is Tabbed.  The new pane will appear in a tab behind the specified existing pane ID.

Get: TabBehind(self: DockablePaneState) -> DockablePaneId

Set: TabBehind(self: DockablePaneState)=value
"""


