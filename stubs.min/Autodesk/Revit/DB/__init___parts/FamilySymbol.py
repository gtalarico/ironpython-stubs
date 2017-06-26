class FamilySymbol(InsertableObject,IDisposable):
 """ An element that represents a single type with a Family. """
 def Activate(self):
  """
  Activate(self: FamilySymbol)
   Activates the symbol to ensure that its geometry is accessible.
  """
  pass
 def CanHaveStructuralSection(self):
  """
  CanHaveStructuralSection(self: FamilySymbol) -> bool
  
   Identifies if this FamilySymbol can have a structural section.
   Returns: True if the FamilySymbol can have structural section,false otherwise.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetFamilyPointLocations(self):
  """
  GetFamilyPointLocations(self: FamilySymbol) -> IList[FamilyPointLocation]
  
   Returns the Point Locations for the Family Symbol.
  """
  pass
 def GetStructuralSection(self):
  """
  GetStructuralSection(self: FamilySymbol) -> StructuralSection
  
   Gets the structural section from element.
   Returns: The structural section. ll if the family symbol does not contain a structural 
    section.
  """
  pass
 def GetThermalProperties(self):
  """
  GetThermalProperties(self: FamilySymbol) -> FamilyThermalProperties
  
   Gets the thermal properties for the given FamilySymbol.
   Returns: The thermal properties. ll if the family symbol does not contain thermal 
    properties.
  """
  pass
 def HasThermalProperties(self):
  """
  HasThermalProperties(self: FamilySymbol) -> bool
  
   Identifies if this FamilySymbol can include thermal properties.
   Returns: True if the FamilySymbol can include thermal properties,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetStructuralSection(self,structuralSection):
  """
  SetStructuralSection(self: FamilySymbol,structuralSection: StructuralSection)
   Sets the structural section in element.
  
   structuralSection: Structural section with values that will be set.
  """
  pass
 def SetThermalProperties(self,thermalProperties):
  """
  SetThermalProperties(self: FamilySymbol,thermalProperties: FamilyThermalProperties)
   Sets the thermal properties for the given FamilySymbol.
  
   thermalProperties: The new thermal properties. If ll,this unsets custom thermal properties for 
    this FamilySymbol.
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
 Family=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Family object to which the symbol belongs.

Get: Family(self: FamilySymbol) -> Family

"""

 IsActive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies whether the symbol is active.

Get: IsActive(self: FamilySymbol) -> bool

"""

 StructuralMaterialType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property returns the physical material from which the type is made.

Get: StructuralMaterialType(self: FamilySymbol) -> StructuralMaterialType

"""


