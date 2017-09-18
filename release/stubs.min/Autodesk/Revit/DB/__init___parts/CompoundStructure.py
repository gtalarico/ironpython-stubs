class CompoundStructure(object,IDisposable):
 """ Describes the internal structure of a wall,floor,roof or ceiling. """
 def AddWallSweep(self,wallSweepInfo):
  """
  AddWallSweep(self: CompoundStructure,wallSweepInfo: WallSweepInfo)

   Adds a new wall sweep or reveal to the compound structure.

  

   wallSweepInfo: The wall sweep info to create a wall sweep.
  """
  pass
 def AssociateRegionWithLayer(self,regionId,layerIdx):
  """
  AssociateRegionWithLayer(self: CompoundStructure,regionId: int,layerIdx: int)

   Associates a region with a layer.

  

   regionId: The id of a region.

   layerIdx: The index of a layer in this CompoundStructure.
  """
  pass
 def CanLayerBeStructuralMaterial(self,layerIndex):
  """
  CanLayerBeStructuralMaterial(self: CompoundStructure,layerIndex: int) -> bool

  

   Identifies if the input layer can be designated as defining the structural 

    material for this structure.

  

  

   layerIndex: Index of a layer in the CompoundStructure.

   Returns: True if the input layer may be used to define the structural material and false 

    otherwise.
  """
  pass
 def CanLayerBeVariable(self,variableLayerIndex):
  """
  CanLayerBeVariable(self: CompoundStructure,variableLayerIndex: int) -> bool

  

   Identifies if the input layer can be designated as a variable thickness layer.

  

   variableLayerIndex: Index of a layer in the CompoundStructure.

   Returns: True if the input layer may be a variable thickness layer and false otherwise.
  """
  pass
 def CanLayerWidthBeNonZero(self,layerIdx):
  """
  CanLayerWidthBeNonZero(self: CompoundStructure,layerIdx: int) -> bool

  

   Identifies if changing the width of an existing layer from zero to a positive 

    value will create a rectangular region.

  

  

   layerIdx: The index of a CompoundStructureLayer.
  """
  pass
 def ChangeRegionWidth(self,regionId,newWidth):
  """
  ChangeRegionWidth(self: CompoundStructure,regionId: int,newWidth: float) -> bool

  

   Adjust the width of an existing simple region.

  

   regionId: The id of a region.

   newWidth: The desired width of the specified region.

   Returns: True if newWidth is zero and the region was deleted.
  """
  pass
 def ClearWallSweeps(self,wallSweepType):
  """
  ClearWallSweeps(self: CompoundStructure,wallSweepType: WallSweepType)

   Removes all sweeps or reveals from the compound structure.

  

   wallSweepType: The type of a wall sweep.
  """
  pass
 @staticmethod
 def CreateSimpleCompoundStructure(layers):
  """ CreateSimpleCompoundStructure(layers: IList[CompoundStructureLayer]) -> CompoundStructure """
  pass
 @staticmethod
 def CreateSingleLayerCompoundStructure(*__args):
  """
  CreateSingleLayerCompoundStructure(layerFunction: MaterialFunctionAssignment,width: float,materialId: ElementId) -> CompoundStructure

  

   Creates a CompoundStructure containing a single layer.

  

   layerFunction: The function of the single layer.

   width: The width of the single layer.

   materialId: The ElementId of the material for the single layer.

   Returns: The newly created compound structure.

  CreateSingleLayerCompoundStructure(sampleHeight: float,layerFunction: MaterialFunctionAssignment,width: float,materialId: ElementId) -> CompoundStructure

  

   Creates a vertically compound CompoundStructure with one layer.

  

   sampleHeight: The sample height of this vertically compound structure.

   layerFunction: The function of the single layer.

   width: The width of the single layer.

   materialId: The ElementId of the material for the single layer.

   Returns: The newly created compound structure.
  """
  pass
 def DeleteLayer(self,layerIdx):
  """
  DeleteLayer(self: CompoundStructure,layerIdx: int) -> bool

  

   Deletes the specified layer from this CompoundStructure.

  

   layerIdx: The layer index is zero based. It counts from the exterior of wall and from the 

    top of roofs,floors and ceilings.

  

   Returns: True if the layer was successfully deleted,and false otherwise.
  """
  pass
 def Dispose(self):
  """ Dispose(self: CompoundStructure) """
  pass
 def FindEnclosingRegionAndSegments(self,gridUV,splitDirection,segmentId1,segmentId2):
  """
  FindEnclosingRegionAndSegments(self: CompoundStructure,gridUV: UV,splitDirection: RectangularGridSegmentOrientation) -> (int,int,int)

  

   Given a pair of grid coordinates,and a direction for splitting,returns the 

    enclosing region and the two segments

     intersected by a line through the 

    grid point.

  

  

   gridUV: Coordinates of a point in the rectangular grid of this compound structure.

   splitDirection: Specifies the direction of the split.

   Returns: Returns the id of the enclosing region,and -1 if no region encloses the point.
  """
  pass
 def GetAdjacentRegions(self,segmentId):
  """
  GetAdjacentRegions(self: CompoundStructure,segmentId: int) -> IList[int]

  

   Gets the ids of region bound to a specified segment.

  

   segmentId: The id of a segment in this CompoundStructure.

   Returns: The ids of the regions that are bounded by the specified segment.
  """
  pass
 def GetCoreBoundaryLayerIndex(self,shellLayerType):
  """
  GetCoreBoundaryLayerIndex(self: CompoundStructure,shellLayerType: ShellLayerType) -> int

  

   Returns the index of the layer just below the core boundary.

  

   shellLayerType: If ShellLayerType.Exterior return the index on the exterior side (or top side 

    for a roof,floor,or ceiling type).

     If ShellLayerType.Interior return the 

    index on the interior side (or bottom side for a roof,floor,or ceiling type).

  

   Returns: The index of the layer.
  """
  pass
 def GetDeckEmbeddingType(self,layerIdx):
  """
  GetDeckEmbeddingType(self: CompoundStructure,layerIdx: int) -> StructDeckEmbeddingType

  

   Retrieves the deck embedding type used for the specified structural deck.

  

   layerIdx: Index of a layer in the CompoundStructure.

   Returns: The embedding type of the structural deck associated to the specified layer. 

    Invalid if it is not a structural deck.
  """
  pass
 def GetDeckProfileId(self,layerIdx):
  """
  GetDeckProfileId(self: CompoundStructure,layerIdx: int) -> ElementId

  

   Retrieves the profile loop used for the specified structural deck.

  

   layerIdx: Index of a layer in the CompoundStructure.

   Returns: The element id of a FamilySymbol which contains a profile loop used by a 

    structural deck associated to the specified layer,

     or invalidElementId if 

    isStructuralDeck(layerIdx) is false.
  """
  pass
 def GetExtendableRegionIds(self,top):
  """
  GetExtendableRegionIds(self: CompoundStructure,top: bool) -> IList[int]

  

   Gets the extendable region ids for the compound structure.

  

   top: If true,retrieve ids of regions which are extendable at the top,otherwise

     

    retrieve the ids of regions which are extendable at the bottom.

  

   Returns: An array of region ids which are marked extendable.
  """
  pass
 def GetFirstCoreLayerIndex(self):
  """
  GetFirstCoreLayerIndex(self: CompoundStructure) -> int

  

   Gets the index of the first core layer.

   Returns: The index of the first core layer.
  """
  pass
 def GetLastCoreLayerIndex(self):
  """
  GetLastCoreLayerIndex(self: CompoundStructure) -> int

  

   Gets the index of the last core layer.

   Returns: The index of the last core layer.
  """
  pass
 def GetLayerAssociatedToRegion(self,regionId):
  """
  GetLayerAssociatedToRegion(self: CompoundStructure,regionId: int) -> int

  

   Gets the layer associated to a particular region.

  

   regionId: The id of a region.

   Returns: The index of a layer in this CompoundStructure.
  """
  pass
 def GetLayerFunction(self,layerIdx):
  """
  GetLayerFunction(self: CompoundStructure,layerIdx: int) -> MaterialFunctionAssignment

  

   Retrieves the function of the specified layer.

  

   layerIdx: Index of a layer in the CompoundStructure.

   Returns: The function of the layer.
  """
  pass
 def GetLayers(self):
  """
  GetLayers(self: CompoundStructure) -> IList[CompoundStructureLayer]

  

   A copy of the layers which define this compound structure.

   Returns: The layers,returned in order (Exterior to Interior for walls,top to bottom 

    for roofs,floors or ceilings). The index of each layer in this array

     can 

    be used in other CompoundStructure methods accepting a layer index.
  """
  pass
 def GetLayerWidth(self,layerIdx):
  """
  GetLayerWidth(self: CompoundStructure,layerIdx: int) -> float

  

   Retrieves the width of a specified layer.

  

   layerIdx: Index of a layer in the CompoundStructure.

   Returns: The width of the specified layer.
  """
  pass
 def GetMaterialId(self,layerIdx):
  """
  GetMaterialId(self: CompoundStructure,layerIdx: int) -> ElementId

  

   Retrieves the material element id of a specified layer.

  

   layerIdx: Index of a layer in the CompoundStructure.

   Returns: The material element id.
  """
  pass
 @staticmethod
 def GetMinimumLayerThickness():
  """
  GetMinimumLayerThickness() -> float

  

   Get the minimum allowable layer thickness.

   Returns: The minimum allowable width of a layer in feet.
  """
  pass
 def GetNumberOfShellLayers(self,shellLayerType):
  """
  GetNumberOfShellLayers(self: CompoundStructure,shellLayerType: ShellLayerType) -> int

  

   Retrieves the number of interior or exterior shell layers.

  

   shellLayerType: If ShellLayerType.Exterior return the number of exterior shell layers (or top 

    shell layers for a roof,floor,or ceiling type).

     If 

    ShellLayerType.Interior return the number of interior shell layers (or bottom 

    shell layers for a roof,floor,or ceiling type).

  

   Returns: The number of shell layers in the interior or exterior shell,as specified by 

    shellLayerType.
  """
  pass
 def GetOffsetForLocationLine(self,wallLocationLine):
  """
  GetOffsetForLocationLine(self: CompoundStructure,wallLocationLine: WallLocationLine) -> float

  

   Returns the offset from the center of the compound structure to the given 

    location line value.

  

  

   wallLocationLine: The alignment type of the wall's location line.

   Returns: The offset.
  """
  pass
 def GetPreviousNonZeroLayerIndex(self,thisIdx):
  """
  GetPreviousNonZeroLayerIndex(self: CompoundStructure,thisIdx: int) -> int

  

   Returns the index of the nearest non-zero width layer before this layer.

  

   thisIdx: The layer from which to look for a non-zero width layer.

   Returns: The index of the layer found.
  """
  pass
 def GetRegionEnvelope(self,regionId):
  """
  GetRegionEnvelope(self: CompoundStructure,regionId: int) -> BoundingBoxUV

  

   Gets the envelope that a specified region spans.

  

   regionId: The id of the region.

   Returns: The envelope of the region.
  """
  pass
 def GetRegionIds(self):
  """
  GetRegionIds(self: CompoundStructure) -> IList[int]

  

   Gets the region ids of this compound structure.

   Returns: The ids of the regions defining this CompoundStructure.
  """
  pass
 def GetRegionsAlongLevel(self,height):
  """
  GetRegionsAlongLevel(self: CompoundStructure,height: float) -> IList[int]

  

   Returns the ids of the regions encountered as the vertically compound structure 

    is traversed

     at a constant height above the bottom a wall to which this 

    structure is applied.

  

  

   height: Distance from the bottom of the wall.

   Returns: The ids of the regions intersected by the specified line.
  """
  pass
 def GetRegionsAssociatedToLayer(self,layerIdx):
  """
  GetRegionsAssociatedToLayer(self: CompoundStructure,layerIdx: int) -> IList[int]

  

   Gets the set of region ids associated to a particular layer.

  

   layerIdx: The index of a layer in this CompoundStructure.

   Returns: An array of region ids which are associated to the specified layer.
  """
  pass
 def GetSegmentCoordinate(self,segmentId):
  """
  GetSegmentCoordinate(self: CompoundStructure,segmentId: int) -> float

  

   Gets the coordinate of a segment.

  

   segmentId: The id of a segment in this CompoundStructure.

   Returns: The local coordinates of the specified segment.
  """
  pass
 def GetSegmentEndPoints(self,segmentId,regionId,end1,end2):
  """
  GetSegmentEndPoints(self: CompoundStructure,segmentId: int,regionId: int) -> (UV,UV)

  

   Gets the end points of a segment.

  

   segmentId: The segment id.

   regionId: The region id.
  """
  pass
 def GetSegmentIds(self):
  """
  GetSegmentIds(self: CompoundStructure) -> IList[int]

  

   Gets the segment ids of this compound structure.

   Returns: The ids of the segments which form the boundary of the regions of this 

    CompoundStructure.
  """
  pass
 def GetSegmentOrientation(self,segmentId):
  """
  GetSegmentOrientation(self: CompoundStructure,segmentId: int) -> RectangularGridSegmentOrientation

  

   Gets the orientation of a segment.

  

   segmentId: The id of a segment in this CompoundStructure.

   Returns: The orientation of the specified segment.
  """
  pass
 def GetSimpleCompoundStructure(self,wallHeight,distAboveBase):
  """
  GetSimpleCompoundStructure(self: CompoundStructure,wallHeight: float,distAboveBase: float) -> CompoundStructure

  

   Takes a horizontal slice through a sample wall to which this CompoundStructure 

    is applied

     and returns a simple compound structure which describes that 

    slice,i.e. a series of

     parallel layers.

  

  

   wallHeight: The height of the wall.

   distAboveBase: The distance from the base of the wall at which to take the section.

     If 

    distAboveBase < 0,then internally distAboveBase=0 is used.

     If 

    distAboveBase > wallHeight,then internally distAboveBase=wallHeight is used.

  

   Returns: A simple CompoundStructure representing a series of parallel layers.
  """
  pass
 def GetWallSweepsInfo(self,wallSweepType):
  """
  GetWallSweepsInfo(self: CompoundStructure,wallSweepType: WallSweepType) -> IList[WallSweepInfo]

  

   Obtains a list of the intrinsic wall sweeps or reveals in this 

    CompoundStructure.

  

  

   wallSweepType: Whether to obtain wall sweeps or reveals.

   Returns: An array which describes the intrinsic wall sweeps or reveals.
  """
  pass
 def GetWidth(self,regionId=None):
  """
  GetWidth(self: CompoundStructure,regionId: int) -> float

  

   Computes the width of the envelope (2d bounding box) of the specified region.

  

   regionId: The id of a region in this vertically compound structure.

   Returns: The width of the envelope (2d bounding box) of the region.

  GetWidth(self: CompoundStructure) -> float

  

   The width implied by this compound structure.

   Returns: The width of a host object with this compound structure.
  """
  pass
 def IsCoreLayer(self,layerIdx):
  """
  IsCoreLayer(self: CompoundStructure,layerIdx: int) -> bool

  

   Checks if the specified layer is a core layer.

  

   layerIdx: The index of a layer in this CompoundStructure.

   Returns: Returns true if the layer is within the core layer boundary,false if it is in 

    the interior or exterior shell layers.
  """
  pass
 def IsEqual(self,otherStructure):
  """
  IsEqual(self: CompoundStructure,otherStructure: CompoundStructure) -> bool

  

   Checks whether this CompoundStructure is the same as another CompoundStructure.

  

   otherStructure: A CompoundStructure.

   Returns: True if the two CompoundStructures are the same,and false otherwise.
  """
  pass
 def IsLayerValid(self,layerIdx,layer):
  """
  IsLayerValid(self: CompoundStructure,layerIdx: int,layer: CompoundStructureLayer) -> bool

  

   Verifies that the data in this layer is internally consistent.

  

   layerIdx: The index of the layer in the compound structure to be set.

   layer: The layer to be set.

   Returns: True if the layer is internally consistent,false if the layer is not 

    internally consistent.
  """
  pass
 def IsRectangularRegion(self,regionId):
  """
  IsRectangularRegion(self: CompoundStructure,regionId: int) -> bool

  

   Determines whether the specified region is rectangular.

  

   regionId: The id of a region.

   Returns: True if the specified region is a rectangle,false otherwise.
  """
  pass
 def IsSimpleRegion(self,regionId):
  """
  IsSimpleRegion(self: CompoundStructure,regionId: int) -> bool

  

   Determines whether the region is a simple region in this CompoundStructure.

  

   regionId: The id of a region in this vertically compound structure.

   Returns: True if the region is simple,false otherwise.
  """
  pass
 def IsStructuralDeck(self,layerIdx):
  """
  IsStructuralDeck(self: CompoundStructure,layerIdx: int) -> bool

  

   Determines whether a specified layer is a structural deck.

  

   layerIdx: Index of a layer in the CompoundStructure.

   Returns: True if specified layer is a structural deck,and false otherwise.
  """
  pass
 def IsValid(self,doc,errMap,twoLayerErrorsMap):
  """ IsValid(self: CompoundStructure,doc: Document) -> (bool,IDictionary[int,CompoundStructureError],IDictionary[int,int]) """
  pass
 def IsValidRegionId(self,regionId):
  """
  IsValidRegionId(self: CompoundStructure,regionId: int) -> bool

  

   Determines whether the specified integer is actually the id of a region in this 

    CompoundStructure.

  

  

   regionId: The id of a region in this vertically compound structure.

   Returns: True if the region is valid,false otherwise.
  """
  pass
 def IsValidSampleHeight(self,height):
  """
  IsValidSampleHeight(self: CompoundStructure,height: float) -> bool

  

   Is the specified height a valid sample height for this compound structure?
  """
  pass
 def IsValidSegmentId(self,segmentId):
  """
  IsValidSegmentId(self: CompoundStructure,segmentId: int) -> bool

  

   Determines whether the specified integer is actually the id of a segment in 

    this CompoundStructure.

  

  

   segmentId: The id of a segment in this CompoundStructure.

   Returns: True if the specified segment is valid,false otherwise.
  """
  pass
 def IsVerticallyHomogeneous(self):
  """
  IsVerticallyHomogeneous(self: CompoundStructure) -> bool

  

   Indicates whether this CompoundStructure represents a single set of parallel 

    layers.

  

   Returns: True if this CompoundStructure represents a series of parallel layers that 

    stretch from bottom to top,false otherwise.
  """
  pass
 def MergeRegionsAdjacentToSegment(self,segmentId,layerIdxForMergedRegion):
  """
  MergeRegionsAdjacentToSegment(self: CompoundStructure,segmentId: int,layerIdxForMergedRegion: int) -> int

  

   Merges the two regions which share the specified segment.

  

   segmentId: The id of a segment in the underlying grid.

   layerIdxForMergedRegion: The index of the layer to which the resulting region will be associated.

   Returns: The id of the resulting region. If -1 is returned,then the operation would 

    have produced

     an invalid region and was not performed.
  """
  pass
 def ParticipatesInWrapping(self,layerIdx):
  """
  ParticipatesInWrapping(self: CompoundStructure,layerIdx: int) -> bool

  

   Identifies if a layer is included in wrapping at inserts and ends.

  

   layerIdx: The index of the layer.

   Returns: If true,then the layer participates in wrapping at inserts and openings. If 

    false,the layer will not

     participate in wrapping.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: CompoundStructure,disposing: bool) """
  pass
 def RemoveWallSweep(self,wallSweepType,id):
  """
  RemoveWallSweep(self: CompoundStructure,wallSweepType: WallSweepType,id: int)

   Removes a single sweep or reveal from the compound structure.

  

   wallSweepType: The type of a wall sweep.

   id: The id of the sweep or reveal to remove.
  """
  pass
 def SetDeckEmbeddingType(self,layerIdx,embedType):
  """
  SetDeckEmbeddingType(self: CompoundStructure,layerIdx: int,embedType: StructDeckEmbeddingType)

   Sets the deck embedding type to use for the specified structural deck.

  

   layerIdx: Index of a layer in the CompoundStructure.

   embedType: The embedding type to be used by the specified layer if it is a structural deck.
  """
  pass
 def SetDeckProfileId(self,layerIdx,profileId):
  """
  SetDeckProfileId(self: CompoundStructure,layerIdx: int,profileId: ElementId)

   Sets the profile loop to use for the specified structural deck.

  

   layerIdx: Index of a layer in the CompoundStructure.

   profileId: The element id of a FamilySymbol which contains a profile loop to be used by 

    the specified layer if it is a structural deck.
  """
  pass
 def SetExtendableRegionIds(self,top,regionIds):
  """ SetExtendableRegionIds(self: CompoundStructure,top: bool,regionIds: IList[int]) """
  pass
 def SetLayer(self,layerIdx,layer):
  """
  SetLayer(self: CompoundStructure,layerIdx: int,layer: CompoundStructureLayer)

   Sets a single layer for this CompoundStructure.

  

   layerIdx: The index of a layer. This should range from 0 to the number of layers - 1.

   layer: The layer to be set.
  """
  pass
 def SetLayerFunction(self,layerIdx,function):
  """
  SetLayerFunction(self: CompoundStructure,layerIdx: int,function: MaterialFunctionAssignment)

   Sets the function of the specified layer.

  

   layerIdx: Index of a layer in the CompoundStructure.

   function: The function of the layer.
  """
  pass
 def SetLayers(self,layers):
  """ SetLayers(self: CompoundStructure,layers: IList[CompoundStructureLayer]) """
  pass
 def SetLayerWidth(self,layerIdx,width):
  """
  SetLayerWidth(self: CompoundStructure,layerIdx: int,width: float)

   Sets the width of a specified layer.

  

   layerIdx: Index of a layer in the CompoundStructure.

   width: The new width of the specified layer.
  """
  pass
 def SetMaterialId(self,layerIdx,materialId):
  """
  SetMaterialId(self: CompoundStructure,layerIdx: int,materialId: ElementId)

   Sets a material element for a specified layer.

  

   layerIdx: Index of a layer in the CompoundStructure.

   materialId: The ElementId of a Material element.
  """
  pass
 def SetNumberOfShellLayers(self,shellLayerType,numLayers):
  """
  SetNumberOfShellLayers(self: CompoundStructure,shellLayerType: ShellLayerType,numLayers: int)

   Sets the number of interior or exterior shell layers.

  

   shellLayerType: If ShellLayerType.Exterior set the number of exterior shell layers (or top 

    shell layers for a roof,floor,or ceiling type).

     If 

    ShellLayerType.Interior set the number of interior shell layers (or bottom 

    shell layers for a roof,floor,or ceiling type).

  

   numLayers: The number of layers to be in the specified shell.
  """
  pass
 def SetParticipatesInWrapping(self,layerIdx,participatesInWrapping):
  """
  SetParticipatesInWrapping(self: CompoundStructure,layerIdx: int,participatesInWrapping: bool)

   Assigns if a layer is included in wrapping at inserts and ends.

  

   layerIdx: The index of the layer.

   participatesInWrapping: True if the specified layer will participate in wrapping at inserts and ends,

    false otherwise.
  """
  pass
 def SplitRegion(self,gridUV,splitDirection,newSegmentId=None):
  """
  SplitRegion(self: CompoundStructure,gridUV: UV,splitDirection: RectangularGridSegmentOrientation) -> (int,int)

  

   Splits the region which contains the specified grid point by a line with the 

    specified direction.

  

  

   gridUV: Coordinates of a point in the rectangular grid of this compound structure.

   splitDirection: Specifies the direction of the split.

   Returns: The id of the region created by this operation.

  SplitRegion(self: CompoundStructure,gridUV: UV,splitDirection: RectangularGridSegmentOrientation) -> int

  

   Splits the region which contains the specified grid point by a line with the 

    specified direction.

  

  

   gridUV: Coordinates of a point in the rectangular grid of this compound structure.

   splitDirection: Specifies the direction of the split.

   Returns: The id of the region created by this operation.
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 CutoffHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Horizontal segments below or at the cutoff height have their distance to the wall bottom fixed,those above

   have their distance to the wall top fixed.



Get: CutoffHeight(self: CompoundStructure) -> float



Set: CutoffHeight(self: CompoundStructure)=value

"""

 EndCap=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates the end cap condition defining which shell layers will participate in end wrapping.



