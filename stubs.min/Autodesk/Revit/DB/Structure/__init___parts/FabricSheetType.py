class FabricSheetType(ElementType,IDisposable):
 """ Represents a fabric sheet type,used in the generation of fabric wires. """
 @staticmethod
 def CreateDefaultFabricSheetType(ADoc):
  """
  CreateDefaultFabricSheetType(ADoc: Document) -> ElementId
  
   Creates a new FabricSheetType object with a default name.
  
   ADoc: The document.
   Returns: The newly created type id.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetReinforcementRoundingManager(self):
  """
  GetReinforcementRoundingManager(self: FabricSheetType) -> FabricRoundingManager
  
   Returns an object for managing reinforcement rounding override settings.
   Returns: The rounding manager.
  """
  pass
 def GetWireItem(self,wireIndex,direction):
  """
  GetWireItem(self: FabricSheetType,wireIndex: int,direction: WireDistributionDirection) -> FabricWireItem
  
   Gets the Wire stored in the FabricSheetType at the associated index.
  
   wireIndex: Item index in the Fabric Sheet
   direction: Wire distribution direction of the inquired item
   Returns: Fabric wire Item
  """
  pass
 def IsCustom(self):
  """
  IsCustom(self: FabricSheetType) -> bool
  
   Verifies if the type is Custom Fabric Sheet
   Returns: True if Layout is set on Custom and if the wireArr is not null
  """
  pass
 def IsValidMajorLapSplice(self,majorLapSplice):
  """
  IsValidMajorLapSplice(self: FabricSheetType,majorLapSplice: float) -> bool
  
   Identifies if the input value is valid to be applied as the major lap splice
    
     value for this FabricSheetType.
  """
  pass
 def IsValidMinorLapSplice(self,minorLapSplice):
  """
  IsValidMinorLapSplice(self: FabricSheetType,minorLapSplice: float) -> bool
  
   Identifies if the input value is valid to be applied as the minor lap splice
    
     value for this FabricSheetType.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetLayoutAsCustomPattern(self,minorStartOverhang,minorEndOverhang,majorStartOverhang,majorEndOverhang,minorFabricWireItems,majorFabricWireItems):
  """ SetLayoutAsCustomPattern(self: FabricSheetType,minorStartOverhang: float,minorEndOverhang: float,majorStartOverhang: float,majorEndOverhang: float,minorFabricWireItems: IList[FabricWireItem],majorFabricWireItems: IList[FabricWireItem]) """
  pass
 def SetMajorLayoutAsActualSpacing(self,overallWidth,minorStartOverhang,spacing):
  """
  SetMajorLayoutAsActualSpacing(self: FabricSheetType,overallWidth: float,minorStartOverhang: float,spacing: float)
   Sets the major layout pattern as ActualSpacing,while specifying the needed 
    parameters for this pattern.
  
  
   overallWidth: The entire width of the wire sheet in the minor direction.
   minorStartOverhang: The distance from the edge of the sheet to the first wire in the minor 
    direction.
  
   spacing: The distance between the wires in the major direction.
  """
  pass
 def SetMajorLayoutAsFixedNumber(self,overallWidth,minorStartOverhang,minorEndOverhang,numberOfWires):
  """
  SetMajorLayoutAsFixedNumber(self: FabricSheetType,overallWidth: float,minorStartOverhang: float,minorEndOverhang: float,numberOfWires: int)
   Sets the major layout pattern as FixedNumber,while specifying the needed 
    parameters for this pattern.
  
  
   overallWidth: The entire width of the wire sheet in the minor direction.
   minorStartOverhang: The distance from the edge of the sheet to the first wire in the minor 
    direction.
  
   minorEndOverhang: The distance from the last wire to the edge of the sheet in the minor direction.
   numberOfWires: The number of the wires to set in the major direction.
  """
  pass
 def SetMajorLayoutAsMaximumSpacing(self,overallWidth,minorStartOverhang,minorEndOverhang,spacing):
  """
  SetMajorLayoutAsMaximumSpacing(self: FabricSheetType,overallWidth: float,minorStartOverhang: float,minorEndOverhang: float,spacing: float)
   Sets the major layout pattern as MaximumSpacing,while specifying the needed 
    parameters for this pattern.
  
  
   overallWidth: The entire width of the wire sheet in the minor direction.
   minorStartOverhang: The distance from the edge of the sheet to the first wire in the minor 
    direction.
  
   minorEndOverhang: The distance from the last wire to the edge of the sheet in the minor direction.
   spacing: The distance between the wires in the major direction.
  """
  pass
 def SetMajorLayoutAsNumberWithSpacing(self,overallWidth,minorStartOverhang,numberOfWires,spacing):
  """
  SetMajorLayoutAsNumberWithSpacing(self: FabricSheetType,overallWidth: float,minorStartOverhang: float,numberOfWires: int,spacing: float)
   Sets the major layout pattern as NumberWithSpacing,while specifying the needed 
    parameters for this pattern.
  
  
   overallWidth: The entire width of the wire sheet in the minor direction.
   minorStartOverhang: The distance from the edge of the sheet to the first wire in the minor 
    direction.
  
   numberOfWires: The number of the wires to set in the major direction.
   spacing: The distance between the wires in the major direction.
  """
  pass
 def SetMinorLayoutAsActualSpacing(self,overallLength,majorStartOverhang,spacing):
  """
  SetMinorLayoutAsActualSpacing(self: FabricSheetType,overallLength: float,majorStartOverhang: float,spacing: float)
   Sets the minor layout pattern as ActualSpacing,while specifying the needed 
    parameters for this pattern.
  
  
   overallLength: The entire length of the wire sheet in the major direction.
   majorStartOverhang: The distance from the edge of the sheet to the first wire in the major 
    direction.
  
   spacing: The distance between the wires in the minor direction.
  """
  pass
 def SetMinorLayoutAsFixedNumber(self,overallLength,majorStartOverhang,majorEndOverhang,numberOfWires):
  """
  SetMinorLayoutAsFixedNumber(self: FabricSheetType,overallLength: float,majorStartOverhang: float,majorEndOverhang: float,numberOfWires: int)
   Sets the major layout pattern as FixedNumber,while specifying the needed 
    parameters for this pattern.
  
  
   overallLength: The entire length of the wire sheet in the major direction.
   majorStartOverhang: The distance from the edge of the sheet to the first wire in the major 
    direction.
  
   majorEndOverhang: The distance from the last wire to the edge of the sheet in the major direction.
   numberOfWires: The number of the wires to set in the minor direction.
  """
  pass
 def SetMinorLayoutAsMaximumSpacing(self,overallLength,majorStartOverhang,majorEndOverhang,spacing):
  """
  SetMinorLayoutAsMaximumSpacing(self: FabricSheetType,overallLength: float,majorStartOverhang: float,majorEndOverhang: float,spacing: float)
   Sets the major layout pattern as MaximumSpacing,while specifying the needed 
    parameters for this pattern.
  
  
   overallLength: The entire length of the wire sheet in the major direction.
   majorStartOverhang: The distance from the edge of the sheet to the first wire in the major 
    direction.
  
   majorEndOverhang: The distance from the last wire to the edge of the sheet in the major direction.
   spacing: The distance between the wires in the minor direction.
  """
  pass
 def SetMinorLayoutAsNumberWithSpacing(self,overallLength,majorStartOverhang,numberOfWires,spacing):
  """
  SetMinorLayoutAsNumberWithSpacing(self: FabricSheetType,overallLength: float,majorStartOverhang: float,numberOfWires: int,spacing: float)
   Sets the major layout pattern as NumberWithSpacing,while specifying the needed 
    parameters for this pattern.
  
  
   overallLength: The entire length of the wire sheet in the major direction.
   majorStartOverhang: The distance from the edge of the sheet to the first wire in the major 
    direction.
  
   numberOfWires: The number of wires in the minor direction.
   spacing: The distance between the wires in the minor direction.
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
 MajorDirectionWireType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the FabricWireType to be used in the major direction.

Get: MajorDirectionWireType(self: FabricSheetType) -> ElementId

Set: MajorDirectionWireType(self: FabricSheetType)=value
"""

 MajorEndOverhang=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The distance from the edge of the sheet to the last wire (measured in the major direction).

