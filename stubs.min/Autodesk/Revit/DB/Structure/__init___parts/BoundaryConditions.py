class BoundaryConditions(Element,IDisposable):
 """ An object that represents a force applied across an area. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def GetBoundaryConditionsType(self):
  """
  GetBoundaryConditionsType(self: BoundaryConditions) -> BoundaryConditionsType
  
   Returns the boundary conditions type.
   Returns: The boundary conditions type.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetCurve(self):
  """
  GetCurve(self: BoundaryConditions) -> Curve
  
   Returns curve that define geometry of the line boundary conditions.
  """
  pass
 def GetDegreesOfFreedomCoordinateSystem(self):
  """
  GetDegreesOfFreedomCoordinateSystem(self: BoundaryConditions) -> Transform
  
   Gets the origin and rotation of coordinate system that is used by translation 
    and rotation parameters,like X Translation or Z Rotation.
  
   Returns: The coordinate system. Origin contains the position of the start of the 
    boundary conditions. BasisX,BasisY and BasisZ contain the directions of the 
    axes in the global coordinate system.
  """
  pass
 def GetLoops(self):
  """
  GetLoops(self: BoundaryConditions) -> IList[CurveLoop]
  
   Returns curve loops that define geometry of the area boundary conditions.
   Returns: The curve loop collection.
  """
  pass
 def GetOrientTo(self):
  """
  GetOrientTo(self: BoundaryConditions) -> BoundaryConditionsOrientTo
  
   Returns the boundary conditions orientation option.
   Returns: The orientation option.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetOrientTo(self,orientTo):
  """
  SetOrientTo(self: BoundaryConditions,orientTo: BoundaryConditionsOrientTo)
   Sets the boundary condition orientation option.
  
   orientTo: The new orientation option.
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
 AssociatedLoadId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Id of the internal load element associated with a boundary conditions.

Get: AssociatedLoadId(self: BoundaryConditions) -> ElementId

Set: AssociatedLoadId(self: BoundaryConditions)=value
"""

 HostElement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The host element for the boundary conditions.

Get: HostElement(self: BoundaryConditions) -> AnalyticalModel

"""

 HostElementId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The host element Id for the boundary conditions.

Get: HostElementId(self: BoundaryConditions) -> ElementId

"""

 Point=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the position of point boundary conditions.

Get: Point(self: BoundaryConditions) -> XYZ

"""


