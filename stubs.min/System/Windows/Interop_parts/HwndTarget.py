class HwndTarget(CompositionTarget,IDisposable,ICompositionTarget):
 """
 Represents a binding to a window handle that supports visual composition.
 
 HwndTarget(hwnd: IntPtr)
 """
 def Dispose(self):
  """
  Dispose(self: HwndTarget)
   Releases all resources used by the System.Windows.Interop.HwndTarget.
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
 def __new__(self,hwnd):
  """ __new__(cls: type,hwnd: IntPtr) """
  pass
 BackgroundColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color of the window referenced by this System.Windows.Interop.HwndTarget.

Get: BackgroundColor(self: HwndTarget) -> Color

Set: BackgroundColor(self: HwndTarget)=value
"""

 RenderMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the rendering mode for the window referenced by this System.Windows.Interop.HwndTarget.

Get: RenderMode(self: HwndTarget) -> RenderMode

Set: RenderMode(self: HwndTarget)=value
"""

 RootVisual=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the root visual object of the page that is hosted by the window.

Set: RootVisual(self: HwndTarget)=value
"""

 TransformFromDevice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a matrix that transforms the coordinates of the device that is associated with the rendering destination of this target.

Get: TransformFromDevice(self: HwndTarget) -> Matrix

"""

 TransformToDevice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a matrix that transforms the coordinates of this target to the device that is associated with the rendering destination.

Get: TransformToDevice(self: HwndTarget) -> Matrix

"""

 UsesPerPixelOpacity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that declares whether the per-pixel opacity value of the source window content is used for rendering.

Get: UsesPerPixelOpacity(self: HwndTarget) -> bool

"""


