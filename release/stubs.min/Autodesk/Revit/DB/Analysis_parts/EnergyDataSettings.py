class EnergyDataSettings(Element,IDisposable):
 """
 This element contains settings for gbXML Export and Heating and Cooling Load Calculations

    and project level settings for Conceptual Energy Analysis.

    for serialization
 """
 @staticmethod
 def CheckAnalysisType(analysisType):
  """
  CheckAnalysisType(analysisType: AnalysisMode) -> bool

  

   Checks that the analysis type falls within an appropriate range.

  

   analysisType: The analysis type to be checked.

   Returns: True if the analysis type falls within an appropriate range,false otherwise.
  """
  pass
 @staticmethod
 def CheckBuildingConstructionClass(buildingConstructionClass):
  """
  CheckBuildingConstructionClass(buildingConstructionClass: HVACLoadConstructionClass) -> bool

  

   Checks that the building construction class falls within an appropriate range.

  

   buildingConstructionClass: The building construction class to be checked.

   Returns: True if the building construction class falls within an appropriate range,

    false otherwise.
  """
  pass
 @staticmethod
 def CheckBuildingEnvelope(determinationMethod):
  """
  CheckBuildingEnvelope(determinationMethod: gbXMLExportBuildingEnvelope) -> bool

  

   Checks that the building envelope determination method falls within an 

    appropriate range.

  

  

   determinationMethod: The building envelope determination method to be checked.

   Returns: True if the building envelope determination method falls within an appropriate 

    range,false otherwise.
  """
  pass
 @staticmethod
 def CheckBuildingHVACSystem(buildingHVACSystem):
  """
  CheckBuildingHVACSystem(buildingHVACSystem: gbXMLBuildingHVACSystem) -> bool

  

   Checks that the building HVAC system falls within an appropriate range.

  

   buildingHVACSystem: The building HVAC system to be checked.

   Returns: True if the building HVAC system falls within an appropriate range,false 

    otherwise.
  """
  pass
 @staticmethod
 def CheckBuildingOperatingSchedule(buildingOperatingSchedule):
  """
  CheckBuildingOperatingSchedule(buildingOperatingSchedule: gbXMLBuildingOperatingSchedule) -> bool

  

   Checks that the building operating schedule falls within an appropriate range.

  

   buildingOperatingSchedule: The building operating schedule to be checked.

   Returns: True if the building operating schedule falls within an appropriate range,

    false otherwise.
  """
  pass
 @staticmethod
 def CheckBuildingType(buildingType):
  """
  CheckBuildingType(buildingType: gbXMLBuildingType) -> bool

  

   Checks that the building type falls within an appropriate range.

  

   buildingType: The building type to be checked.

   Returns: True if the building type falls within an appropriate range,false otherwise.
  """
  pass
 def CheckConstructionSetElement(self,constructionSetElementId):
  """
  CheckConstructionSetElement(self: EnergyDataSettings,constructionSetElementId: ElementId) -> bool

  

   Checks that the construction set ElementId is acceptable.

  

   constructionSetElementId: The construction set ElementId to be checked.

   Returns: True if the construction set ElementId is a valid construction set element,

    false otherwise.
  """
  pass
 @staticmethod
 def CheckExportCategory(exportCategoryId):
  """
  CheckExportCategory(exportCategoryId: ElementId) -> bool

  

   Checks whether the export category falls within the list:

     

    OST_RoomsOST_MEPSpaces

  

  

   exportCategoryId: The export category to be checked.

   Returns: True if the export category falls within the list,false otherwise.
  """
  pass
 @staticmethod
 def CheckExportComplexity(exportComplexity):
  """
  CheckExportComplexity(exportComplexity: gbXMLExportComplexity) -> bool

  

   Checks that the export complexity falls within an appropriate range.

  

   exportComplexity: The export complexity to be checked.

   Returns: True if the export complexity falls within an appropriate range,false 

    otherwise.
  """
  pass
 @staticmethod
 def CheckGroundPlane(*__args):
  """
  CheckGroundPlane(self: EnergyDataSettings,groundPlaneId: ElementId) -> bool

  

   The ground plane should be an Element of type Level.  This method checks to 

    confirm that an ElementId is for a Level element.

  

  

   groundPlaneId: The element id to be checked to confirm that it is suitable to be a ground 

    plane (i.e.,that it is a level) or

     that it is invalidElementId.  Setting 

    ground plane with invalidElementId will lead to the ground plane being "reset".

  

   Returns: True if the input element is a level or invalidElementId,false otherwise.

  CheckGroundPlane(ccda: Document,groundPlaneId: ElementId) -> bool

  

   The ground plane should be an Element of type Level.  This method checks to 

    confirm that an ElementId is for a Level element.

  

  

   ccda: The Document.

   groundPlaneId: The element id to be checked to confirm that it is suitable to be a ground 

    plane (i.e.,that it is a level) or

     that it is invalidElementId.  Setting 

    ground plane with invalidElementId will lead to the ground plane being "reset".

  

   Returns: True if the input element is a level or invalidElementId,false otherwise.
  """
  pass
 def CheckProjectPhase(self,projectPhaseId):
  """
  CheckProjectPhase(self: EnergyDataSettings,projectPhaseId: ElementId) -> bool

  

   Checks that the input element is a project phase.

  

   projectPhaseId: The element to be checked.

   Returns: True if the input element is a project phase,false otherwise.
  """
  pass
 @staticmethod
 def CheckProjectReportType(projectReportType):
  """
  CheckProjectReportType(projectReportType: HVACLoadLoadsReportType) -> bool

  

   Checks that the project report type falls within an appropriate range.

  

   projectReportType: The project report type to be checked.

   Returns: True if the project report type falls within an appropriate range,false 

    otherwise.
  """
  pass
 @staticmethod
 def CheckRangeOfMassZoneCoreOffset(massZoneCoreOffset):
  """
  CheckRangeOfMassZoneCoreOffset(massZoneCoreOffset: float) -> bool

  

   Checks that the mass zone core offset is greater than or equal to zero.

  

   massZoneCoreOffset: The mass zone core offset to be checked.  Should be greater than or equal to 

    zero.

  

   Returns: True if the mass zone core offset is greater than or equal to zero,false 

    otherwise.
  """
  pass
 @staticmethod
 def CheckRangeOfPercentageGlazing(percentageGlazing):
  """
  CheckRangeOfPercentageGlazing(percentageGlazing: float) -> bool

  

   Checks that the percentage glazing value is between 0.00 and 0.95.

  

   percentageGlazing: The percentage glazing to be checked.

   Returns: True if the percentage glazing value is between 0.00 and 0.95,false otherwise.
  """
  pass
 @staticmethod
 def CheckRangeOfPercentageSkylights(percentageSkylights):
  """
  CheckRangeOfPercentageSkylights(percentageSkylights: float) -> bool

  

   Checks that the percentage skylights value is between 0.00 and 0.95.

  

   percentageSkylights: The percentage skylights to be checked.

   Returns: True if the percentage skylights value is between 0.00 and 0.95,false 

    otherwise.
  """
  pass
 @staticmethod
 def CheckRangeOfShadeDepth(shadeDepth):
  """
  CheckRangeOfShadeDepth(shadeDepth: float) -> bool

  

   Checks that the shade depth is greater than or equal to zero.

  

   shadeDepth: The shade depth to be checked.

   Returns: True if the shade depth is greater than or equal to zero,false otherwise.
  """
  pass
 @staticmethod
 def CheckRangeOfSillHeight(sillHeight):
  """
  CheckRangeOfSillHeight(sillHeight: float) -> bool

  

   Checks that the sill height is greater than or equal to zero.

  

   sillHeight: The sill height to be checked.

   Returns: True if the sill height falls is greater than or equal to zero,false otherwise.
  """
  pass
 @staticmethod
 def CheckRangeOfSkylightWidth(skylightWidth):
  """
  CheckRangeOfSkylightWidth(skylightWidth: float) -> bool

  

   Checks that the skylight width is greater than or equal to eight inches.

  

   skylightWidth: The skylight width to be checked.  Should be greater than or equal to eight 

    inches.

  

   Returns: True if the skylight width is greater than or equal to eight inches,false 

    otherwise.
  """
  pass
 @staticmethod
 def CheckRangeOfSliverSpaceTolerance(silverSpaceTolerance):
  """
  CheckRangeOfSliverSpaceTolerance(silverSpaceTolerance: float) -> bool

  

   Checks that the sliver space tolerance is greater than or equal to zero.

  

   silverSpaceTolerance: The sliver space tolerance to be checked.

   Returns: Returns true if the sliver space tolerance is greater than or equal to zero,

    false otherwise.
  """
  pass
 @staticmethod
 def CheckServiceType(serviceType):
  """
  CheckServiceType(serviceType: gbXMLServiceType) -> bool

  

   Checks that the service type falls within an appropriate range.

  

   serviceType: The service type to be checked.

   Returns: True if the service type falls within an appropriate range,false otherwise.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 @staticmethod
 def EnableConceptualEnergyAnalyticalModel():
  """
  EnableConceptualEnergyAnalyticalModel() -> bool

  

   Turns on functionality related to conceptual energy analysis.

   Returns: Returns true if the Conceptual Energy Analytical model is turned on,false 

    otherwise.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 @staticmethod
 def GetBuildingConstructionSetElementId(ccda):
  """
  GetBuildingConstructionSetElementId(ccda: Document) -> ElementId

  

   Id of the building construction set.

   Returns: Returns the id of the building construction set.
  """
  pass
 @staticmethod
 def GetFromDocument(cda):
  """
  GetFromDocument(cda: Document) -> EnergyDataSettings

  

   Every project document has a EnergyDataSettings element.

     Family documents 

    do not have EnergyDataSettings elements.

  

  

   cda: The document.

   Returns: Returns the EnergyDataSettings element or NULL.
  """
  pass
 @staticmethod
 def IsDocumentUsingEnergyDataAnalyticalModel(ccda):
  """
  IsDocumentUsingEnergyDataAnalyticalModel(ccda: Document) -> bool

  

   Get EnergyDataSettings element and if it exists,return result from 

    getCreateAnalyticalModel.

  

  

   ccda: The document.

   Returns: Returns true if the Conceptual Energy Analytical Model is enabled,false 

    otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def SetCreateAnalyticalModel(self,createAnalyticalModel):
  """
  SetCreateAnalyticalModel(self: EnergyDataSettings,createAnalyticalModel: bool)

   If this is true,data,features,and geometry related to the Energy Analytical 

    Model

     will be created,allowing the energy performance to be analyzed 

    through GreenBuilidingXML.

  

  

   createAnalyticalModel: True to enable the Energy Analytical Model otherwise.
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
 AnalysisType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type of analysis mode.



