class MEPSize(object,IDisposable):
 """
 Stores the basic size information for an MEP duct,pipe,cable tray,or conduit.

 

 MEPSize(nominalDiameter: float,innerDiameter: float,outerDiameter: float,usedInSizeLists: bool,usedInSizing: bool)
 """
 def Dispose(self):
  """ Dispose(self: MEPSize) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: MEPSize,disposing: bool) """
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
 @staticmethod
 def __new__(self,nominalDiameter,innerDiameter,outerDiameter,usedInSizeLists,usedInSizing):
  """ __new__(cls: type,nominalDiameter: float,innerDiameter: float,outerDiameter: float,usedInSizeLists: bool,usedInSizing: bool) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 InnerDiameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Inner diameter



Get: InnerDiameter(self: MEPSize) -> float



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: MEPSize) -> bool



"""

 NominalDiameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Nominal diameter



Get: NominalDiameter(self: MEPSize) -> float



"""

 OuterDiameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Outer diameter



Get: OuterDiameter(self: MEPSize) -> float



"""

 UsedInSizeLists=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether it is used in size lists.



Get: UsedInSizeLists(self: MEPSize) -> bool



"""

 UsedInSizing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether is used in sizing.



Get: UsedInSizing(self: MEPSize) -> bool



"""


