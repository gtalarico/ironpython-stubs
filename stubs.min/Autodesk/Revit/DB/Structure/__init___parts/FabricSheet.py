class FabricSheet(Element,IDisposable):
 """ An object that represents an Fabric Sheet Element within the Autodesk Revit project. """
 @staticmethod
 def Create(document,*__args):
  """
  Create(document: Document,hostElement: Element,fabricSheetTypeId: ElementId) -> FabricSheet
  
   Creates a new instance of a single flat Fabric Sheet element within the project.
  
   document: The document in which the fabric sheet is to be created.
   hostElement: The element that will host the FabricSheet. The host can be a Structural Floor,
    Structural Wall,Structural Slab,or a Part created from a structural layer 
    belonging to one of those element types.
  
   fabricSheetTypeId: The id of the FabricSheetType.
   Returns: The newly created single Fabric Sheet instance.
  Create(document: Document,concreteHostElementId: ElementId,fabricSheetTypeId: ElementId,bendProfile: CurveLoop) -> FabricSheet
  
   Creates a new instance of a single bent Fabric Sheet element within the project.
  
   document: The document in which the fabric sheet is to be created.
   concreteHostElementId: The element that will host the FabricSheet.
     The host can be a Structural 
    Floor,Structural Wall,Structural Slab,Structural Floor Edge,Structural Slab 
    Edge,
     Structural Column,Beam and Brace.
     Also,host can be a 
    Autodesk::Revit::DB::Part created from a structural layer of Structural Floor,
    Structural Wall or Structural Slab.
  
   fabricSheetTypeId: The id of the FabricSheetType.
   bendProfile: A profile that defines the bending shape of the fabric sheet.
     The profile 
    can be provided without fillets (eg. for L shape,only two lines not two lines 
    and one arc),if so,
     then fillets (in example one arc) will be 
    automatically generated basing on the Bend Diameter parameter defined in the 
    Fabric Wire system family.
     If the provided profile has no corners (has a 
    tangent defined at each point except the ends),no fillets will be generated.
   
      The provided profile defines the center-curve of a wire.
  
   Returns: The instance of the newly created bent fabric sheet.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def GetBendProfile(self):
  """
  GetBendProfile(self: FabricSheet) -> CurveLoop
  
   Returns the profile (not including generated fillets) that defines the shape of 
    the Fabric Sheet bending.
  
   Returns: The profile that defines the shape of the fabric sheet bending for bent fabric 
    sheet,for flat fabric sheet ll will be returned.
  """
  pass
 def GetBendProfileWithFillets(self):
  """
  GetBendProfileWithFillets(self: FabricSheet) -> CurveLoop
  
   Returns the profile with generated fillets that defines the shape of the Fabric 
    Sheet bending.
  
   Returns: The bend profile with generated fillets that defines the shape of the fabric 
    sheet bending for bent fabric sheet,
     for flat fabric sheet ll will be 
    returned.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetReinforcementRoundingManager(self):
  """
  GetReinforcementRoundingManager(self: FabricSheet) -> FabricRoundingManager
  
   Returns an object for managing reinforcement rounding override settings.
   Returns: The rounding manager.
  """
  pass
 def GetSegmentParameterIdsAndLengths(self,rounded):
  """
  GetSegmentParameterIdsAndLengths(self: FabricSheet,rounded: bool) -> IDictionary[ElementId,float]
  
   Returns the array of pairs [parameter ID,length] that correspond to segments 
    of a bent fabric sheet (like A,B,C,D etc.).
  
  
   rounded: Set to true to return rounded values for segments lengths.
   Returns: Array of pairs [parameter ID,length] that correspond to segments of a bent 
    fabric sheet (like A,B,C,D etc.) is returned for bend fabric sheet.
     For 
    flat fabric sheet (not bent) empty array is returned.
  """
  pass
 def GetSheetLocation(self):
  """
  GetSheetLocation(self: FabricSheet) -> Transform
  
   Gets the position and the orientation of the Fabric Sheet instance.
   Returns: The location of the Fabric Sheet instance.
  """
  pass
 def GetWireCenterlines(self,wireDirection=None):
  """
  GetWireCenterlines(self: FabricSheet,wireDirection: WireDistributionDirection) -> IList[Curve]
  
   Gets a list of curves representing the wires centerlines of the Fabric Sheet.
  
   wireDirection: The direction of wire distribution in the Fabric Sheet.
   Returns: The centerline curves.
  GetWireCenterlines(self: FabricSheet) -> IList[Curve]
  
   Gets a list of curves representing the wires centerlines of the Fabric Sheet in 
    the both distribution directions.
  
   Returns: The centerline curves.
  """
  pass
 def IsCoverOffsetValid(self,coverOffset):
  """
  IsCoverOffsetValid(self: FabricSheet,coverOffset: float) -> bool
  
   Identifies if the specified value is valid for use as a cover offset.
  
   coverOffset: The cover offset value.
   Returns: True if the value is valid,false if the value is invalid.
  """
  pass
 def IsSingleFabricSheetWithinHost(self,hostElement,transform):
  """
  IsSingleFabricSheetWithinHost(self: FabricSheet,hostElement: Element,transform: Transform) -> bool
  
   Identifies if the specified single Fabric Sheet position is within the host.
  
   hostElement: A structural element that will host the Fabric Sheet.
   transform: The transform that defines the placement of the instance single Fabric Sheet.
   Returns: True if the single Fabric Sheet instance is within the host,false if the 
    single Fabric Sheet instance is out of host.
  """
  pass
 @staticmethod
 def IsValidHost(*__args):
  """
  IsValidHost(document: Document,concreteHostElementId: ElementId) -> bool
  
   Checks whether an element is a valid host for fabric sheet.
  
   document: The document.
   concreteHostElementId: The elementId to check.
   Returns: True if the element is a valid host for fabric sheet,false otherwise.
  IsValidHost(host: Element) -> bool
  
   Checks whether an element is a valid host for fabric sheet.
  
   host: The element to check.
   Returns: True if the element is a valid host for fabric sheet,false otherwise.
  """
  pass
 def PlaceInHost(self,hostElement,transform):
  """
  PlaceInHost(self: FabricSheet,hostElement: Element,transform: Transform)
   Inserts the single Fabric Sheet instance into the host element.
  
   hostElement: A structural element that will host the Fabric Sheet. The element must support 
    fabric hosting.
  
   transform: The transform that defines the placement of the instance single Fabric Sheet.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def SetBendProfile(self,bendProfile):
  """
  SetBendProfile(self: FabricSheet,bendProfile: CurveLoop)
   Sets new profile that defines the shape of the Fabric Sheet bending.
  
   bendProfile: A profile that defines the bending shape of the fabric sheet.
     The profile 
    can be provided without fillets (eg. for L shape,only two lines not two lines 
    and one arc),if so,
     then fillets (in example one arc) will be 
    automatically generated basing on the Bend Diameter parameter defined in the 
    Fabric Wire system family.
     If the provided profile has no corners (has a 
    tangent defined at each point except the ends),no fillets will be generated.
   
      The provided profile defines the center-curve of a wire.
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetSegmentLength(self,segmentParameterId,value):
  """
  SetSegmentLength(self: FabricSheet,segmentParameterId: ElementId,value: float)
   Sets the value of the bent fabric sheet segment(like A,B,C,D etc.)
  
   segmentParameterId: The segment ID of the bent fabric sheet.
   value: The length value to set
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
 BendFinalLoopOrientationVector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Direction of local Fabric Sheet Y axis in bending polyline LCS.

Get: BendFinalLoopOrientationVector(self: FabricSheet) -> XYZ

"""

 BentFabricBendDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies which wire direction of the fabric sheet is bent.