Get: AnalysisType(self: EnergyDataSettings) -> AnalysisMode



Set: AnalysisType(self: EnergyDataSettings)=value

"""

 AnalyticalGridCellSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The cell size for the uniform cubical grid used when computing the building envelope



Get: AnalyticalGridCellSize(self: EnergyDataSettings) -> float



Set: AnalyticalGridCellSize(self: EnergyDataSettings)=value

"""

 BuildingConstructionClass=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Used for both the detailed and conceptual energy model

   Construction class of building as defined by:

   loose,medium,tight,or none.



Get: BuildingConstructionClass(self: EnergyDataSettings) -> HVACLoadConstructionClass



Set: BuildingConstructionClass(self: EnergyDataSettings)=value

"""

 BuildingEnvelopeDeterminationMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if an analysis should be perform to find the model elements that are part of the building envelope



Get: BuildingEnvelopeDeterminationMethod(self: EnergyDataSettings) -> gbXMLExportBuildingEnvelope



Set: BuildingEnvelopeDeterminationMethod(self: EnergyDataSettings)=value

"""

 BuildingHVACSystem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type of HVAC system used by the building for conceptual model energy calculations.



Get: BuildingHVACSystem(self: EnergyDataSettings) -> gbXMLBuildingHVACSystem



Set: BuildingHVACSystem(self: EnergyDataSettings)=value

