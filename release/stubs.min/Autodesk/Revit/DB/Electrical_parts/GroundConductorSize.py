class GroundConductorSize(APIObject,IDisposable):
 """ Represents electrical ground conductor size definition information. """
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
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
 Ampacity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get ampacity which is used for specifying size,the unit is ampere.



Get: Ampacity(self: GroundConductorSize) -> Int64



"""

 ConductorSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get conductor size corresponding to specific ampacity.



Get: ConductorSize(self: GroundConductorSize) -> str



"""

 MaterialBelongTo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get the material type which include this ground conductor size information.



Get: MaterialBelongTo(self: GroundConductorSize) -> WireMaterialType



"""


