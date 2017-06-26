class ConnectorElement(Element,IDisposable,IConnector):
 """ A base class that provides support for all connector elements occurring in families. """
 def AssignAsPrimary(self):
  """
  AssignAsPrimary(self: ConnectorElement)
   Assign a connector as a primary connector.
  """
  pass
 @staticmethod
 def CreateCableTrayConnector(document,planarFace,edge=None):
  """
  CreateCableTrayConnector(document: Document,planarFace: Reference) -> ConnectorElement
  
   Create a new cable tray ConnectorElement.
  
   document: The document to add the connector to.
   planarFace: The planar face to place the connector on.
   Returns: The cable tray ConnectorElement.
  CreateCableTrayConnector(document: Document,planarFace: Reference,edge: Edge) -> ConnectorElement
  
   Create a new cable tray ConnectorElement.
  
   document: The document to add the connector to.
   planarFace: The planar face to place the connector on.
   edge: One of the edges in the edge loop that defines the connector location on the 
    planar face.
  
   Returns: The cable tray ConnectorElement.
  """
  pass
 @staticmethod
 def CreateConduitConnector(document,planarFace,edge=None):
  """
  CreateConduitConnector(document: Document,planarFace: Reference) -> ConnectorElement
  
   Create a new conduit ConnectorElement.
  
   document: The document to add the connector to.
   planarFace: The planar face to place the connector on.
   Returns: The conduit ConnectorElement.
  CreateConduitConnector(document: Document,planarFace: Reference,edge: Edge) -> ConnectorElement
  
   Create a new conduit ConnectorElement.
  
   document: The document to add the connector to.
   planarFace: The planar face to place the connector on.
   edge: One of the edges in the edge loop that defines the connector location on the 
    planar face.
  
   Returns: The conduit ConnectorElement.
  """
  pass
 @staticmethod
 def CreateDuctConnector(document,ductSystemType,profileShape,planarFace,edge=None):
  """
  CreateDuctConnector(document: Document,ductSystemType: DuctSystemType,profileShape: ConnectorProfileType,planarFace: Reference) -> ConnectorElement
  
   Create a new duct ConnectorElement.
  
   document: The document to add the connector to.
   ductSystemType: The DuctSystemType of the connector.
   profileShape: The profile shape of the duct.
   planarFace: The planar face to place the connector on.
   Returns: The duct ConnectorElement.
  CreateDuctConnector(document: Document,ductSystemType: DuctSystemType,profileShape: ConnectorProfileType,planarFace: Reference,edge: Edge) -> ConnectorElement
  
   Create a new duct ConnectorElement.
  
   document: The document to add the connector to.
   ductSystemType: The DuctSystemType of the connector.
   profileShape: The profile shape of the duct.
   planarFace: The planar face to place the connector on.
   edge: One of the edges in the edge loop that defines the connector location on the 
    planar face.
  
   Returns: The duct ConnectorElement.
  """
  pass
 @staticmethod
 def CreateElectricalConnector(document,electricalSystemType,planarFace,edge=None):
  """
  CreateElectricalConnector(document: Document,electricalSystemType: ElectricalSystemType,planarFace: Reference) -> ConnectorElement
  
   Create a new electrical ConnectorElement.
  
   document: The document to add the connector to.
   electricalSystemType: The ElectricalSystemTYpe of the connector.
   planarFace: The planar face to place the connector on.
   Returns: The electrical ConnectorElement.
  CreateElectricalConnector(document: Document,electricalSystemType: ElectricalSystemType,planarFace: Reference,edge: Edge) -> ConnectorElement
  
   Create a new electrical ConnectorElement.
  
   document: The document to add the connector to.
   electricalSystemType: The ElectricalSystemTYpe of the connector.
   planarFace: The planar face to place the connector on.
   edge: One of the edges in the edge loop that defines the connector location on the 
    planar face.
  
   Returns: The electrical ConnectorElement.
  """
  pass
 @staticmethod
 def CreatePipeConnector(document,pipeSystemType,planarFace,edge=None):
  """
  CreatePipeConnector(document: Document,pipeSystemType: PipeSystemType,planarFace: Reference) -> ConnectorElement
  
   Create a new pipe ConnectorElement.
  
   document: The document to add the connector to.
   pipeSystemType: The PipeSystemType of the connector.
   planarFace: The planar face to place the connector on.
   Returns: The pipe ConnectorElement.
  CreatePipeConnector(document: Document,pipeSystemType: PipeSystemType,planarFace: Reference,edge: Edge) -> ConnectorElement
  
   Create a new pipe ConnectorElement with a face and an edge.
  
   document: The document to add the connector to.
   pipeSystemType: The PipeSystemType of the connector.
   planarFace: The planar face to place the connector on.
   edge: One of the edges in the edge loop that defines the connector location on the 
    planar face.
  
   Returns: The pipe ConnectorElement.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def FlipDirection(self):
  """
  FlipDirection(self: ConnectorElement)
   Reverses the direction of the connector element.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetLinkedConnectorElement(self):
  """
  GetLinkedConnectorElement(self: ConnectorElement) -> ConnectorElement
  
   Get the linked connector element.
   Returns: The linked connector element.  If ll,the connector has no link.
  """
  pass
 def IsSystemClassificationValid(self,systemClassification):
  """
  IsSystemClassificationValid(self: ConnectorElement,systemClassification: MEPSystemClassification) -> bool
  
   Checks that the MEPSystemType is valid for the domain of connector.
  
   systemClassification: The MEPSystemType to be validated.
   Returns: True if the MEPSystemType is valid for the domain of the connector,false 
    otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetLinkedConnectorElement(self,otherConnector):
  """
  SetLinkedConnectorElement(self: ConnectorElement,otherConnector: ConnectorElement)
   Set the linked connector element.
  
   otherConnector: The connector to link to.
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
 CoordinateSystem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The coordinate system of the connector.

Get: CoordinateSystem(self: ConnectorElement) -> Transform

"""

 Direction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the direction of the connector element.

Get: Direction(self: ConnectorElement) -> XYZ

"""

 Domain=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The domain of the connector.

Get: Domain(self: ConnectorElement) -> Domain

"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The height of the connector.

Get: Height(self: ConnectorElement) -> float

"""

 IsPrimary=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if this is the primary connector in the family.

Get: IsPrimary(self: ConnectorElement) -> bool

"""

 Origin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The location of the connector in family document.

Get: Origin(self: ConnectorElement) -> XYZ

"""

 Radius=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The radius of the connector.

Get: Radius(self: ConnectorElement) -> float

"""

 Shape=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The shape of the connector.

Get: Shape(self: ConnectorElement) -> ConnectorProfileType

"""

 SystemClassification=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The system classification of the connector.

Get: SystemClassification(self: ConnectorElement) -> MEPSystemClassification

Set: SystemClassification(self: ConnectorElement)=value
"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The width of the connector.

Get: Width(self: ConnectorElement) -> float

"""


