class MassSurfaceData(Element,IDisposable):
 """ Holds properties and other data about a face in the MassEnergyAnalyticalModel element. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetFaceReferences(self):
  """
  GetFaceReferences(self: MassSurfaceData) -> IList[Reference]
  
   Gets References to the faces that the MassSurfaceData provides properties for.
   Returns: Returns an array of References to Faces that the MassSurfaceData provides 
    properties for.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
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
 Area=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Area of the references that the MassSurfaceData provides properties for.

Get: Area(self: MassSurfaceData) -> float

"""

 CategoryIdForConceptualSurfaceType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the mass subcategory ElementId used for ConceptualSurfaceType for this MassSurfaceData.

Get: CategoryIdForConceptualSurfaceType(self: MassSurfaceData) -> ElementId

"""

 ConceptualConstructionId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the conceptual construction associated with the reference surface.

Get: ConceptualConstructionId(self: MassSurfaceData) -> ElementId

Set: ConceptualConstructionId(self: MassSurfaceData)=value
"""

 IsConceptualConstructionByEnergyData=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True when the ConceptualConstructionType id is synchronized to the EnergyDataSettings.
   False when the ConceptualConstructionType id is overridden for this MassSurfaceData.

Get: IsConceptualConstructionByEnergyData(self: MassSurfaceData) -> bool

Set: IsConceptualConstructionByEnergyData(self: MassSurfaceData)=value
"""

 IsGlazingShaded=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if shade geometry is auto-generated on the top edge of auto-generated glazing.

Get: IsGlazingShaded(self: MassSurfaceData) -> bool

Set: IsGlazingShaded(self: MassSurfaceData)=value
"""

 IsSlab=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if a floor is a slab.

Get: IsSlab(self: MassSurfaceData) -> bool

"""

 IsUnderground=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the roof,floor,slab,or wall surface reference is underground.

Get: IsUnderground(self: MassSurfaceData) -> bool

Set: IsUnderground(self: MassSurfaceData)=value
"""

 MassLevelDataId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The MassLevelData used when the surface is horizontal,planar,and at the same height as a MassLevelData
   related to the same mass as the referenced face.

Get: MassLevelDataId(self: MassSurfaceData) -> ElementId

"""

 MaterialId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The visualization material used for the surface for displaying the energy analytical model.

Get: MaterialId(self: MassSurfaceData) -> ElementId

Set: MaterialId(self: MassSurfaceData)=value
"""

 MaterialType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """material type of mass zone

Get: MaterialType(self: MassSurfaceData) -> MassSurfaceDataMaterialType

Set: MaterialType(self: MassSurfaceData)=value
"""

 PercentageGlazing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The target percentage of the reference wall surface that is to
   be covered with automatically generated windows. Revit will use this number when
   determining the size,shape,and location of automatically generated windows.

Get: PercentageGlazing(self: MassSurfaceData) -> float

Set: PercentageGlazing(self: MassSurfaceData)=value
"""

 PercentageSkylights=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The target percentage of the reference roof surface that is to
   be covered with automatically generated skylights.  Revit will use this number when
   determining the size,shape,and location of automatically generated skylights.

Get: PercentageSkylights(self: MassSurfaceData) -> float

Set: PercentageSkylights(self: MassSurfaceData)=value
"""

 ReferenceElementId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The ElementId of the element whose face the MassSurfaceData primarily refers to.

Get: ReferenceElementId(self: MassSurfaceData) -> ElementId

"""

 ShadeDepth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """How far any auto-generated shades should extend from the wall surface.

Get: ShadeDepth(self: MassSurfaceData) -> float

Set: ShadeDepth(self: MassSurfaceData)=value
"""

 SillHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The height above the level where the bottoms of auto-generated windows will be located.

Get: SillHeight(self: MassSurfaceData) -> float

Set: SillHeight(self: MassSurfaceData)=value
"""

 SkylightWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The length dimension to be used for the sides of each individual square skylight
   produced in the grid of auto-generated skylights.

Get: SkylightWidth(self: MassSurfaceData) -> float

Set: SkylightWidth(self: MassSurfaceData)=value
"""

 SurfaceDataSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the MassSurfaceData properties are driven by the EnergyDataSettings
   of the Document or are overridden for the surface.

Get: SurfaceDataSource(self: MassSurfaceData) -> MassSurfaceDataSource

Set: SurfaceDataSource(self: MassSurfaceData)=value
"""


