class SyncHandler(MulticastDelegate):
 """ SyncHandler(object: object,method: IntPtr) """
 def BeginInvoke(self,callback,object):
  """ BeginInvoke(self: SyncHandler,callback: AsyncCallback,object: object) -> IAsyncResult """
  pass
 def EndInvoke(self,result):
  """ EndInvoke(self: SyncHandler,result: IAsyncResult) """
  pass
 def Invoke(self):
  """ Invoke(self: SyncHandler) """
  pass
 @staticmethod
 def __new__(self,object,method):
  """ __new__(cls: type,object: object,method: IntPtr) """
  pass
