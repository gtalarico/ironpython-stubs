class ImportInstance(Instance,IDisposable):
 """ An element created during either import or link operation in Autodesk Revit. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetVisibility(self):
  """
  GetVisibility(self: ImportInstance) -> FamilyElementVisibility
  
   Gets the visibility for the import instance in a family document.
   Returns: A copy of visibility settings for the import instance in a family document.
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
  SetVisibility(self: ImportInstance,visibility: FamilyElementVisibility)
   Sets the visibility for the import instance in a family document.
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
 IsLinked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies whether this instance is a linked object rather than imported one.

Get: IsLinked(self: ImportInstance) -> bool

"""


