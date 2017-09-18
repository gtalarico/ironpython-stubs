class StructuralConnectionHandler(Element,IDisposable):
 """ An object of Structural Connection Handler. """
 def AddElementIds(self,elemIds):
  """ AddElementIds(self: StructuralConnectionHandler,elemIds: IList[ElementId]) """
  pass
 @staticmethod
 def Create(document,idsToConnect,typeId=None):
  """
  Create(document: Document,idsToConnect: IList[ElementId]) -> StructuralConnectionHandler

  Create(document: Document,idsToConnect: IList[ElementId],typeId: ElementId) -> StructuralConnectionHandler
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetConnectedElementIds(self):
  """
  GetConnectedElementIds(self: StructuralConnectionHandler) -> IList[ElementId]

  

   Retrieves list of element ids of connected elements.

   Returns: Returns connected element ids.
  """
  pass
 def GetOrigin(self):
  """
  GetOrigin(self: StructuralConnectionHandler) -> XYZ

  

   Retrieves origin point of Structural Connection Handler element.

   Returns: The origin point of element.
  """
  pass
 def IsDetailed(self):
  """
  IsDetailed(self: StructuralConnectionHandler) -> bool

  

   Checks if Structural Connection Handler has the detailed connection style.

   Returns: True if Structural Connection Handler has the detailed connection style.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def RemoveElementIds(self,elemIds):
  """ RemoveElementIds(self: StructuralConnectionHandler,elemIds: IList[ElementId]) """
  pass
 def SetDefaultPrimaryElement(self):
  """
  SetDefaultPrimaryElement(self: StructuralConnectionHandler)

   Sets primary element in connection according to structural categories,element 

    materials and geometries.

     The steel element is set rather than an element 

    of other material.

     The priorities of the elements are set according 

    structural categories in following order: columns,framings,walls,

    foundations,floors.

     In case of several Structural Framing elements order 

    is determined by cutting - the cutting element is set as the primary one rather 

    than element being cut.
  """
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
 ApprovalTypeId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves or changes approval type of the Structural Connection Handler.



Get: ApprovalTypeId(self: StructuralConnectionHandler) -> ElementId



Set: ApprovalTypeId(self: StructuralConnectionHandler)=value

"""

 CodeCheckingStatus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Code checking status of the structural connection.



Get: CodeCheckingStatus(self: StructuralConnectionHandler) -> StructuralConnectionCodeCheckingStatus



Set: CodeCheckingStatus(self: StructuralConnectionHandler)=value

"""

 SingleElementEndIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Element end index for single element connections (0: start,1: end).



Get: SingleElementEndIndex(self: StructuralConnectionHandler) -> int



Set: SingleElementEndIndex(self: StructuralConnectionHandler)=value

"""


