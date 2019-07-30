# encoding: utf-8
# module Wms.RemotingImplementation.EdiMessaging.Messages calls itself Messages
# from Wms.RemotingImplementation,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from System.Collections.Generic import *
from ..__init__ import *

# no functions
# classes

class ProcessDirectOrderMessage(MessageBase):
 """
 ProcessDirectOrderMessage()
 ProcessDirectOrderMessage(message: IMessage)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ProcessDirectOrderMessage()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message=None):
  """
  __new__(cls: type)
  __new__(cls: type,message: IMessage)
  """
  pass
 Data=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Data(self: ProcessDirectOrderMessage) -> ProcessDirectOrderMessageData

Set: Data(self: ProcessDirectOrderMessage)=value
"""


 TypeName='Direct Order Fulfillment'


class ProcessDirectOrderMessageData(object):
 """
 ProcessDirectOrderMessageData()
 ProcessDirectOrderMessageData(directOrder: DirectOrder)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ProcessDirectOrderMessageData()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,directOrder=None):
  """
  __new__(cls: type)
  __new__(cls: type,directOrder: DirectOrder)
  """
  pass
 DirectOrder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DirectOrder(self: ProcessDirectOrderMessageData) -> DirectOrder

Set: DirectOrder(self: ProcessDirectOrderMessageData)=value
"""

 IsFulFilledInBoxWise=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsFulFilledInBoxWise(self: ProcessDirectOrderMessageData) -> bool

Set: IsFulFilledInBoxWise(self: ProcessDirectOrderMessageData)=value
"""

 IsLoggedInHistoryTables=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsLoggedInHistoryTables(self: ProcessDirectOrderMessageData) -> bool

Set: IsLoggedInHistoryTables(self: ProcessDirectOrderMessageData)=value
"""

 IsProcessedInErp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsProcessedInErp(self: ProcessDirectOrderMessageData) -> bool

Set: IsProcessedInErp(self: ProcessDirectOrderMessageData)=value
"""

 Label=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Label(self: ProcessDirectOrderMessageData) -> str

"""



class ProcessPreReceiptMessage(MessageBase):
 """
 ProcessPreReceiptMessage()
 ProcessPreReceiptMessage(message: IMessage)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ProcessPreReceiptMessage()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message=None):
  """
  __new__(cls: type)
  __new__(cls: type,message: IMessage)
  """
  pass
 Data=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Data(self: ProcessPreReceiptMessage) -> ProcessPreReceiptMessageData

Set: Data(self: ProcessPreReceiptMessage)=value
"""


 TypeName='Prereceipt Fulfillment'


class ProcessPreReceiptMessageData(object):
 """ ProcessPreReceiptMessageData() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ProcessPreReceiptMessageData()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 DefaultInboundLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DefaultInboundLocation(self: ProcessPreReceiptMessageData) -> str

Set: DefaultInboundLocation(self: ProcessPreReceiptMessageData)=value
"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Description(self: ProcessPreReceiptMessageData) -> str

Set: Description(self: ProcessPreReceiptMessageData)=value
"""

 PreReceiptId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreReceiptId(self: ProcessPreReceiptMessageData) -> int

Set: PreReceiptId(self: ProcessPreReceiptMessageData)=value
"""

 TransactionId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TransactionId(self: ProcessPreReceiptMessageData) -> Guid

Set: TransactionId(self: ProcessPreReceiptMessageData)=value
"""

 YourReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: YourReference(self: ProcessPreReceiptMessageData) -> str

Set: YourReference(self: ProcessPreReceiptMessageData)=value
"""



class ProcessSalesOrderMessage(MessageBase):
 """
 ProcessSalesOrderMessage()
 ProcessSalesOrderMessage(message: IMessage)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ProcessSalesOrderMessage()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message=None):
  """
  __new__(cls: type)
  __new__(cls: type,message: IMessage)
  """
  pass
 Data=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Data(self: ProcessSalesOrderMessage) -> ProcessSalesOrderMessageData

Set: Data(self: ProcessSalesOrderMessage)=value
"""


 TypeName='Sales Order Fulfillment'


class ProcessSalesOrderMessageData(object):
 """ ProcessSalesOrderMessageData() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ProcessSalesOrderMessageData()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Arguments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Arguments(self: ProcessSalesOrderMessageData) -> ProcessSalesOrderLinesArgs

Set: Arguments(self: ProcessSalesOrderMessageData)=value
"""

 Lines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Lines(self: ProcessSalesOrderMessageData) -> List[SalesOrderLine]

Set: Lines(self: ProcessSalesOrderMessageData)=value
"""

 Order=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Order(self: ProcessSalesOrderMessageData) -> SalesOrder

Set: Order(self: ProcessSalesOrderMessageData)=value
"""



class StockOnLocationChangedMessage(MessageBase):
 """ StockOnLocationChangedMessage() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return StockOnLocationChangedMessage()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Location=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Location(self: StockOnLocationChangedMessage) -> Location

Set: Location(self: StockOnLocationChangedMessage)=value
"""


 TypeName='Stock changed on location'


# variables with complex values

