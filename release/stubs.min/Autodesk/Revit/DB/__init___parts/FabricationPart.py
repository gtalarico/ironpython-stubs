class FabricationPart(Element,IDisposable):
 """ Represents a fabrication component in the Autodesk Revit MEP product. """
 def AdjustEndLength(self,partConn,lengthToAdjust,totalLengthOnly):
  """
  AdjustEndLength(self: FabricationPart,partConn: Connector,lengthToAdjust: float,totalLengthOnly: bool) -> float

  

   Adjusts the length for the specified connector.

  

   partConn: # The connector of the fabrication part to adjust length.

   lengthToAdjust: The length to adjust.

   totalLengthOnly: True if adjust the total length only when adjust length.

   Returns: The adjusted length.
  """
  pass
 @staticmethod
 def AlignPartByConnectors(doc,partConn,toConn,axisRotation):
  """
  AlignPartByConnectors(doc: Document,partConn: Connector,toConn: Connector,axisRotation: float) -> bool

  

   Moves fabrication part by one of its connectors and aligns it to another 

    connector.

  

  

   doc: The document.

   partConn: The connector of the fabrication part to move and align by.

   toConn: The connector of the fabrication part or family to align to.

   axisRotation: Rotation around the direction of connection - angle between width vectors in 

    radians.

  

   Returns: True if alignment succeeds,false otherwise.
  """
  pass
 def CanAdjustEndLength(self,partConn):
  """
  CanAdjustEndLength(self: FabricationPart,partConn: Connector) -> bool

  

   Checks if the end of fabrication part can be adjusted.

  

   partConn: # The connector of the fabrication part to adjust length.

   Returns: True if the end of fabrication part can be adjusted.
  """
  pass
 @staticmethod
 def ConnectAndCouple(doc,partConn,toConn):
  """
  ConnectAndCouple(doc: Document,partConn: Connector,toConn: Connector) -> bool

  

   Makes a connection between the specified connectors and adds coupling if 

    necessary.

  

  

   doc: The document.

   partConn: The connector of the fabrication part.

   toConn: The connector of the fabrication part or family to connect to.

   Returns: True if connection succeeded,false otherwise.
  """
  pass
 @staticmethod
 def Create(document,button,*__args):
  """
  Create(document: Document,button: FabricationServiceButton,width: float,depth: float,levelId: ElementId) -> FabricationPart

  

   Creates a fabrication part element based on button and size.

  

   document: The document.

   button: The fabrication service button to use. Matches button condition based on the 

    specified size.

  

   width: The width of the part. Units are in feet (ft).

   depth: The depth of the part. Units are in feet (ft). It should be equal to width for 

    round part.

  

   levelId: The level identifier.

   Returns: The new fabrication part.

  Create(document: Document,button: FabricationServiceButton,condition: int,levelId: ElementId) -> FabricationPart

  

   Creates a fabrication part element based on button.

  

   document: The document.

   button: The fabrication service button to use.

   condition: The condition index.

   levelId: The level identifier.

   Returns: The new fabrication part.
  """
  pass
 @staticmethod
 def CreateHanger(document,button,*__args):
  """
  CreateHanger(document: Document,button: FabricationServiceButton,hostId: ElementId,hostConnector: Connector,distance: float,attachToStructure: bool) -> FabricationPart

  

   Creates a hanger on the fabrication part.

  

   document: The document.

   button: The fabrication service button to use. It finds the matching condition 

    automatically if the button has multiple condition.

  

   hostId: The host part id. The host should be one horizontal straight part.

   hostConnector: The connector of the host.

   distance: The distance from the input connector of the host part. Units are in feet (ft).

   attachToStructure: Attach to the nearest structural element. The structural element might be one 

    of Floor/Roof/Stair/Structure Framing.

  

   Returns: The newly-created fabrication hanger.

  CreateHanger(document: Document,button: FabricationServiceButton,condition: int,hostId: ElementId,hostConnector: Connector,distance: float,attachToStructure: bool) -> FabricationPart

  

   Creates a hanger on the fabrication part.

  

   document: The document.

   button: The fabrication service button to use.

   condition: The condition index. If the button has multiple conditions.

   hostId: The host part id. The host should be one horizontal straight part.

   hostConnector: The connector of the host.

   distance: The distance from the input connector of the host part. Units are in feet (ft).

   attachToStructure: Attach to the nearest structural element. The structural element might be one 

    of Floor/Roof/Stair/Structural Framing.

  

   Returns: The newly-created fabrication hanger.

  CreateHanger(document: Document,button: FabricationServiceButton,condition: int,levelId: ElementId) -> FabricationPart

  

   Creates a free placed hanger.

  

   document: The document.

   button: The fabrication service button to use.

   condition: The condition index. If the button has multiple conditions.

   levelId: The level identifier of the hanger.

   Returns: The newly-created fabrication hanger.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetCalculatedDimensionValue(self,dim):
  """
  GetCalculatedDimensionValue(self: FabricationPart,dim: FabricationDimensionDefinition) -> str

  

   Gets the calculated dimension value.

  

   dim: The fabrication dimension.

   Returns: The calculated dimension value.
  """
  pass
 def GetDimensionCalculatedOptions(self,dim):
  """
  GetDimensionCalculatedOptions(self: FabricationPart,dim: FabricationDimensionDefinition) -> IList[str]

  

   Gets the calculated options of the fabrication dimension.

  

   dim: The fabrication dimension.

   Returns: The calculated options of the fabrication dimension.
  """
  pass
 def GetDimensions(self):
  """
  GetDimensions(self: FabricationPart) -> IList[FabricationDimensionDefinition]

  

   Gets all fabrication dimensions.

   Returns: Returns an array of fabrication dimensions.
  """
  pass
 def GetDimensionValue(self,dim):
  """
  GetDimensionValue(self: FabricationPart,dim: FabricationDimensionDefinition) -> float

  

   Gets the value of the fabrication dimension,returns value in Revit internal 

    units.

  

  

   dim: The fabrication dimension.

   Returns: The dimension value.
  """
  pass
 def GetHostedInfo(self):
  """
  GetHostedInfo(self: FabricationPart) -> FabricationHostedInfo

  

   Gets the fabrication hosted element information.

   Returns: The fabrication hosted element information. Returns null if the fabrication 

    part does not have a host.
  """
  pass
 def GetProductListEntryCount(self):
  """
  GetProductListEntryCount(self: FabricationPart) -> int

  

   Gets the number of product entries for this part.

   Returns: Returns the number of product entries.
  """
  pass
 def GetProductListEntryName(self,index):
  """
  GetProductListEntryName(self: FabricationPart,index: int) -> str

  

   Gets the specified product list entry name.

  

   index: The product entry index.

   Returns: Returns the specified product entry name.
  """
  pass
 def GetRodInfo(self):
  """
  GetRodInfo(self: FabricationPart) -> FabricationRodInfo

  

   Gets the fabrication rod information.

   Returns: The fabrication rod information. Returns null if the fabrication part does not 

    have any rod.
  """
  pass
 def GetTransform(self):
  """
  GetTransform(self: FabricationPart) -> Transform

  

   Gets the transformation matrix of the fabrication part element.

   Returns: The transformation matrix of the fabrication part element.
  """
  pass
 def IsAHanger(self):
  """
  IsAHanger(self: FabricationPart) -> bool

  

   Checks whether it is a hanger.

   Returns: True if the part is a hanger. False otherwise.
  """
  pass
 def IsAStraight(self):
  """
  IsAStraight(self: FabricationPart) -> bool

  

   Checks whether it is a straight part.

   Returns: True if the part is a straight part. False otherwise.
  """
  pass
 def IsATap(self):
  """
  IsATap(self: FabricationPart) -> bool

  

   Checks if it is any sort of tap.

   Returns: True if it is any sort of tap.
  """
  pass
 def IsDimensionCalculated(self,dim):
  """
  IsDimensionCalculated(self: FabricationPart,dim: FabricationDimensionDefinition) -> bool

  

   Checks if the fabrication dimension is calculated.

  

   dim: The fabrication dimension.

   Returns: True if the fabrication dimension is calculated.
  """
  pass
 def IsProductList(self):
  """
  IsProductList(self: FabricationPart) -> bool

  

   Gets whether or not the fabrication part is a product list.

   Returns: Returns true if the fabrication part is a product list.
  """
  pass
 def IsProductListEntryCompatibleSize(self,productEntry):
  """
  IsProductListEntryCompatibleSize(self: FabricationPart,productEntry: int) -> bool

  

   Checks to see if this part can be changed to the specified product entry 

    without altering any connected dimensions.

  

  

   productEntry: The product entry index.

   Returns: Returns true if the part can be changed to the specified product entry without 

    altering any connected dimensions.
  """
  pass
 @staticmethod
 def OptimizeLengths(doc,partIds):
  """ OptimizeLengths(doc: Document,partIds: ISet[ElementId]) -> ISet[ElementId] """
  pass
 @staticmethod
 def PlaceAsTap(doc,tapPartConn,hostPartConn,distance,axisRotation,secondaryAxisRotation):
  """
  PlaceAsTap(doc: Document,tapPartConn: Connector,hostPartConn: Connector,distance: float,axisRotation: float,secondaryAxisRotation: float)

   Places the part by its connector to a specific position on the straight part at 

    the specified distance from the host part connector.

  

  

   doc: The document.

   tapPartConn: The connector of the part to place.

   hostPartConn: The connector of host part.

   distance: The distance to host part connector where to place the part.

   axisRotation: The axis rotation in radians.

   secondaryAxisRotation: The secondary axis rotation in radians.
  """
  pass
 @staticmethod
 def PlaceFittingAsCutIn(doc,straightId,fittingId,position,fittingConn,axisRotation):
  """
  PlaceFittingAsCutIn(doc: Document,straightId: ElementId,fittingId: ElementId,position: XYZ,fittingConn: Connector,axisRotation: float) -> bool

  

   Places the fitting on the straight part by cut in,use the fitting's focal 

    point as the insertion position.

  

  

   doc: The document.

   straightId: Id of the straight to be cut in.

   fittingId: Id of the fitting to cut in.

   position: The position to cut in the straight.

   fittingConn: The connector of the fitting to align with the primary connector of the 

    straight part.

  

   axisRotation: Rotation around the direction of connection - angle between width vectors in 

    radians.

  

   Returns: True if cuts in successfully.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 @staticmethod
 def Reposition(doc,partId):
  """
  Reposition(doc: Document,partId: ElementId)

   Repositions the fabrication straight part to another end of the run.

  

   doc: The document.

   partId: Id of the fabrication part to reposition.
  """
  pass
 @staticmethod
 def RotateConnectedPartByConnector(doc,conn,axisRotationBy):
  """
  RotateConnectedPartByConnector(doc: Document,conn: Connector,axisRotationBy: float)

   Rotates a connected fabrication part around the axis of the specified connector.

  

   doc: The document.

   conn: The connected connector of the fabrication part to be rotated.

   axisRotationBy: The angle in radians to rotate by.
  """
  pass
 @staticmethod
 def RotateConnectedTap(doc,tap,primaryAxisRotateBy,secondaryAxisRotateBy):
  """
  RotateConnectedTap(doc: Document,tap: FabricationPart,primaryAxisRotateBy: float,secondaryAxisRotateBy: float)

   Rotates a connected fabrication tap by the specified angles about the primary 

    and secondary axis.

  

  

   doc: The document.

   tap: The connected fabrication part tap to rotate.

   primaryAxisRotateBy: The primary axis rotation angle in radians to rotate by.

   secondaryAxisRotateBy: The secondary axis rotation angle in radians to rotate by.
  """
  pass
 def SetCalculatedDimensionValue(self,dim,value):
  """
  SetCalculatedDimensionValue(self: FabricationPart,dim: FabricationDimensionDefinition,value: str)

   Sets the calculated dimension value.

  

   dim: The fabrication dimension.

   value: The calculated dimension value.
  """
  pass
 def SetDimensionValue(self,dim,newValue):
  """
  SetDimensionValue(self: FabricationPart,dim: FabricationDimensionDefinition,newValue: float)

   Sets the fabrication dimension value. The value is in Revit internal units.

  

   dim: The fabrication dimension.

   newValue: The dimension value.
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetPositionByEnd(self,connector,position):
  """
  SetPositionByEnd(self: FabricationPart,connector: Connector,position: XYZ)

   Positions the connector of the fabrication part element by the passed point.

  

   connector: The connector of the fabrication part element.

   position: The position to move to.
  """
  pass
 @staticmethod
 def StretchAndFit(document,stretchConnector,target,newPartIds):
  """ StretchAndFit(document: Document,stretchConnector: Connector,target: FabricationPartRouteEnd) -> (FabricationPartFitResult,ISet[ElementId]) """
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
 Alias=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The alias of the fabrication part.



Get: Alias(self: FabricationPart) -> str



"""

 BottomOfPartElevation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The associated elevation to the bottom of fabrication part off of the current level.



