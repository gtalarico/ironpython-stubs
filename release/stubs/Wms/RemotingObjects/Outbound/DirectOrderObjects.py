from Wms.RemotingObjects.Caching import *
from Wms.RemotingObjects import *
# encoding: utf-8
# module Wms.RemotingObjects.Outbound.DirectOrderObjects calls itself DirectOrderObjects
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DirectOrder(CacheObject):
    """
    DirectOrder()
    DirectOrder(customer: Customer, warehouseCode: str)
    """
    def AddOrderLine(self, orderLine):
        """ AddOrderLine(self: DirectOrder, orderLine: DirectOrderLine) """
        pass

    def CloneHeaderOnly(self):
        """ CloneHeaderOnly(self: DirectOrder) -> DirectOrder """
        pass

    def EnsureValidLineNumber(self, orderLine):
        """ EnsureValidLineNumber(self: DirectOrder, orderLine: DirectOrderLine) """
        pass

    def IndexOf(self, lineNumber):
        """ IndexOf(self: DirectOrder, lineNumber: int) -> int """
        pass

    def TryGetOrderLineByItemAndLocation(self, itemCode, locationCode, directOrderLineFound):
        """ TryGetOrderLineByItemAndLocation(self: DirectOrder, itemCode: str, locationCode: str) -> (bool, DirectOrderLine) """
        pass

    def TryGetOrderLineByLineNumber(self, lineNumber, directOrderLineFound):
        """ TryGetOrderLineByLineNumber(self: DirectOrder, lineNumber: int) -> (bool, DirectOrderLine) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, customer=None, warehouseCode=None):
        """
        __new__(cls: type)
        __new__(cls: type, customer: Customer, warehouseCode: str)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    AllocationReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllocationReference(self: DirectOrder) -> AllocatedStockItemReference

Set: AllocationReference(self: DirectOrder) = value
"""

    CustomerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomerName(self: DirectOrder) -> str

Set: CustomerName(self: DirectOrder) = value
"""

    CustomerNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomerNumber(self: DirectOrder) -> str

Set: CustomerNumber(self: DirectOrder) = value
"""

    ErpId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErpId(self: DirectOrder) -> str

Set: ErpId(self: DirectOrder) = value
"""

    HasLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasLines(self: DirectOrder) -> bool

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: DirectOrder) -> Guid

Set: Id(self: DirectOrder) = value
"""

    IdAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IdAsString(self: DirectOrder) -> str

"""

    IsProcessed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsProcessed(self: DirectOrder) -> bool

Set: IsProcessed(self: DirectOrder) = value
"""

    LastLineNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastLineNumber(self: DirectOrder) -> int

Set: LastLineNumber(self: DirectOrder) = value
"""

    Lifetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lifetime(self: DirectOrder) -> CacheLifeTimes

"""

    OrderDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderDate(self: DirectOrder) -> DateTime

Set: OrderDate(self: DirectOrder) = value
"""

    OrderLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderLines(self: DirectOrder) -> List[DirectOrderLine]

Set: OrderLines(self: DirectOrder) = value
"""

    PreserveState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreserveState(self: DirectOrder) -> bool

"""

    Reference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reference(self: DirectOrder) -> str

Set: Reference(self: DirectOrder) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: DirectOrder) -> str

Set: WarehouseCode(self: DirectOrder) = value
"""


    DisplayMember = 'CustomerName'
    ValueMember = 'CustomerNumber'

    Instance = DirectOrder()
    """hardcoded/returns an instance of the class"""

class DirectOrderCrudArgs():
    """ DirectOrderCrudArgs(directOrder: DirectOrder) """
    @staticmethod # known case of __new__
    def __new__(self, directOrder):
        """ __new__(cls: type, directOrder: DirectOrder) """
        pass

    DirectOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DirectOrder(self: DirectOrderCrudArgs) -> DirectOrder

Set: DirectOrder(self: DirectOrderCrudArgs) = value
"""


    Instance = DirectOrderCrudArgs()
    """hardcoded/returns an instance of the class"""

class DirectOrderLine():
    """ DirectOrderLine(item: Item, location: Location) """
    def ConvertToOutboundOrderLine(self, parent):
        """ ConvertToOutboundOrderLine(self: DirectOrderLine, parent: DirectOrder) -> OutboundOrderLine """
        pass

    def TryGetItemIdentificationByNumber(self, itemIdentificationNumber, itemIdentification):
        """ TryGetItemIdentificationByNumber(self: DirectOrderLine, itemIdentificationNumber: str) -> (bool, ItemIdentification) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, item, location):
        """ __new__(cls: type, item: Item, location: Location) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    ContainsBatchNumberItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Don't set directly. Setter is for serialization purpose only

Get: ContainsBatchNumberItem(self: DirectOrderLine) -> bool

Set: ContainsBatchNumberItem(self: DirectOrderLine) = value
"""

    ContainsItemIdentificationItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContainsItemIdentificationItem(self: DirectOrderLine) -> bool

"""

    ContainsSerialNumberItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Don't set directly. Setter is for serialization purpose only

