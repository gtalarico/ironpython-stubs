class Opening(Element,IDisposable):
 """ An opening in an Autodesk Revit project or family document. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
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
 BoundaryCurves=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The geometry information for non-rectangular openings in project documents,
or for all openings in family documents.

Get: BoundaryCurves(self: Opening) -> CurveArray

"""

 BoundaryRect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves the geometry information if the opening boundary is a rect.

Get: BoundaryRect(self: Opening) -> IList[XYZ]

"""

 Host=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves the host element of this opening.

Get: Host(self: Opening) -> Element

"""

 IsRectBoundary=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves the information whether the opening has a rectangular boundary.

Get: IsRectBoundary(self: Opening) -> bool

"""

 IsTransparentIn3D=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the opening is transparent in 3D view when loaded into the project.

Get: IsTransparentIn3D(self: Opening) -> bool

Set: IsTransparentIn3D(self: Opening)=value
"""

 IsTransparentInElevation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the opening is transparent in elevation view when loaded into the project.

Get: IsTransparentInElevation(self: Opening) -> bool

Set: IsTransparentInElevation(self: Opening)=value
"""


