# encoding: utf-8
# module Wms.RemotingImplementation.RemotePublish calls itself RemotePublish
# from Wms.RemotingImplementation,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class RemotePublishingInboundFileListener:
 """ RemotePublishingInboundFileListener(appSetttings: RemotePublishingInboundFileOptions,general: General,messaging: Messaging,api: RemotePublishing) """
 def DownloadFile(self,*args):
  """ DownloadFile(self: RemotePublishingInboundFileListener,filepath: str) -> Task[Stream] """
  pass
 def ProcessMessageTask(self,*args):
  """ ProcessMessageTask(self: RemotePublishingInboundFileListener,msgJson: str) -> Task """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,appSetttings,general,messaging,api):
  """ __new__(cls: type,appSetttings: RemotePublishingInboundFileOptions,general: General,messaging: Messaging,api: RemotePublishing) """
  pass
 NameOfClass=property(lambda self: object(),lambda self,v: None,lambda self: None)


 ResolverKey='RP'
 _general=None
 _messaging=None


class RemotePublishingInboundFileOptions:
 """ RemotePublishingInboundFileOptions(appSettings: IApplicationSettings) """
 @staticmethod
 def __new__(self,appSettings):
  """ __new__(cls: type,appSettings: IApplicationSettings) """
  pass

class RemotePublishingInboundFileUploadedEvent:
 """ RemotePublishingInboundFileUploadedEvent() """
 Event=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Event(self: RemotePublishingInboundFileUploadedEvent) -> str

Set: Event(self: RemotePublishingInboundFileUploadedEvent)=value
"""

 Filename=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Filename(self: RemotePublishingInboundFileUploadedEvent) -> str

Set: Filename(self: RemotePublishingInboundFileUploadedEvent)=value
"""

 Filepath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Filepath(self: RemotePublishingInboundFileUploadedEvent) -> str

Set: Filepath(self: RemotePublishingInboundFileUploadedEvent)=value
"""

 Licenseid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Licenseid(self: RemotePublishingInboundFileUploadedEvent) -> str

Set: Licenseid(self: RemotePublishingInboundFileUploadedEvent)=value
"""

 Md5Hash=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Md5Hash(self: RemotePublishingInboundFileUploadedEvent) -> str

Set: Md5Hash(self: RemotePublishingInboundFileUploadedEvent)=value
"""

 Prefix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Prefix(self: RemotePublishingInboundFileUploadedEvent) -> str

Set: Prefix(self: RemotePublishingInboundFileUploadedEvent)=value
"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Size(self: RemotePublishingInboundFileUploadedEvent) -> str

Set: Size(self: RemotePublishingInboundFileUploadedEvent)=value
"""



