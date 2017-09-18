class RevSurface(Surface,IDisposable,ISerializable):
 """
 Represents a surface of revolution.

    Revolutions can be incomplete (they can form arcs).
 """
 def ConstructConstObject(self,*args):
  """
  ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int)

   Assigns a parent object and a subobject index to this.

  

   parentObject: The parent object.

   subobject_index: The subobject index.
  """
  pass
 @staticmethod
 def Create(*__args):
  """
  Create(revoluteLine: Line,axisOfRevolution: Line) -> RevSurface

  

   Constructs a new surface of revolution from a generatrix line and an axis.

     If the 

    operation succeeds,results can be (truncated) cones,cylinders and circular hyperboloids.

  

  

   revoluteLine: A generatrix.

   axisOfRevolution: An axis.

   Returns: A new surface of revolution,or null if any of the inputs is invalid or on error.

  Create(revolutePolyline: Polyline,axisOfRevolution: Line,startAngleRadians: float,endAngleRadians: float) -> RevSurface

  

   Constructs a new surface of revolution from a generatrix polyline and an axis.

     This 

    overload accepts a slice start and end angles.

  

  

   revolutePolyline: A generatrix.

   axisOfRevolution: An axis.

   startAngleRadians: An angle in radias for the start.

   endAngleRadians: An angle in radias for the end.

   Returns: A new surface of revolution,or null if any of the inputs is invalid or on error.

  Create(revolutePolyline: Polyline,axisOfRevolution: Line) -> RevSurface

  

   Constructs a new surface of revolution from a generatrix polyline and an axis.

  

   revolutePolyline: A generatrix.

   axisOfRevolution: An axis.

   Returns: A new surface of revolution,or null if any of the inputs is invalid or on error.

  Create(revoluteCurve: Curve,axisOfRevolution: Line,startAngleRadians: float,endAngleRadians: float) -> RevSurface

  

   Constructs a new surface of revolution from a generatrix curve and an axis.

     This 

    overload accepts a slice start and end angles.

  

  

   revoluteCurve: A generatrix.

   axisOfRevolution: An axis.

   startAngleRadians: An angle in radias for the start.

   endAngleRadians: An angle in radias for the end.

   Returns: A new surface of revolution,or null if any of the inputs is invalid or on error.

  Create(revoluteCurve: Curve,axisOfRevolution: Line) -> RevSurface

  

   Constructs a new surface of revolution from a generatrix curve and an axis.

  

   revoluteCurve: A generatrix.

   axisOfRevolution: An axis.

   Returns: A new surface of revolution,or null if any of the inputs is invalid or on error.

  Create(revoluteLine: Line,axisOfRevolution: Line,startAngleRadians: float,endAngleRadians: float) -> RevSurface

  

   Constructs a new surface of revolution from a generatrix line and an axis.

     This 

    overload accepts a slice start and end angles.Results can be (truncated) cones,cylinders and 

    circular hyperboloids,or can fail.

  

  

   revoluteLine: A generatrix.

   axisOfRevolution: An axis.

   startAngleRadians: An angle in radias for the start.

   endAngleRadians: An angle in radias for the end.

   Returns: A new surface of revolution,or null if any of the inputs is invalid or on error.
  """
  pass
 @staticmethod
 def CreateFromCone(cone):
  """
  CreateFromCone(cone: Cone) -> RevSurface

  

   Constructs a new surface of revolution from the values of a cone.

  

   cone: A cone.

   Returns: A new surface of revolution,or null if any of the inputs is invalid or on error.
  """
  pass
 @staticmethod
 def CreateFromCylinder(cylinder):
  """
  CreateFromCylinder(cylinder: Cylinder) -> RevSurface

  

   Constructs a new surface of revolution from the values of a cylinder.

  

   cylinder: A cylinder.

   Returns: A new surface of revolution,or null if any of the inputs is invalid or on error.
  """
  pass
 @staticmethod
 def CreateFromSphere(sphere):
  """
  CreateFromSphere(sphere: Sphere) -> RevSurface

  

   Constructs a new surface of revolution from the values of a sphere.

  

   sphere: A sphere.

   Returns: A new surface of revolution,or null if any of the inputs is invalid or on error.
  """
  pass
 @staticmethod
 def CreateFromTorus(torus):
  """
  CreateFromTorus(torus: Torus) -> RevSurface

  

   Constructs a new surface of revolution from the values of a torus.

  

   torus: A torus.

   Returns: A new surface of revolution,or null if any of the inputs is invalid or on error.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: CommonObject,disposing: bool)

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
  NonConstOperation(self: CommonObject)

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
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,info: SerializationInfo,context: StreamingContext) """
  pass
 def __reduce_ex__(self,*args):
  pass
