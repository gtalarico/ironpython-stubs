class PolylineCurve(Curve,IDisposable,ISerializable):
 """
 Represents the geometry of a set of linked line segments.

    This is fundamentally a class that derives from Rhino.Geometry.Curve

    and internally contains a Rhino.Geometry.Polyline.

 

 PolylineCurve()

 PolylineCurve(other: PolylineCurve)

 PolylineCurve(points: IEnumerable[Point3d])
 """
 def ConstructConstObject(self,*args):
  """
  ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int)

   Assigns a parent object and a subobject index to this.

  

   parentObject: The parent object.

   subobject_index: The subobject index.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: Curve,disposing: bool)

   For derived class implementers.

     This method is called with argument true when class 

    user calls Dispose(),while with argument false when

     the Garbage Collector invokes 

    the finalizer,or Finalize() method.You must reclaim all used unmanaged resources in both cases,

    and can use this chance to call Dispose on disposable fields if the argument is true.Also,you 

    must call the base virtual method within your overriding method.

  

  

   disposing: true if the call comes from the Dispose() method; false if it comes from the Garbage Collector 

    finalizer.
  """
  pass
 def NonConstOperation(self,*args):
  """
  NonConstOperation(self: Curve)

   For derived classes implementers.

     Defines the necessary implementation to free the 

    instance from being const.
  """
  pass
 def OnSwitchToNonConst(self,*args):
  """
  OnSwitchToNonConst(self: GeometryBase)

   Is called when a non-const operation occurs.
  """
  pass
 def Point(self,index):
  """
  Point(self: PolylineCurve,index: int) -> Point3d

  

   Gets a point at a specified index in the polyline curve.

  

   index: An index.

   Returns: A point.
  """
  pass
 def SetPoint(self,index,point):
  """
  SetPoint(self: PolylineCurve,index: int,point: Point3d)

   Sets a point at a specified index in the polyline curve.

  

   index: An index.

   point: A point location to set.
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
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,other: PolylineCurve)

  __new__(cls: type,points: IEnumerable[Point3d])

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 PointCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of points in this polyline.



Get: PointCount(self: PolylineCurve) -> int



"""


