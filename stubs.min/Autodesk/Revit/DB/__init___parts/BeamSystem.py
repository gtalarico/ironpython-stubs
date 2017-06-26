class BeamSystem(Element,IDisposable):
 """ An object that represents a BeamSystem within the Autodesk Revit project. """
 @staticmethod
 def BeamBelongsTo(beam):
  """
  BeamBelongsTo(beam: FamilyInstance) -> BeamSystem
  
   Find out the BeamSystem to which the beam belongs.
  
   beam: The beam want to ask.
   Returns: The BeamSystem.
  """
  pass
 @staticmethod
 def Create(document,profile,*__args):
  """
  Create(document: Document,profile: IList[Curve],sketchPlane: SketchPlane,direction: XYZ,is3d: bool) -> BeamSystem
  Create(document: Document,profile: IList[Curve],sketchPlane: SketchPlane,curveIndexForDirection: int) -> BeamSystem
  Create(document: Document,profile: IList[Curve],level: Level,curveIndexForDirection: int,is3d: bool) -> BeamSystem
  Create(document: Document,profile: IList[Curve],level: Level,direction: XYZ,is3d: bool) -> BeamSystem
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 @staticmethod
 def DropBeamSystem(beamSystem):
  """
  DropBeamSystem(beamSystem: BeamSystem)
   Drop beam system,it will disassociate all members from the beam system and 
    delete the beam system.
  
  
   beamSystem: The beam system to be deleted.
  """
  pass
 def GetBeamIds(self):
  """
  GetBeamIds(self: BeamSystem) -> ICollection[ElementId]
  
   Gets all the beams of the BeamSystem.
   Returns: The beam Ids.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
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
 BeamSystemType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves or changes the type of the BeamSystem.

Get: BeamSystemType(self: BeamSystem) -> BeamSystemType

Set: BeamSystemType(self: BeamSystem)=value
"""

 BeamType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves or changes the Beam Type of the BeamSystem.

Get: BeamType(self: BeamSystem) -> FamilySymbol

Set: BeamType(self: BeamSystem)=value
"""

 Direction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Direction of the BeamSystem.

Get: Direction(self: BeamSystem) -> XYZ

"""

 Elevation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves or changes the Elevation of the BeamSystem.

Get: Elevation(self: BeamSystem) -> float

Set: Elevation(self: BeamSystem)=value
"""

 LayoutRule=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves or changes the LayoutRule of the BeamSystem.

Get: LayoutRule(self: BeamSystem) -> LayoutRule

Set: LayoutRule(self: BeamSystem)=value
"""

 Level=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or change the level of the BeamSystem.
When the level is changed,the elevation is changed to make the 
the BeamSystem remain the location.

Get: Level(self: BeamSystem) -> Level

Set: Level(self: BeamSystem)=value
"""

 Profile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieve or set the profile of the BeamSystem.

Get: Profile(self: BeamSystem) -> CurveArray

Set: Profile(self: BeamSystem)=value
"""


