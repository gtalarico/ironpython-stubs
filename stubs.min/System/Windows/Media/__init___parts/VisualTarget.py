class VisualTarget(CompositionTarget,IDisposable,ICompositionTarget):
 """
 Provides functionality for connecting one visual tree to another visual tree across thread boundaries.
 
 VisualTarget(hostVisual: HostVisual)
 """
 def Dispose(self):
  """
  Dispose(self: VisualTarget)
   Cleans up the state associated with the System.Windows.Interop.HwndTarget.
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
 def __new__(self,hostVisual):
  """ __new__(cls: type,hostVisual: HostVisual) """
  pass
 TransformFromDevice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns a matrix that can be used to transform coordinates from the rendering destination device to the System.Windows.Media.VisualTarget.

Get: TransformFromDevice(self: VisualTarget) -> Matrix

"""

 TransformToDevice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns a matrix that can be used to transform coordinates from the System.Windows.Media.VisualTarget to the rendering destination device.

Get: TransformToDevice(self: VisualTarget) -> Matrix

"""


