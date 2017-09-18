class FabricArea(Element,IDisposable):
 """ An object that represents an Fabric Area Distribution within the Autodesk Revit project. It is container for Fabric Sheet elements. """
 def CopyCurveLoopsInSketch(self):
  """
  CopyCurveLoopsInSketch(self: FabricArea) -> IList[CurveLoop]

  

   Creates copies of the CurveLoops in the FabricArea sketch.

   Returns: The copy of the curve loops.
  """
  pass
 @staticmethod
 def Create(aDoc,hostElement,*__args):
  """
  Create(aDoc: Document,hostElement: Element,curveLoops: IList[CurveLoop],majorDirection: XYZ,majorDirectionOrigin: XYZ,fabricAreaTypeId: ElementId,fabricSheetTypeId: ElementId) -> FabricArea

  Create(aDoc: Document,hostElement: Element,majorDirection: XYZ,fabricAreaTypeId: ElementId,fabricSheetTypeId: ElementId) -> FabricArea

  

   Creates a FabricArea based on a host boundary.

  

   aDoc: The document.

   hostElement: The element that will host the FabricArea. The host can be a Structural Floor,

    Structural Wall,Structural Slab,or a Part created from a structural layer 

    belonging to one of those element types.

  

   majorDirection: A vector to define the major direction of the FabricArea.

   fabricAreaTypeId: The id of the FabricAreaType.

   fabricSheetTypeId: The id of the FabricSheetType.

   Returns: The newly created FabricArea.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def GetBoundaryCurveIds(self):
  """
  GetBoundaryCurveIds(self: FabricArea) -> IList[ElementId]

  

   Retrieves the identifiers of the set of curves forming the boundary of the 

    Fabric Area.

  

   Returns: A collection of ElementIds of FabricAreaCurve elements.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetFabricSheetElementIds(self):
  """
  GetFabricSheetElementIds(self: FabricArea) -> IList[ElementId]

  

   Retrieves the identifiers of all the FabricSheet Elements in the FabricArea.

   Returns: A collection of ElementIds of FabricSheet elements.
  """
  pass
 def GetReinforcementRoundingManager(self):
  """
  GetReinforcementRoundingManager(self: FabricArea) -> FabricRoundingManager

  

   Returns an object for managing reinforcement rounding override settings.

   Returns: The rounding manager.
  """
  pass
 def GetTotalSheetMass(self):
  """
  GetTotalSheetMass(self: FabricArea) -> float

  

   Calculates the total sheet mass: Volume of Wire * Unit Weight.

   Returns: The total sheet mass.
  """
  pass
 def GetValidViewsForTags(self):
  """
  GetValidViewsForTags(self: FabricArea) -> IList[ElementId]

  

   Gets ids of the views where tags and symbols can be placed for the FabricArea 

    and/or FabricSheets

  

   Returns: The collection of View ElementIds.
  """
  pass
 def IsCoverOffsetValid(self,coverOffset):
  """
  IsCoverOffsetValid(self: FabricArea,coverOffset: float) -> bool

  

   Identifies if the specified value is valid for use as a cover offset.

  

   coverOffset: The cover offset value.

   Returns: True if the value is valid,false if the value is invalid.
  """
  pass
 def IsValidMajorLapSplice(self,majorLapSplice):
  """
  IsValidMajorLapSplice(self: FabricArea,majorLapSplice: float) -> bool

  

   Identifies if the specified value is valid for use as a major lap splice.

  

   majorLapSplice: The major lap splice value.

   Returns: True if the value is valid,false if the value is invalid.
  """
  pass
 def IsValidMinorLapSplice(self,minorLapSplice):
  """
  IsValidMinorLapSplice(self: FabricArea,minorLapSplice: float) -> bool

  

   Identifies if the specified value is valid for use as a minor lap splice.

  

   minorLapSplice: The minor lap splice value.

   Returns: True if the value is valid,false if the value is invalid.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 @staticmethod
 def RemoveFabricReinforcementSystem(doc,system):
  """
  RemoveFabricReinforcementSystem(doc: Document,system: FabricArea) -> IList[ElementId]

  

   Deletes the specified FabricArea,and converts its FabricSheet elements

     to 

    equivalent Single Fabric Sheet elements.

  

  

   doc: The document.

   system: An FabricArea Reinforcement element in the document.

   Returns: The ids of the newly created Single Fabric Sheet elements.
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
 CoverOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The additional cover offset of the fabric distribution.



Get: CoverOffset(self: FabricArea) -> float



Set: CoverOffset(self: FabricArea)=value

"""

 Direction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Major Direction of the Fabric Area.



Get: Direction(self: FabricArea) -> XYZ



"""

 DirectionOrigin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Origin Point of the Major Direction of the Fabric Area.



Get: DirectionOrigin(self: FabricArea) -> XYZ



"""

 FabricAreaType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type of the Fabric Area.



Get: FabricAreaType(self: FabricArea) -> FabricAreaType



"""

 FabricLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Fabric location in the host.



Get: FabricLocation(self: FabricArea) -> FabricLocation



Set: FabricLocation(self: FabricArea)=value

"""

 FabricSheetTypeId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the Fabric Sheet Type for this element.



Get: FabricSheetTypeId(self: FabricArea) -> ElementId



Set: FabricSheetTypeId(self: FabricArea)=value

"""

 HostId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the Host element for the fabric area.



Get: HostId(self: FabricArea) -> ElementId



"""

 LapSplicePosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The fabric lap splice position in the fabric distribution.



Get: LapSplicePosition(self: FabricArea) -> FabricLapSplicePosition



Set: LapSplicePosition(self: FabricArea)=value

"""

 MajorLapSpliceLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The fabric lap splice length in the fabric distribution in the major direction.



Get: MajorLapSpliceLength(self: FabricArea) -> float



Set: MajorLapSpliceLength(self: FabricArea)=value

"""

 MajorSheetAlignment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The fabric sheet alignment in the fabric distribution in the major direction.



Get: MajorSheetAlignment(self: FabricArea) -> FabricSheetAlignment



Set: MajorSheetAlignment(self: FabricArea)=value

"""

 MinorLapSpliceLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The fabric lap splice length in the fabric distribution in the minor direction.



Get: MinorLapSpliceLength(self: FabricArea) -> float



Set: MinorLapSpliceLength(self: FabricArea)=value

"""

 MinorSheetAlignment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The fabric sheet alignment in the fabric distribution in the minor direction.



Get: MinorSheetAlignment(self: FabricArea) -> FabricSheetAlignment



Set: MinorSheetAlignment(self: FabricArea)=value

"""

 SketchId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the Sketch element for this element.



Get: SketchId(self: FabricArea) -> ElementId



"""

 TagViewId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The element of the view in which to tag new members of this element.



Get: TagViewId(self: FabricArea) -> ElementId



Set: TagViewId(self: FabricArea)=value

"""


