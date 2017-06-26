class LinePatternElement(Element,IDisposable):
 """ An element that represents a line pattern. """
 @staticmethod
 def Create(document,linePattern):
  """
  Create(document: Document,linePattern: LinePattern) -> LinePatternElement
  
   Creates a new LinePatternElement.
  
   document: The document in which to create the LinePatternElement.
   linePattern: The LinePattern associated to the newly created LinePatternElement.
   Returns: The newly created LinePatternElement.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 @staticmethod
 def GetLinePattern(document=None,elementId=None):
  """
  GetLinePattern(self: LinePatternElement) -> LinePattern
  
   Gets the LinePattern associated to this element.
   Returns: A copy of LinePattern object.
  GetLinePattern(document: Document,elementId: ElementId) -> LinePattern
  
   Gets the LinePattern associated to an element or from a built-in line pattern.
  
   document: The document in which to retrieve the LinePattern.
   elementId: The ElementId of the LinePatternElement or the built-in line pattern id.
   Returns: A copy of LinePattern object. ll if the ElementId doesn't represent a line 
    pattern element
     or built-in line pattern. ll for Solid.
  """
  pass
 @staticmethod
 def GetLinePatternElementByName(document,name):
  """
  GetLinePatternElementByName(document: Document,name: str) -> LinePatternElement
  
   Retrieves the LinePatternElement by its name.
  
   document: The document in which to retrieve the LinePatternElement.
   name: The name of the LinePatternElement.
   Returns: The LinePatternElement.
  """
  pass
 @staticmethod
 def GetSolidPatternId():
  """
  GetSolidPatternId() -> ElementId
  
   Gets the solid line pattern element id.
   Returns: The element id of the solid line pattern.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetLinePattern(self,newLinePattern):
  """
  SetLinePattern(self: LinePatternElement,newLinePattern: LinePattern)
   Sets the LinePattern associated to this element.
  
   newLinePattern: The new LinePattern object.
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
