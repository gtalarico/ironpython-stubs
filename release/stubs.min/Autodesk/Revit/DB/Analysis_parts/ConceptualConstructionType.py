class ConceptualConstructionType(ElementType,IDisposable):
 """
 This element is used to describe the conceptual physical,construction,and energy properties in a manner

    that can be understood by both the Revit BIM model and Green Building Studio/Green Building XML.

    For serialization
 """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 @staticmethod
 def GetAllConceptualConstructionsForCategory(ccda,massSubCategoryId):
  """
  GetAllConceptualConstructionsForCategory(ccda: Document,massSubCategoryId: ElementId) -> ICollection[ElementId]

  

   Get all the ids of constructions applicable to the input massSubCategory

  

   ccda: The document.

   massSubCategoryId: The ElementId of the mass subcategory.

   Returns: Returns a set of ElementIds that for the ConceptualConstructionTypes that are 

    appropriate for the subcategory.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 @staticmethod
 def GetFloorOrSlabConstructionType(ccda,typeEnum):
  """
  GetFloorOrSlabConstructionType(ccda: Document,typeEnum: ConceptualConstructionFloorSlabType) -> ElementId

  

   Get a Floor or Slab ConceptualConstructionType by its 

    ConceptualConstructionFloorSlabType.

  

  

   ccda: The Document.

   typeEnum: The ConceptualConstructionFloorSlabType to get the ConceptualConstructionType 

    for.

  

   Returns: Returns ElementId of a ConceptualConstructionType.
  """
  pass
 def GetGBSId(self,massSurfaceSubCategoryId):
  """
  GetGBSId(self: ConceptualConstructionType,massSurfaceSubCategoryId: ElementId) -> int

  

   Gets the Green Building Studio identifier associated with the construction.

  

   massSurfaceSubCategoryId: The ElementId of a valid Mass subcategory of a MassSurfaceData.

   Returns: Returns the integer id used to represent the ConceptualConstructionType.
  """
  pass
 @staticmethod
 def GetOpeningConstructionType(ccda,typeEnum):
  """
  GetOpeningConstructionType(ccda: Document,typeEnum: ConceptualConstructionOpeningType) -> ElementId

  

   Get an Opening ConceptualConstructionType by its 

    ConceptualConstructionOpeningType.

  

  

   ccda: The Document.

   typeEnum: The ConceptualConstructionOpeningType to get the ConceptualConstructionType for.

   Returns: Returns ElementId of a ConceptualConstructionType.
  """
  pass
 @staticmethod
 def GetRoofConstructionType(ccda,typeEnum):
  """
  GetRoofConstructionType(ccda: Document,typeEnum: ConceptualConstructionRoofType) -> ElementId

  

   Get a Roof ConceptualConstructionType by its ConceptualConstructionRoofType.

  

   ccda: The Document.

   typeEnum: The ConceptualConstructionRoofType to get the ConceptualConstructionType for.

   Returns: Returns ElementId of a ConceptualConstructionType.
  """
  pass
 @staticmethod
 def GetShadeConstructionType(ccda,typeEnum):
  """
  GetShadeConstructionType(ccda: Document,typeEnum: ConceptualConstructionShadeType) -> ElementId

  

   Get a Shade ConceptualConstructionType by its ConceptualConstructionShadeType.

  

   ccda: The Document.

   typeEnum: The ConceptualConstructionShadeType to get the ConceptualConstructionType for.

   Returns: Returns ElementId of a ConceptualConstructionType.
  """
  pass
 @staticmethod
 def GetWallConstructionType(ccda,typeEnum):
  """
  GetWallConstructionType(ccda: Document,typeEnum: ConceptualConstructionWallType) -> ElementId

  

   Get a Wall ConceptualConstructionType by its ConceptualConstructionWallType.

  

   ccda: The Document.

   typeEnum: The ConceptualConstructionWallType to get the ConceptualConstructionType for.

   Returns: Returns ElementId of a ConceptualConstructionType.
  """
  pass
 @staticmethod
 def GetWindowOrSkylightConstructionType(ccda,typeEnum):
  """
  GetWindowOrSkylightConstructionType(ccda: Document,typeEnum: ConceptualConstructionWindowSkylightType) -> ElementId

  

   Get a Window or Skylight ConceptualConstructionType by its 

    ConceptualConstructionWindowSkylightType.

  

  

   ccda: The Document.

   typeEnum: The ConceptualConstructionWindowSkylightType to get the 

    ConceptualConstructionType for.

  

   Returns: Returns ElementId of a ConceptualConstructionType.
  """
  pass
 @staticmethod
 def IsValidConceptualConstructionId(ccda,constructionTypeId):
  """
  IsValidConceptualConstructionId(ccda: Document,constructionTypeId: ElementId) -> bool

  

   Indicates if the ElementId is an id of a ConceptualConstructionType.

  

   ccda: The document.

   constructionTypeId: The ElementId of the ConceptualConstructionType.

   Returns: Returns true if is an id of a ConceptualConstructionType,false otherwise.
  """
  pass
 @staticmethod
 def IsValidConceptualConstructionIdForCategory(ccda,constructionTypeId,massSubcategoryId):
  """
  IsValidConceptualConstructionIdForCategory(ccda: Document,constructionTypeId: ElementId,massSubcategoryId: ElementId) -> bool

  

   Indicate if a ConceptualConstruction is appropriate to assign to a 

    MassSurfaceData of a particular Mass subcategory.

  

  

   ccda: The document.

   constructionTypeId: The ElementId of the ConceptualConstructionType.

   massSubcategoryId: The ElementId of the Mass subcategory.

   Returns: Returns true if valid,false otherwise
  """
  pass
 @staticmethod
 def IsValidSubcategoryForMassSurfaceDatas(massSubCategoryId):
  """
  IsValidSubcategoryForMassSurfaceDatas(massSubCategoryId: ElementId) -> bool

  

   Validate if a subcategory is appropriate for assignment to Massing surfaces 

    (MassSurfaceData).

     This is the list of acceptable values:

     

    OST_MassInteriorWallOST_MassExteriorWallOST_MassExteriorWallUndergroundOST_MassR

    oofOST_MassFloorOST_MassSlabOST_MassShadeOST_MassGlazingOST_MassSkylightsOST_Mas

    sOpening

  

  

   massSubCategoryId: The mass sub-category to be checked.

   Returns: True if the mass sub-category falls within the list,false otherwise.
  """
  pass
 def IsValidSurfaceSubcategoryForConstruction(self,massSurfaceSubcategoryId):
  """
  IsValidSurfaceSubcategoryForConstruction(self: ConceptualConstructionType,massSurfaceSubcategoryId: ElementId) -> bool

  

   Indicates if this ConceptualConstructionType is appropriate for the input 

    MassSurfaceData subcategory.

  

  

   massSurfaceSubcategoryId: The ElementId of a Mass subcategory of a MassSurfaceData.

   Returns: Returns true if appropriate for the input subcategory,false otherwise.
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
 MassSurfaceSubCategoryId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The surface type subcategory element id associated with the ConceptualConstructionType.



Get: MassSurfaceSubCategoryId(self: ConceptualConstructionType) -> ElementId



"""

 MaterialId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Material used for visualization of this construction.



Get: MaterialId(self: ConceptualConstructionType) -> ElementId



Set: MaterialId(self: ConceptualConstructionType)=value

"""


