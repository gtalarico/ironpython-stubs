class MEPCalculationServerInfo(object,IDisposable):
 """
 a struct to hold the information about a MEP calucation servers
 
 MEPCalculationServerInfo(other: MEPCalculationServerInfo)
 MEPCalculationServerInfo(server: IExternalServer)
 MEPCalculationServerInfo()
 """
 def Dispose(self):
  """ Dispose(self: MEPCalculationServerInfo) """
  pass
 @staticmethod
 def GetMEPCalculationServerInfo(famInst):
  """
  GetMEPCalculationServerInfo(famInst: FamilyInstance) -> MEPCalculationServerInfo
  
   Gets a MEPCalculationServerInfo by family instance.
  
   famInst: The family instance.
   Returns: The MEPCalculationServerInfo.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: MEPCalculationServerInfo,disposing: bool) """
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
 def __new__(self,*__args):
  """
  __new__(cls: type,other: MEPCalculationServerInfo)
  __new__(cls: type,server: IExternalServer)
  __new__(cls: type)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Description of the server.

Get: Description(self: MEPCalculationServerInfo) -> str

Set: Description(self: MEPCalculationServerInfo)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: MEPCalculationServerInfo) -> bool

"""

 ServerId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Id of the server.

Get: ServerId(self: MEPCalculationServerInfo) -> Guid

Set: ServerId(self: MEPCalculationServerInfo)=value
"""

 ServerName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Name of the server.

Get: ServerName(self: MEPCalculationServerInfo) -> str

Set: ServerName(self: MEPCalculationServerInfo)=value
"""


 PipeUseDefinitionOnTypeGUID=None

