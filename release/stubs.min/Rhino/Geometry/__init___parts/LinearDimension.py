class LinearDimension(AnnotationBase,IDisposable,ISerializable):
 """
 Represents a linear dimension.

    This entity refers to the geometric element that is independent from the document.

 

 LinearDimension()

 LinearDimension(dimensionPlane: Plane,extensionLine1End: Point2d,extensionLine2End: Point2d,pointOnDimensionLine: Point2d)
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
 @staticmethod
 def FromPoints(extensionLine1End,extensionLine2End,pointOnDimensionLine):
  """
  FromPoints(extensionLine1End: Point3d,extensionLine2End: Point3d,pointOnDimensionLine: Point3d) -> LinearDimension

  

   Initializes a new instance of the Rhino.Geometry.LinearDimension class,based on three points.
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
 def SetLocations(self,extensionLine1End,extensionLine2End,pointOnDimensionLine):
  """
  SetLocations(self: LinearDimension,extensionLine1End: Point2d,extensionLine2End: Point2d,pointOnDimensionLine: Point2d)

   Sets the three locations of the point,using two-dimensional points that refer to the plane of 

    the annotation.
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
 def __new__(self,dimensionPlane=None,extensionLine1End=None,extensionLine2End=None,pointOnDimensionLine=None):
  """
  __new__(cls: type)

  __new__(cls: type,dimensionPlane: Plane,extensionLine1End: Point2d,extensionLine2End: Point2d,pointOnDimensionLine: Point2d)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 Aligned=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether this annotation is aligned.



Get: Aligned(self: LinearDimension) -> bool



Set: Aligned(self: LinearDimension)=value

"""

 Arrowhead1End=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the arrow head end of the first extension line.



Get: Arrowhead1End(self: LinearDimension) -> Point2d



"""

 Arrowhead2End=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the arrow head end of the second extension line.



Get: Arrowhead2End(self: LinearDimension) -> Point2d



"""

 DimensionStyleIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Index of DimensionStyle in document DimStyle table used by the dimension.



Get: DimensionStyleIndex(self: LinearDimension) -> int



Set: DimensionStyleIndex(self: LinearDimension)=value

"""

 DistanceBetweenArrowTips=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the distance between arrow tips.



Get: DistanceBetweenArrowTips(self: LinearDimension) -> float



"""

 ExtensionLine1End=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the end of the first extension line.



Get: ExtensionLine1End(self: LinearDimension) -> Point2d



"""

 ExtensionLine2End=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the end of the second extension line.



Get: ExtensionLine2End(self: LinearDimension) -> Point2d



"""

 TextPosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets and sets the position of text on the plane.



Get: TextPosition(self: LinearDimension) -> Point2d



Set: TextPosition(self: LinearDimension)=value

"""


