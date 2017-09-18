class PlaneSurface(Surface,IDisposable,ISerializable):
 """
 Represents a plane surface,with plane and two intervals.

 

 PlaneSurface(plane: Plane,xExtents: Interval,yExtents: Interval)
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
 def CreateThroughBox(*__args):
  """
  CreateThroughBox(plane: Plane,box: BoundingBox) -> PlaneSurface

  

   Extends a plane into a plane surface so that the latter goes through a bounding box.

  

   plane: An original plane value.

   box: A box to use for extension boundary.

   Returns: A new plane surface on success,or null on error.

  CreateThroughBox(lineInPlane: Line,vectorInPlane: Vector3d,box: BoundingBox) -> PlaneSurface

  

   Makes a plane that includes a line and a vector and goes through a bounding box.

  

   lineInPlane: A line that will lie on the plane.

   vectorInPlane: A vector the direction of which will be in plane.

   box: A box to cut through.

   Returns: A new plane surface on success,or null on error.
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
 def __new__(self,plane,xExtents,yExtents):
  """
  __new__(cls: type,plane: Plane,xExtents: Interval,yExtents: Interval)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
