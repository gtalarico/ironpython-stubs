class BufferedGraphics(object,IDisposable):
 """ Provides a graphics buffer for double buffering. """
 def Dispose(self):
  """
  Dispose(self: BufferedGraphics)

   Releases all resources used by the System.Drawing.BufferedGraphics object.
  """
  pass
 def Render(self,*__args):
  """
  Render(self: BufferedGraphics,targetDC: IntPtr)

   Writes the contents of the graphics buffer to the device context associated with the specified 

    System.IntPtr handle.

  

  

   targetDC: An System.IntPtr that points to the device context to which to write the contents of the 

    graphics buffer.

  

  Render(self: BufferedGraphics,target: Graphics)

   Writes the contents of the graphics buffer to the specified System.Drawing.Graphics object.

  

   target: A System.Drawing.Graphics object to which to write the contents of the graphics buffer.

  Render(self: BufferedGraphics)

   Writes the contents of the graphics buffer to the default device.
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Graphics=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Drawing.Graphics object that outputs to the graphics buffer.



Get: Graphics(self: BufferedGraphics) -> Graphics



"""


