class FabricationDimensionDefinition(object,IDisposable):
 """ Fabricaition dimension definition """
 def Dispose(self):
  """ Dispose(self: FabricationDimensionDefinition) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FabricationDimensionDefinition,disposing: bool) """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsModifiable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If the fabrication dimension is modifiable by user.



Get: IsModifiable(self: FabricationDimensionDefinition) -> bool



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: FabricationDimensionDefinition) -> bool



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Fabrication dimension name.



Get: Name(self: FabricationDimensionDefinition) -> str



"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Fabrication dimension type.



Get: Type(self: FabricationDimensionDefinition) -> FabricationDimensionType



"""

 UnitType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Fabrication dimension unit type.



Get: UnitType(self: FabricationDimensionDefinition) -> FabricationDimensionUnitType



"""


