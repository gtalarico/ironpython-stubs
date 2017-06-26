class FabricationConnectorInfo(object,IDisposable):
 """ Fabrication connector information. """
 def Dispose(self):
  """ Dispose(self: FabricationConnectorInfo) """
  pass
 def HasDoubleWallConnector(self):
  """
  HasDoubleWallConnector(self: FabricationConnectorInfo) -> bool
  
   Checks if there are any double wall connectors fabricated.
   Returns: True if there are any double wall connectors fabricated.
  """
  pass
 def IsValid(self):
  """
  IsValid(self: FabricationConnectorInfo) -> bool
  
   Checks if the connector has fabrication parameters associated with it that can 
    be set.
  
   Returns: True if the connector has fabrication parameters associated with it that can be 
    set.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FabricationConnectorInfo,disposing: bool) """
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
 BodyConnectorId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Fabrication body connector Id.

Get: BodyConnectorId(self: FabricationConnectorInfo) -> int

Set: BodyConnectorId(self: FabricationConnectorInfo)=value
"""

 DoubleWallConnectorId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Fabrication double wall connector Id.

Get: DoubleWallConnectorId(self: FabricationConnectorInfo) -> int

Set: DoubleWallConnectorId(self: FabricationConnectorInfo)=value
"""

 FabricationIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The index of the connector shown within the fabrication software.

Get: FabricationIndex(self: FabricationConnectorInfo) -> int

"""

 IsBodyConnectorLocked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Fabrication body connector lock.

Get: IsBodyConnectorLocked(self: FabricationConnectorInfo) -> bool

Set: IsBodyConnectorLocked(self: FabricationConnectorInfo)=value
"""

 IsDoubleWallConnectorLocked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Fabrication double wall connector lock.

Get: IsDoubleWallConnectorLocked(self: FabricationConnectorInfo) -> bool

Set: IsDoubleWallConnectorLocked(self: FabricationConnectorInfo)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FabricationConnectorInfo) -> bool

"""


