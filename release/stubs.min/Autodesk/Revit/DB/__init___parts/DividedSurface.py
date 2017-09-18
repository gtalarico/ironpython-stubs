class DividedSurface(Element,IDisposable):
 """
 An element that represents a mesh on the surface of another element,a family instance,an import instance or a geometry combination,

    and a tile pattern built on that mesh.
 """
 def AddIntersectionElement(self,newIntersectionElemId):
  """
  AddIntersectionElement(self: DividedSurface,newIntersectionElemId: ElementId)

   Adds an intersection element to the divided surface.

  

   newIntersectionElemId: The intersection element to be added.
  """
  pass
 @staticmethod
 def CanBeDivided(document,reference):
  """
  CanBeDivided(document: Document,reference: Reference) -> bool

  

   This returns true if the reference represents a face that can be used to create 

    a divided surface.

  

  

   document: The document.

   reference: The reference.

   Returns: True if the reference can be used to create a divided surface,false otherwise.
  """
  pass
 def CanBeIntersectionElement(self,id):
  """
  CanBeIntersectionElement(self: DividedSurface,id: ElementId) -> bool

  

   Checks if the element can be an intersection reference.

  

   id: The element to be checked.

   Returns: True if the element can be an intersection reference.,false otherwise.
  """
  pass
 @staticmethod
 def Create(document,faceReference):
  """
  Create(document: Document,faceReference: Reference) -> DividedSurface

  

   Creates a new instance of a divided surface with a default layout.

  

   document: The document.

   faceReference: Reference that represents a face.

   Returns: The newly created divided surface.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def GetAllIntersectionElements(self):
  """
  GetAllIntersectionElements(self: DividedSurface) -> ICollection[ElementId]

  

   Gets all intersection elements which produce division lines.

   Returns: The intersection elements.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 @staticmethod
 def GetDividedSurfaceForReference(document,faceReference):
  """
  GetDividedSurfaceForReference(document: Document,faceReference: Reference) -> DividedSurface

  

   Get a divided surface for a given reference.  Returns null if the reference 

    does not host a divided surface.

  

  

   document: The document.

   faceReference: Reference that represents a face.

   Returns: The newly created divided surface.
  """
  pass
 def GetGridNodeLocation(self,gridNode):
  """
  GetGridNodeLocation(self: DividedSurface,gridNode: GridNode) -> GridNodeLocation

  

   Specify whether a particular grid node is 

  interior to the surface,on the 

    boundary,or outside

  the boundary.
  """
  pass
 def GetGridNodeReference(self,gridNode):
  """
  GetGridNodeReference(self: DividedSurface,gridNode: GridNode) -> Reference

  

   Get a reference to the geometric point

  associated with a grid node.
  """
  pass
 def GetGridNodeUV(self,gridNode):
  """
  GetGridNodeUV(self: DividedSurface,gridNode: GridNode) -> UV

  

   Get the position of a grid node in UV

  coordinates in the surface.
  """
  pass
 def GetGridSegmentReference(self,gridNode,gridSegmentDirection):
  """
  GetGridSegmentReference(self: DividedSurface,gridNode: GridNode,gridSegmentDirection: GridSegmentDirection) -> Reference

  

   Get a reference to a line segment connecting

  two adjacent grid nodes.
  """
  pass
 @staticmethod
 def GetReferencesWithDividedSurfaces(host):
  """
  GetReferencesWithDividedSurfaces(host: Element) -> IList[Reference]

  

   For a given host element get references to all the faces that host a divided 

    surface

  

  

   host: The element that hosts the divided surfaces

   Returns: References that host a divided surface
  """
  pass
 def GetTileFamilyInstance(self,gridNode,tileIndex):
  """
  GetTileFamilyInstance(self: DividedSurface,gridNode: GridNode,tileIndex: int) -> FamilyInstance

  

   Get a reference to a tile element

  associated with a given seed node.

   Returns: A FamilyInstance object. Returns ll if

  the ObjectType property is not a 

    FamilySymbol.

  Returns ll

  if the grid node is not a "seed node",or

  if the 

    tile is omitted due to boundary conditions.
  """
  pass
 def GetTileReference(self,gridNode,tileIndex):
  """
  GetTileReference(self: DividedSurface,gridNode: GridNode,tileIndex: int) -> Reference

  

   Get a reference to one of the tile surfaces

  associated with a given seed node.

  

   tileIndex: An integer between 0 and T-1,

  where T is 

    Autodesk.Revit.DB.TilePattern.TilesPerSeedNode.

  

   Returns: A reference to a Face (surface). Returns ll

  if the grid node is not a "seed 

    node",or

  if the tile is omitted due to boundary conditions.
  """
  pass
 def IsSeedNode(self,gridNode):
  """
  IsSeedNode(self: DividedSurface,gridNode: GridNode) -> bool

  

   Reports whether a grid node is a "seed node," a node

  that is associated with 

    one or more tiles.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def RemoveAllIntersectionElements(self):
  """
  RemoveAllIntersectionElements(self: DividedSurface)

   Removes all the intersection elements from a divided surface.
  """
  pass
 def RemoveIntersectionElement(self,referenceElemIdToRemove):
  """
  RemoveIntersectionElement(self: DividedSurface,referenceElemIdToRemove: ElementId)

   Removes an intersection element from a divided surface.

  

   referenceElemIdToRemove: The intersection element to be removed.
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
 AllGridRotation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Angle of rotation applied to the U- and V- directions together.



