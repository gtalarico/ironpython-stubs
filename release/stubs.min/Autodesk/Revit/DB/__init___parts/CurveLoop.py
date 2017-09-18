class CurveLoop(object,IEnumerable[Curve],IEnumerable,IDisposable):
 """
 A class that represents a chain of curves.

 

 CurveLoop()
 """
 def Append(self,curve):
  """
  Append(self: CurveLoop,curve: Curve)

   Append the curve to this loop.

  

   curve: The curve.
  """
  pass
 @staticmethod
 def Create(curves):
  """ Create(curves: IList[Curve]) -> CurveLoop """
  pass
 @staticmethod
 def CreateViaCopy(original):
  """
  CreateViaCopy(original: CurveLoop) -> CurveLoop

  

   Creates a new curve loop as a copy of the input.

  

   original: The original curve loop.

   Returns: The copied curve loop.
  """
  pass
 @staticmethod
 def CreateViaOffset(original,offsetDist,normal):
  """
  CreateViaOffset(original: CurveLoop,offsetDist: float,normal: XYZ) -> CurveLoop

  

   Creates a new curve loop that is an offset of the existing curve loop.

  

   original: The original curve loop.

   offsetDist: The signed offset distance.

   normal: The normal of the offset plane.

   Returns: The offset curve loop.
  """
  pass
 @staticmethod
 def CreateViaThicken(*__args):
  """
  CreateViaThicken(pCurve: Curve,thickness: float,normal: XYZ) -> CurveLoop

  

   Creates a new closed curve loop by thickening the input curve with respect to a 

    given plane.

  

  

   pCurve: The input curve.

   thickness: The distance between the offset curves created on either side of the input 

    curve.

  

   normal: The normal vector to the plane used for thickening.

   Returns: The new curve loop.

  CreateViaThicken(curveLoop: CurveLoop,thickness: float,normal: XYZ) -> CurveLoop

  

   Creates a new closed curve loop by thickening the input open curve loop with 

    respect to a given plane.

  

  

   curveLoop: The input curve loop.

   thickness: The distance between the offset curves created on either side of the input 

    curve.

  

   normal: The normal vector to the plane used for thickening.

   Returns: The new curve loop.
  """
  pass
 @staticmethod
 def CreateViaTransform(curveLoop,transform):
  """
  CreateViaTransform(curveLoop: CurveLoop,transform: Transform) -> CurveLoop

  

   Creates a new curve loop as a transformed copy of the input curve loop.

  

   curveLoop: The input curve loop.

   transform: The transformation.

   Returns: The new curve loop.
  """
  pass
 def Dispose(self):
  """ Dispose(self: CurveLoop) """
  pass
 def Flip(self):
  """
  Flip(self: CurveLoop)

   Reverses the orientation of the curve loop.
  """
  pass
 def GetCurveLoopIterator(self):
  """
  GetCurveLoopIterator(self: CurveLoop) -> CurveLoopIterator

  

   Returns a curve that iterates through the curve loop.

   Returns: A curve loop iterator object that can be used to iterate through key-value 

    pairs in the collection.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: CurveLoop) -> IEnumerator[Curve]

  

   Returns an enumerator that iterates through a collection.

   Returns: An IEnumerator object that can be used to iterate through the collection.
  """
  pass
 def GetExactLength(self):
  """
  GetExactLength(self: CurveLoop) -> float

  

   Returns the sum of exact lengths of all curves in the loop.

   Returns: The total length of the curves in the loop.
  """
  pass
 def GetPlane(self):
  """
  GetPlane(self: CurveLoop) -> Plane

  

   Gets the plane of the curve loop,if it is planar.

   Returns: The plane of the curve loop.
  """
  pass
 def GetRectangularHeight(self,plane):
  """
  GetRectangularHeight(self: CurveLoop,plane: Plane) -> float

  

   Returns the width of a curve loop if it is rectangular with respect to the 

    projection plane.

  

  

   plane: The plane to which the curves will be projected.

   Returns: The height.
  """
  pass
 def GetRectangularWidth(self,plane):
  """
  GetRectangularWidth(self: CurveLoop,plane: Plane) -> float

  

   Returns the width of a curve loop if it is rectangular with respect to the 

    projection plane.

  

  

   plane: The plane to which the curves will be projected.

   Returns: The width.
  """
  pass
 def HasPlane(self):
  """
  HasPlane(self: CurveLoop) -> bool

  

   Identifies if the CurveLoop is planar.

   Returns: True if the curve loop is planar,false otherwise.
  """
  pass
 def IsCounterclockwise(self,normal):
  """
  IsCounterclockwise(self: CurveLoop,normal: XYZ) -> bool

  

   Determines if this CurveLoop is oriented counter-clockwise (CCW) or clockwise 

    (CW) with

     respect to the specified 3D direction.

  

  

   normal: The normal vector to the plane used for this determination.

   Returns: True if the curve loop is oriented counter-clockwise with respect to the 

    specified 3D direction,

     false if the loop is oriented clockwise.
  """
  pass
 def IsOpen(self):
  """
  IsOpen(self: CurveLoop) -> bool

  

   Returns whether the curve loop is open or closed,as determined by an internal 

    flag.

  

   Returns: True if the CurveLoop is marked open,false if marked closed.
  """
  pass
 def IsRectangular(self,plane):
  """
  IsRectangular(self: CurveLoop,plane: Plane) -> bool

  

   Identifies if the curve loop is rectangular with respect to a given projection 

    plane.

  

  

   plane: The plane to which the curves will be projected to determine if they represent 

    a rectangle.

  

   Returns: True if the curve loop is rectangular,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: CurveLoop,disposing: bool) """
  pass
 def Transform(self,transform):
  """
  Transform(self: CurveLoop,transform: Transform)

   Transforms this curve loop and all of its component curves by the supplied 

    transformation.

  

  

   transform: The transformation.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[Curve](enumerable: IEnumerable[Curve],value: Curve) -> bool """
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
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: CurveLoop) -> bool



"""


