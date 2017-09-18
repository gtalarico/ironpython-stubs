class BrepLoop(GeometryBase,IDisposable,ISerializable):
 """
 Represent a single loop in a Brep object. A loop is composed

    of a list of trim curves.
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
 def To2dCurve(self):
  """
  To2dCurve(self: BrepLoop) -> Curve

  

   Create a 2d curve that traces the entire loop
  """
  pass
 def To3dCurve(self):
  """
  To3dCurve(self: BrepLoop) -> Curve

  

   Create a 3D curve that approximates the loop geometry.

   Returns: A 3D curve that approximates the loop or null on failure.
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
 Brep=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Brep that owns this loop.



Get: Brep(self: BrepLoop) -> Brep



"""

 Face=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """BrepFace this loop belongs to.



Get: Face(self: BrepLoop) -> BrepFace



"""

 LoopIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of this loop in the Brep.Loops collection.



Get: LoopIndex(self: BrepLoop) -> int



"""

 LoopType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """type of loop.



Get: LoopType(self: BrepLoop) -> BrepLoopType



"""

 Trims=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """List of trims for this loop



Get: Trims(self: BrepLoop) -> BrepTrimList



"""