Get: AllGridRotation(self: DividedSurface) -> float



Set: AllGridRotation(self: DividedSurface)=value

"""

 BorderTile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines the handling of tiles that overlap the surface's

boundary.



Get: BorderTile(self: DividedSurface) -> BorderTile



Set: BorderTile(self: DividedSurface)=value

"""

 ComponentRotation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The rotation of the pattern by a multiple

of 90 degrees.



Get: ComponentRotation(self: DividedSurface) -> ComponentRotation



Set: ComponentRotation(self: DividedSurface)=value

"""

 Host=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The element whose surface has been divided.



Get: Host(self: DividedSurface) -> Element



"""

 HostReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A reference to the divided face on the host.



Get: HostReference(self: DividedSurface) -> Reference



"""

 IsComponentFlipped=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether the pattern is flipped.



Get: IsComponentFlipped(self: DividedSurface) -> bool



Set: IsComponentFlipped(self: DividedSurface)=value

"""

 IsComponentMirrored=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether the pattern is mirror-imaged.



Get: IsComponentMirrored(self: DividedSurface) -> bool



Set: IsComponentMirrored(self: DividedSurface)=value

"""

 NumberOfUGridlines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get the number of U-gridlines used on the

surface.



Get: NumberOfUGridlines(self: DividedSurface) -> int



"""

 NumberOfVGridlines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get the number of V-gridlines used on the

surface.



Get: NumberOfVGridlines(self: DividedSurface) -> int



"""

 UPatternIndent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The offset applied to the pattern by an

integral number of grid nodes in the U-direction.



Get: UPatternIndent(self: DividedSurface) -> int



Set: UPatternIndent(self: DividedSurface)=value

"""

 USpacingRule=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Access to the rule for laying out the first series of equidistant

parallel lines on the surface.



Get: USpacingRule(self: DividedSurface) -> SpacingRule



"""

 VPatternIndent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The offset applied to the pattern by an 

integral number of grid nodes in the V-direction.



Get: VPatternIndent(self: DividedSurface) -> int



Set: VPatternIndent(self: DividedSurface)=value

"""

 VSpacingRule=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Access to the rule for laying out the second series of equidistant

parallel lines on the surface.



Get: VSpacingRule(self: DividedSurface) -> SpacingRule



"""


