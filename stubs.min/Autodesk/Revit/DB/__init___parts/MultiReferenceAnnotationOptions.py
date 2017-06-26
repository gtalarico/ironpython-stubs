class MultiReferenceAnnotationOptions(object,IDisposable):
 """
 Options which control the creation of MultiReferenceAnnotations.
 
 MultiReferenceAnnotationOptions(multiReferenceAnnotationType: MultiReferenceAnnotationType)
 """
 def Dispose(self):
  """ Dispose(self: MultiReferenceAnnotationOptions) """
  pass
 def ElementsMatchReferenceCategory(self,elements):
  """ ElementsMatchReferenceCategory(self: MultiReferenceAnnotationOptions,elements: ICollection[ElementId]) -> bool """
  pass
 def GetElementsToDimension(self):
  """
  GetElementsToDimension(self: MultiReferenceAnnotationOptions) -> ICollection[ElementId]
  
   Gets the elements which the dimension will witness.
   Returns: The elements which the dimension will witness.
  """
  pass
 def IsAllowedDimensionStyleType(self,dimensionStyleType):
  """
  IsAllowedDimensionStyleType(self: MultiReferenceAnnotationOptions,dimensionStyleType: DimensionStyleType) -> bool
  
   Only Linear and LinearFixed dimension style types are allowed for new 
    MultiReferenceAnnotations.
  
  
   dimensionStyleType: The dimension style type to test.
   Returns: True if the type is allowed.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: MultiReferenceAnnotationOptions,disposing: bool) """
  pass
 def SetElementsToDimension(self,elementsToDimension):
  """ SetElementsToDimension(self: MultiReferenceAnnotationOptions,elementsToDimension: ICollection[ElementId]) """
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
 @staticmethod
 def __new__(self,multiReferenceAnnotationType):
  """ __new__(cls: type,multiReferenceAnnotationType: MultiReferenceAnnotationType) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 DimensionLineDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The direction vector of the dimension line.

Get: DimensionLineDirection(self: MultiReferenceAnnotationOptions) -> XYZ

Set: DimensionLineDirection(self: MultiReferenceAnnotationOptions)=value
"""

 DimensionLineOrigin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The origin point for the dimension line.

Get: DimensionLineOrigin(self: MultiReferenceAnnotationOptions) -> XYZ

Set: DimensionLineOrigin(self: MultiReferenceAnnotationOptions)=value
"""

 DimensionPlaneNormal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The normal vector to the dimension plane.

Get: DimensionPlaneNormal(self: MultiReferenceAnnotationOptions) -> XYZ

Set: DimensionPlaneNormal(self: MultiReferenceAnnotationOptions)=value
"""

 DimensionStyleType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The dimension style type to be used by the new MultiReferenceAnnotation.

Get: DimensionStyleType(self: MultiReferenceAnnotationOptions) -> DimensionStyleType

Set: DimensionStyleType(self: MultiReferenceAnnotationOptions)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: MultiReferenceAnnotationOptions) -> bool

"""

 MultiReferenceAnnotationType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The MultiReferenceAnnotationType to be used by the new MultiReferenceAnnotation.

Get: MultiReferenceAnnotationType(self: MultiReferenceAnnotationOptions) -> MultiReferenceAnnotationType

"""

 TagHasLeader=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When true the tag will be created with an attached leader.
   When false the tag will be created without a leader.

Get: TagHasLeader(self: MultiReferenceAnnotationOptions) -> bool

Set: TagHasLeader(self: MultiReferenceAnnotationOptions)=value
"""

 TagHeadPosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The position for the tag's head.

Get: TagHeadPosition(self: MultiReferenceAnnotationOptions) -> XYZ

Set: TagHeadPosition(self: MultiReferenceAnnotationOptions)=value
"""


