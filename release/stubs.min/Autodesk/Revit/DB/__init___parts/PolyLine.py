class PolyLine(GeometryObject,IDisposable):
 """ A polyline. """
 def Clone(self):
  """
  Clone(self: PolyLine) -> PolyLine

  

   Returns a copy of this polyline.
  """
  pass
 @staticmethod
 def Create(coordinates):
  """ Create(coordinates: IList[XYZ]) -> PolyLine """
  pass
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def Evaluate(self,param):
  """
  Evaluate(self: PolyLine,param: float) -> XYZ

  

   Evaluates a parameter on the polyline.

  

   param: The parameter to be evaluated. It is expected to be in [0,1] interval mapped to 

    the bounds of the whole polyline.
  """
  pass
 def GetCoordinate(self,index):
  """
  GetCoordinate(self: PolyLine,index: int) -> XYZ

  

   Gets the coordinate point of the specified index.

  

   index: The index of the coordinates.
  """
  pass
 def GetCoordinates(self):
  """
  GetCoordinates(self: PolyLine) -> IList[XYZ]

  

   Gets the coordinate points of the polyline.
  """
  pass
 def GetOutline(self):
  """
  GetOutline(self: PolyLine) -> Outline

  

   Gets the outline of the polyline.
  """
  pass
 def GetTransformed(self,transform):
  """
  GetTransformed(self: PolyLine,transform: Transform) -> PolyLine

  

   Gets the copy of the polyline which is applied the specified transformation.
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
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 NumberOfCoordinates=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of the coordinate points.



Get: NumberOfCoordinates(self: PolyLine) -> int



"""


