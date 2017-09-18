class Color(APIObject,IDisposable):
 """
 Represents a color in Autodesk Revit.

 

 Color(red: Byte,green: Byte,blue: Byte)
 """
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: APIObject) """
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
 def __new__(self,red,green,blue):
  """ __new__(cls: type,red: Byte,green: Byte,blue: Byte) """
  pass
 Blue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get the blue channel of the color.  Setting a channel is obsolete in Autodesk Revit 2013.  Please create a new color instead.



Get: Blue(self: Color) -> Byte



Set: Blue(self: Color)=value

"""

 Green=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get the green channel of the color.  Setting a channel is obsolete in Autodesk Revit 2013.  Please create a new color instead.



Get: Green(self: Color) -> Byte



Set: Green(self: Color)=value

"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if the color represents a valid color,or an uninitialized/invalid value.



Get: IsValid(self: Color) -> bool



"""

 Red=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get the red channel of the color.  Setting a channel is obsolete in Autodesk Revit 2013.  Please create a new color instead.



Get: Red(self: Color) -> Byte



Set: Red(self: Color)=value

"""


 InvalidColorValue=None

