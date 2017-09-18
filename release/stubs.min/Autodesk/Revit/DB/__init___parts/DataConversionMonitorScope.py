class DataConversionMonitorScope(object,IDisposable):
 """
 This class is used to regsiter an application-supplied object that implements IDataConversionMonitor.

    Creating the object registers an implementation of IDataConversionMonitor supplied as constructor argument.

    When the scope object is destroyed,that object is unregistered.

 

 DataConversionMonitorScope(IDCM: IDataConversionMonitor)
 """
 def Dispose(self):
  """ Dispose(self: DataConversionMonitorScope) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: DataConversionMonitorScope,disposing: bool) """
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
 def __new__(self,IDCM):
  """ __new__(cls: type,IDCM: IDataConversionMonitor) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: DataConversionMonitorScope) -> bool



"""


