class Rectangle(object,IDisposable):
 """
 Stores a set of four integers that represent the left,top,right and bottom of a rectangle.

 

 Rectangle(left: int,top: int,right: int,bottom: int)

 Rectangle()

 Rectangle(other: Rectangle)
 """
 def Dispose(self):
  """ Dispose(self: Rectangle) """
  pass
 def IsNormalized(self):
  """
  IsNormalized(self: Rectangle) -> bool

  

   Returns true if the rectangle coordinates are normalized to the screen 

    coordinate space; that is,left is less than right and top is less than bottom.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Rectangle,disposing: bool) """
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
  __new__(cls: type,left: int,top: int,right: int,bottom: int)

  __new__(cls: type)

  __new__(cls: type,other: Rectangle)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Bottom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The y-coordinate of the bottom-right corner of the rectangle.



Get: Bottom(self: Rectangle) -> int



Set: Bottom(self: Rectangle)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: Rectangle) -> bool



"""

 Left=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The x-coordinate of the top-left corner of the rectangle.



Get: Left(self: Rectangle) -> int



Set: Left(self: Rectangle)=value

"""

 Right=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The x-coordinate of the bottom-right corner of the rectangle.



Get: Right(self: Rectangle) -> int



Set: Right(self: Rectangle)=value

"""

 Top=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The y-coordinate of the top-left corner of the rectangle.



Get: Top(self: Rectangle) -> int



Set: Top(self: Rectangle)=value

"""


