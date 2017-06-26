class Cursor(object,IDisposable):
 """
 Represents the image used for the mouse pointer.
 
 Cursor(cursorStream: Stream,scaleWithDpi: bool)
 Cursor(cursorFile: str)
 Cursor(cursorFile: str,scaleWithDpi: bool)
 Cursor(cursorStream: Stream)
 """
 def Dispose(self):
  """
  Dispose(self: Cursor)
   Releases the resources used by the System.Windows.Input.Cursor class.
  """
  pass
 def ToString(self):
  """
  ToString(self: Cursor) -> str
  
   Returns the string representation of the System.Windows.Input.Cursor.
   Returns: The name of the cursor.
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
 def __new__(self,*__args):
  """
  __new__(cls: type,cursorFile: str)
  __new__(cls: type,cursorFile: str,scaleWithDpi: bool)
  __new__(cls: type,cursorStream: Stream)
  __new__(cls: type,cursorStream: Stream,scaleWithDpi: bool)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
