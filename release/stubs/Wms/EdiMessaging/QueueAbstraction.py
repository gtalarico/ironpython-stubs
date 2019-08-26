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
    def Read(self, messageHandler, cancellationtoken):
        """ Read(self: IQueueListener, messageHandler: Action[IMessage], cancellationtoken: CancellationToken) -> Task """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Instance = IQueueListener()
    """hardcoded/returns an instance of the class"""

class IQueuePublisher:
    # no doc
    def Enqueue(self, message):
        """ Enqueue(self: IQueuePublisher, message: IMessage) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Instance = IQueuePublisher()
    """hardcoded/returns an instance of the class"""

class QueueConnectResult():
    """
    QueueConnectResult(success: bool)
    QueueConnectResult(success: bool, messages: str)
    """
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


    Instance = QueueConnectResult()
    """hardcoded/returns an instance of the class"""

