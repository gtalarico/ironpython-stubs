# encoding: utf-8
# module Wms.RemotingObjects.MessageQueue calls itself MessageQueue
# from Wms.RemotingObjects,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CleanupMessageHistoryArgs:
 """ CleanupMessageHistoryArgs() """
 OlderThenDays=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OlderThenDays(self: CleanupMessageHistoryArgs) -> int

Set: OlderThenDays(self: CleanupMessageHistoryArgs)=value
"""



class DequeueResult:
 """ DequeueResult() """
 IsLastMessage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsLastMessage(self: DequeueResult) -> bool

Set: IsLastMessage(self: DequeueResult)=value
"""

 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Message(self: DequeueResult) -> IMessage

Set: Message(self: DequeueResult)=value
"""



class ExecuteMessageHandlerArgs:
 """ ExecuteMessageHandlerArgs() """
 ExecutedIsolated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExecutedIsolated(self: ExecuteMessageHandlerArgs) -> bool

Set: ExecutedIsolated(self: ExecuteMessageHandlerArgs)=value
"""

 HandlerId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HandlerId(self: ExecuteMessageHandlerArgs) -> Guid

Set: HandlerId(self: ExecuteMessageHandlerArgs)=value
"""

 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Message(self: ExecuteMessageHandlerArgs) -> IMessage

Set: Message(self: ExecuteMessageHandlerArgs)=value
"""



class ExecuteMessageHandlerResult:
 """ ExecuteMessageHandlerResult() """
 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Message(self: ExecuteMessageHandlerResult) -> str

Set: Message(self: ExecuteMessageHandlerResult)=value
"""

 Success=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Success(self: ExecuteMessageHandlerResult) -> bool

Set: Success(self: ExecuteMessageHandlerResult)=value
"""



class ExecuteMessagePublisherArgs:
 """ ExecuteMessagePublisherArgs() """
 ExecuteIsolated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExecuteIsolated(self: ExecuteMessagePublisherArgs) -> bool

Set: ExecuteIsolated(self: ExecuteMessagePublisherArgs)=value
"""

 PublisherId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PublisherId(self: ExecuteMessagePublisherArgs) -> Guid

Set: PublisherId(self: ExecuteMessagePublisherArgs)=value
"""



class ExecuteMessagePublisherResult:
 """ ExecuteMessagePublisherResult() """
 Success=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Success(self: ExecuteMessagePublisherResult) -> bool

Set: Success(self: ExecuteMessagePublisherResult)=value
"""



class GetDistinctTypeListArgs:
 """ GetDistinctTypeListArgs() """
 DaysBackToIncludeInDistinct=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DaysBackToIncludeInDistinct(self: GetDistinctTypeListArgs) -> Nullable[int]

Set: DaysBackToIncludeInDistinct(self: GetDistinctTypeListArgs)=value
"""



class GetMessageHandlersArgs:
 """ GetMessageHandlersArgs() """

class GetMessagePublishersArgs:
 """ GetMessagePublishersArgs() """

class GetMessagesArgs:
 """ GetMessagesArgs() """
 MessageStatusses=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MessageStatusses(self: GetMessagesArgs) -> Array[int]

Set: MessageStatusses(self: GetMessagesArgs)=value
"""

 MessageTypes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MessageTypes(self: GetMessagesArgs) -> List[str]

Set: MessageTypes(self: GetMessagesArgs)=value
"""

 SearchText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SearchText(self: GetMessagesArgs) -> str

Set: SearchText(self: GetMessagesArgs)=value
"""



class MessageBodyDecodeAs:
 """ enum MessageBodyDecodeAs,values: Ascii (0),Unicode (3),Utf16 (2),Utf8 (1) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Ascii=None
 Unicode=None
 Utf16=None
 Utf8=None
 value__=None


class MessageHandlerDescriptorSerializable:
 """
 MessageHandlerDescriptorSerializable()
 MessageHandlerDescriptorSerializable(seed: MessageHandlerDescriptor)
 """
 @staticmethod
 def __new__(self,seed=None):
  """
  __new__(cls: type)
  __new__(cls: type,seed: MessageHandlerDescriptor)
  """
  pass
 ExecuteIsolated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExecuteIsolated(self: MessageHandlerDescriptorSerializable) -> bool

Set: ExecuteIsolated(self: MessageHandlerDescriptorSerializable)=value
"""

 FriendlyName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FriendlyName(self: MessageHandlerDescriptorSerializable) -> str

Set: FriendlyName(self: MessageHandlerDescriptorSerializable)=value
"""

 FullName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FullName(self: MessageHandlerDescriptorSerializable) -> str

Set: FullName(self: MessageHandlerDescriptorSerializable)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: MessageHandlerDescriptorSerializable) -> Guid

Set: Id(self: MessageHandlerDescriptorSerializable)=value
"""



class MessagePublisherDescriptorSerializable:
 """
 MessagePublisherDescriptorSerializable()
 MessagePublisherDescriptorSerializable(seed: MessagePublisherDescriptor)
 """
 @staticmethod
 def __new__(self,seed=None):
  """
  __new__(cls: type)
  __new__(cls: type,seed: MessagePublisherDescriptor)
  """
  pass
 ExecuteIsolated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExecuteIsolated(self: MessagePublisherDescriptorSerializable) -> bool

Set: ExecuteIsolated(self: MessagePublisherDescriptorSerializable)=value
"""

 FriendlyName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FriendlyName(self: MessagePublisherDescriptorSerializable) -> str

Set: FriendlyName(self: MessagePublisherDescriptorSerializable)=value
"""

 FullName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FullName(self: MessagePublisherDescriptorSerializable) -> str

Set: FullName(self: MessagePublisherDescriptorSerializable)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: MessagePublisherDescriptorSerializable) -> Guid

Set: Id(self: MessagePublisherDescriptorSerializable)=value
"""



class Messages:
 """ Messages() """
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 TotalRowsMatched=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TotalRowsMatched(self: Messages) -> Int64

Set: TotalRowsMatched(self: Messages)=value
"""



class MessagingMessage:
 """
 MessagingMessage()
 MessagingMessage(id: Guid)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,id=None):
  """
  __new__(cls: type)
  __new__(cls: type,id: Guid)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 BodySize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BodySize(self: MessagingMessage) -> Int64

Set: BodySize(self: MessagingMessage)=value
"""

 CreatedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CreatedBy(self: MessagingMessage) -> str

Set: CreatedBy(self: MessagingMessage)=value
"""

 CreatedOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CreatedOn(self: MessagingMessage) -> DateTime

Set: CreatedOn(self: MessagingMessage)=value
"""

 ModifiedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ModifiedBy(self: MessagingMessage) -> str

Set: ModifiedBy(self: MessagingMessage)=value
"""

 ModifiedOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ModifiedOn(self: MessagingMessage) -> DateTime

Set: ModifiedOn(self: MessagingMessage)=value
"""