Get: ContainsSerialNumberItem(self: DirectOrderLine) -> bool

Set: ContainsSerialNumberItem(self: DirectOrderLine) = value
"""

    CustomErpFields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomErpFields(self: DirectOrderLine) -> SerializableDictionary[str, object]

Set: CustomErpFields(self: DirectOrderLine) = value
"""

    DefaultVendorBarcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultVendorBarcode(self: DirectOrderLine) -> str

Set: DefaultVendorBarcode(self: DirectOrderLine) = value
"""

    HasItemIdentifications = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasItemIdentifications(self: DirectOrderLine) -> bool

"""

    Item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Item(self: DirectOrderLine) -> Item

Set: Item(self: DirectOrderLine) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: DirectOrderLine) -> str

"""

    ItemDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemDescription(self: DirectOrderLine) -> str

"""

    ItemIdentifications = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIdentifications(self: DirectOrderLine) -> ItemIdentifications

Set: ItemIdentifications(self: DirectOrderLine) = value
"""

    LineNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineNumber(self: DirectOrderLine) -> int

Set: LineNumber(self: DirectOrderLine) = value
"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: DirectOrderLine) -> Location

Set: Location(self: DirectOrderLine) = value
"""

    LocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationCode(self: DirectOrderLine) -> str

"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: DirectOrderLine) -> Decimal

Set: Quantity(self: DirectOrderLine) = value
"""


    DisplayMember = 'ItemDescription'
    NoLinenumberValue = -1
    ValueMember = 'ItemCode'

    Instance = DirectOrderLine()
    """hardcoded/returns an instance of the class"""

class DirectOrderLineCrudArgs(DirectOrderCrudArgs):
    """ DirectOrderLineCrudArgs(directOrder: DirectOrder, directOrderLine: DirectOrderLine) """
    @staticmethod # known case of __new__
    def __new__(self, directOrder, directOrderLine):
        """ __new__(cls: type, directOrder: DirectOrder, directOrderLine: DirectOrderLine) """
        pass

    DirectOrderLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DirectOrderLine(self: DirectOrderLineCrudArgs) -> DirectOrderLine

Set: DirectOrderLine(self: DirectOrderLineCrudArgs) = value
"""


    Instance = DirectOrderLineCrudArgs()
    """hardcoded/returns an instance of the class"""

class DirectOrderLineItemIdentificationCrudArgs(DirectOrderLineCrudArgs):
    """ DirectOrderLineItemIdentificationCrudArgs(order: DirectOrder, directOrderLine: DirectOrderLine, itemIdentification: ItemIdentification) """
    @staticmethod # known case of __new__
    def __new__(self, order, directOrderLine, itemIdentification):
        """ __new__(cls: type, order: DirectOrder, directOrderLine: DirectOrderLine, itemIdentification: ItemIdentification) """
        pass

    ItemIdentification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIdentification(self: DirectOrderLineItemIdentificationCrudArgs) -> ItemIdentification

Set: ItemIdentification(self: DirectOrderLineItemIdentificationCrudArgs) = value
"""


    Instance = DirectOrderLineItemIdentificationCrudArgs()
    """hardcoded/returns an instance of the class"""

class DirectOrderLineItemIdentificationsCrudArgs(DirectOrderLineCrudArgs):
    """ DirectOrderLineItemIdentificationsCrudArgs(directOrder: DirectOrder, directOrderLine: DirectOrderLine, itemIdentifications: ItemIdentifications) """
    @staticmethod # known case of __new__
    def __new__(self, directOrder, directOrderLine, itemIdentifications):
        """ __new__(cls: type, directOrder: DirectOrder, directOrderLine: DirectOrderLine, itemIdentifications: ItemIdentifications) """
        pass

    ItemIdentifications = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIdentifications(self: DirectOrderLineItemIdentificationsCrudArgs) -> ItemIdentifications

Set: ItemIdentifications(self: DirectOrderLineItemIdentificationsCrudArgs) = value
"""


    Instance = DirectOrderLineItemIdentificationsCrudArgs()
    """hardcoded/returns an instance of the class"""

class ErpProcessDirecOrderResult():
    """ ErpProcessDirecOrderResult() """
    OrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderNumber(self: ErpProcessDirecOrderResult) -> str

Set: OrderNumber(self: ErpProcessDirecOrderResult) = value
"""

    Success = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Success(self: ErpProcessDirecOrderResult) -> bool

Set: Success(self: ErpProcessDirecOrderResult) = value
"""


    Instance = ErpProcessDirecOrderResult()
    """hardcoded/returns an instance of the class"""

class HistoryDirectOrder():
    """ HistoryDirectOrder() """
    CreatedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatedBy(self: HistoryDirectOrder) -> str

