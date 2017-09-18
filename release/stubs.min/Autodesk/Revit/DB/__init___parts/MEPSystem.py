class MEPSystem(Element,IDisposable):
 """ A system in the Autodesk Revit MEP product. """
 def Add(self,connectors):
  """
  Add(self: MEPSystem,connectors: ConnectorSet)
   Add elements into the system and connect them with the system using given 
    connectors.
  
  
   connectors: Connectors which are used to connect with the system.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def DivideSystem(self,ADoc):
  """
  DivideSystem(self: MEPSystem,ADoc: Document) -> ICollection[ElementId]
  
   Divide the phyisical networks in the system and create a new system for each 
    network.
  
  
   ADoc: The document.
   Returns: The id of new created systems.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetCriticalPathSectionNumbers(self):
  """
  GetCriticalPathSectionNumbers(self: MEPSystem) -> IList[int]
  
   Obtains a list of the critical path section numbers.
   Returns: The section numbers.
  """
  pass
 def getElementsInNetwork(self,*args):
  """ getElementsInNetwork(self: MEPSystem) -> ElementSet """
  pass
 def getFlow(self,*args):
  """ getFlow(self: MEPSystem,param: BuiltInParameter) -> float """
  pass
 def GetPhysicalNetworksNumber(self):
  """
  GetPhysicalNetworksNumber(self: MEPSystem) -> int
  
   Get the physical networks number in the system.
   Returns: The number of physical networks.
  """
  pass
 def GetSectionByIndex(self,index):
  """
  GetSectionByIndex(self: MEPSystem,index: int) -> MEPSection
  
   Get the section from the index.
  
   index: The index of the section in the system.
   Returns: The section.
  """
  pass
 def GetSectionByNumber(self,sectionNumber):
  """
  GetSectionByNumber(self: MEPSystem,sectionNumber: int) -> MEPSection
  
   Get the Section from section number
  
   sectionNumber: The Section number.
   Returns: The section. ll if the no section exists for the input section number.
  """
  pass
 def getStaticPressure(self,*args):
  """ getStaticPressure(self: MEPSystem,param: BuiltInParameter) -> float """
  pass
 def IsSystemDividable(self):
  """
  IsSystemDividable(self: MEPSystem) -> bool
  
   Checks if the system is dividable. The system is dividable if there is more 
    than one physical network in the system. Currently,only HVAC and piping 
    systems support dividing.
  
   Returns: True if the system can be divided.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def Remove(self,*__args):
  """
  Remove(self: MEPSystem,connectors: ConnectorSet)
   Removes connectors from system.
  
   connectors: The connectors to be removed from the system.
  Remove(self: MEPSystem,elementIds: ICollection[ElementId])
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
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
 BaseEquipment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The base panel or equipment of the system.

Get: BaseEquipment(self: MEPSystem) -> FamilyInstance

"""

 BaseEquipmentConnector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The connector within base equipment which is used to connect with system.

Get: BaseEquipmentConnector(self: MEPSystem) -> Connector

"""

 ConnectorManager=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Connector manager of the system.

Get: ConnectorManager(self: MEPSystem) -> ConnectorManager

"""

 Elements=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Terminal elements in the system.

Get: Elements(self: MEPSystem) -> ElementSet

"""

 HasDesignParts=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the system has one or more design parts.

Get: HasDesignParts(self: MEPSystem) -> bool

"""

 HasFabricationParts=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the system has one or more fabrication parts.

Get: HasFabricationParts(self: MEPSystem) -> bool

"""

 HasPlaceholders=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the system has one or more placeholders.

Get: HasPlaceholders(self: MEPSystem) -> bool

"""

 IsEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the system is empty or not.

Get: IsEmpty(self: MEPSystem) -> bool

"""

 IsMultipleNetwork=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the system is well connected or not. The flag will enable the "Divide System" button.

Get: IsMultipleNetwork(self: MEPSystem) -> bool

"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the system is valid or not.
   atom AtomValidateSystem
   default false

Get: IsValid(self: MEPSystem) -> bool

"""

 PressureLossOfCriticalPath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The total pressure loss of the sections in critical path.

Get: PressureLossOfCriticalPath(self: MEPSystem) -> float

"""

 SectionsCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of sections.

Get: SectionsCount(self: MEPSystem) -> int

"""


