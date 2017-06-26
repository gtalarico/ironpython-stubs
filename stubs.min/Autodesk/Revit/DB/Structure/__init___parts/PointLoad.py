class PointLoad(LoadBase,IDisposable):
 """ An object that represents a force/moment applied to a single point. """
 @staticmethod
 def Create(aDoc,*__args):
  """
  Create(aDoc: Document,host: AnalyticalModelStick,selector: AnalyticalElementSelector,forceVector: XYZ,momentVector: XYZ,symbol: PointLoadType) -> PointLoad
  
   Creates a new hosted point load within the project.
  
   aDoc: Document to which new point load will be added.
   host: The AnalyticalModelStick (Analytical Beam,Analytical Brace,Analytical Column) 
    host element for the point Load.
  
   selector: The start or end point of the Analytical stick element.
   forceVector: The applied 3d force vector.
   momentVector: The applied 3d moment vector.
   symbol: The symbol of the PointLoad. Set ll to use default type.
   Returns: If successful,returns the newly created PointLoad,ll otherwise.
  Create(aDoc: Document,host: AnalyticalModel,forceVector: XYZ,momentVector: XYZ,symbol: PointLoadType) -> PointLoad
  
   Creates a new hosted point load within the project.
  
   aDoc: Document to which new point load will be added.
   host: The Analytical Isolated Foundation type host element for the point Load.
   forceVector: The applied 3d force vector.
   momentVector: The applied 3d moment vector.
   symbol: The symbol of the PointLoad. Set ll to use default type.
   Returns: If successful,returns the newly created PointLoad,ll otherwise.
  Create(aDoc: Document,point: XYZ,forceVector: XYZ,momentVector: XYZ,symbol: PointLoadType,plane: SketchPlane) -> PointLoad
  
   Creates a new non-hosted point load within the project using data at point.
  
   aDoc: Document to which new point load will be added.
   point: The position of point load,measured in decimal feet.
   forceVector: The applied 3d force vector.
   momentVector: The applied 3d moment vector.
   symbol: The symbol of the PointLoad. Set ll to use default type.
   plane: The work plane of the PointLoad. Set ll to use default plane.
   Returns: If successful,returns the newly created PointLoad,ll otherwise.
  """
  pass
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
 ForceVector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The force vector applied to the point load,oriented according to OrientTo setting.

Get: ForceVector(self: PointLoad) -> XYZ

Set: ForceVector(self: PointLoad)=value
"""

 MomentVector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The moment vector applied to the point load,oriented according to OrientTo setting.

Get: MomentVector(self: PointLoad) -> XYZ

Set: MomentVector(self: PointLoad)=value
"""

 Point=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the position of point load,measured in decimal feet.

Get: Point(self: PointLoad) -> XYZ

Set: Point(self: PointLoad)=value
"""