Get: BottomOfPartElevation(self: FabricationPart) -> float



"""

 ConnectorManager=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The connector manager of the fabrication part.



Get: ConnectorManager(self: FabricationPart) -> ConnectorManager



"""

 CutType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The cut type of the fabrication part.



Get: CutType(self: FabricationPart) -> int



"""

 DomainType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The domain type for the fabrication part.



Get: DomainType(self: FabricationPart) -> ConnectorDomainType



"""

 DoubleWallMaterial=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The double wall material identifier of the fabrication part.



Get: DoubleWallMaterial(self: FabricationPart) -> int



"""

 DoubleWallMaterialArea=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The double wall material area of the fabrication part. If the fabrication part is not double walled,returns zero.



Get: DoubleWallMaterialArea(self: FabricationPart) -> float



"""

 DoubleWallMaterialThickness=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The double wall material thickness of the fabrication part. If the fabrication part is not double walled,returns zero.



Get: DoubleWallMaterialThickness(self: FabricationPart) -> float



"""

 HasDoubleWall=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if the fabrication part is double walled.



Get: HasDoubleWall(self: FabricationPart) -> bool



"""

 HasInsulation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if the fabrication part is insulated.



Get: HasInsulation(self: FabricationPart) -> bool



"""

 HasLining=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if the fabrication part is lined.



Get: HasLining(self: FabricationPart) -> bool



"""

 InsulationArea=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The insulation area of the fabrication part. If the fabrication part is not insulated,returns zero.



