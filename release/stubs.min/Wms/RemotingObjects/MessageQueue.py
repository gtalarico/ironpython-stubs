# encoding: utf-8
# module Wms.RemotingObjects.MessageQueue calls itself MessageQueue
# from Wms.RemotingObjects,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class CleanupMessageHistoryArgs(object):
 """ CleanupMessageHistoryArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return CleanupMessageHistoryArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 OlderThenDays=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Messages before this date will be deleted.

Get: OlderThenDays(self: CleanupMessageHistoryArgs) -> int

Set: OlderThenDays(self: CleanupMessageHistoryArgs)=value
"""



class DequeueResult(object):
 """ DequeueResult() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DequeueResult()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 IsLastMessage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Signals caller if there are any messages left after this message.

Get: IsLastMessage(self: DequeueResult) -> bool

Set: IsLastMessage(self: DequeueResult)=value
"""

 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Dequeued Message. Record in table already has status Enqueued.

Get: Message(self: DequeueResult) -> IMessage

Set: Message(self: DequeueResult)=value
"""



class ExecuteMessageHandlerArgs(object):
 """ ExecuteMessageHandlerArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ExecuteMessageHandlerArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 ExecutedIsolated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ExecutedIsolated(self: ExecuteMessageHandlerArgs) -> bool

Set: ExecutedIsolated(self: ExecuteMessageHandlerArgs)=value
"""

 HandlerId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: HandlerId(self: ExecuteMessageHandlerArgs) -> Guid

Set: HandlerId(self: ExecuteMessageHandlerArgs)=value
"""

 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Message(self: ExecuteMessageHandlerArgs) -> IMessage

Set: Message(self: ExecuteMessageHandlerArgs)=value
"""



class ExecuteMessageHandlerResult(object):
 """ ExecuteMessageHandlerResult() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ExecuteMessageHandlerResult()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Message(self: ExecuteMessageHandlerResult) -> str

Set: Message(self: ExecuteMessageHandlerResult)=value
"""

 Success=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Success(self: ExecuteMessageHandlerResult) -> bool

Set: Success(self: ExecuteMessageHandlerResult)=value
"""



class ExecuteMessagePublisherArgs(object):
 """ ExecuteMessagePublisherArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ExecuteMessagePublisherArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 ExecuteIsolated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ExecuteIsolated(self: ExecuteMessagePublisherArgs) -> bool

Set: ExecuteIsolated(self: ExecuteMessagePublisherArgs)=value
"""

 PublisherId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PublisherId(self: ExecuteMessagePublisherArgs) -> Guid

Set: PublisherId(self: ExecuteMessagePublisherArgs)=value
"""



class ExecuteMessagePublisherResult(object):
 """ ExecuteMessagePublisherResult() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ExecuteMessagePublisherResult()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Success=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Success(self: ExecuteMessagePublisherResult) -> bool

Set: Success(self: ExecuteMessagePublisherResult)=value
"""



class GetDistinctTypeListArgs(object):
 """ GetDistinctTypeListArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return GetDistinctTypeListArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 DaysBackToIncludeInDistinct=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DaysBackToIncludeInDistinct(self: GetDistinctTypeListArgs) -> Nullable[int]

Set: DaysBackToIncludeInDistinct(self: GetDistinctTypeListArgs)=value
"""



class GetMessageHandlersArgs(object):
 """ GetMessageHandlersArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return GetMessageHandlersArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""

class GetMessagePublishersArgs(object):
 """ GetMessagePublishersArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return GetMessagePublishersArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""

class GetMessagesArgs(object):
 """ GetMessagesArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return GetMessagesArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 MessageStatusses=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: MessageStatusses(self: GetMessagesArgs) -> Array[int]

Set: MessageStatusses(self: GetMessagesArgs)=value
"""

 MessageTypes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: MessageTypes(self: GetMessagesArgs) -> List[str]

Set: MessageTypes(self: GetMessagesArgs)=value
"""

 SearchText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: SearchText(self: GetMessagesArgs) -> str

Set: SearchText(self: GetMessagesArgs)=value
"""



class MessageBodyDecodeAs:
 """ enum MessageBodyDecodeAs,values: Ascii (0),Unicode (3),Utf16 (2),Utf8 (1) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MessageBodyDecodeAs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
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


class MessageHandlerDescriptorSerializable(object):
 """
 MessageHandlerDescriptorSerializable()
 MessageHandlerDescriptorSerializable(seed: MessageHandlerDescriptor)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MessageHandlerDescriptorSerializable()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,seed=None):
  """
  __new__(cls: type)
  __new__(cls: type,seed: MessageHandlerDescriptor)
  """
  pass
 ExecuteIsolated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ExecuteIsolated(self: MessageHandlerDescriptorSerializable) -> bool

Set: ExecuteIsolated(self: MessageHandlerDescriptorSerializable)=value
"""

 FriendlyName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: FriendlyName(self: MessageHandlerDescriptorSerializable) -> str

Set: FriendlyName(self: MessageHandlerDescriptorSerializable)=value
"""

 FullName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: FullName(self: MessageHandlerDescriptorSerializable) -> str

Set: FullName(self: MessageHandlerDescriptorSerializable)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Id(self: MessageHandlerDescriptorSerializable) -> Guid

Set: Id(self: MessageHandlerDescriptorSerializable)=value
"""



class MessagePublisherDescriptorSerializable(object):
 """
 MessagePublisherDescriptorSerializable()
 MessagePublisherDescriptorSerializable(seed: MessagePublisherDescriptor)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MessagePublisherDescriptorSerializable()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,seed=None):
  """
  __new__(cls: type)
  __new__(cls: type,seed: MessagePublisherDescriptor)
  """
  pass
 ExecuteIsolated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ExecuteIsolated(self: MessagePublisherDescriptorSerializable) -> bool

Set: ExecuteIsolated(self: MessagePublisherDescriptorSerializable)=value
"""

 FriendlyName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: FriendlyName(self: MessagePublisherDescriptorSerializable) -> str

Set: FriendlyName(self: MessagePublisherDescriptorSerializable)=value
"""

 FullName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: FullName(self: MessagePublisherDescriptorSerializable) -> str

Set: FullName(self: MessagePublisherDescriptorSerializable)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Id(self: MessagePublisherDescriptorSerializable) -> Guid

Set: Id(self: MessagePublisherDescriptorSerializable)=value
"""



class Messages(FindableList):
 """
 Container for the Wms.EdiMessaging.IMessage objects.
 
 Messages()
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Messages()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
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
 """when paging is used this property holds the total number of rows 
   which are returned by the query

Get: TotalRowsMatched(self: Messages) -> Int64

Set: TotalRowsMatched(self: Messages)=value
"""



class MessagingMessage(MessageBase):
 """
 MessagingMessage()
 MessagingMessage(id: Guid)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MessagingMessage()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
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
 """Message's Body Size in Bytes

Get: BodySize(self: MessagingMessage) -> Int64

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



