from Wms.EdiMessaging import MessageBase
# encoding: utf-8
# module Wms.RemotingImplementation.EdiMessaging.Messages calls itself Messages
# from Wms.RemotingImplementation, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DebugMessage(MessageBase):
    """
    DebugMessage()
    DebugMessage(message: IMessage)
    """
    def Callback(self):
        """ Callback(self: DebugMessage) -> HandleResult """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: IMessage)
        """
        pass

    PublicTypeName = 'DebugMessage'

    Instance = DebugMessage()
    """hardcoded/returns an instance of the class"""

class ProcessDirectOrderMessage(MessageBase):
    """
    ProcessDirectOrderMessage()
    ProcessDirectOrderMessage(message: IMessage)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: IMessage)
        """
        pass

    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Data(self: ProcessDirectOrderMessage) -> ProcessDirectOrderMessageData

Set: Data(self: ProcessDirectOrderMessage) = value
"""


    TypeName = 'Direct Order Fulfillment'

    Instance = ProcessDirectOrderMessage()
    """hardcoded/returns an instance of the class"""

class ProcessDirectOrderMessageData():
    """
    ProcessDirectOrderMessageData()
    ProcessDirectOrderMessageData(directOrder: DirectOrder)
    """
    @staticmethod # known case of __new__
    def __new__(self, directOrder=None):
        """
        __new__(cls: type)
        __new__(cls: type, directOrder: DirectOrder)
        """
        pass

    DirectOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DirectOrder(self: ProcessDirectOrderMessageData) -> DirectOrder

Set: DirectOrder(self: ProcessDirectOrderMessageData) = value
"""

    IsFulFilledInBoxWise = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFulFilledInBoxWise(self: ProcessDirectOrderMessageData) -> bool

Set: IsFulFilledInBoxWise(self: ProcessDirectOrderMessageData) = value
"""

    IsLoggedInHistoryTables = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLoggedInHistoryTables(self: ProcessDirectOrderMessageData) -> bool

Set: IsLoggedInHistoryTables(self: ProcessDirectOrderMessageData) = value
"""

    IsProcessedInErp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsProcessedInErp(self: ProcessDirectOrderMessageData) -> bool

Set: IsProcessedInErp(self: ProcessDirectOrderMessageData) = value
"""

    Label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Label(self: ProcessDirectOrderMessageData) -> str

"""


    Instance = ProcessDirectOrderMessageData()
    """hardcoded/returns an instance of the class"""

class ProcessPreReceiptMessage(MessageBase):
    """
    ProcessPreReceiptMessage()
    ProcessPreReceiptMessage(message: IMessage)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: IMessage)
        """
        pass

    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Data(self: ProcessPreReceiptMessage) -> ProcessPreReceiptMessageData

Set: Data(self: ProcessPreReceiptMessage) = value
"""


    TypeName = 'Prereceipt Fulfillment'

    Instance = ProcessPreReceiptMessage()
    """hardcoded/returns an instance of the class"""

class ProcessPreReceiptMessageData():
    """ ProcessPreReceiptMessageData() """
    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ProcessPreReceiptMessageData) -> str

Set: Description(self: ProcessPreReceiptMessageData) = value
"""

    PreReceiptId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreReceiptId(self: ProcessPreReceiptMessageData) -> int

Set: PreReceiptId(self: ProcessPreReceiptMessageData) = value
"""

    TransactionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransactionId(self: ProcessPreReceiptMessageData) -> Guid

Set: TransactionId(self: ProcessPreReceiptMessageData) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: ProcessPreReceiptMessageData) -> str

Set: WarehouseCode(self: ProcessPreReceiptMessageData) = value
"""

    YourReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YourReference(self: ProcessPreReceiptMessageData) -> str

Set: YourReference(self: ProcessPreReceiptMessageData) = value
"""


    Instance = ProcessPreReceiptMessageData()
    """hardcoded/returns an instance of the class"""

class ProcessSalesOrderMessage(MessageBase):
    """
    ProcessSalesOrderMessage()
    ProcessSalesOrderMessage(message: IMessage)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: IMessage)
        """
        pass

    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Data(self: ProcessSalesOrderMessage) -> ProcessSalesOrderMessageData

Set: Data(self: ProcessSalesOrderMessage) = value
"""


    TypeName = 'Sales Order Fulfillment'

    Instance = ProcessSalesOrderMessage()
    """hardcoded/returns an instance of the class"""

class ProcessSalesOrderMessageData():
    """ ProcessSalesOrderMessageData() """
    Arguments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arguments(self: ProcessSalesOrderMessageData) -> ProcessSalesOrderLinesArgs

Set: Arguments(self: ProcessSalesOrderMessageData) = value
"""

    CreatedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatedBy(self: ProcessSalesOrderMessageData) -> Dictionary[str, str]

Set: CreatedBy(self: ProcessSalesOrderMessageData) = value
"""

    Lines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lines(self: ProcessSalesOrderMessageData) -> List[SalesOrderLine]

Set: Lines(self: ProcessSalesOrderMessageData) = value
"""

    Order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Order(self: ProcessSalesOrderMessageData) -> SalesOrder

Set: Order(self: ProcessSalesOrderMessageData) = value
"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: State(self: ProcessSalesOrderMessageData) -> ProcessOutboundOrderMessageState

"""


    Instance = ProcessSalesOrderMessageData()
    """hardcoded/returns an instance of the class"""

class StockOnLocationChangedMessage(MessageBase):
    """ StockOnLocationChangedMessage() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: StockOnLocationChangedMessage) -> Location

Set: Location(self: StockOnLocationChangedMessage) = value
"""


    TypeName = 'Stock changed on location'

    Instance = StockOnLocationChangedMessage()
    """hardcoded/returns an instance of the class"""

# variables with complex values