Get: InsulationArea(self: FabricationPart) -> float



"""

 InsulationSpecification=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The fabrication part insulation specification identifier.



Get: InsulationSpecification(self: FabricationPart) -> int



Set: InsulationSpecification(self: FabricationPart)=value

"""

 InsulationThickness=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The insulation thickness of the fabrication part. If the fabrication part is not insulated,returns zero.



Get: InsulationThickness(self: FabricationPart) -> float



"""

 InsulationType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The insulation type of the fabrication part.



Get: InsulationType(self: FabricationPart) -> str



"""

 IsBoughtOut=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if the fabrication part is bought out.



Get: IsBoughtOut(self: FabricationPart) -> bool



"""

 ItemCustomId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The item custom identifier for the fabrication part.



Get: ItemCustomId(self: FabricationPart) -> int



"""

 ItemNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The item number that is used for identification,re-ordering from shop.



Get: ItemNumber(self: FabricationPart) -> str



Set: ItemNumber(self: FabricationPart)=value

"""

 LevelOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The associated level offset that indicates the distance from the center of the fabrication part to the current level.



Get: LevelOffset(self: FabricationPart) -> float



"""

 LiningArea=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The lining area of the fabrication part. If the fabrication part is not lined,returns zero.



Get: LiningArea(self: FabricationPart) -> float



