# encoding: utf-8
# module Wms.EdiMessaging.QueueAbstraction calls itself QueueAbstraction
# from Wms.EdiMessaging,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# functions

def IQueue(args,kwargs): # real signature unknown
 """  """
 pass
# classes

class IQueueListener:
 # no doc
 def Read(self,messageHandler,cancellationtoken):
  """ Read(self: IQueueListener,messageHandler: Action[IMessage],cancellationtoken: CancellationToken) -> Task """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class IQueuePublisher:
 # no doc
 def Enqueue(self,message):
  """ Enqueue(self: IQueuePublisher,message: IMessage) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class QueueConnectResult:
 """
 QueueConnectResult(success: bool)
 QueueConnectResult(success: bool,messages: str)
 """
 @staticmethod
 def __new__(self,success,messages=None):
  """
  __new__(cls: type,success: bool)
  __new__(cls: type,success: bool,messages: str)
  """
  pass
 Messages=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Messages(self: QueueConnectResult) -> str

"""

 Success=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Success(self: QueueConnectResult) -> bool

"""



