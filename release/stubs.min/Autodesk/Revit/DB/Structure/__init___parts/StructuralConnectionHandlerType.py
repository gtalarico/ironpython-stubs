class StructuralConnectionHandlerType(ElementType,IDisposable):
 """ A StructuralConnectionHandlerType is used in StructuralConnectionHandler element generation. """
 @staticmethod
 def Create(pADoc,name,guid,familyName):
  """
  Create(pADoc: Document,name: str,guid: Guid,familyName: str) -> StructuralConnectionHandlerType
  
   Creates a new StructuralConnectionHandlerType object.
  
   pADoc: The document.
   name: The type name.
   guid: Connection GUID.
   familyName: Name of system family which created type will belong to.
   Returns: The newly created instance.
  """
  pass
 @staticmethod
 def CreateDefaultStructuralConnectionHandlerType(pADoc):
  """
  CreateDefaultStructuralConnectionHandlerType(pADoc: Document) -> ElementId
  
   Creates a new StructuralConnectionHandlerType object with a default name.
  
   pADoc: The document.
   Returns: The newly created type id.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 @staticmethod
 def GetDefaultConnectionHandlerType(pADoc):
  """
  GetDefaultConnectionHandlerType(pADoc: Document) -> ElementId
  
   Gets a default type id for Structural Connection.
  
   pADoc: The document.
   Returns: The type id.
  """
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
 ConnectionGuid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The GUID to use for identifying connection geometry generation algorithm.

Get: ConnectionGuid(self: StructuralConnectionHandlerType) -> Guid

"""