Get: MajorEndOverhang(self: FabricSheetType) -> float

"""

 MajorLapSpliceLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The lap splice length in the major direction.

Get: MajorLapSpliceLength(self: FabricSheetType) -> float

Set: MajorLapSpliceLength(self: FabricSheetType)=value
"""

 MajorLayoutPattern=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The layout pattern in the major direction.

Get: MajorLayoutPattern(self: FabricSheetType) -> FabricSheetLayoutPattern

"""

 MajorNumberOfWires=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of wires used in the major direction (includes the first and last wires).

Get: MajorNumberOfWires(self: FabricSheetType) -> int

"""

 MajorReinforcementArea=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The area of fabric divided by the spacing of the wire in the major direction.

Get: MajorReinforcementArea(self: FabricSheetType) -> float

"""

 MajorSpacing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The spacing between the wires in the major direction (not including the overhangs).

Get: MajorSpacing(self: FabricSheetType) -> float

"""

 MajorStartOverhang=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The distance from the edge of the sheet to the first wire (measured in the major direction).

Get: MajorStartOverhang(self: FabricSheetType) -> float

"""

 Material=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the material assigned to wires.

Get: Material(self: FabricSheetType) -> ElementId

Set: Material(self: FabricSheetType)=value
"""

 MinorDirectionWireType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the FabricWireType to be used in the minor direction.

