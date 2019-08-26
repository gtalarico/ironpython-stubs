# encoding: utf-8
# module Wms.EdiMessaging calls itself EdiMessaging
# from Wms.EdiMessaging, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null, Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class HandleResult():
    """ HandleResult() """
    Messages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Messages(self: HandleResult) -> StringBuilder

Set: Messages(self: HandleResult) = value
"""

    Success = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Success(self: HandleResult) -> bool

Set: Success(self: HandleResult) = value
"""


    Instance = HandleResult()
    """hardcoded/returns an instance of the class"""

class IMessage:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Body(self: IMessage) -> Array[Byte]

Set: Body(self: IMessage) = value
"""

    BodyMimeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: BodyMimeType(self: IMessage) -> str

Set: BodyMimeType(self: IMessage) = value
"""

    HasStockAllocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An indication wether this message has stock allocations.
            if set to True, on certain events, the allocations will be automatically removed.

Get: HasStockAllocations(self: IMessage) -> bool

Set: HasStockAllocations(self: IMessage) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Guid of the message. Should be created on instance creation.

Get: Id(self: IMessage) -> Guid

"""

    Label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Label(self: IMessage) -> str

Set: Label(self: IMessage) = value
"""

    Log = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Log(self: IMessage) -> str

Set: Log(self: IMessage) = value
"""

    ParentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ParentId(self: IMessage) -> Nullable[Guid]

Set: ParentId(self: IMessage) = value
"""

    Priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Priority(self: IMessage) -> MessagePriority

Set: Priority(self: IMessage) = value
"""

    ReferenceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A reference which remain the same when messages are resubmitted.

Get: ReferenceId(self: IMessage) -> Nullable[Guid]

Set: ReferenceId(self: IMessage) = value
"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Source(self: IMessage) -> str

Set: Source(self: IMessage) = value
"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Status(self: IMessage) -> MessageStatus

Set: Status(self: IMessage) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Type(self: IMessage) -> str

Set: Type(self: IMessage) = value
"""


    Instance = IMessage()
    """hardcoded/returns an instance of the class"""

class IMessageHandler:
    # no doc
    def CanHandle(self, message):
        """ CanHandle(self: IMessageHandler, message: IMessage) -> bool """
        pass

    def Handle(self, message):
        """ Handle(self: IMessageHandler, message: IMessage) -> HandleResult """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    MetaData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MetaData(self: IMessageHandler) -> HandlerDescriptorAttribute

"""

    OnLogError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnLogError(self: IMessageHandler) -> OnLogMessage

Set: OnLogError(self: IMessageHandler) = value
"""

    OnLogMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnLogMessage(self: IMessageHandler) -> OnLogMessage

Set: OnLogMessage(self: IMessageHandler) = value
"""

    OnLogWarning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnLogWarning(self: IMessageHandler) -> OnLogMessage

Set: OnLogWarning(self: IMessageHandler) = value
"""


    Instance = IMessageHandler()
    """hardcoded/returns an instance of the class"""

class IMessagePublisher:
    # no doc
    def Start(self, onStoreMessage):
        """ Start(self: IMessagePublisher, onStoreMessage: OnStoreMessage) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    MetaData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MetaData(self: IMessagePublisher) -> PublisherDescriptorAttribute

"""

    OnLogError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnLogError(self: IMessagePublisher) -> OnLogMessage

Set: OnLogError(self: IMessagePublisher) = value
"""

    OnLogMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnLogMessage(self: IMessagePublisher) -> OnLogMessage

Set: OnLogMessage(self: IMessagePublisher) = value
"""

    OnLogWarning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnLogWarning(self: IMessagePublisher) -> OnLogMessage

Set: OnLogWarning(self: IMessagePublisher) = value
"""


    Instance = IMessagePublisher()
    """hardcoded/returns an instance of the class"""

class IMessagingProvider:
    # no doc
    def GetHandlers(self):
        """ GetHandlers(self: IMessagingProvider) -> IEnumerable[MessageHandlerDescriptor] """
        pass

    def GetPublishers(self):
        """ GetPublishers(self: IMessagingProvider) -> IEnumerable[MessagePublisherDescriptor] """
        pass

    def Initialize(self, args):
        """ Initialize(self: IMessagingProvider, args: MessagingProviderInitializationArguments) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Instance = IMessagingProvider()
    """hardcoded/returns an instance of the class"""

class IQueueProvider:
    # no doc
    def GetQueueListener(self):
        """ GetQueueListener(self: IQueueProvider) -> IQueueListener """
        pass

    def GetQueuePublisher(self):
        """ GetQueuePublisher(self: IQueueProvider) -> IQueuePublisher """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Instance = IQueueProvider()
    """hardcoded/returns an instance of the class"""

class MessageBase:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Body(self: MessageBase) -> Array[Byte]

Set: Body(self: MessageBase) = value
"""

    BodyMimeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: BodyMimeType(self: MessageBase) -> str

Set: BodyMimeType(self: MessageBase) = value
"""

    HasStockAllocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HasStockAllocations(self: MessageBase) -> bool