"""

 LiningThickness=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The lining thickness of the fabrication part. If the fabrication part is not lined,returns zero.



Get: LiningThickness(self: FabricationPart) -> float



"""

 LiningType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The lining type of the fabrication part.



Get: LiningType(self: FabricationPart) -> str



"""

 Material=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The fabrication material identifier.



Get: Material(self: FabricationPart) -> int



Set: Material(self: FabricationPart)=value

"""

 MaterialThickness=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The material thickness of the fabrication part.



Get: MaterialThickness(self: FabricationPart) -> float



"""

 Notes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The notes of the fabrication part.



Get: Notes(self: FabricationPart) -> str



Set: Notes(self: FabricationPart)=value

"""

 Origin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The origin of the fabrication part element.



Get: Origin(self: FabricationPart) -> XYZ



"""

 OverallSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The overall size of the fabrication part.



Get: OverallSize(self: FabricationPart) -> str



"""

 ProductCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The current database id of the part within the fabrication database.



Get: ProductCode(self: FabricationPart) -> str



"""

 ProductDataRange=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The product data range of the fabrication part.



Get: ProductDataRange(self: FabricationPart) -> str



"""

 ProductFinishDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The product finish description of the fabrication part.



Get: ProductFinishDescription(self: FabricationPart) -> str