"""

 BuildingOperatingSchedule=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The operating schedule of the building used for conceptual model energy calculations.



Get: BuildingOperatingSchedule(self: EnergyDataSettings) -> gbXMLBuildingOperatingSchedule



Set: BuildingOperatingSchedule(self: EnergyDataSettings)=value

"""

 BuildingType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type of building.



Get: BuildingType(self: EnergyDataSettings) -> gbXMLBuildingType



Set: BuildingType(self: EnergyDataSettings)=value

"""

 CoreOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The default offset used to determine the outer perimeter to be divided into zones.



Get: CoreOffset(self: EnergyDataSettings) -> float



Set: CoreOffset(self: EnergyDataSettings)=value

"""

 CreateAnalyticalModel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If this is true,data,features,and geometry related to the Energy Analytical Model

   will be created,allowing the energy performance to be analyzed through GreenBuilidingXML.



Get: CreateAnalyticalModel(self: EnergyDataSettings) -> bool



"""

 DividePerimeter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If this is true,zones with exterior boundaries on each floor of the building will be divided based on geometric criteria.



Get: DividePerimeter(self: EnergyDataSettings) -> bool



Set: DividePerimeter(self: EnergyDataSettings)=value

"""

 EnergyModel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """if this is on there should be an energy model dependent on the current AnalysisType

   if it is off the conceptual energy model should be turned off

   but setting this datum does not do the work,just reflects the state.



Get: EnergyModel(self: EnergyDataSettings) -> bool



Set: EnergyModel(self: EnergyDataSettings)=value

"""

 ExportCategory=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Value is a category indicating which discipline model will be used for GreenBuildingXML export.



