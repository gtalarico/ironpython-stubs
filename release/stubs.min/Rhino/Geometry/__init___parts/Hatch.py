class Hatch(GeometryBase,IDisposable,ISerializable):
 """
 Represents a hatch in planar boundary loop or loops.

    This is a 2d entity with a plane defining a local coordinate system.

    The loops,patterns,angles,etc are all in this local coordinate system.

    The Hatch object manages the plane and loop array

    Fill definitions are in the HatchPattern or class derived from HatchPattern

    Hatch has an index to get the pattern definition from the pattern table.
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
  Create(curve: Curve,hatchPatternIndex: int,rotationRadians: float,scale: float) -> Array[Hatch]

  

   Constructs an array of Rhino.Geometry.Hatchhatches from one curve.

  

   curve: A Rhino.Geometry.Curve.

   hatchPatternIndex: The index of the hatch pattern in the document hatch pattern table.

   rotationRadians: The relative rotation of the pattern.

   scale: A scaling factor.

   Returns: An array of hatches. The array might be empty on error.

  Create(curves: IEnumerable[Curve],hatchPatternIndex: int,rotationRadians: float,scale: float) -> Array[Hatch]
  """
  pass
 def CreateDisplayGeometry(self,pattern,patternScale,bounds,lines,solidBrep):
  """
  CreateDisplayGeometry(self: Hatch,pattern: HatchPattern,patternScale: float) -> (Array[Curve],Array[Line],Brep)

  

   Generate geometry that would be used to draw the hatch with a given hatch pattern
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
 def Explode(self):
  """
  Explode(self: Hatch) -> Array[GeometryBase]

  

   Decomposes the hatch pattern into an array of geometry.

   Returns: An array of geometry that formed the appearance of the original elements.
  """
  pass
 def Get3dCurves(self,outer):
  """
  Get3dCurves(self: Hatch,outer: bool) -> Array[Curve]

  

   Gets 3d curves that define the boundaries of the hatch

  

   outer: true to get the outer curves,false to get the inner curves
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
 PatternIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the index of the pattern in the document hatch pattern table.



Get: PatternIndex(self: Hatch) -> int



Set: PatternIndex(self: Hatch)=value

"""

 PatternRotation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the relative rotation of the pattern.



Get: PatternRotation(self: Hatch) -> float



Set: PatternRotation(self: Hatch)=value

"""

 PatternScale=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the scaling factor of the pattern.



Get: PatternScale(self: Hatch) -> float



Set: PatternScale(self: Hatch)=value

"""


