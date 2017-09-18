class UpdaterId(object,IDisposable):
 """
 A unique identifier of an Updater

 

 UpdaterId(addInId: AddInId,val: Guid)
 """
 def Dispose(self):
  """ Dispose(self: UpdaterId) """
  pass
 def GetAddInId(self):
  """
  GetAddInId(self: UpdaterId) -> AddInId

  

   AddInId of the UpdaterId
  """
  pass
 def GetGUID(self):
  """
  GetGUID(self: UpdaterId) -> Guid

  

   GUID value of the UpdaterId
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: UpdaterId,disposing: bool) """
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
 def __new__(self,addInId,val):
  """ __new__(cls: type,addInId: AddInId,val: Guid) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: UpdaterId) -> bool



"""


