class Connector(object,IConnector,IDisposable):
 """ A connector in an Autodesk Revit MEP project document. """
 def ConnectTo(self,connector):
  """
  ConnectTo(self: Connector,connector: Connector)
   Make connection between two connectors.
  
   connector: Indicate the connector will be connected to.
  """
  pass
 def DisconnectFrom(self,connector):
  """
  DisconnectFrom(self: Connector,connector: Connector)
   Remove connection between two connectors.
  
   connector: Indicate the connector,connection will be removed from.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Connector) """
  pass
 def GetFabricationConnectorInfo(self):
  """
  GetFabricationConnectorInfo(self: Connector) -> FabricationConnectorInfo
  
   Gets fabrication connectivity information.
   Returns: Returns ll if there is no fabrication connector information associated.
  """
  pass
 def GetMEPConnectorInfo(self):
  """
  GetMEPConnectorInfo(self: Connector) -> MEPConnectorInfo
  
   Gets MEP connector information.
   Returns: Returns ll if there is no MEP connector information associated.
  """
  pass
 def IsConnectedTo(self,connector):
  """
  IsConnectedTo(self: Connector,connector: Connector) -> bool
  
   Identifies if the connector is connected to the specified connector.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Connector,disposing: bool) """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 AllowsSlopeAdjustments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the connector allows the slope adjustment.

Get: AllowsSlopeAdjustments(self: Connector) -> bool

"""

 AllRefs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """All references of the connector.

Get: AllRefs(self: Connector) -> ConnectorSet

"""

 Angle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The angle of the Connector.

Get: Angle(self: Connector) -> float

Set: Angle(self: Connector)=value
"""

 AssignedDuctFlowConfiguration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The assigned duct flow configuration of the connector.

Get: AssignedDuctFlowConfiguration(self: Connector) -> DuctFlowConfigurationType

"""

 AssignedDuctLossMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The duct loss method of the connector.

Get: AssignedDuctLossMethod(self: Connector) -> DuctLossMethodType

"""

 AssignedFixtureUnits=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The assigned fixture units of the connector.

Get: AssignedFixtureUnits(self: Connector) -> float

Set: AssignedFixtureUnits(self: Connector)=value
"""

 AssignedFlow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The assigned flow of the connector.

Get: AssignedFlow(self: Connector) -> float

Set: AssignedFlow(self: Connector)=value
"""

 AssignedFlowDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The assigned flow direction of the connector.

Get: AssignedFlowDirection(self: Connector) -> FlowDirectionType

"""

 AssignedFlowFactor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The assigned flow factor of this connector.

Get: AssignedFlowFactor(self: Connector) -> float

Set: AssignedFlowFactor(self: Connector)=value
"""

 AssignedKCoefficient=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The assigned kCoefficient of the connector.

Get: AssignedKCoefficient(self: Connector) -> float

Set: AssignedKCoefficient(self: Connector)=value
"""

 AssignedLossCoefficient=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The assigned loss coefficient of the connector.

Get: AssignedLossCoefficient(self: Connector) -> float

Set: AssignedLossCoefficient(self: Connector)=value
"""

 AssignedPipeFlowConfiguration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The pipe flow configuration type of the connector.

Get: AssignedPipeFlowConfiguration(self: Connector) -> PipeFlowConfigurationType

"""

 AssignedPipeLossMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The pipe loss method of the connector.

Get: AssignedPipeLossMethod(self: Connector) -> PipeLossMethodType

"""

 AssignedPressureDrop=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The assigned pressure drop of the connector.

Get: AssignedPressureDrop(self: Connector) -> float

Set: AssignedPressureDrop(self: Connector)=value
"""

 Coefficient=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The coefficient of the connector.

Get: Coefficient(self: Connector) -> float

"""

 ConnectorManager=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The connector manager of the connector.

Get: ConnectorManager(self: Connector) -> ConnectorManager

"""

 ConnectorType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The connector type of the connector.

Get: ConnectorType(self: Connector) -> ConnectorType

"""

 CoordinateSystem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The coordinate system of the connector.

Get: CoordinateSystem(self: Connector) -> Transform

"""

 Demand=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The demand of the connector.

Get: Demand(self: Connector) -> float

"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The description.

Get: Description(self: Connector) -> str

"""

 Direction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The direction of the connector.

Get: Direction(self: Connector) -> FlowDirectionType

"""

 Domain=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The domain of the connector.

Get: Domain(self: Connector) -> Domain

"""

 DuctSystemType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The duct system type of the connector.

Get: DuctSystemType(self: Connector) -> DuctSystemType

"""

 ElectricalSystemType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The electrical system type of the connector.

Get: ElectricalSystemType(self: Connector) -> ElectricalSystemType

"""

 EngagementLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Connector engagement length

Get: EngagementLength(self: Connector) -> float

"""

 Flow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The flow of the connector.

Get: Flow(self: Connector) -> float

"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The height of the connector.

Get: Height(self: Connector) -> float

Set: Height(self: Connector)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A unique identifier to identify this connector.

Get: Id(self: Connector) -> int

"""

 IsConnected=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if the connector is physically connected to a connector on another element.

Get: IsConnected(self: Connector) -> bool

"""

 IsMovable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """whether the connector can be moved.

Get: IsMovable(self: Connector) -> bool

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: Connector) -> bool

"""

 MEPSystem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The system of the connector belong to.

Get: MEPSystem(self: Connector) -> MEPSystem

"""

 Origin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The location of the connector.

Get: Origin(self: Connector) -> XYZ

Set: Origin(self: Connector)=value
"""

 Owner=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The host of the connector.

Get: Owner(self: Connector) -> Element

"""

 PipeSystemType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The pipe system type of the connector.

Get: PipeSystemType(self: Connector) -> PipeSystemType

"""

 PressureDrop=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The pressure drop of the connector.

Get: PressureDrop(self: Connector) -> float

"""

 Radius=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The radius of the connector.

Get: Radius(self: Connector) -> float

Set: Radius(self: Connector)=value
"""

 Shape=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The shape of the connector.

Get: Shape(self: Connector) -> ConnectorProfileType

"""

 Utility=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the connector is a utility connector.

Get: Utility(self: Connector) -> bool

"""

 VelocityPressure=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The velocity pressure of the connector.

Get: VelocityPressure(self: Connector) -> float

"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The width of the connector.

Get: Width(self: Connector) -> float

Set: Width(self: Connector)=value
"""


