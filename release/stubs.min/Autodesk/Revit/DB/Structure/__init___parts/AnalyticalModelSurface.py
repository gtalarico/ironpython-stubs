class AnalyticalModelSurface(AnalyticalModel,IDisposable):
 """ An element that represents a surface in the structural analytical model. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetHiddenOpenings(self,openingsIds):
  """ GetHiddenOpenings(self: AnalyticalModelSurface) -> ICollection[ElementId] """
  pass
 def GetLocalCoordinateSystem(self,point=None):
  """
  GetLocalCoordinateSystem(self: AnalyticalModelSurface,point: XYZ) -> Transform

  

   Gets the local coordinate system (LCS) reflects analytical model orientation at 

    the specified point.

  

  

   point: The point on the analytical model surface element.

   Returns: Transformation matrix.

     x - longitudinal axis,y - transversal,section - 

    horizontal,strong axis,z - transversal,section - vertical,weak axis,origin 

    - base point of LCS.
  """
  pass
 def GetLoops(self,loopType):
  """
  GetLoops(self: AnalyticalModelSurface,loopType: AnalyticalLoopType) -> IList[CurveLoop]

  

   Retrieves Analytical Model Loops with respect to the loopType.

   Returns: Loops that satisfy loopType criteria are returned.
  """
  pass
 def GetOpeningLoops(self,openingId):
  """
  GetOpeningLoops(self: AnalyticalModelSurface,openingId: ElementId) -> IList[CurveLoop]

  

   Retrieves Array of CurveLoops of Analytical Surface Opening..

     Only valid 

    openings for hide are allowed.

  

  

   openingId: Identifies which Opening creates the CurveLoop in the analytical surface.

   Returns: Array of CurveLoops associated with Opening.
  """
  pass
 def GetOpenings(self,openingsIds):
  """ GetOpenings(self: AnalyticalModelSurface) -> ICollection[ElementId] """
  pass
 def GetPlane(self):
  """
  GetPlane(self: AnalyticalModelSurface) -> Plane

  

   Returns plane on which Analytical Model Surface Element is lying.

     Only 

    planar surface elements are valid for this function.

  

   Returns: Plane object on which Analytical Model is projected.
  """
  pass
 def HasOpenings(self):
  """
  HasOpenings(self: AnalyticalModelSurface) -> bool

  

   Checks if the analytical model surface have any openings.

   Returns: True if Analytical Surface Element contains any openings (included invalid for 

    hide).
  """
  pass
 def HideOpening(self,openingId):
  """
  HideOpening(self: AnalyticalModelSurface,openingId: ElementId) -> bool

  

   Hides set of curves originating from Opening.

  

   openingId: Opening to hide in analytical surface.

   Returns: True if given opening was hidden (operation was successful).
  """
  pass
 def IsOpeningHidden(self,openingId):
  """
  IsOpeningHidden(self: AnalyticalModelSurface,openingId: ElementId) -> bool

  

   Returns true if opening with given Identifier is hidden.

  

   openingId: Identifier of opening to check.

   Returns: True for openings which are hidden,false for all other Identifiers.
  """
  pass
 def IsPlanar(self):
  """
  IsPlanar(self: AnalyticalModelSurface) -> bool

  

   Indicates if the Analytical Model Surface Element is planar.

   Returns: True if Analytical Model Surface Element is planar,false otherwise.
  """
  pass
 def IsValidOpeningForHide(self,openingId):
  """
  IsValidOpeningForHide(self: AnalyticalModelSurface,openingId: ElementId) -> bool

  

   Returns true if opening with given Identifier could be hidden,false for all 

    other Identifiers.

  

  

   openingId: Identifier of opening to check.

   Returns: True for openings which are valid to be hidden,false for all other Identifiers.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetLoops(self,loopType,newLoops):
  """ SetLoops(self: AnalyticalModelSurface,loopType: AnalyticalLoopType,newLoops: IList[CurveLoop]) -> bool """
  pass
 def ShowOpening(self,openingId):
  """
  ShowOpening(self: AnalyticalModelSurface,openingId: ElementId) -> bool

  

   Shows previously hidden set of curves originating from Opening.

  

   openingId: Opening to show in analytical surface.

   Returns: True if given opening was shown (operation was successful).
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
 AlignmentMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The alignment method option.



Get: AlignmentMethod(self: AnalyticalModelSurface) -> AnalyticalAlignmentMethod



Set: AlignmentMethod(self: AnalyticalModelSurface)=value

"""

 BottomExtension=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The bottom extension option.



Get: BottomExtension(self: AnalyticalModelSurface) -> SurfaceElementExtension



Set: BottomExtension(self: AnalyticalModelSurface)=value

"""

 BottomExtensionMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The bottom extension method option.



Get: BottomExtensionMethod(self: AnalyticalModelSurface) -> AnalyticalAlignmentMethod



Set: BottomExtensionMethod(self: AnalyticalModelSurface)=value

"""

 BottomExtensionPlaneId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The bottom extension plane ID option.



Get: BottomExtensionPlaneId(self: AnalyticalModelSurface) -> ElementId



Set: BottomExtensionPlaneId(self: AnalyticalModelSurface)=value

"""

 HasExtension=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the element supports an extension option.



Get: HasExtension(self: AnalyticalModelSurface) -> bool



"""

 ProjectionPlaneZ=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Z projection option.



Get: ProjectionPlaneZ(self: AnalyticalModelSurface) -> ElementId



Set: ProjectionPlaneZ(self: AnalyticalModelSurface)=value

"""

 ProjectionZ=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Z projection option.



Get: ProjectionZ(self: AnalyticalModelSurface) -> SurfaceElementProjectionZ



Set: ProjectionZ(self: AnalyticalModelSurface)=value

"""

 TopExtension=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The top extension option.



Get: TopExtension(self: AnalyticalModelSurface) -> SurfaceElementExtension



Set: TopExtension(self: AnalyticalModelSurface)=value

"""

 TopExtensionMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The top extension method option.



Get: TopExtensionMethod(self: AnalyticalModelSurface) -> AnalyticalAlignmentMethod



Set: TopExtensionMethod(self: AnalyticalModelSurface)=value

"""

 TopExtensionPlaneId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The top extension plane ID option.



Get: TopExtensionPlaneId(self: AnalyticalModelSurface) -> ElementId



Set: TopExtensionPlaneId(self: AnalyticalModelSurface)=value

"""


