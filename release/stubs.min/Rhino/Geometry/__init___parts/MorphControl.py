class MorphControl(GeometryBase,IDisposable,ISerializable):
 """
 Represents a geometry that is able to control the morphing behaviour of some other geometry.

 

 MorphControl(originCurve: NurbsCurve,targetCurve: NurbsCurve)
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
 def Morph(self,geometry):
  """
  Morph(self: MorphControl,geometry: GeometryBase) -> bool

  

   Applies the space morph to geometry.

  

   geometry: The geometry to be morphed.

   Returns: true on success,false on failure.
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
 def __new__(self,originCurve,targetCurve):
  """
  __new__(cls: type,originCurve: NurbsCurve,targetCurve: NurbsCurve)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 PreserveStructure=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """true if the morph should be done in a way that preserves the structure

   of the geometry.  In particular,for NURBS objects,true  eans that

   only the control points are moved.  The PreserveStructure value does not

   affect the way meshes and points are morphed. The default is false.



Get: PreserveStructure(self: MorphControl) -> bool



Set: PreserveStructure(self: MorphControl)=value

"""

 QuickPreview=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """true if the morph should be done as quickly as possible because the

   result is being used for some type of dynamic preview.  If QuickPreview

   is true,the tolerance may be ignored. The QuickPreview value does not

   affect the way meshes and points are morphed. The default is false.



Get: QuickPreview(self: MorphControl) -> bool



Set: QuickPreview(self: MorphControl)=value

"""

 SpaceMorphTolerance=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The 3d fitting tolerance used when morphing surfaces and breps.

   The default is 0.0 and any value <= 0.0 is ignored by morphing functions.

   The value returned by Tolerance does not affect the way meshes and points are morphed.



Get: SpaceMorphTolerance(self: MorphControl) -> float



Set: SpaceMorphTolerance(self: MorphControl)=value

"""


