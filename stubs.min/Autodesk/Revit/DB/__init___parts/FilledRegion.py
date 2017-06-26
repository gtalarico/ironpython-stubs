class FilledRegion(Element,IDisposable):
 """ A filled region element. """
 @staticmethod
 def Create(document,typeId,viewId,boundaries):
  """ Create(document: Document,typeId: ElementId,viewId: ElementId,boundaries: IList[CurveLoop]) -> FilledRegion """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def GetBoundaries(self):
  """
  GetBoundaries(self: FilledRegion) -> IList[CurveLoop]
  
   Gets the boundaries.
   Returns: The filled region boundaries.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 @staticmethod
 def GetValidLineStyleIdsForFilledRegion(document):
  """
  GetValidLineStyleIdsForFilledRegion(document: Document) -> IList[ElementId]
  
   Gets the line style Ids which are permitted to be assigned to a filled region.
  
   document: The document.
   Returns: The valid line style Ids.
  """
  pass
 @staticmethod
 def IsValidFilledRegionTypeId(document,typeId):
  """
  IsValidFilledRegionTypeId(document: Document,typeId: ElementId) -> bool
  
   Indicates whether the given Id is a valid filled region type Id.
  
   document: The document.
   typeId: The filled region type Id.
   Returns: True if it is a valid filled region type Id,false otherwise.
  """
  pass
 @staticmethod
 def IsValidLineStyleIdForFilledRegion(document,lineStyleId):
  """
  IsValidLineStyleIdForFilledRegion(document: Document,lineStyleId: ElementId) -> bool
  
   Indicates whether the given Id is a valid line style Id.
  
   document: The document.
   lineStyleId: The line style Id.
   Returns: True if it is a valid line style Id,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetLineStyleId(self,lineStyleId):
  """
  SetLineStyleId(self: FilledRegion,lineStyleId: ElementId)
   Sets the line style Id for all boundaries.
  
   lineStyleId: The line style Id.
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
 IsMasking=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the filled region is masking or not.

Get: IsMasking(self: FilledRegion) -> bool

"""


