from Wms.EdiMessaging import *
# encoding: utf-8
# module Wms.EdiMessaging.Processor calls itself Processor
# from Wms.EdiMessaging, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class IMessageHandler:
    # no doc
    def Handle(self, message):
        """ Handle(self: IMessageHandler, message: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Instance = IMessageHandler()
    """hardcoded/returns an instance of the class"""

class JsonMessage(MessageBase):
    """
    JsonMessage()
    JsonMessage(messageType: Type, jsonString: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, messageType=None, jsonString=None):
        """
        __new__(cls: type)
        __new__(cls: type, messageType: Type, jsonString: str)
        """
        pass

    Instance = JsonMessage()
    """hardcoded/returns an instance of the class"""

class MessageHandlerBase:
    # no doc
    def Handle(self, message):
        """ Handle(self: MessageHandlerBase[TMessage], message: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Instance = MessageHandlerBase()
    """hardcoded/returns an instance of the class"""

class MessageProcessor():
    # no doc
    def AddHandler(self):
        """ AddHandler[(TMessage, THandler)](self: MessageProcessor) -> MessageProcessor """
        pass

    def CreateHandlerOfType(self, *args): #cannot find CLR method
        """ CreateHandlerOfType(self: MessageProcessor, handlerType: Type) -> IMessageHandler """
        pass

    def ExtractMessage(self, *args): #cannot find CLR method
        """ ExtractMessage(self: MessageProcessor, message: IMessage) -> object """
        pass

    def HandleMessage(self, *args): #cannot find CLR method
        """ HandleMessage(self: MessageProcessor, obj: IMessage) """
        pass

    def Start(self, token):
        """ Start(self: MessageProcessor, token: CancellationToken) -> Task """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, queueProvider: IQueueProvider) """
        pass

    _queueProvider = None

    Instance = MessageProcessor()
    """hardcoded/returns an instance of the class"""