Get: BentFabricBendDirection(self: FabricSheet) -> BentFabricBendDirection

Set: BentFabricBendDirection(self: FabricSheet)=value
"""

 BentFabricLongitudinalCutLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies the cut length of the fabric sheet perpendicular to the bend edge.

Get: BentFabricLongitudinalCutLength(self: FabricSheet) -> float

Set: BentFabricLongitudinalCutLength(self: FabricSheet)=value
"""

 BentFabricStraightWiresLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies the location of straight bars with respect to bent bars in the fabric sheet.

Get: BentFabricStraightWiresLocation(self: FabricSheet) -> BentFabricStraightWiresLocation

Set: BentFabricStraightWiresLocation(self: FabricSheet)=value
"""

 BentFabricWiresOrientation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies the location of the straight bars in the fabric sheet.

Get: BentFabricWiresOrientation(self: FabricSheet) -> BentFabricWiresOrientation

Set: BentFabricWiresOrientation(self: FabricSheet)=value
"""

 CoverOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The additional cover offset of the Fabric Sheet.

Get: CoverOffset(self: FabricSheet) -> float

Set: CoverOffset(self: FabricSheet)=value
"""

 CutOverallLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The sheet length after cutting has taken place.

Get: CutOverallLength(self: FabricSheet) -> float

"""

 CutOverallWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The sheet length after cutting has taken place.

Get: CutOverallWidth(self: FabricSheet) -> float

"""

 CutSheetMass=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The sheet mass after cutting has taken place.

Get: CutSheetMass(self: FabricSheet) -> float

"""

 FabricAreaOwnerId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Fabric Area Id.

Get: FabricAreaOwnerId(self: FabricSheet) -> ElementId

"""

 FabricHostReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Controls if Single Fabric Sheet should be cut by the Host Cover

Get: FabricHostReference(self: FabricSheet) -> FabricHostReference

Set: FabricHostReference(self: FabricSheet)=value
"""

 FabricLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Fabric Sheet location in the host.

Get: FabricLocation(self: FabricSheet) -> FabricLocation

Set: FabricLocation(self: FabricSheet)=value
"""

 FabricNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies the numerical parameter assigned to the fabric sheet and any sheet of the same type,dimension,material,shape,and partition.

Get: FabricNumber(self: FabricSheet) -> str

"""

 HostId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The structure element that contains the Fabric Sheet.

Get: HostId(self: FabricSheet) -> ElementId

"""

 IsBent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type of fabric sheet. True for bent fabric sheet,false for flat fabric sheet.

Get: IsBent(self: FabricSheet) -> bool

"""

 SketchId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the Sketch element for this element.

Get: SketchId(self: FabricSheet) -> ElementId

"""


