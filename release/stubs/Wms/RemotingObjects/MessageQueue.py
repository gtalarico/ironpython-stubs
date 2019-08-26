from Wms.EdiMessaging import *
from Wms.RemotingObjects import *
# encoding: utf-8
# module Wms.RemotingObjects.MessageQueue calls itself MessageQueue
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CleanupMessageHistoryArgs():
    """ CleanupMessageHistoryArgs() """
    OlderThenDays = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Messages before this date will be deleted.

Get: OlderThenDays(self: CleanupMessageHistoryArgs) -> int

Set: OlderThenDays(self: CleanupMessageHistoryArgs) = value
"""


    Instance = CleanupMessageHistoryArgs()
    """hardcoded/returns an instance of the class"""

class DequeueResult():
    """ DequeueResult() """
    IsLastMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Signals caller if there are any messages left after this message.

Get: IsLastMessage(self: DequeueResult) -> bool

Set: IsLastMessage(self: DequeueResult) = value
"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Dequeued Message. Record in table already has status Enqueued.

Get: Message(self: DequeueResult) -> IMessage

Set: Message(self: DequeueResult) = value
"""


    Instance = DequeueResult()
    """hardcoded/returns an instance of the class"""

class ExecuteMessageHandlerArgs():
    """ ExecuteMessageHandlerArgs() """
    ExecutedIsolated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ExecutedIsolated(self: ExecuteMessageHandlerArgs) -> bool

Set: ExecutedIsolated(self: ExecuteMessageHandlerArgs) = value
"""

    HandlerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HandlerId(self: ExecuteMessageHandlerArgs) -> Guid

Set: HandlerId(self: ExecuteMessageHandlerArgs) = value
"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Message(self: ExecuteMessageHandlerArgs) -> IMessage

Set: Message(self: ExecuteMessageHandlerArgs) = value
"""


    Instance = ExecuteMessageHandlerArgs()
    """hardcoded/returns an instance of the class"""

class ExecuteMessageHandlerResult():
    """ ExecuteMessageHandlerResult() """
    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Message(self: ExecuteMessageHandlerResult) -> str

Set: Message(self: ExecuteMessageHandlerResult) = value
"""

    Success = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Success(self: ExecuteMessageHandlerResult) -> bool

Set: Success(self: ExecuteMessageHandlerResult) = value
"""


    Instance = ExecuteMessageHandlerResult()
    """hardcoded/returns an instance of the class"""

class ExecuteMessagePublisherArgs():
    """ ExecuteMessagePublisherArgs() """
    ExecuteIsolated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ExecuteIsolated(self: ExecuteMessagePublisherArgs) -> bool

Set: ExecuteIsolated(self: ExecuteMessagePublisherArgs) = value
"""

    PublisherId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PublisherId(self: ExecuteMessagePublisherArgs) -> Guid

Set: PublisherId(self: ExecuteMessagePublisherArgs) = value
"""


    Instance = ExecuteMessagePublisherArgs()
    """hardcoded/returns an instance of the class"""

class ExecuteMessagePublisherResult():
    """ ExecuteMessagePublisherResult() """
    Success = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Success(self: ExecuteMessagePublisherResult) -> bool

Set: Success(self: ExecuteMessagePublisherResult) = value
"""


    Instance = ExecuteMessagePublisherResult()
    """hardcoded/returns an instance of the class"""

class GetDistinctTypeListArgs():
    """ GetDistinctTypeListArgs() """
    DaysBackToIncludeInDistinct = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DaysBackToIncludeInDistinct(self: GetDistinctTypeListArgs) -> Nullable[int]

Set: DaysBackToIncludeInDistinct(self: GetDistinctTypeListArgs) = value
"""


    Instance = GetDistinctTypeListArgs()
    """hardcoded/returns an instance of the class"""

class GetMessageHandlersArgs():
    """ GetMessageHandlersArgs() """
    Instance = GetMessageHandlersArgs()
    """hardcoded/returns an instance of the class"""

class GetMessagePublishersArgs():
    """ GetMessagePublishersArgs() """
    Instance = GetMessagePublishersArgs()
    """hardcoded/returns an instance of the class"""

class GetMessagesArgs():
    """ GetMessagesArgs() """
    MessageStatusses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MessageStatusses(self: GetMessagesArgs) -> Array[int]

