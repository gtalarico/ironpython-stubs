class ElectricalSetting(Element,IDisposable):
 """ The ElectricalSetting class represents an instance of element of electrical settings. """
 def AddDistributionSysType(self,name,phase,phaseConfig,numWire,volLineToLine,volLineToGround):
  """
  AddDistributionSysType(self: ElectricalSetting,name: str,phase: ElectricalPhase,phaseConfig: ElectricalPhaseConfiguration,numWire: int,volLineToLine: VoltageType,volLineToGround: VoltageType) -> DistributionSysType

  

   Add a new distribution system type to project.

  

   name: The name of new added distribution system type

   phase: Single or three phase this type is

   phaseConfig: Configuration property of given phase

   numWire: Wire number of this distribution system

   volLineToLine: Type of line to line voltage in this system

   volLineToGround: Type of line to ground voltage in this system

   Returns: New added distribution system type object.
  """
  pass
 def AddVoltageType(self,name,actualValue,minValue,maxValue):
  """
  AddVoltageType(self: ElectricalSetting,name: str,actualValue: float,minValue: float,maxValue: float) -> VoltageType

  

   Add a new type definition of voltage into project.

  

   name: Specify voltage type name

   actualValue: Specify actual value of voltage type.

   minValue: Specify acceptable minimum value of the voltage type.

   maxValue: Specify acceptable maximum value of the voltage type.

   Returns: New added voltage type object.
  """
  pass
 def AddWireMaterialType(self,name,baseMaterial):
  """
  AddWireMaterialType(self: ElectricalSetting,name: str,baseMaterial: WireMaterialType) -> WireMaterialType

  

   Add a new type of wire material.

  

   name: Name of new material type.

   baseMaterial: Specify an existing material type which New material will be constructed based 

    on.

  

   Returns: New added wire material type object.
  """
  pass
 def AddWireType(self,name,materialType,temperatureRating,insulation,maxSize,neutralMultiplier,neutralRequired,neutralMode,conduit):
  """
  AddWireType(self: ElectricalSetting,name: str,materialType: WireMaterialType,temperatureRating: TemperatureRatingType,insulation: InsulationType,maxSize: WireSize,neutralMultiplier: float,neutralRequired: bool,neutralMode: NeutralMode,conduit: WireConduitType) -> WireType

  

   Add a new wire type to project.

  

   name: Name of the new wire type.

   materialType: Wire material of new wire type.

   temperatureRating: Temperature rating type information of new wire type.

   insulation: Insulation of new wire type.

   maxSize: Max wire size of new wire type.

   neutralMultiplier: Neutral multiplier of new wire type.

   neutralRequired: Specify whether neutral point is required.

   neutralMode: Specify neutral mode.

   conduit: Conduit type of new wire type.

   Returns: New added wire type object.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 @staticmethod
 def GetElectricalSettings(document):
  """
  GetElectricalSettings(document: Document) -> ElectricalSetting

  

   Get the electrical settings of the project.

  

   document: The document.

   Returns: The electrical settings of the project.
  """
  pass
 def GetSpecificFittingAngles(self):
  """
  GetSpecificFittingAngles(self: ElectricalSetting) -> IList[float]

  

   Gets the list of specific fitting angles.

   Returns: Angles (in degrees).
  """
  pass
 def GetSpecificFittingAngleStatus(self,angle):
  """
  GetSpecificFittingAngleStatus(self: ElectricalSetting,angle: float) -> bool

  

   Gets the status of given specific fitting angle.

  

   angle: The specific fitting angle (in degree) that must be one of 90,60,45,30,22.5 

    or 11.25 degrees.
  """
  pass
 def IsValidSpecificFittingAngle(self,angle):
  """
  IsValidSpecificFittingAngle(self: ElectricalSetting,angle: float) -> bool

  

   Checks that the given value is a valid specific fitting angle. The specific 

    fitting angles are angles of 90,60,45,30,22.5 or 11.25 degrees.

  

  

   angle: The angle value (in degree).

   Returns: True if the given value is a valid specific fitting angle.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def RemoveDistributionSysType(self,distributionSysType):
  """
  RemoveDistributionSysType(self: ElectricalSetting,distributionSysType: DistributionSysType)

   Remove an existing distribution system type from the project.
  """
  pass
 def RemoveVoltageType(self,voltageType):
  """
  RemoveVoltageType(self: ElectricalSetting,voltageType: VoltageType)

   Remove the voltage type from project.

  

   voltageType: Specify the voltage type to be removed.
  """
  pass
 def RemoveWireMaterialType(self,materialType):
  """
  RemoveWireMaterialType(self: ElectricalSetting,materialType: WireMaterialType)

   Remove the wire material type from project.

  

   materialType: The wire material type to be removed.
  """
  pass
 def RemoveWireType(self,wireType):
  """
  RemoveWireType(self: ElectricalSetting,wireType: WireType)

   Remove wire type definition from project.
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetSpecificFittingAngleStatus(self,angle,bStatus):
  """
  SetSpecificFittingAngleStatus(self: ElectricalSetting,angle: float,bStatus: bool)

   Sets the status of given specific angle.

  

   angle: The specific angle (in degree) that must be 60,45,30,22.5 or 11.25 degrees.

   bStatus: Status,true - using the given angle during the pipe layout.
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
 CircuitLoadCalculationMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The method to calculate circuit load



Get: CircuitLoadCalculationMethod(self: ElectricalSetting) -> CircuitLoadCalculationMethod



Set: CircuitLoadCalculationMethod(self: ElectricalSetting)=value

"""

 CircuitNamePhaseA=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Circuit Naming by Phase - Phase A Label.



Get: CircuitNamePhaseA(self: ElectricalSetting) -> str



Set: CircuitNamePhaseA(self: ElectricalSetting)=value

"""

 CircuitNamePhaseB=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Circuit Naming by Phase - Phase B Label.



Get: CircuitNamePhaseB(self: ElectricalSetting) -> str



Set: CircuitNamePhaseB(self: ElectricalSetting)=value

"""

 CircuitNamePhaseC=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Circuit Naming by Phase - Phase C Label.



Get: CircuitNamePhaseC(self: ElectricalSetting) -> str



Set: CircuitNamePhaseC(self: ElectricalSetting)=value

"""

 CircuitRating=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The default circuit rating for newly created circuit.



Get: CircuitRating(self: ElectricalSetting) -> float



Set: CircuitRating(self: ElectricalSetting)=value

"""

 CircuitSequence=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The sequence in which power circuits are created.



Get: CircuitSequence(self: ElectricalSetting) -> CircuitSequence



Set: CircuitSequence(self: ElectricalSetting)=value

"""

 DistributionSysTypes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get all distribution system types of the project.



Get: DistributionSysTypes(self: ElectricalSetting) -> DistributionSysTypeSet



"""

 VoltageTypes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get all voltage type definitions information of the project.



Get: VoltageTypes(self: ElectricalSetting) -> VoltageTypeSet



"""

 WireConduitTypes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get electrical conduit types information of the project.



Get: WireConduitTypes(self: ElectricalSetting) -> WireConduitTypeSet



"""

 WireMaterialTypes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get electrical wire material types information of the project.



Get: WireMaterialTypes(self: ElectricalSetting) -> WireMaterialTypeSet



"""

 WireTypes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get all wire type definition information of the project.



Get: WireTypes(self: ElectricalSetting) -> WireTypeSet



"""


