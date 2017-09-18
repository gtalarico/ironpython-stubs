class PartMaker(Element,IDisposable):
 """
 PartMaker is an element which takes some source elements (e.g.,a wall

    with all its layers) and creates one or more Parts out of it. The logic

    according to which these Parts are created is non-trivial and PartMaker

    uses various PartMakerMethods which represents these logics.

    This element manages the strategy to make Part elements for one or more original elements.
 """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetSourceElementIds(self):
  """
  GetSourceElementIds(self: PartMaker) -> ICollection[LinkElementId]

  

   Get the source elements for the PartMaker.

   Returns: Elements that are the sources for this PartMaker.
  """
  pass
 def IsSourceElement(self,elemId):
  """
  IsSourceElement(self: PartMaker,elemId: ElementId) -> bool

  

   Is the element a source for this PartMaker

   Returns: Returns true if elemId is among the source elements of this PartMaker
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetSourceElementIds(self,sourceElementIds):
  """ SetSourceElementIds(self: PartMaker,sourceElementIds: ICollection[ElementId]) """
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
