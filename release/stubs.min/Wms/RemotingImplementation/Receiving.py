# encoding: utf-8
# module Wms.RemotingImplementation.Receiving calls itself Receiving
# from Wms.RemotingImplementation,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class Receiver(object):
 """ Receiver(lines: InboundReceiveLines,args: DataFlowObject[ReceiveArgs]) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Receiver()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Dispose(self):
  """ Dispose(self: Receiver) """
  pass
 def GetReceiveLine(self):
  """ GetReceiveLine(self: Receiver) -> InboundReceiveLine """
  pass
 def Receive(self):
  """ Receive(self: Receiver) -> DataFlowObject[ReceiveArgs] """
  pass
 def ValidateReceiveArgs(self,*args):
  """ ValidateReceiveArgs(self: Receiver) -> bool """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,lines,args):
  """ __new__(cls: type,lines: InboundReceiveLines,args: DataFlowObject[ReceiveArgs]) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Args=None
 DeleteLine=None
 Lines=None


class AdhocReceiver(Receiver):
 """ AdhocReceiver(lines: InboundReceiveLines,args: DataFlowObject[ReceiveArgs]) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return AdhocReceiver()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Receive(self):
  """ Receive(self: Receiver,receiveLine: InboundReceiveLine,orderNumber: str,itemIdNumber: str,quantity: Decimal,endDate: Nullable[DateTime],deleteLine: bool) -> bool """
  pass
 def ValidateReceiveArgs(self,*args):
  """ ValidateReceiveArgs(self: AdhocReceiver) -> bool """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,lines,args):
  """ __new__(cls: type,lines: InboundReceiveLines,args: DataFlowObject[ReceiveArgs]) """
  pass
 Args=None
 DeleteLine=None
 Lines=None


class AdHocRmaReceiver(Receiver):
 """ AdHocRmaReceiver(lines: InboundReceiveLines,args: DataFlowObject[ReceiveArgs]) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return AdHocRmaReceiver()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def AddItemIfNotExists(self,*args):
  """ AddItemIfNotExists(self: AdHocRmaReceiver,id: str) -> bool """
  pass
 def QuantityExceedsQuantityDelivered(self,*args):
  """ QuantityExceedsQuantityDelivered(self: AdHocRmaReceiver,orderLines: HistoryOutboundOrderLines) -> (bool,str) """
  pass
 def Receive(self):
  """ Receive(self: Receiver,receiveLine: InboundReceiveLine,orderNumber: str,itemIdNumber: str,quantity: Decimal,endDate: Nullable[DateTime],deleteLine: bool) -> bool """
  pass
 def ValidateReceiveArgs(self,*args):
  """ ValidateReceiveArgs(self: AdHocRmaReceiver) -> bool """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,lines,args):
  """ __new__(cls: type,lines: InboundReceiveLines,args: DataFlowObject[ReceiveArgs]) """
  pass
 RmaArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)


 Args=None
 DeleteLine=None
 Lines=None
 _item=None


class AdhocRmaTouchReceiver(AdHocRmaReceiver):
 """ AdhocRmaTouchReceiver(lines: InboundReceiveLines,args: DataFlowObject[ReceiveArgs]) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return AdhocRmaTouchReceiver()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def AddItemIfNotExists(self,*args):
  """ AddItemIfNotExists(self: AdhocRmaTouchReceiver,id: str) -> bool """
  pass
 def GetReceiveLine(self):
  """ GetReceiveLine(self: AdhocRmaTouchReceiver) -> InboundReceiveLine """
  pass
 def QuantityExceedsQuantityDelivered(self,*args):
  """ QuantityExceedsQuantityDelivered(self: AdHocRmaReceiver,orderLines: HistoryOutboundOrderLines) -> (bool,str) """
  pass
 def Receive(self):
  """ Receive(self: AdhocRmaTouchReceiver) -> DataFlowObject[ReceiveArgs] """
  pass
 def ValidateReceiveArgs(self,*args):
  """ ValidateReceiveArgs(self: AdHocRmaReceiver) -> bool """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,lines,args):
  """ __new__(cls: type,lines: InboundReceiveLines,args: DataFlowObject[ReceiveArgs]) """
  pass
 RmaArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)


 Args=None
 DeleteLine=None
 Lines=None
 _item=None


class InboundReceiveLineManager(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return InboundReceiveLineManager()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def CheckForExistingPreReceipts(dfObject):
  """ CheckForExistingPreReceipts(dfObject: DataFlowObject[ReceiveLinesForPreReceiptArgs]) -> InboundReceiveLines """
  pass
 @staticmethod
 def CheckForExistingReceipts(dfObject,orderType,receiveLines):
  """ CheckForExistingReceipts[T](dfObject: DataFlowObject[T],orderType: InboundOrderTypeEnum) -> (DataFlowObject[T],InboundReceiveLines) """
  pass
 @staticmethod
 def GetInboundReceiveLines(warehouseCode,customerNumber,orderType):
  """ GetInboundReceiveLines(warehouseCode: str,customerNumber: str,orderType: InboundOrderTypeEnum) -> InboundReceiveLines """
  pass
 __all__=[
  'CheckForExistingPreReceipts',
  'CheckForExistingReceipts',
  'GetInboundReceiveLines',
 ]


class ReceiverFactory(object):
 """ ReceiverFactory(lines: InboundReceiveLines,dfObject: DataFlowObject[ReceiveArgs]) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReceiverFactory()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def CreateReceiver(self):
  """ CreateReceiver(self: ReceiverFactory) -> Receiver """
  pass
 def Dispose(self):
  """ Dispose(self: ReceiverFactory) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,lines,dfObject):
  """ __new__(cls: type,lines: InboundReceiveLines,dfObject: DataFlowObject[ReceiveArgs]) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass

