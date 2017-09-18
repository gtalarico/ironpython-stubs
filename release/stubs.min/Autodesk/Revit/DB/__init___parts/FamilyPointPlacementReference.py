class FamilyPointPlacementReference(APIObject,IDisposable):
 """
 This object represents data corresponding to the placement references in a

 certain types of Family Instances (see examples listed below).
 """
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def getCDA(self,*args):
  """ getCDA(self: FamilyPointPlacementReference) -> ControlledDocAccess* """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: APIObject) """
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
 Location=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The location of the point.



Get: Location(self: FamilyPointPlacementReference) -> Transform



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the corresponding reference point in the Family document.



Get: Name(self: FamilyPointPlacementReference) -> str



"""

 PointReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The reference on which the point depends on.



Get: PointReference(self: FamilyPointPlacementReference) -> Reference



"""