Get: ExportCategory(self: EnergyDataSettings) -> ElementId



Set: ExportCategory(self: EnergyDataSettings)=value

"""

 ExportComplexity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Value determines Export Complexity for GreenBuildingXML detailed model export.



Get: ExportComplexity(self: EnergyDataSettings) -> gbXMLExportComplexity



Set: ExportComplexity(self: EnergyDataSettings)=value

"""

 ExportDefaults=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Use for detailed model GreenBuildingXML export.

   When this setting is true,all building and space defaults,schedules,and constructions will be exported to GreenBuildingXML.

   When this setting is false,only values that are specified on the zone or space will be exported to GreenBuildingXML.



Get: ExportDefaults(self: EnergyDataSettings) -> bool



Set: ExportDefaults(self: EnergyDataSettings)=value

"""

 GroundPlane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Id of level which represents ground level.



Get: GroundPlane(self: EnergyDataSettings) -> ElementId



Set: GroundPlane(self: EnergyDataSettings)=value

"""

 IncludeThermalProperties=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if thermal information from model assemblies and components is included in GreenBuildingXML export of the detailed model.



Get: IncludeThermalProperties(self: EnergyDataSettings) -> bool



Set: IncludeThermalProperties(self: EnergyDataSettings)=value

"""

 IsExportMullionsEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if mullions are included in GreenBuildingXML export of the detailed model.



Get: IsExportMullionsEnabled(self: EnergyDataSettings) -> bool



"""

 IsExportShadingSurfacesEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if "shading surfaces" are included in GreenBuildingXML export of the detailed model.



Get: IsExportShadingSurfacesEnabled(self: EnergyDataSettings) -> bool



"""

 IsExportSimplifiedCurtainSystemsEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if curtain system geometry is being simplified for GreenBuildingXML export of the detailed model.



Get: IsExportSimplifiedCurtainSystemsEnabled(self: EnergyDataSettings) -> bool



"""

 IsGlazingShaded=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If this is true,glazing/windows that are auto-created on exterior walls will automatically

   have a shading device created on their top edge.



Get: IsGlazingShaded(self: EnergyDataSettings) -> bool



Set: IsGlazingShaded(self: EnergyDataSettings)=value

"""

 MassZoneCoreOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """It defines the default behavior for the automatic generation of Mass Zones

   for each Mass Floor in the Project.  Specifying a value here will offset the

   outside perimeter of a Mass Zone to create the core.



Get: MassZoneCoreOffset(self: EnergyDataSettings) -> float



Set: MassZoneCoreOffset(self: EnergyDataSettings)=value

"""

 MassZoneDividePerimeter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If this is true,outward facing zones on each floor of the building will be divided based on the four compass directions.



Get: MassZoneDividePerimeter(self: EnergyDataSettings) -> bool



Set: MassZoneDividePerimeter(self: EnergyDataSettings)=value

"""

 OutsideAirChangesRatePerHour=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of times the volume of air interchanges in the room in one hour.



