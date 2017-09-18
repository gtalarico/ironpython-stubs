class BuildingPadType(HostObjAttributes,IDisposable):
 """ Represents a specific type of Building Pad. """
 @staticmethod
 def CreateDefault(document):
  """
  CreateDefault(document: Document) -> BuildingPadType
  
   Creates a BuildingPadType element and adds it to the document.
  
   document: The document to be modified.
   Returns: The new BuildingPadType element.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
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
 ThermalProperties=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The calculated and settable thermal properties of the BuildingPadType

Get: ThermalProperties(self: BuildingPadType) -> ThermalProperties

"""


