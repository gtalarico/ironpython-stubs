class ModelText(Element,IDisposable):
 """ A model text element in an Autodesk Revit family document. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetVisibility(self):
  """
  GetVisibility(self: ModelText) -> FamilyElementVisibility
  
   Gets the visibility for the model text in a family document.
   Returns: A copy of visibility settings for the model text in a family document.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetVisibility(self,visibility):
  """
  SetVisibility(self: ModelText,visibility: FamilyElementVisibility)
   Sets the visibility for the model text in a family document.
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
 Depth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The depth of the model text.

Get: Depth(self: ModelText) -> float

Set: Depth(self: ModelText)=value
"""

 HorizontalAlignment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The horizontal alignment.

Get: HorizontalAlignment(self: ModelText) -> HorizontalAlign

Set: HorizontalAlignment(self: ModelText)=value
"""

 Location=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is used to find the physical location of an instance within project.

Get: Location(self: ModelText) -> Location

"""

 ModelTextType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type for the model text.

Get: ModelTextType(self: ModelText) -> ModelTextType

Set: ModelTextType(self: ModelText)=value
"""

 Subcategory=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The subcategory.

Get: Subcategory(self: ModelText) -> Category

Set: Subcategory(self: ModelText)=value
"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The text string in the model text.

Get: Text(self: ModelText) -> str

Set: Text(self: ModelText)=value
"""


