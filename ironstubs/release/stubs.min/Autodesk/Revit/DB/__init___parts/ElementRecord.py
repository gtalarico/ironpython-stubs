class ElementRecord(object,IDisposable):
 """ A record in the Revit database representing an element. """
 def Dispose(self):
  """ Dispose(self: ElementRecord) """
  pass
 def GetBoundingBox(self):
  """
  GetBoundingBox(self: ElementRecord) -> Outline
  
   Gets the bounding box of the element record.
   Returns: The bounding box outline. ll if there is no bounding box for this element.
  """
  pass
 def GetCategoryId(self):
  """
  GetCategoryId(self: ElementRecord) -> ElementId
  
   Gets the category id of the element record.
   Returns: The category id.
  """
  pass
 def GetDesignOptionId(self):
  """
  GetDesignOptionId(self: ElementRecord) -> ElementId
  
   Gets the design option id of the element record.
   Returns: The design option id.
  """
  pass
 def GetId(self):
  """
  GetId(self: ElementRecord) -> ElementId
  
   Gets the id of the element record.
   Returns: The element id.
  """
  pass
 def GetOwnerViewId(self):
  """
  GetOwnerViewId(self: ElementRecord) -> ElementId
  
   Gets the element id of the owner view record.
   Returns: The view record element id.
  """
  pass
 def HasBoundingBox(self):
  """
  HasBoundingBox(self: ElementRecord) -> bool
  
   Determines whether this element record has a bounding box.
   Returns: True if the element record has a bounding box or false otherwise.
  """
  pass
 def IsAnElementType(self):
  """
  IsAnElementType(self: ElementRecord) -> bool
  
   Identifies if the element record represents an ElementType.
   Returns: True if the element record represents an ElementType.
  """
  pass
 def IsCurveDriven(self):
  """
  IsCurveDriven(self: ElementRecord) -> bool
  
   Identifies if the element is curve driven.
   Returns: True if the element is curve driven.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ElementRecord,disposing: bool) """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ElementRecord) -> bool

"""

 WorksetId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get Id of the workset which owns the element.

Get: WorksetId(self: ElementRecord) -> WorksetId

"""


