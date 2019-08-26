from Wms.EdiMessaging import *
# encoding: utf-8
# module Wms.RemotingImplementation.EdiMessaging.Messages.Rp calls itself Rp
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class RpInboundFileMessage(MessageBase):
    """
    RpInboundFileMessage()
    RpInboundFileMessage(message: IMessage)
    RpInboundFileMessage(data: RpInboundFileMessageData)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: IMessage)
        __new__(cls: type, data: RpInboundFileMessageData)
        """
        pass

    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Data(self: RpInboundFileMessage) -> RpInboundFileMessageData

Set: Data(self: RpInboundFileMessage) = value
"""


    TypeName = 'RP Inbound File: {0}'

    Instance = RpInboundFileMessage()
    """hardcoded/returns an instance of the class"""

class RpInboundFileMessageData():
    """ RpInboundFileMessageData() """
    Base64Content = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base64Content(self: RpInboundFileMessageData) -> str

Set: Base64Content(self: RpInboundFileMessageData) = value
"""

    Event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Event(self: RpInboundFileMessageData) -> str

Set: Event(self: RpInboundFileMessageData) = value
"""

    Filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filename(self: RpInboundFileMessageData) -> str

Set: Filename(self: RpInboundFileMessageData) = value
"""

    Filepath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filepath(self: RpInboundFileMessageData) -> str

Set: Filepath(self: RpInboundFileMessageData) = value
"""

    Md5Hash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Md5Hash(self: RpInboundFileMessageData) -> str

Set: Md5Hash(self: RpInboundFileMessageData) = value
"""

    Prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Prefix(self: RpInboundFileMessageData) -> str

Set: Prefix(self: RpInboundFileMessageData) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: RpInboundFileMessageData) -> str

Set: Size(self: RpInboundFileMessageData) = value
"""


    Instance = RpInboundFileMessageData()
    """hardcoded/returns an instance of the class"""

