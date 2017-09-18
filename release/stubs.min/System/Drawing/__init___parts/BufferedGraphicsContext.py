class BufferedGraphicsContext(object,IDisposable):
 """
 Provides methods for creating graphics buffers that can be used for double buffering.

 

 BufferedGraphicsContext()
 """
 def Allocate(self,*__args):
  """
  Allocate(self: BufferedGraphicsContext,targetDC: IntPtr,targetRectangle: Rectangle) -> BufferedGraphics

  

   Creates a graphics buffer of the specified size using the pixel format of the specified 

    System.Drawing.Graphics.

  

  

   targetDC: An System.IntPtr to a device context to match the pixel format of the new buffer to.

   targetRectangle: A System.Drawing.Rectangle indicating the size of the buffer to create.

   Returns: A System.Drawing.BufferedGraphics that can be used to draw to a buffer of the specified 

    dimensions.

  

  Allocate(self: BufferedGraphicsContext,targetGraphics: Graphics,targetRectangle: Rectangle) -> BufferedGraphics

  

   Creates a graphics buffer of the specified size using the pixel format of the specified 

    System.Drawing.Graphics.

  

  

   targetGraphics: The System.Drawing.Graphics to match the pixel format for the new buffer to.

   targetRectangle: A System.Drawing.Rectangle indicating the size of the buffer to create.

   Returns: A System.Drawing.BufferedGraphics that can be used to draw to a buffer of the specified 

    dimensions.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: BufferedGraphicsContext)

   Releases all resources used by the System.Drawing.BufferedGraphicsContext.
  """
  pass
 def Invalidate(self):
  """
  Invalidate(self: BufferedGraphicsContext)

   Disposes of the current graphics buffer,if a buffer has been allocated and has not yet been 

    disposed.
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
 MaximumBuffer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum size of the buffer to use.



Get: MaximumBuffer(self: BufferedGraphicsContext) -> Size



Set: MaximumBuffer(self: BufferedGraphicsContext)=value

"""


