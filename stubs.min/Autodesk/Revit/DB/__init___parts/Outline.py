class Outline(object,IDisposable):
 """
 Outline is a generic object that provides a bounding box/bounding outline. It supports
    operations to scale and transform. It also supports intersections and contains operations.
 
 Outline(minimumPoint: XYZ,maximumPoint: XYZ)
 Outline(other: Outline)
 """
 def AddPoint(self,point):
  """
  AddPoint(self: Outline,point: XYZ)
   Adds a point to the bounding box,expanding it if the point is outside the 
    existing boundary.
  
  
   point: The point to add.
  """
  pass
 def Contains(self,point,tolerance):
  """
  Contains(self: Outline,point: XYZ,tolerance: float) -> bool
  
   Determine if this Outline contains the specified point to within a tolerance.
  
   point: The point to test for containment.
   tolerance: The tolerance to use when determining whether the point is contained. Defaults 
    to zero.
  
   Returns: True if this outline contains the given point,or false otherwise.
  """
  pass
 def ContainsOtherOutline(self,otherOutline,tolerance):
  """
  ContainsOtherOutline(self: Outline,otherOutline: Outline,tolerance: float) -> bool
  
   Determine if this Outline contains another Outline to within tolerance.
  
   otherOutline: The outline to test for containment.
   tolerance: The tolerance to use when determining whether the point is contained. Defaults 
    to zero.
  
   Returns: True if this outline contains the given outline,or false otherwise.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Outline) """
  pass
 def GetDiagonalLength(self):
  """
  GetDiagonalLength(self: Outline) -> float
  
   Get the length of outline's diagonal. If called on empty outline,0.
     is 
    returned
  
   Returns: The length of the diagonal.
  """
  pass
 def Intersects(self,outline,tolerance):
  """
  Intersects(self: Outline,outline: Outline,tolerance: float) -> bool
  
   Determine if this Outline intersects the input Outline to within a specified 
    tolerance.
  
  
   outline: The outline to test for intersection with this one.
   tolerance: The tolerance to use when determining intersection. Defaults to zero.
   Returns: True if the given outline intersects this outline.
  """
  pass
 def IsScaleValid(self,scale):
  """
  IsScaleValid(self: Outline,scale: float) -> bool
  
   Checks if given scale is valid. Should be greater than zero.
  
   scale: The scale.
   Returns: True if the scale is valid,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Outline,disposing: bool) """
  pass
 def Scale(self,scale):
  """
  Scale(self: Outline,scale: float)
   Scales the bounding box by given scale.
  
   scale: The scale value. It should be greater than zero.
  """
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
 def __new__(self,*__args):
  """
  __new__(cls: type,minimumPoint: XYZ,maximumPoint: XYZ)
  __new__(cls: type,other: Outline)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if the outline represents an empty outline.

Get: IsEmpty(self: Outline) -> bool

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: Outline) -> bool

"""

 MaximumPoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The maximum point of the bounding box.

Get: MaximumPoint(self: Outline) -> XYZ

Set: MaximumPoint(self: Outline)=value
"""

 MinimumPoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The minimum point of the bounding box.

Get: MinimumPoint(self: Outline) -> XYZ

Set: MinimumPoint(self: Outline)=value
"""


