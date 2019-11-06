from System import Object
# encoding: utf-8
# module Wms.RemotingImplementation.EdiMessaging calls itself EdiMessaging
# from Wms.RemotingImplementation, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class IronPythonMessagingProvider(Object):
    """ IronPythonMessagingProvider() """
    def ClearHandlers(self):
        """ ClearHandlers(self: IronPythonMessagingProvider) """
        pass

    def ClearPublishers(self):
        """ ClearPublishers(self: IronPythonMessagingProvider) """
        pass

    def GetHandlers(self):
        """ GetHandlers(self: IronPythonMessagingProvider) -> IEnumerable[MessageHandlerDescriptor] """
        pass

    def GetPublishers(self):
        """ GetPublishers(self: IronPythonMessagingProvider) -> IEnumerable[MessagePublisherDescriptor] """
        pass

    def Initialize(self, args):
        """ Initialize(self: IronPythonMessagingProvider, args: MessagingProviderInitializationArguments) """
        pass

    def RegisterHandler(self, handler):
        """ RegisterHandler(self: IronPythonMessagingProvider, handler: MessageHandlerDescriptor) """
        pass

    def RegisterPublisher(self, publisher):
        """ RegisterPublisher(self: IronPythonMessagingProvider, publisher: MessagePublisherDescriptor) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Instance = None

    Instance = IronPythonMessagingProvider()
    """hardcoded/returns an instance of the class"""

class ProcessOutboundOrderMessageState():
    """ ProcessOutboundOrderMessageState() """
    IsErpIdStored = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsErpIdStored(self: ProcessOutboundOrderMessageState) -> bool

Set: IsErpIdStored(self: ProcessOutboundOrderMessageState) = value
"""

    IsFulFilledInBoxWise = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFulFilledInBoxWise(self: ProcessOutboundOrderMessageState) -> bool

Set: IsFulFilledInBoxWise(self: ProcessOutboundOrderMessageState) = value
"""

    IsProcessedInErp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsProcessedInErp(self: ProcessOutboundOrderMessageState) -> bool

Set: IsProcessedInErp(self: ProcessOutboundOrderMessageState) = value
"""

    IsUnlockedInErp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUnlockedInErp(self: ProcessOutboundOrderMessageState) -> bool

Set: IsUnlockedInErp(self: ProcessOutboundOrderMessageState) = value
"""

    PackageSlipNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PackageSlipNumber(self: ProcessOutboundOrderMessageState) -> str

Set: PackageSlipNumber(self: ProcessOutboundOrderMessageState) = value
"""


    Instance = ProcessOutboundOrderMessageState()
    """hardcoded/returns an instance of the class"""

class StandardMessagingProvider(Object):
    """ StandardMessagingProvider() """
    def GetHandlers(self):
        """ GetHandlers(self: StandardMessagingProvider) -> IEnumerable[MessageHandlerDescriptor] """
        pass

    def GetPublishers(self):
        """ GetPublishers(self: StandardMessagingProvider) -> IEnumerable[MessagePublisherDescriptor] """
        pass

    def Initialize(self, args):
        """ Initialize(self: StandardMessagingProvider, args: MessagingProviderInitializationArguments) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Instance = StandardMessagingProvider()
    """hardcoded/returns an instance of the class"""

# variables with complex values

