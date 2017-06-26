class FabricationConfigurationInfo(object,IDisposable):
 """ Represents an MEP object that holds the properties of an MEP fabrication configuration. """
 def Dispose(self):
  """ Dispose(self: FabricationConfigurationInfo) """
  pass
 @staticmethod
 def FindSourceFabricationConfiguration(fabricationConfiguration):
  """
  FindSourceFabricationConfiguration(fabricationConfiguration: FabricationConfigurationInfo) -> FabricationConfigurationInfo
  
   Finds the source fabrication configuration on disk which matches the input 
    fabrication configuration.
  
  
   fabricationConfiguration: The fabrication configuration to match.
   Returns: The matching source fabrication configuration.
  """
  pass
 @staticmethod
 def GetAllFabricationConfigurations():
  """
  GetAllFabricationConfigurations() -> IList[FabricationConfigurationInfo]
  
   Gets all added fabrication configurations.
   Returns: All added fabrication configurations.
  """
  pass
 def GetProfiles(self):
  """
  GetProfiles(self: FabricationConfigurationInfo) -> IList[str]
  
   Return the profiles in the fabrication configuration.
  """
  pass
 def IsValid(self):
  """
  IsValid(self: FabricationConfigurationInfo) -> bool
  
   Checks if the fabrication configuration is valid.
   Returns: True if the fabrication configuration is valid.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FabricationConfigurationInfo,disposing: bool) """
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
 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The description of the fabrication configuration.

Get: Description(self: FabricationConfigurationInfo) -> str

"""

 GUID=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The unique identification of the fabrication configuration.

Get: GUID(self: FabricationConfigurationInfo) -> Guid

"""

 IsLocked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Checks whether the fabrication configuration is locked. If true,the configuration is locked and cannot be removed.

Get: IsLocked(self: FabricationConfigurationInfo) -> bool

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FabricationConfigurationInfo) -> bool

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the fabrication configuration.

Get: Name(self: FabricationConfigurationInfo) -> str

"""

 Path=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The path where the fabrication configuration is located.

Get: Path(self: FabricationConfigurationInfo) -> str

"""

 UnitSystem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The unit system of the fabrication configuration. Units can be UnitSystem.Metric or UnitSystem.Imperial.

Get: UnitSystem(self: FabricationConfigurationInfo) -> UnitSystem

"""

 Version=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The version of the fabrication configuration.

Get: Version(self: FabricationConfigurationInfo) -> float

"""


