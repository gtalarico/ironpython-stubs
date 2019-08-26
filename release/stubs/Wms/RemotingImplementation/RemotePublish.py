from Wms.RemotingImplementation.OfflineScanners import *
# encoding: utf-8
# module Wms.RemotingImplementation.RemotePublish calls itself RemotePublish
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class RemotePublishingInboundFileListener(GcloudInboundFileListenerBase):
    """ RemotePublishingInboundFileListener(appSetttings: RemotePublishingInboundFileOptions, general: General, messaging: Messaging, api: RemotePublishing) """
    def DownloadFile(self, *args): #cannot find CLR method
        """ DownloadFile(self: RemotePublishingInboundFileListener, filepath: str) -> Task[Stream] """
        pass

    def ProcessMessageTask(self, *args): #cannot find CLR method
        """ ProcessMessageTask(self: RemotePublishingInboundFileListener, msgJson: str) -> Task """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, appSetttings, general, messaging, api):
        """ __new__(cls: type, appSetttings: RemotePublishingInboundFileOptions, general: General, messaging: Messaging, api: RemotePublishing) """
        pass

    NameOfClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    ResolverKey = 'RP'
    _general = None
    _messaging = None

    Instance = RemotePublishingInboundFileListener()
    """hardcoded/returns an instance of the class"""

class RemotePublishingInboundFileOptions(GcloudInboundFileListenerOptions):
    """ RemotePublishingInboundFileOptions(appSettings: IApplicationSettings) """
    @staticmethod # known case of __new__
    def __new__(self, appSettings):
        """ __new__(cls: type, appSettings: IApplicationSettings) """
        pass

    Instance = RemotePublishingInboundFileOptions()
    """hardcoded/returns an instance of the class"""

class RemotePublishingInboundFileUploadedEvent():
    """ RemotePublishingInboundFileUploadedEvent() """
    Event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Event(self: RemotePublishingInboundFileUploadedEvent) -> str

Set: Event(self: RemotePublishingInboundFileUploadedEvent) = value
"""

    Filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filename(self: RemotePublishingInboundFileUploadedEvent) -> str

Set: Filename(self: RemotePublishingInboundFileUploadedEvent) = value
"""

    Filepath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filepath(self: RemotePublishingInboundFileUploadedEvent) -> str

Set: Filepath(self: RemotePublishingInboundFileUploadedEvent) = value
"""

    Licenseid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Licenseid(self: RemotePublishingInboundFileUploadedEvent) -> str

Set: Licenseid(self: RemotePublishingInboundFileUploadedEvent) = value
"""

    Md5Hash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Md5Hash(self: RemotePublishingInboundFileUploadedEvent) -> str

Set: Md5Hash(self: RemotePublishingInboundFileUploadedEvent) = value
"""

    Prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Prefix(self: RemotePublishingInboundFileUploadedEvent) -> str

Set: Prefix(self: RemotePublishingInboundFileUploadedEvent) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: RemotePublishingInboundFileUploadedEvent) -> str

Set: Size(self: RemotePublishingInboundFileUploadedEvent) = value
"""


    Instance = RemotePublishingInboundFileUploadedEvent()
    """hardcoded/returns an instance of the class"""

