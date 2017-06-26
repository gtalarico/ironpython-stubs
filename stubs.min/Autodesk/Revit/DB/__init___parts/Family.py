class Family(Element,IDisposable):
 """ An element that represents a custom family (not a system family) in Autodesk Revit. """
 def CanHaveStructuralSection(self):
  """
  CanHaveStructuralSection(self: Family) -> bool
  
   Identifies if this Family can have a structural section.
   Returns: True if the Family can have structural section,false otherwise.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def ExtractPartAtom(self,xmlFilePath):
  """
  ExtractPartAtom(self: Family,xmlFilePath: str)
   Writes a PartAtom XML from the contents of a family object.
  
   xmlFilePath: The xml file to be saved.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetFamilySymbolIds(self):
  """
  GetFamilySymbolIds(self: Family) -> ISet[ElementId]
  
   Gets the ids of the FamilySymbols owned by this Family.
   Returns: The ids of the FamilySymbols.
  """
  pass
 def GetFamilyTypeParameterValues(self,parameterId):
  """
  GetFamilyTypeParameterValues(self: Family,parameterId: ElementId) -> ISet[ElementId]
  
   Returns all applicable values for a FamilyType parameter of this family.
  
   parameterId: A valid Id of a FamilyType parameter defined for this family.
   Returns: Ids of all applicable Autodesk.Revit.DB.ElementType and 
    Autodesk.Revit.DB.NestedFamilyTypeReference elements.
  """
  pass
 def HasLargeSketches(self):
  """
  HasLargeSketches(self: Family) -> bool
  
   Checks whether the family contains sketches with a large number of elements.
  """
  pass
 def IsAppropriateCategoryId(self,categoryId):
  """
  IsAppropriateCategoryId(self: Family,categoryId: ElementId) -> bool
  
   Identifies if the input category id can be assigned as the new category for 
    this family.
  
  
   categoryId: The category id.
   Returns: True if the input category id can be assigned as the new category for this 
    family,false otherwise.
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
 CurtainPanelHorizontalSpacing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """For Curtain Panel families,the horizontal spacing of the
driving mesh.

Get: CurtainPanelHorizontalSpacing(self: Family) -> float

Set: CurtainPanelHorizontalSpacing(self: Family)=value
"""

 CurtainPanelTilePattern=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """For Curtain Panel families,the choice of tile pattern.

Get: CurtainPanelTilePattern(self: Family) -> TilePatternsBuiltIn

"""

 CurtainPanelVerticalSpacing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """For Curtain Panel families,the vertical spacing of the
driving mesh.

Get: CurtainPanelVerticalSpacing(self: Family) -> float

Set: CurtainPanelVerticalSpacing(self: Family)=value
"""

 FamilyCategory=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves or sets a Category object that represents the category or sub category in which the elements
( this family could generate ) reside.

Get: FamilyCategory(self: Family) -> Category

Set: FamilyCategory(self: Family)=value
"""

 FamilyCategoryId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the category or sub category in which the elements that this family could generate reside.

Get: FamilyCategoryId(self: Family) -> ElementId

Set: FamilyCategoryId(self: Family)=value
"""

 FamilyPlacementType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies the type of placement required by a given family.

Get: FamilyPlacementType(self: Family) -> FamilyPlacementType

"""

 IsConceptualMassFamily=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether the Family is a Conceptual Mass family.

Get: IsConceptualMassFamily(self: Family) -> bool

"""

 IsCurtainPanelFamily=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether the Family is a Curtain Panel family. Curtain Panel family
symbols are used as the ObjectTypes of 
Autodesk.Revit.DB.DividedSurface elements.

Get: IsCurtainPanelFamily(self: Family) -> bool

"""

 IsEditable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if the family supports editing,false otherwise.

Get: IsEditable(self: Family) -> bool

"""

 IsInPlace=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if the family is an in-place family,false if the family is a loadable family.

Get: IsInPlace(self: Family) -> bool

"""

 IsOwnerFamily=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if the family is the owner family for its own editable document,false otherwise.

Get: IsOwnerFamily(self: Family) -> bool

"""

 IsParametric=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies whether the family contains parametric relations
   between some of its elements.

Get: IsParametric(self: Family) -> bool

"""

 IsUserCreated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determine whether the family has been defined by the user.

Get: IsUserCreated(self: Family) -> bool

"""

 ShowSpatialElementCalculationPoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """For families that can have a calculation point for spatial elements,
hide or show the calculation point. 
Autodesk.Revit.DB.SpatialElementCalculationPoint elements.

Get: ShowSpatialElementCalculationPoint(self: Family) -> bool

Set: ShowSpatialElementCalculationPoint(self: Family)=value
"""

 StructuralCodeName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The family's structural code name.

Get: StructuralCodeName(self: Family) -> str

Set: StructuralCodeName(self: Family)=value
"""

 StructuralFamilyNameKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The family's structural section shape name key.

Get: StructuralFamilyNameKey(self: Family) -> str

Set: StructuralFamilyNameKey(self: Family)=value
"""

 StructuralMaterialType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The family's structural material type.

Get: StructuralMaterialType(self: Family) -> StructuralMaterialType

"""

 StructuralSectionShape=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The family's structural section shape.

Get: StructuralSectionShape(self: Family) -> StructuralSectionShape

Set: StructuralSectionShape(self: Family)=value
"""


