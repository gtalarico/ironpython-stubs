class MassLevelData(Element,IDisposable):
 """
 MassLevelData is a conceptual representation of an occupiable floor (Mass Floor) in a conceptual building model.

    It is defined by associating a particular level with a particular mass element in a Revit project.
 """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def IsEmpty(self):
  """
  IsEmpty(self: MassLevelData) -> bool

  

   Indicates if the MassLevelData (Mass Floor) has a geometrical representation.  

    May not

     if the level does not intersect the mass geometry.

  

   Returns: Returns True if MassLevelData is dimensionless,False otherwise.
  """
  pass
 @staticmethod
 def IsMassFamilyInstance(document,id):
  """
  IsMassFamilyInstance(document: Document,id: ElementId) -> bool

  

   Checks if the ElementId is a mass family instance.

  

   document: The document.

   id: The ElementId to be checked.

   Returns: True if the ElementId is a mass family instance,false otherwise.
  """
  pass
 def IsValidConceptualConstructionTypeElement(self,id):
  """
  IsValidConceptualConstructionTypeElement(self: MassLevelData,id: ElementId) -> bool

  

   Checks if the ElementId is an acceptable conceptual construction type ElementId 

    for the MassLevelData (Mass Floor).

  

  

   id: The ElementId to be checked.

   Returns: True if the ElementId is an acceptable conceptual construction type ElementId,

    false otherwise.
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
 ConceptualConstructionId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The ElementId of the conceptual construction associated with the MassLevelData (Mass Floor).



Get: ConceptualConstructionId(self: MassLevelData) -> ElementId



Set: ConceptualConstructionId(self: MassLevelData)=value

"""

 ConceptualConstructionIsByEnergyData=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the ConceptualConstructionType of the MassLevelData (Mass Floor) is synchronized

   with the EnergyDataSettings or if it overrides those settings.



Get: ConceptualConstructionIsByEnergyData(self: MassLevelData) -> bool



Set: ConceptualConstructionIsByEnergyData(self: MassLevelData)=value

"""

 MaterialId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The ElementId of the visualization material used for the MassLevelData (Mass Floor)



Get: MaterialId(self: MassLevelData) -> ElementId



Set: MaterialId(self: MassLevelData)=value

"""

 MaterialType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the material used for the graphical appearance is by category or a specific material,or

   if the material to be used should be taken from the ConceptualConstructionType of the MassLevelData.



Get: MaterialType(self: MassLevelData) -> MassSurfaceDataMaterialType



Set: MaterialType(self: MassLevelData)=value

"""

 NExteriorSurfaceArea=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The exterior surface area of the volume of the mass between the level of this MassLevelData (Mass Floor) to the next in the mass.



Get: NExteriorSurfaceArea(self: MassLevelData) -> float



"""

 NLevelFafArea=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The surface area of the intersection of the MassLevelData's level with the mass geometry.



Get: NLevelFafArea(self: MassLevelData) -> float



"""

 NLevelPerimeter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The perimeter of the intersection of the MassLevelData's level with the mass geometry.



Get: NLevelPerimeter(self: MassLevelData) -> float



"""

 NVolume=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The volume of from the level of this MassLevelData (Mass Floor) to the next in the mass.



Get: NVolume(self: MassLevelData) -> float



"""

 OwningMassId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The ElementId of the mass that the MassLevelData (Mass Floor) is associated with.



Get: OwningMassId(self: MassLevelData) -> ElementId



"""

 StrUsage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A String which describes the usage or occupancy type of the level of the MassLevelData.



Get: StrUsage(self: MassLevelData) -> str



Set: StrUsage(self: MassLevelData)=value

"""