"""

 ProductInstallType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The product install type of the fabrication part.



Get: ProductInstallType(self: FabricationPart) -> str



"""

 ProductListEntry=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The product entry index of the fabrication part. A value of -1 indicates the fabrication part is not a product list.



Get: ProductListEntry(self: FabricationPart) -> int



Set: ProductListEntry(self: FabricationPart)=value

"""

 ProductLongDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The product long description of the fabrication part.



Get: ProductLongDescription(self: FabricationPart) -> str



"""

 ProductMaterialDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The product material description of the fabrication part.



Get: ProductMaterialDescription(self: FabricationPart) -> str



"""

 ProductName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The product name of the fabrication part.



Get: ProductName(self: FabricationPart) -> str



"""

 ProductOriginalEquipmentManufacture=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The product original equipment manufacture (OEM) of the fabrication part.



Get: ProductOriginalEquipmentManufacture(self: FabricationPart) -> str



"""

 ProductShortDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The product short description of the fabrication part.



Get: ProductShortDescription(self: FabricationPart) -> str



"""

 ProductSizeDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The product size description of the fabrication part.



Get: ProductSizeDescription(self: FabricationPart) -> str



"""

 ProductSpecificationDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The product specification description of the fabrication part.



Get: ProductSpecificationDescription(self: FabricationPart) -> str



"""

 ServiceAbbreviation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The associated service abbreviation for the fabrication service.



Get: ServiceAbbreviation(self: FabricationPart) -> str



"""

 ServiceId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The fabrication part service identifier. The service can only be changed to compatible services.



Get: ServiceId(self: FabricationPart) -> int



"""

 ServiceName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the service associated with the fabrication part.



Get: ServiceName(self: FabricationPart) -> str



"""

 SheetMetalArea=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The sheet metal area of the fabrication part.



Get: SheetMetalArea(self: FabricationPart) -> float



"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The size of the fabrication part.



Get: Size(self: FabricationPart) -> str



"""

 Slope=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The slope for the straight fabrication part.



Get: Slope(self: FabricationPart) -> float



"""

 Specification=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The fabrication part specification identifier.



Get: Specification(self: FabricationPart) -> int



Set: Specification(self: FabricationPart)=value

"""

 TopOfPartElevation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The associated elevation to the top of fabrication part off of the current level.



Get: TopOfPartElevation(self: FabricationPart) -> float



"""

 ValidationStatus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The validation status of the fabrication part.



Get: ValidationStatus(self: FabricationPart) -> ValidationStatus



"""

 Vendor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The vendor of the fabrication part.



Get: Vendor(self: FabricationPart) -> str



"""

 VendorCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The vendor code of the fabrication part.



Get: VendorCode(self: FabricationPart) -> str



"""

 Weight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The weight of the fabrication part.



Get: Weight(self: FabricationPart) -> float



"""


