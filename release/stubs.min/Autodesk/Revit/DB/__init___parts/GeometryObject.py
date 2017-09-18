class GeometryObject(APIObject,IDisposable):
 """ The common base class for all geometric primitives. """
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def Equals(self,obj):
  """
  Equals(self: GeometryObject,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to the current 

    System.Object.

  

  

   obj: Another object.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: GeometryObject) -> int

  

   Gets the integer value of the geometry object as hash code
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: GeometryObject) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __ne__(self,*args):
  pass
 GraphicsStyleId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The ElementId of the GeometryObject's GraphicsStyle



Get: GraphicsStyleId(self: GeometryObject) -> ElementId



"""

 IsElementGeometry=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether this geometry is obtained directly from an Element.



Get: IsElementGeometry(self: GeometryObject) -> bool



"""

 Visibility=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The visibility.



Get: Visibility(self: GeometryObject) -> Visibility



"""


