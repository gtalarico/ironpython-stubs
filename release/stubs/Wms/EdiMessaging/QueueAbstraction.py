# encoding: utf-8
# module Wms.EdiMessaging.QueueAbstraction calls itself QueueAbstraction
# from Wms.EdiMessaging, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# functions

def IQueue(args, kwargs): # real signature unknown
    """  """
    pass

# classes

class IQueueListener:
    # no doc
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return IQueueListener()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    def Read(self, messageHandler, cancellationtoken):
        """ Read(self: IQueueListener, messageHandler: Action[IMessage], cancellationtoken: CancellationToken) -> Task """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IQueuePublisher:
    # no doc
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return IQueuePublisher()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    def Enqueue(self, message):
        """ Enqueue(self: IQueuePublisher, message: IMessage) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class QueueConnectResult():
    """
    QueueConnectResult(success: bool)
    QueueConnectResult(success: bool, messages: str)
    """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return QueueConnectResult()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    @staticmethod # known case of __new__
    def __new__(self, success, messages=None):
        """
        __new__(cls: type, success: bool)
        __new__(cls: type, success: bool, messages: str)
        """
        pass

    Messages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Messages(self: QueueConnectResult) -> str

"""

    Success = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Success(self: QueueConnectResult) -> bool

"""



