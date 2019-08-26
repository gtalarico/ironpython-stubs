# encoding: utf-8
# module Wms.RemotingImplementation.Receiving calls itself Receiving
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Receiver:
    """ Receiver(lines: InboundReceiveLines, args: DataFlowObject[ReceiveArgs]) """
    def Dispose(self):
        """ Dispose(self: Receiver) """
        pass

    def GetReceiveLine(self):
        """ GetReceiveLine(self: Receiver) -> InboundReceiveLine """
        pass

    def Receive(self):
        """ Receive(self: Receiver) -> DataFlowObject[ReceiveArgs] """
        pass

    def ValidateReceiveArgs(self, *args): #cannot find CLR method
        """ ValidateReceiveArgs(self: Receiver) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, lines, args):
        """ __new__(cls: type, lines: InboundReceiveLines, args: DataFlowObject[ReceiveArgs]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Args = None
    DeleteLine = None
    Lines = None

    Instance = Receiver()
    """hardcoded/returns an instance of the class"""

class AdhocReceiver(Receiver):
    """ AdhocReceiver(lines: InboundReceiveLines, args: DataFlowObject[ReceiveArgs]) """
    def Receive(self):
        """ Receive(self: Receiver, receiveLine: InboundReceiveLine, orderNumber: str, itemIdNumber: str, quantity: Decimal, endDate: Nullable[DateTime], deleteLine: bool) -> bool """
        pass

    def ValidateReceiveArgs(self, *args): #cannot find CLR method
        """ ValidateReceiveArgs(self: AdhocReceiver) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, lines, args):
        """ __new__(cls: type, lines: InboundReceiveLines, args: DataFlowObject[ReceiveArgs]) """
        pass

    Args = None
    DeleteLine = None
    Lines = None

    Instance = AdhocReceiver()
    """hardcoded/returns an instance of the class"""

class AdHocRmaReceiver(Receiver):
    """ AdHocRmaReceiver(lines: InboundReceiveLines, args: DataFlowObject[ReceiveArgs]) """
    def AddItemIfNotExists(self, *args): #cannot find CLR method
        """ AddItemIfNotExists(self: AdHocRmaReceiver, id: str) -> bool """
        pass

    def QuantityExceedsQuantityDelivered(self, *args): #cannot find CLR method
        """ QuantityExceedsQuantityDelivered(self: AdHocRmaReceiver, orderLines: HistoryOutboundOrderLines) -> (bool, str) """
        pass

    def Receive(self):
        """ Receive(self: Receiver, receiveLine: InboundReceiveLine, orderNumber: str, itemIdNumber: str, quantity: Decimal, endDate: Nullable[DateTime], deleteLine: bool) -> bool """
        pass

    def ValidateReceiveArgs(self, *args): #cannot find CLR method
        """ ValidateReceiveArgs(self: AdHocRmaReceiver) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, lines, args):
        """ __new__(cls: type, lines: InboundReceiveLines, args: DataFlowObject[ReceiveArgs]) """
        pass

    RmaArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    Args = None
    DeleteLine = None
    Lines = None
    _item = None

    Instance = AdHocRmaReceiver()
    """hardcoded/returns an instance of the class"""

class AdhocRmaTouchReceiver(AdHocRmaReceiver):
    """ AdhocRmaTouchReceiver(lines: InboundReceiveLines, args: DataFlowObject[ReceiveArgs]) """
    def AddItemIfNotExists(self, *args): #cannot find CLR method
        """ AddItemIfNotExists(self: AdhocRmaTouchReceiver, id: str) -> bool """
        pass

    def GetReceiveLine(self):
        """ GetReceiveLine(self: AdhocRmaTouchReceiver) -> InboundReceiveLine """
        pass

    def QuantityExceedsQuantityDelivered(self, *args): #cannot find CLR method
        """ QuantityExceedsQuantityDelivered(self: AdHocRmaReceiver, orderLines: HistoryOutboundOrderLines) -> (bool, str) """
        pass

    def Receive(self):
        """ Receive(self: AdhocRmaTouchReceiver) -> DataFlowObject[ReceiveArgs] """
        pass

    def ValidateReceiveArgs(self, *args): #cannot find CLR method
        """ ValidateReceiveArgs(self: AdHocRmaReceiver) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, lines, args):
        """ __new__(cls: type, lines: InboundReceiveLines, args: DataFlowObject[ReceiveArgs]) """
        pass

    RmaArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    Args = None
    DeleteLine = None
    Lines = None
    _item = None

    Instance = AdhocRmaTouchReceiver()
    """hardcoded/returns an instance of the class"""

class InboundReceiveLineManager():
    # no doc
    @staticmethod
    def CheckForExistingPreReceipts(dfObject):
        """ CheckForExistingPreReceipts(dfObject: DataFlowObject[ReceiveLinesForPreReceiptArgs]) -> InboundReceiveLines """
        pass

    @staticmethod
    def CheckForExistingReceipts(dfObject, orderType, receiveLines):
        """ CheckForExistingReceipts[T](dfObject: DataFlowObject[T], orderType: InboundOrderTypeEnum) -> (DataFlowObject[T], InboundReceiveLines) """
        pass

    @staticmethod
    def GetInboundReceiveLines(warehouseCode, customerNumber, orderType):
        """ GetInboundReceiveLines(warehouseCode: str, customerNumber: str, orderType: InboundOrderTypeEnum) -> InboundReceiveLines """
        pass

    __all__ = [
        'CheckForExistingPreReceipts',
        'CheckForExistingReceipts',
        'GetInboundReceiveLines',
    ]

    Instance = InboundReceiveLineManager()
    """hardcoded/returns an instance of the class"""

class ReceiverFactory:
    """ ReceiverFactory(lines: InboundReceiveLines, dfObject: DataFlowObject[ReceiveArgs]) """
    def CreateReceiver(self):
        """ CreateReceiver(self: ReceiverFactory) -> Receiver """
        pass

    def Dispose(self):
        """ Dispose(self: ReceiverFactory) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, lines, dfObject):
        """ __new__(cls: type, lines: InboundReceiveLines, dfObject: DataFlowObject[ReceiveArgs]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Instance = ReceiverFactory()
    """hardcoded/returns an instance of the class"""

