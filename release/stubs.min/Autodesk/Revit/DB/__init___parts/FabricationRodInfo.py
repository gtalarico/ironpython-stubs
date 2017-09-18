class FabricationRodInfo(object,IDisposable):
 """ The rod information of the fabrication part. """
 def AttachToHanger(self,hangerId,rodIndex,position):
  """
  AttachToHanger(self: FabricationRodInfo,hangerId: ElementId,rodIndex: int,position: XYZ)
   Attaches the hanger rod to another bearer hanger.
  
   hangerId: Id of the bearer hanger to which the rod attaches.
   rodIndex: The index of the rod.
   position: The position of the rod end. It should be on bearer centerline.
  """
  pass
 def AttachToStructure(self):
  """
  AttachToStructure(self: FabricationRodInfo)
   Attaches to the nearest structural element.
  """
  pass
 def Dispose(self):
  """ Dispose(self: FabricationRodInfo) """
  pass
 def GetBearerExtension(self,rodIndex):
  """
  GetBearerExtension(self: FabricationRodInfo,rodIndex: int) -> float
  
   Gets the bearer extension. The method is applicable only for bearer hanger.
  
   rodIndex: The index of the rod.
  """
  pass
 def GetRodAttachedElementId(self,rodIndex):
  """
  GetRodAttachedElementId(self: FabricationRodInfo,rodIndex: int) -> LinkElementId
  
   Gets the id of the attached component for the specified rod.
  
   rodIndex: The index of the specified rod.
  """
  pass
 def GetRodEndPosition(self,rodIndex):
  """
  GetRodEndPosition(self: FabricationRodInfo,rodIndex: int) -> XYZ
  
   Gets the position of the rod end.
  
   rodIndex: The index of the rod.
   Returns: The position of the rod end.
  """
  pass
 def IsRodLockedWithHost(self,rodIndex):
  """
  IsRodLockedWithHost(self: FabricationRodInfo,rodIndex: int) -> bool
  
   Checks if the rod is locked with the host. The method is applicable only for 
    bearer hanger.
  
  
   rodIndex: The index of the rod.
   Returns: True if the rod is locked with its host.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FabricationRodInfo,disposing: bool) """
  pass
 def SetBearerExtension(self,rodIndex,length):
  """
  SetBearerExtension(self: FabricationRodInfo,rodIndex: int,length: float)
   Sets the bearer extension. The method is applicable only for bearer hanger.
  
   rodIndex: The index of the rod.
   length: The new length of bearer extension.
  """
  pass
 def SetRodEndPosition(self,rodIndex,position):
  """
  SetRodEndPosition(self: FabricationRodInfo,rodIndex: int,position: XYZ)
   Sets the position of the rod end. The method is applicable only for bearer 
    hanger.
  
  
   rodIndex: The index of the rod.
   position: The position of the rod end.
  """
  pass
 def SetRodLockedWithHost(self,rodIndex,locked):
  """
  SetRodLockedWithHost(self: FabricationRodInfo,rodIndex: int,locked: bool)
   Locks the rod with the host. The method is applicable only for bearer hanger.
  
   rodIndex: The index of the rod.
   locked: Locks the rod with the host.
  """
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
 IsAttachedToStructure=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Checks if the hanger is attached to structure.

Get: IsAttachedToStructure(self: FabricationRodInfo) -> bool

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FabricationRodInfo) -> bool

"""

 RodCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of rods.

Get: RodCount(self: FabricationRodInfo) -> int

"""