Set: MessageStatusses(self: GetMessagesArgs) = value
"""

    MessageTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MessageTypes(self: GetMessagesArgs) -> List[str]

Set: MessageTypes(self: GetMessagesArgs) = value
"""

    SearchText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SearchText(self: GetMessagesArgs) -> str

Set: SearchText(self: GetMessagesArgs) = value
"""


    Instance = GetMessagesArgs()
    """hardcoded/returns an instance of the class"""

class MessageBodyDecodeAs:
    """ enum MessageBodyDecodeAs, values: Ascii (0), Unicode (3), Utf16 (2), Utf8 (1) """
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

    Ascii = None
    Unicode = None
    Utf16 = None
    Utf8 = None
    value__ = None

    Instance = MessageBodyDecodeAs()
    """hardcoded/returns an instance of the class"""

class MessageHandlerDescriptorSerializable():
    """
    MessageHandlerDescriptorSerializable()
    MessageHandlerDescriptorSerializable(seed: MessageHandlerDescriptor)
    """
    @staticmethod # known case of __new__
    def __new__(self, seed=None):
        """
        __new__(cls: type)
        __new__(cls: type, seed: MessageHandlerDescriptor)
        """
        pass

    ExecuteIsolated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ExecuteIsolated(self: MessageHandlerDescriptorSerializable) -> bool

Set: ExecuteIsolated(self: MessageHandlerDescriptorSerializable) = value
"""

    FriendlyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: FriendlyName(self: MessageHandlerDescriptorSerializable) -> str

Set: FriendlyName(self: MessageHandlerDescriptorSerializable) = value
"""

    FullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: FullName(self: MessageHandlerDescriptorSerializable) -> str

Set: FullName(self: MessageHandlerDescriptorSerializable) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Id(self: MessageHandlerDescriptorSerializable) -> Guid

Set: Id(self: MessageHandlerDescriptorSerializable) = value
"""


    Instance = MessageHandlerDescriptorSerializable()
    """hardcoded/returns an instance of the class"""

class MessagePublisherDescriptorSerializable():
    """
    MessagePublisherDescriptorSerializable()
    MessagePublisherDescriptorSerializable(seed: MessagePublisherDescriptor)
    """
    @staticmethod # known case of __new__
    def __new__(self, seed=None):
        """
        __new__(cls: type)
        __new__(cls: type, seed: MessagePublisherDescriptor)
        """
        pass

    ExecuteIsolated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ExecuteIsolated(self: MessagePublisherDescriptorSerializable) -> bool

Set: ExecuteIsolated(self: MessagePublisherDescriptorSerializable) = value
"""

    FriendlyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: FriendlyName(self: MessagePublisherDescriptorSerializable) -> str

Set: FriendlyName(self: MessagePublisherDescriptorSerializable) = value
"""

    FullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: FullName(self: MessagePublisherDescriptorSerializable) -> str

Set: FullName(self: MessagePublisherDescriptorSerializable) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Id(self: MessagePublisherDescriptorSerializable) -> Guid

Set: Id(self: MessagePublisherDescriptorSerializable) = value
"""


    Instance = MessagePublisherDescriptorSerializable()
    """hardcoded/returns an instance of the class"""

class Messages(FindableList):
    """
    Container for the Wms.EdiMessaging.IMessage objects.
    
    Messages()
    """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """when paging is used this property holds the total number of rows 
            which are returned by the query

Get: TotalRowsMatched(self: Messages) -> Int64

Set: TotalRowsMatched(self: Messages) = value
"""


    Instance = Messages()
    """hardcoded/returns an instance of the class"""

class MessagingMessage(MessageBase):
    """
    MessagingMessage()
    MessagingMessage(id: Guid)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, id=None):
        """
        __new__(cls: type)
        __new__(cls: type, id: Guid)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    BodySize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Message's Body Size in Bytes

Get: BodySize(self: MessagingMessage) -> Int64

Set: BodySize(self: MessagingMessage) = value
"""

    CreatedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatedBy(self: MessagingMessage) -> str

Set: CreatedBy(self: MessagingMessage) = value
"""

    CreatedOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatedOn(self: MessagingMessage) -> DateTime

Set: CreatedOn(self: MessagingMessage) = value
"""

    ModifiedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModifiedBy(self: MessagingMessage) -> str

Set: ModifiedBy(self: MessagingMessage) = value
"""

    ModifiedOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModifiedOn(self: MessagingMessage) -> DateTime

Set: ModifiedOn(self: MessagingMessage) = value
"""


    Instance = MessagingMessage()
    """hardcoded/returns an instance of the class"""

