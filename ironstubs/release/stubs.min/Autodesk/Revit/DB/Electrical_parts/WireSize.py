class WireSize(APIObject,IDisposable):
 """ Represents specific electrical wire size information. """
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
 """Get ampacity which be used for specifying size,the unit is ampere.

Get: Ampacity(self: WireSize) -> Int64

"""

 Diameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get diameter of wire.

Get: Diameter(self: WireSize) -> float

"""

 InUse=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or set whether the size can be used in sizing.

Get: InUse(self: WireSize) -> bool

Set: InUse(self: WireSize)=value
"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get size symbol of wire.

Get: Size(self: WireSize) -> str

"""