Get: MinorDirectionWireType(self: FabricSheetType) -> ElementId

Set: MinorDirectionWireType(self: FabricSheetType)=value
"""

 MinorEndOverhang=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The distance from the edge of the sheet to the last wire (measured in the minor direction).

Get: MinorEndOverhang(self: FabricSheetType) -> float

"""

 MinorLapSpliceLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The lap splice length in the minor direction.

Get: MinorLapSpliceLength(self: FabricSheetType) -> float

Set: MinorLapSpliceLength(self: FabricSheetType)=value
"""

 MinorLayoutPattern=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The layout pattern in the minor direction.

Get: MinorLayoutPattern(self: FabricSheetType) -> FabricSheetLayoutPattern

"""

 MinorNumberOfWires=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of wires used in the minor direction (includes the 1st and last wires).

Get: MinorNumberOfWires(self: FabricSheetType) -> int

"""

 MinorReinforcementArea=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The area of fabric divided by the spacing of the wire in the minor direction.

Get: MinorReinforcementArea(self: FabricSheetType) -> float

"""

 MinorSpacing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The spacing between the wires in the minor direction (not including the overhangs).

Get: MinorSpacing(self: FabricSheetType) -> float

"""

 MinorStartOverhang=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The distance from the edge of the sheet to the first wire (measured in the minor direction).

Get: MinorStartOverhang(self: FabricSheetType) -> float

"""

 OverallLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The length of the wire sheet (including overhangs) in the major direction.

Get: OverallLength(self: FabricSheetType) -> float

"""

 OverallWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The length of the wire sheet (including overhangs) in the minor direction.

Get: OverallWidth(self: FabricSheetType) -> float

"""

 SheetMass=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The sheet mass.

Get: SheetMass(self: FabricSheetType) -> float

Set: SheetMass(self: FabricSheetType)=value
"""

 SheetMassUnit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The sheet mass per area unit.

Get: SheetMassUnit(self: FabricSheetType) -> float

"""


