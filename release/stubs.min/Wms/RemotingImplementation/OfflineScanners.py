# encoding: utf-8
# module Wms.RemotingImplementation.OfflineScanners calls itself OfflineScanners
# from Wms.RemotingImplementation,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class GcloudInboundFileListenerBase:
 """ GcloudInboundFileListenerBase(appSetttings: GcloudInboundFileListenerOptions,general: General,messaging: Messaging) """
 def DownloadFile(self,*args):
  """ DownloadFile(self: GcloudInboundFileListenerBase,filepath: str) -> Task[Stream] """
  pass
 def ProcessMessageTask(self,*args):
  """ ProcessMessageTask(self: GcloudInboundFileListenerBase,msgJson: str) -> Task """
  pass
 def PullAllMessages(self,token):
  """ PullAllMessages(self: GcloudInboundFileListenerBase,token: CancellationToken) -> Task[int] """
  pass
 def Start(self,token,newTaskStarted):
  """ Start(self: GcloudInboundFileListenerBase,token: CancellationToken) -> (Task,bool) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,appSetttings,general,messaging):
  """ __new__(cls: type,appSetttings: GcloudInboundFileListenerOptions,general: General,messaging: Messaging) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 NameOfClass=property(lambda self: object(),lambda self,v: None,lambda self: None)

 PullingTask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PullingTask(self: GcloudInboundFileListenerBase) -> Task

"""


 _general=None
 _messaging=None


class BosInboundFileListener:
 """ BosInboundFileListener(appSetttings: BosInboundFileOptions,general: General,messaging: Messaging,offlineScanning: OfflineScanning) """
 def DownloadFile(self,*args):
  """ DownloadFile(self: BosInboundFileListener,filepath: str) -> Task[Stream] """
  pass
 def ProcessMessageTask(self,*args):
  """ ProcessMessageTask(self: GcloudInboundFileListenerBase,msgJson: str) -> Task """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,appSetttings,general,messaging,offlineScanning):
  """ __new__(cls: type,appSetttings: BosInboundFileOptions,general: General,messaging: Messaging,offlineScanning: OfflineScanning) """
  pass
 NameOfClass=property(lambda self: object(),lambda self,v: None,lambda self: None)


 ResolverKey='BOS'
 _general=None
 _messaging=None


class GcloudInboundFileListenerOptions:
 """ GcloudInboundFileListenerOptions() """
 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Enabled(self: GcloudInboundFileListenerOptions) -> bool

Set: Enabled(self: GcloudInboundFileListenerOptions)=value
"""

 GCloudProjectId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GCloudProjectId(self: GcloudInboundFileListenerOptions) -> str

Set: GCloudProjectId(self: GcloudInboundFileListenerOptions)=value
"""

 GCloudPubSubPrefix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GCloudPubSubPrefix(self: GcloudInboundFileListenerOptions) -> str

Set: GCloudPubSubPrefix(self: GcloudInboundFileListenerOptions)=value
"""



class BosInboundFileOptions:
 """ BosInboundFileOptions(appSettings: IApplicationSettings) """
 @staticmethod
 def __new__(self,appSettings):
  """ __new__(cls: type,appSettings: IApplicationSettings) """
  pass

class BosInboundFileUploadedEvent:
 """ BosInboundFileUploadedEvent() """
 Event=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Event(self: BosInboundFileUploadedEvent) -> str

Set: Event(self: BosInboundFileUploadedEvent)=value
"""

 Filepath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Filepath(self: BosInboundFileUploadedEvent) -> str

Set: Filepath(self: BosInboundFileUploadedEvent)=value
"""

 Licenseid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Licenseid(self: BosInboundFileUploadedEvent) -> str

Set: Licenseid(self: BosInboundFileUploadedEvent)=value
"""

 Md5Hash=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Md5Hash(self: BosInboundFileUploadedEvent) -> str

Set: Md5Hash(self: BosInboundFileUploadedEvent)=value
"""

 Serialno=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Serialno(self: BosInboundFileUploadedEvent) -> str

Set: Serialno(self: BosInboundFileUploadedEvent)=value
"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Size(self: BosInboundFileUploadedEvent) -> str

Set: Size(self: BosInboundFileUploadedEvent)=value
"""



class IGcloudInboundFileListener:
 # no doc
 def PullAllMessages(self,token):
  """ PullAllMessages(self: IGcloudInboundFileListener,token: CancellationToken) -> Task[int] """
  pass
 def Start(self,token,newTaskStarted):
  """ Start(self: IGcloudInboundFileListener,token: CancellationToken) -> (Task,bool) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 PullingTask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PullingTask(self: IGcloudInboundFileListener) -> Task

"""



class ModuleOptions:
 """ ModuleOptions() """
 OfflineScanning='OS'
 RemotePublishing='RP'


