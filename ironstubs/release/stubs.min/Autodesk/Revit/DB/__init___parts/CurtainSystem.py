class CurtainSystem(CurtainSystemBase,IDisposable):
 """ Provides access to the CurtainSystem object in Autodesk Revit. """
 def AddCurtainGrid(self,face):
  """
  AddCurtainGrid(self: CurtainSystem,face: Reference)
   Add CurtainGrid on the specified face for the CurtainSystem.
  
   face: The face new CurtainGrid will be created on.
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
 def RemoveCurtainGrid(self,face):
  """
  RemoveCurtainGrid(self: CurtainSystem,face: Reference)
   Remove CurtainGrid from the specified face for the CurtainSystem.
  
   face: The face CurtainGrid will be removed from.
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
 CurtainGrids=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get all the CurtainGrid object of this CurtainSystem. Each CurtainGrid corresponds to one face.

Get: CurtainGrids(self: CurtainSystem) -> CurtainGridSet

"""

 CurtainSystemType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """get or set the type of the CurtainSystem.

Get: CurtainSystemType(self: CurtainSystem) -> CurtainSystemType

Set: CurtainSystemType(self: CurtainSystem)=value
"""


