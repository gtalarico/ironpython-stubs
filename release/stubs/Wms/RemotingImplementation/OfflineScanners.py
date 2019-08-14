# encoding: utf-8
# module Wms.RemotingImplementation.OfflineScanners calls itself OfflineScanners
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class GcloudInboundFileListenerBase:
    """ GcloudInboundFileListenerBase(appSetttings: GcloudInboundFileListenerOptions, general: General, messaging: Messaging) """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return GcloudInboundFileListenerBase()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    def DownloadFile(self, *args): #cannot find CLR method
        """ DownloadFile(self: GcloudInboundFileListenerBase, filepath: str) -> Task[Stream] """
        pass

    def ProcessMessageTask(self, *args): #cannot find CLR method
        """ ProcessMessageTask(self: GcloudInboundFileListenerBase, msgJson: str) -> Task """
        pass

    def PullAllMessages(self, token):
        """ PullAllMessages(self: GcloudInboundFileListenerBase, token: CancellationToken) -> Task[int] """
        pass

    def Start(self, token, newTaskStarted):
        """ Start(self: GcloudInboundFileListenerBase, token: CancellationToken) -> (Task, bool) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, appSetttings, general, messaging):
        """ __new__(cls: type, appSetttings: GcloudInboundFileListenerOptions, general: General, messaging: Messaging) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    NameOfClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    PullingTask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PullingTask(self: GcloudInboundFileListenerBase) -> Task

"""


    _general = None
    _messaging = None


class BosInboundFileListener(GcloudInboundFileListenerBase):
    """ BosInboundFileListener(appSetttings: BosInboundFileOptions, general: General, messaging: Messaging, offlineScanning: OfflineScanning) """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return BosInboundFileListener()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    def DownloadFile(self, *args): #cannot find CLR method
        """ DownloadFile(self: BosInboundFileListener, filepath: str) -> Task[Stream] """
        pass

    def ProcessMessageTask(self, *args): #cannot find CLR method
        """ ProcessMessageTask(self: GcloudInboundFileListenerBase, msgJson: str) -> Task """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, appSetttings, general, messaging, offlineScanning):
        """ __new__(cls: type, appSetttings: BosInboundFileOptions, general: General, messaging: Messaging, offlineScanning: OfflineScanning) """
        pass

    NameOfClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    ResolverKey = 'BOS'
    _general = None
    _messaging = None


class GcloudInboundFileListenerOptions():
    """ GcloudInboundFileListenerOptions() """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return GcloudInboundFileListenerOptions()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: GcloudInboundFileListenerOptions) -> bool

Set: Enabled(self: GcloudInboundFileListenerOptions) = value
"""

    GCloudProjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GCloudProjectId(self: GcloudInboundFileListenerOptions) -> str

Set: GCloudProjectId(self: GcloudInboundFileListenerOptions) = value
"""

    GCloudPubSubPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GCloudPubSubPrefix(self: GcloudInboundFileListenerOptions) -> str

Set: GCloudPubSubPrefix(self: GcloudInboundFileListenerOptions) = value
"""



class BosInboundFileOptions(GcloudInboundFileListenerOptions):
    """ BosInboundFileOptions(appSettings: IApplicationSettings) """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return BosInboundFileOptions()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    @staticmethod # known case of __new__
    def __new__(self, appSettings):
        """ __new__(cls: type, appSettings: IApplicationSettings) """
        pass


class BosInboundFileUploadedEvent():
    """ BosInboundFileUploadedEvent() """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return BosInboundFileUploadedEvent()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    Event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Event(self: BosInboundFileUploadedEvent) -> str

Set: Event(self: BosInboundFileUploadedEvent) = value
"""

    Filepath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filepath(self: BosInboundFileUploadedEvent) -> str

Set: Filepath(self: BosInboundFileUploadedEvent) = value
"""

    Licenseid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Licenseid(self: BosInboundFileUploadedEvent) -> str

Set: Licenseid(self: BosInboundFileUploadedEvent) = value
"""

    Md5Hash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Md5Hash(self: BosInboundFileUploadedEvent) -> str

Set: Md5Hash(self: BosInboundFileUploadedEvent) = value
"""

    Serialno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Serialno(self: BosInboundFileUploadedEvent) -> str

Set: Serialno(self: BosInboundFileUploadedEvent) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: BosInboundFileUploadedEvent) -> str

Set: Size(self: BosInboundFileUploadedEvent) = value
"""



class IGcloudInboundFileListener:
    # no doc
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return IGcloudInboundFileListener()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    def PullAllMessages(self, token):
        """ PullAllMessages(self: IGcloudInboundFileListener, token: CancellationToken) -> Task[int] """
        pass

    def Start(self, token, newTaskStarted):
        """ Start(self: IGcloudInboundFileListener, token: CancellationToken) -> (Task, bool) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    PullingTask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PullingTask(self: IGcloudInboundFileListener) -> Task

"""



class ModuleOptions():
    """ ModuleOptions() """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return ModuleOptions()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    OfflineScanning = 'OS'
    RemotePublishing = 'RP'