Get: OutsideAirChangesRatePerHour(self: EnergyDataSettings) -> float



Set: OutsideAirChangesRatePerHour(self: EnergyDataSettings)=value

"""

 OutsideAirPerArea=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The rate of flow of outside air available per unit area.



Get: OutsideAirPerArea(self: EnergyDataSettings) -> float



Set: OutsideAirPerArea(self: EnergyDataSettings)=value

"""

 OutsideAirPerPerson=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The rate of flow of outside air available per person.



Get: OutsideAirPerPerson(self: EnergyDataSettings) -> float



Set: OutsideAirPerPerson(self: EnergyDataSettings)=value

"""

 PercentageGlazing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Used for the conceptual energy model.

   The approximate percentage of the building exterior wall surfaces

   which are covered by windows or other glazing.



Get: PercentageGlazing(self: EnergyDataSettings) -> float



Set: PercentageGlazing(self: EnergyDataSettings)=value

"""

 PercentageSkylights=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Used for the conceptual energy model.

   The approximate percentage of the building roof surfaces in

   massing instances for the Conceptual Energy Analytical Model.



Get: PercentageSkylights(self: EnergyDataSettings) -> float



Set: PercentageSkylights(self: EnergyDataSettings)=value

"""

 ProjectPhase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The project phase of the EnergyData information.



Get: ProjectPhase(self: EnergyDataSettings) -> ElementId



Set: ProjectPhase(self: EnergyDataSettings)=value

"""

 ProjectReportType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Report type: None,simple,standard,detailed



Get: ProjectReportType(self: EnergyDataSettings) -> HVACLoadLoadsReportType



Set: ProjectReportType(self: EnergyDataSettings)=value

"""

 ServiceType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type of heating or cooling system.



Get: ServiceType(self: EnergyDataSettings) -> gbXMLServiceType



Set: ServiceType(self: EnergyDataSettings)=value

"""

 ShadeDepth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Used for the conceptual energy model.

   Amount that auto-generated shading will extend from auto-generated windows.



Get: ShadeDepth(self: EnergyDataSettings) -> float



Set: ShadeDepth(self: EnergyDataSettings)=value

"""

 SillHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Used for the conceptual energy model.

   The height from the nearest lower level used for auto-glazing created

   on walls.



Get: SillHeight(self: EnergyDataSettings) -> float



Set: SillHeight(self: EnergyDataSettings)=value

"""

 SkylightWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Used for the conceptual energy model.  The approximate width used for the skylights in

   massing instances when the Energy Analytical model is being created.



Get: SkylightWidth(self: EnergyDataSettings) -> float



Set: SkylightWidth(self: EnergyDataSettings)=value

"""

 SliverSpaceTolerance=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Used for Detailed GreenBuildingXML export.

   This value is used to identify sliver spaces,i.e. spaces bounded by parallel surfaces belonging to different rooms.



Get: SliverSpaceTolerance(self: EnergyDataSettings) -> float



Set: SliverSpaceTolerance(self: EnergyDataSettings)=value

"""

 UseAirChangesPerHour=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if user is specifying air changes per hour,false otherwise.



Get: UseAirChangesPerHour(self: EnergyDataSettings) -> bool



Set: UseAirChangesPerHour(self: EnergyDataSettings)=value

"""

 UseHeatingCredits=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If true,Revit will use heating credits in the final load sum calculations.

   If false,Revit will ignore heating credits in the final load sum calculations.



Get: UseHeatingCredits(self: EnergyDataSettings) -> bool



Set: UseHeatingCredits(self: EnergyDataSettings)=value

"""

 UseOutsideAirPerArea=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True is user is specifying outside air per area,false otherwise.



Get: UseOutsideAirPerArea(self: EnergyDataSettings) -> bool



Set: UseOutsideAirPerArea(self: EnergyDataSettings)=value

"""

 UseOutsideAirPerPerson=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if user is specifying outside air per person,false otherwise.



Get: UseOutsideAirPerPerson(self: EnergyDataSettings) -> bool



Set: UseOutsideAirPerPerson(self: EnergyDataSettings)=value

"""


