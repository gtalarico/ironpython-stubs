class PaintEventArgs(EventArgs,IDisposable):
 """
 Provides data for the System.Windows.Forms.Control.Paint event.

 

 PaintEventArgs(graphics: Graphics,clipRect: Rectangle)
 """
 def Dispose(self):
  """
  Dispose(self: PaintEventArgs)

   Releases all resources used by the System.Windows.Forms.PaintEventArgs.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,graphics,clipRect):
  """ __new__(cls: type,graphics: Graphics,clipRect: Rectangle) """
  pass
 ClipRectangle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the rectangle in which to paint.



Get: ClipRectangle(self: PaintEventArgs) -> Rectangle



"""

 Graphics=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the graphics used to paint.



Get: Graphics(self: PaintEventArgs) -> Graphics



"""


