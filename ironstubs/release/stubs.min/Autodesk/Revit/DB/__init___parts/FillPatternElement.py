class FillPatternElement(Element,IDisposable):
 """ An element that represents a fill pattern. """
 @staticmethod
 def Create(document,fillPattern):
  """
  Create(document: Document,fillPattern: FillPattern) -> FillPatternElement
  
   Creates a new FillPatternElement.
  
   document: The document in which to create the FillPatternElement.
   fillPattern: The FillPattern associated to the newly created FillPatternElement.
   Returns: The newly created FillPatternElement.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetFillPattern(self):
  """
  GetFillPattern(self: FillPatternElement) -> FillPattern
  
   Gets the FillPattern associated to this element.
   Returns: A copy of FillPattern object.
  """
  pass
 @staticmethod
 def GetFillPatternElementByName(document,target,name):
  """
  GetFillPatternElementByName(document: Document,target: FillPatternTarget,name: str) -> FillPatternElement
  
   Retrieves the FillPatternElement by its name.
  
   document: The document in which to retrieve the FillPatternElement.
   target: The FillPatternTarget of the FillPatternElement.
   name: The name of the FillPatternElement.
   Returns: The FillPatternElement.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetFillPattern(self,newFillPattern):
  """
  SetFillPattern(self: FillPatternElement,newFillPattern: FillPattern)
   Sets the FillPattern associated to this element.
  
   newFillPattern: The new FillPattern object.
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