Set: CreatedBy(self: HistoryDirectOrder) = value
"""

    CreatedOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatedOn(self: HistoryDirectOrder) -> DateTime

Set: CreatedOn(self: HistoryDirectOrder) = value
"""

    CustomerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomerName(self: HistoryDirectOrder) -> str

Set: CustomerName(self: HistoryDirectOrder) = value
"""

    CustomerNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomerNumber(self: HistoryDirectOrder) -> str

Set: CustomerNumber(self: HistoryDirectOrder) = value
"""

    DirectOrders_pk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DirectOrders_pk(self: HistoryDirectOrder) -> int

Set: DirectOrders_pk(self: HistoryDirectOrder) = value
"""

    ErpId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErpId(self: HistoryDirectOrder) -> str

Set: ErpId(self: HistoryDirectOrder) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: HistoryDirectOrder) -> str

Set: Id(self: HistoryDirectOrder) = value
"""

    ModifiedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModifiedBy(self: HistoryDirectOrder) -> str

Set: ModifiedBy(self: HistoryDirectOrder) = value
"""

    ModifiedOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModifiedOn(self: HistoryDirectOrder) -> DateTime

Set: ModifiedOn(self: HistoryDirectOrder) = value
"""

    OrderDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderDate(self: HistoryDirectOrder) -> DateTime

Set: OrderDate(self: HistoryDirectOrder) = value
"""

    Reference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reference(self: HistoryDirectOrder) -> str

Set: Reference(self: HistoryDirectOrder) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: HistoryDirectOrder) -> str

Set: WarehouseCode(self: HistoryDirectOrder) = value
"""


    Instance = HistoryDirectOrder()
    """hardcoded/returns an instance of the class"""

class HistoryDirectOrderLine():
    """ HistoryDirectOrderLine() """
    CreatedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatedBy(self: HistoryDirectOrderLine) -> str

Set: CreatedBy(self: HistoryDirectOrderLine) = value
"""

    CreatedOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatedOn(self: HistoryDirectOrderLine) -> DateTime

Set: CreatedOn(self: HistoryDirectOrderLine) = value
"""

    DirectOrderLines_pk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DirectOrderLines_pk(self: HistoryDirectOrderLine) -> int

Set: DirectOrderLines_pk(self: HistoryDirectOrderLine) = value
"""

    DirectOrder_fk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DirectOrder_fk(self: HistoryDirectOrderLine) -> int

Set: DirectOrder_fk(self: HistoryDirectOrderLine) = value
"""

    ErpId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErpId(self: HistoryDirectOrderLine) -> str

Set: ErpId(self: HistoryDirectOrderLine) = value
"""

    IsBatchNumberItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBatchNumberItem(self: HistoryDirectOrderLine) -> bool

Set: IsBatchNumberItem(self: HistoryDirectOrderLine) = value
"""

    IsSerialNumberItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSerialNumberItem(self: HistoryDirectOrderLine) -> bool

Set: IsSerialNumberItem(self: HistoryDirectOrderLine) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: HistoryDirectOrderLine) -> str

Set: ItemCode(self: HistoryDirectOrderLine) = value
"""

    ItemDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemDescription(self: HistoryDirectOrderLine) -> str

Set: ItemDescription(self: HistoryDirectOrderLine) = value
"""

    Linenumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Linenumber(self: HistoryDirectOrderLine) -> int

Set: Linenumber(self: HistoryDirectOrderLine) = value
"""

    ModifiedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModifiedBy(self: HistoryDirectOrderLine) -> str

Set: ModifiedBy(self: HistoryDirectOrderLine) = value
"""

    ModifiedOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModifiedOn(self: HistoryDirectOrderLine) -> DateTime

Set: ModifiedOn(self: HistoryDirectOrderLine) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: HistoryDirectOrderLine) -> Decimal

Set: Quantity(self: HistoryDirectOrderLine) = value
"""

    WarehouseLocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseLocationCode(self: HistoryDirectOrderLine) -> str

Set: WarehouseLocationCode(self: HistoryDirectOrderLine) = value
"""


    Instance = HistoryDirectOrderLine()
    """hardcoded/returns an instance of the class"""

class HistoryDirectOrderLinesFilter():
    """ HistoryDirectOrderLinesFilter() """
    DirectOrderKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DirectOrderKey(self: HistoryDirectOrderLinesFilter) -> int

Set: DirectOrderKey(self: HistoryDirectOrderLinesFilter) = value
"""

    SearchText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SearchText(self: HistoryDirectOrderLinesFilter) -> str

Set: SearchText(self: HistoryDirectOrderLinesFilter) = value
"""


    Instance = HistoryDirectOrderLinesFilter()
    """hardcoded/returns an instance of the class"""

class HistoryDirectOrdersFilter(HistoryFilterBase):
    """ HistoryDirectOrdersFilter() """
    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: HistoryDirectOrdersFilter) -> str

Set: WarehouseCode(self: HistoryDirectOrdersFilter) = value
"""


    Instance = HistoryDirectOrdersFilter()
    """hardcoded/returns an instance of the class"""