Get: EndCap(self: CompoundStructure) -> EndCapCondition



Set: EndCap(self: CompoundStructure)=value

"""

 HasStructuralDeck=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Checks if the compound structure has a structural deck.



Get: HasStructuralDeck(self: CompoundStructure) -> bool



"""

 IsEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Checks whether this CompoundStructure is empty.



Get: IsEmpty(self: CompoundStructure) -> bool



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: CompoundStructure) -> bool



"""

 IsVerticallyCompound=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if this CompoundStructure represents a layout that is more complicated than a simple set of parallel layers.



Get: IsVerticallyCompound(self: CompoundStructure) -> bool



"""

 LayerCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the number of layers contained in this CompoundStructure.



Get: LayerCount(self: CompoundStructure) -> int



"""

 MinimumSampleHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The minimum sample height determined by the current sample height and the horizontal segments.



Get: MinimumSampleHeight(self: CompoundStructure) -> float



"""

 OpeningWrapping=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates the opening wrapping condition defining which shell layers of a wall,in plan view,wrap at inserts and openings.



Get: OpeningWrapping(self: CompoundStructure) -> OpeningWrappingCondition



Set: OpeningWrapping(self: CompoundStructure)=value

"""

 SampleHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The sample height is the presumed height of the wall to which the data in this CompoundStructure is applied.



Get: SampleHeight(self: CompoundStructure) -> float



Set: SampleHeight(self: CompoundStructure)=value

"""

 StructuralMaterialIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates the layer whose material defines the structural properties of the type for the purposes of analysis.



Get: StructuralMaterialIndex(self: CompoundStructure) -> int



Set: StructuralMaterialIndex(self: CompoundStructure)=value

"""

 VariableLayerIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates the index of the layer which is designated as variable.



Get: VariableLayerIndex(self: CompoundStructure) -> int



Set: VariableLayerIndex(self: CompoundStructure)=value

"""


