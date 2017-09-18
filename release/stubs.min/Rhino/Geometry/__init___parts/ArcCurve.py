class ArcCurve(Curve,IDisposable,ISerializable):
 """
 Represent arcs and circles.

    ArcCurve.IsCircle returns true if the curve is a complete circle.

 

 ArcCurve()

 ArcCurve(other: ArcCurve)

 ArcCurve(arc: Arc)

 ArcCurve(arc: Arc,t0: float,t1: float)

 ArcCurve(circle: Circle)

 ArcCurve(circle: Circle,t0: float,t1: float)
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

  __new__(cls: type,other: ArcCurve)

  __new__(cls: type,arc: Arc)

  __new__(cls: type,arc: Arc,t0: float,t1: float)

  __new__(cls: type,circle: Circle)

  __new__(cls: type,circle: Circle,t0: float,t1: float)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 AngleDegrees=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the angles of this arc in degrees.



Get: AngleDegrees(self: ArcCurve) -> float



"""

 AngleRadians=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the angles of this arc in radians.



Get: AngleRadians(self: ArcCurve) -> float



"""

 Arc=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the arc that is contained within this ArcCurve.



Get: Arc(self: ArcCurve) -> Arc



"""

 IsCompleteCircle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether or not this curve can be represented by a complete circle.



Get: IsCompleteCircle(self: ArcCurve) -> bool



"""

 Radius=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the radius of this ArcCurve.



Get: Radius(self: ArcCurve) -> float



"""