Set: HasStockAllocations(self: MessageBase) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Id(self: MessageBase) -> Guid

"""

    Label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Label(self: MessageBase) -> str

Set: Label(self: MessageBase) = value
"""

    Log = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Log(self: MessageBase) -> str

Set: Log(self: MessageBase) = value
"""

    ParentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ParentId(self: MessageBase) -> Nullable[Guid]

Set: ParentId(self: MessageBase) = value
"""

    Priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Priority(self: MessageBase) -> MessagePriority

Set: Priority(self: MessageBase) = value
"""

    ReferenceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ReferenceId(self: MessageBase) -> Nullable[Guid]

Set: ReferenceId(self: MessageBase) = value
"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Source(self: MessageBase) -> str

Set: Source(self: MessageBase) = value
"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Status(self: MessageBase) -> MessageStatus

Set: Status(self: MessageBase) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Type(self: MessageBase) -> str

Set: Type(self: MessageBase) = value
"""


    Instance = MessageBase()
    """hardcoded/returns an instance of the class"""

class MessageHandlerBase:
    # no doc
    def CanHandle(self, message):
        """ CanHandle(self: MessageHandlerBase, message: IMessage) -> bool """
        pass

    def Handle(self, message):
        """ Handle(self: MessageHandlerBase, message: IMessage) -> HandleResult """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    MetaData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MetaData(self: MessageHandlerBase) -> HandlerDescriptorAttribute

"""

    OnLogError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OnLogError(self: MessageHandlerBase) -> OnLogMessage

Set: OnLogError(self: MessageHandlerBase) = value
"""

    OnLogMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OnLogMessage(self: MessageHandlerBase) -> OnLogMessage

Set: OnLogMessage(self: MessageHandlerBase) = value
"""

    OnLogWarning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OnLogWarning(self: MessageHandlerBase) -> OnLogMessage

Set: OnLogWarning(self: MessageHandlerBase) = value
"""


    Instance = MessageHandlerBase()
    """hardcoded/returns an instance of the class"""

class MessagePriority:
    """ enum MessagePriority, values: AboveNormal (4), High (5), Highest (7), Low (2), Lowest (0), Normal (3), VeryHigh (6), VeryLow (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AboveNormal = None
    High = None
    Highest = None
    Low = None
    Lowest = None
    Normal = None
    value__ = None
    VeryHigh = None
    VeryLow = None

    Instance = MessagePriority()
    """hardcoded/returns an instance of the class"""

class MessagePublisherBase:
    # no doc
    def Start(self, onStoreMessage):
        """ Start(self: MessagePublisherBase, onStoreMessage: OnStoreMessage) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    MetaData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MetaData(self: MessagePublisherBase) -> PublisherDescriptorAttribute

"""

    OnLogError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OnLogError(self: MessagePublisherBase) -> OnLogMessage

Set: OnLogError(self: MessagePublisherBase) = value
"""

    OnLogMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OnLogMessage(self: MessagePublisherBase) -> OnLogMessage

Set: OnLogMessage(self: MessagePublisherBase) = value
"""

    OnLogWarning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OnLogWarning(self: MessagePublisherBase) -> OnLogMessage

Set: OnLogWarning(self: MessagePublisherBase) = value
"""


    Instance = MessagePublisherBase()
    """hardcoded/returns an instance of the class"""

class MessageStatus:
    """ enum MessageStatus, values: Enqueued (10), Handled (20), HandledWithErrors (30), Handling (15), New (0), ReSubmitted (40), Undefined (-1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Enqueued = None
    Handled = None
    HandledWithErrors = None
    Handling = None
    New = None
    ReSubmitted = None
    Undefined = None
    value__ = None

    Instance = MessageStatus()
    """hardcoded/returns an instance of the class"""

class MessagingProviderInitializationArguments():
    """ MessagingProviderInitializationArguments() """
    Instance = MessagingProviderInitializationArguments()
    """hardcoded/returns an instance of the class"""

class MessagingProvidersFactory():
    """ MessagingProvidersFactory() """
    @staticmethod
    def GetAll():
        """ GetAll() -> IEnumerable[IMessagingProvider] """
        pass

    @staticmethod
    def GetAllHandlers():
        """ GetAllHandlers() -> IEnumerable[MessageHandlerDescriptor] """
        pass

    @staticmethod
    def GetAllPublishers():
        """ GetAllPublishers() -> IEnumerable[MessagePublisherDescriptor] """
        pass

    @staticmethod
    def InitializeAll():
        """ InitializeAll() -> IEnumerable[IMessagingProvider] """
        pass

    Instance = MessagingProvidersFactory()
    """hardcoded/returns an instance of the class"""

class MsmqProvider:
    """ MsmqProvider(options: MsmqOptions) """
    def GetQueueListener(self):
        """ GetQueueListener(self: MsmqProvider) -> IQueueListener """
        pass

    def GetQueuePublisher(self):
        """ GetQueuePublisher(self: MsmqProvider) -> IQueuePublisher """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, options):
        """ __new__(cls: type, options: MsmqOptions) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Instance = MsmqProvider()
    """hardcoded/returns an instance of the class"""

# variables with complex values

