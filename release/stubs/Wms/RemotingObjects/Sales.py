from Wms.RemotingObjects.Outbound import *
from Wms.RemotingObjects import *
# encoding: utf-8
# module Wms.RemotingObjects.Sales calls itself Sales
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BatchPackProcessingModeEnum:
    """ enum BatchPackProcessingModeEnum, values: Direct (0), Queued (1) """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return BatchPackProcessingModeEnum()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
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

    Direct = None
    Queued = None
    value__ = None


class Customer():
    """
    Represents a single customer. Contains all general information of a customer.
    
    Customer()
    """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return Customer()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    def GetHashCode(self):
        """ GetHashCode(self: Customer) -> int """
        pass

    def ToAddress(self):
        """ ToAddress(self: Customer) -> Address """
        pass

    AddressLine1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Address of the customer, containing the street name and number.

Get: AddressLine1(self: Customer) -> str

Set: AddressLine1(self: Customer) = value
"""

    AddressLine2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Second address of the customer, containing the street name and number.

Get: AddressLine2(self: Customer) -> str

Set: AddressLine2(self: Customer) = value
"""

    AddressLine3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Third address of the customer, containing the street name and number.

Get: AddressLine3(self: Customer) -> str

Set: AddressLine3(self: Customer) = value
"""

    Barcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Barcode(self: Customer) -> str

Set: Barcode(self: Customer) = value
"""

    BatchId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: BatchId(self: Customer) -> str

Set: BatchId(self: Customer) = value
"""

    City = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: City(self: Customer) -> str

Set: City(self: Customer) = value
"""

    Contact = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Contact(self: Customer) -> str

Set: Contact(self: Customer) = value
"""

    ContactEmail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ContactEmail(self: Customer) -> str

Set: ContactEmail(self: Customer) = value
"""

    CountryCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CountryCode(self: Customer) -> str

Set: CountryCode(self: Customer) = value
"""

    CountryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CountryName(self: Customer) -> str

Set: CountryName(self: Customer) = value
"""

    DateOldestSalesOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DateOldestSalesOrder(self: Customer) -> DateTime

Set: DateOldestSalesOrder(self: Customer) = value
"""

    EoriNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: EoriNumber(self: Customer) -> str

Set: EoriNumber(self: Customer) = value
"""

    FullAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: FullAddress(self: Customer) -> str

"""

    GroupKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: GroupKey(self: Customer) -> int

Set: GroupKey(self: Customer) = value
"""

    HasBackOrders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HasBackOrders(self: Customer) -> bool

Set: HasBackOrders(self: Customer) = value
"""

    HasOrdersWithoutPartialDelivery = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HasOrdersWithoutPartialDelivery(self: Customer) -> bool

Set: HasOrdersWithoutPartialDelivery(self: Customer) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Id(self: Customer) -> int

Set: Id(self: Customer) = value
"""

    InBatch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: InBatch(self: Customer) -> str

Set: InBatch(self: Customer) = value
"""

    ItemCountInPendingOrders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemCountInPendingOrders(self: Customer) -> int

"""

    ItemsInPendingOrders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemsInPendingOrders(self: Customer) -> Dictionary[str, Decimal]

Set: ItemsInPendingOrders(self: Customer) = value
"""

    ItemUnitCountInPendingOrders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemUnitCountInPendingOrders(self: Customer) -> Decimal

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Full name of the customer.

Get: Name(self: Customer) -> str

Set: Name(self: Customer) = value
"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Number(self: Customer) -> str

Set: Number(self: Customer) = value
"""

    OrderTags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderTags(self: Customer) -> Tags

Set: OrderTags(self: Customer) = value
"""

    OrderType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderType(self: Customer) -> OutboundOrderTypeEnum

Set: OrderType(self: Customer) = value
"""

    PendingOrderCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PendingOrderCount(self: Customer) -> int

Set: PendingOrderCount(self: Customer) = value
"""

    PhoneNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PhoneNumber(self: Customer) -> str

Set: PhoneNumber(self: Customer) = value
"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: State(self: Customer) -> str

Set: State(self: Customer) = value
"""

    UniqueId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is used for GUI interaction only.

Get: UniqueId(self: Customer) -> str

"""

    ZipCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ZipCode(self: Customer) -> str

Set: ZipCode(self: Customer) = value
"""



class Customers(FindableList):
    """
    Container for the Wms.RemotingObjects.Sales.Customer objects.
    
    Customers()
    """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return Customers()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def FromIEnumerable(list):
        """ FromIEnumerable(list: IEnumerable[Customer]) -> Customers """
        pass

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

    DisplayMember = 'Name'
    ValueMember = 'Number'


class ErpProcessSalesOrderLinesResult():
    """ ErpProcessSalesOrderLinesResult() """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return ErpProcessSalesOrderLinesResult()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    NetInvoiceAmount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: NetInvoiceAmount(self: ErpProcessSalesOrderLinesResult) -> Decimal

Set: NetInvoiceAmount(self: ErpProcessSalesOrderLinesResult) = value
"""

    NetInvoiceAmountCurrencyCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: NetInvoiceAmountCurrencyCode(self: ErpProcessSalesOrderLinesResult) -> str

Set: NetInvoiceAmountCurrencyCode(self: ErpProcessSalesOrderLinesResult) = value
"""

    PackageSlipNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PackageSlipNumber(self: ErpProcessSalesOrderLinesResult) -> str

Set: PackageSlipNumber(self: ErpProcessSalesOrderLinesResult) = value
"""

    Reports = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The reports that are generated while processing the orders

Get: Reports(self: ErpProcessSalesOrderLinesResult) -> List[Attachment]

Set: Reports(self: ErpProcessSalesOrderLinesResult) = value
"""



class GetCustomersArgs():
    """ GetCustomersArgs() """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return GetCustomersArgs()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    CustomerNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerNumber(self: GetCustomersArgs) -> str

Set: CustomerNumber(self: GetCustomersArgs) = value
"""

    FilterText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: FilterText(self: GetCustomersArgs) -> str

Set: FilterText(self: GetCustomersArgs) = value
"""

    Paging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Paging(self: GetCustomersArgs) -> PagingParams

Set: Paging(self: GetCustomersArgs) = value
"""



class GetCustomersPendingArgs():
    """ GetCustomersPendingArgs() """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return GetCustomersPendingArgs()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    IncludeReplenishmentOrders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IncludeReplenishmentOrders(self: GetCustomersPendingArgs) -> bool

Set: IncludeReplenishmentOrders(self: GetCustomersPendingArgs) = value
"""

    IncludeSalesOrders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IncludeSalesOrders(self: GetCustomersPendingArgs) -> bool

Set: IncludeSalesOrders(self: GetCustomersPendingArgs) = value
"""

    SearchTags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SearchTags(self: GetCustomersPendingArgs) -> Tags

Set: SearchTags(self: GetCustomersPendingArgs) = value
"""

    SearchText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SearchText(self: GetCustomersPendingArgs) -> str

Set: SearchText(self: GetCustomersPendingArgs) = value
"""



class GetCustomersWithPendingPackagesArgs():
    """
    Arguments wich are used for retrieving the customers of a sales order.
    
    GetCustomersWithPendingPackagesArgs()
    GetCustomersWithPendingPackagesArgs(batchIds: List[str], filterText: str)
    """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return GetCustomersWithPendingPackagesArgs()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    @staticmethod # known case of __new__
    def __new__(self, batchIds=None, filterText=None):
        """
        __new__(cls: type)
        __new__(cls: type, batchIds: List[str], filterText: str)
        """
        pass

    BatchIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: BatchIds(self: GetCustomersWithPendingPackagesArgs) -> List[str]

Set: BatchIds(self: GetCustomersWithPendingPackagesArgs) = value
"""

    FilterTags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: FilterTags(self: GetCustomersWithPendingPackagesArgs) -> Tags

Set: FilterTags(self: GetCustomersWithPendingPackagesArgs) = value
"""

    FilterText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: FilterText(self: GetCustomersWithPendingPackagesArgs) -> str

Set: FilterText(self: GetCustomersWithPendingPackagesArgs) = value
"""


    Default = None


class GetOutboundOrdersBatchableArgs():
    """ GetOutboundOrdersBatchableArgs() """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return GetOutboundOrdersBatchableArgs()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    DeliveryDateFromTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DeliveryDateFromTo(self: GetOutboundOrdersBatchableArgs) -> Tuple[DateTime, DateTime]

Set: DeliveryDateFromTo(self: GetOutboundOrdersBatchableArgs) = value
"""

    IncludeIncompleteOrdersWithoutPartialDelivery = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IncludeIncompleteOrdersWithoutPartialDelivery(self: GetOutboundOrdersBatchableArgs) -> bool

Set: IncludeIncompleteOrdersWithoutPartialDelivery(self: GetOutboundOrdersBatchableArgs) = value
"""

    OrderDateFromTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderDateFromTo(self: GetOutboundOrdersBatchableArgs) -> Tuple[DateTime, DateTime]

Set: OrderDateFromTo(self: GetOutboundOrdersBatchableArgs) = value
"""

    Paging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Paging(self: GetOutboundOrdersBatchableArgs) -> PagingParams

Set: Paging(self: GetOutboundOrdersBatchableArgs) = value
"""

    SearchTags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SearchTags(self: GetOutboundOrdersBatchableArgs) -> Tags

Set: SearchTags(self: GetOutboundOrdersBatchableArgs) = value
"""

    SearchText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SearchText(self: GetOutboundOrdersBatchableArgs) -> str

Set: SearchText(self: GetOutboundOrdersBatchableArgs) = value
"""

    TypeOfOrders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: TypeOfOrders(self: GetOutboundOrdersBatchableArgs) -> TagTarget

Set: TypeOfOrders(self: GetOutboundOrdersBatchableArgs) = value
"""



class GetSalesOrderCustomersArgs():
    """
    Arguments wich are used for retrieving the customers of a sales order.
    
    GetSalesOrderCustomersArgs()
    GetSalesOrderCustomersArgs(warehouseCode: str, filterText: str)
    """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return GetSalesOrderCustomersArgs()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    @staticmethod # known case of __new__
    def __new__(self, warehouseCode=None, filterText=None):
        """
        __new__(cls: type)
        __new__(cls: type, warehouseCode: str, filterText: str)
        """
        pass

    DaysToFuture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DaysToFuture(self: GetSalesOrderCustomersArgs) -> int

Set: DaysToFuture(self: GetSalesOrderCustomersArgs) = value
"""

    FilterText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: FilterText(self: GetSalesOrderCustomersArgs) -> str

Set: FilterText(self: GetSalesOrderCustomersArgs) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: WarehouseCode(self: GetSalesOrderCustomersArgs) -> str

Set: WarehouseCode(self: GetSalesOrderCustomersArgs) = value
"""


    Default = None


class HistorySalesOrder(HistoryOutboundOrder):
    """ HistorySalesOrder() """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return HistorySalesOrder()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    def Clone(self):
        """ Clone(self: HistorySalesOrder) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    BusinessUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: BusinessUnit(self: HistorySalesOrder) -> str

Set: BusinessUnit(self: HistorySalesOrder) = value
"""

    QuantityLeftToReturn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: QuantityLeftToReturn(self: HistorySalesOrder) -> Decimal

Set: QuantityLeftToReturn(self: HistorySalesOrder) = value
"""

    QuantityReturned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: QuantityReturned(self: HistorySalesOrder) -> Decimal

Set: QuantityReturned(self: HistorySalesOrder) = value
"""

    SalesRepresentative = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SalesRepresentative(self: HistorySalesOrder) -> str

Set: SalesRepresentative(self: HistorySalesOrder) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Type(self: HistorySalesOrder) -> OutboundOrderTypeEnum

"""



class HistorySalesOrders(HistoryOutboundOrders):
    """
    Container for the Wms.RemotingObjects.Outbound.HistoryOutboundOrder objects.
    
    HistorySalesOrders()
    """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return HistorySalesOrders()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def FromIEnumerable(list):
        """ FromIEnumerable(list: IEnumerable[HistorySalesOrder]) -> HistorySalesOrders """
        pass

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


class PackCustomer(Customer):
    """
    PackCustomer()
    PackCustomer(customer: Customer, deliveryMethod: str)
    """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return PackCustomer()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    def Clone(self):
        """ Clone(self: PackCustomer) -> object """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: PackCustomer) -> int """
        pass

    def ToAddress(self):
        """ ToAddress(self: PackCustomer) -> Address """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, customer=None, deliveryMethod=None):
        """
        __new__(cls: type)
        __new__(cls: type, customer: Customer, deliveryMethod: str)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    AreOutboundOrdersProcessed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if all orders are processed, otherwise false.

Get: AreOutboundOrdersProcessed(self: PackCustomer) -> bool

Set: AreOutboundOrdersProcessed(self: PackCustomer) = value
"""

    ColliLetterCachedImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ColliLetterCachedImage(self: PackCustomer) -> Image

"""

    ColliLetterImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ColliLetterImage(self: PackCustomer) -> Array[Byte]

Set: ColliLetterImage(self: PackCustomer) = value
"""

    ColliLetters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ColliLetters(self: PackCustomer) -> List[str]

Set: ColliLetters(self: PackCustomer) = value
"""

    DeliveryMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DeliveryMethod(self: PackCustomer) -> str

Set: DeliveryMethod(self: PackCustomer) = value
"""

    HasDeliveredItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HasDeliveredItems(self: PackCustomer) -> bool

Set: HasDeliveredItems(self: PackCustomer) = value
"""

    OrderTags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderTags(self: PackCustomer) -> Tags

Set: OrderTags(self: PackCustomer) = value
"""

    OutboundOrders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OutboundOrders(self: PackCustomer) -> OutboundOrders

Set: OutboundOrders(self: PackCustomer) = value
"""

    OutboundOrdersProcessed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OutboundOrdersProcessed(self: PackCustomer) -> OutboundOrders

Set: OutboundOrdersProcessed(self: PackCustomer) = value
"""



class PackCustomers(FindableList):
    """
    Container for the Wms.RemotingObjects.Sales.PackCustomer objects.
    
    PackCustomers()
    """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return PackCustomers()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    def Add(self, *__args):
        """ Add(self: PackCustomers, customer: PackCustomer) -> FindableList[PackCustomer] """
        pass

    def AddRange(self, *__args):
        """ AddRange(self: PackCustomers, customers: IEnumerable[PackCustomer]) -> FindableList[PackCustomer] """
        pass

    def Clone(self):
        """ Clone(self: PackCustomers) -> object """
        pass

    @staticmethod
    def FromIEnumerable(list):
        """ FromIEnumerable(list: IEnumerable[PackCustomer]) -> PackCustomers """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

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

    DisplayMember = 'Name'
    ValueMember = 'Number'


class PartialDeliveryTypeEnum:
    """ enum PartialDeliveryTypeEnum, values: Allow (0), OnlyEntireLines (2), OnlyEntireOrder (1) """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return PartialDeliveryTypeEnum()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
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

    Allow = None
    OnlyEntireLines = None
    OnlyEntireOrder = None
    value__ = None


class ReplenishmentOrderArgs():
    """
    ReplenishmentOrderArgs()
    ReplenishmentOrderArgs(warehouseToCode: str)
    ReplenishmentOrderArgs(orderFilterType: ReplenishmentOrderArgsOrderFilterType)
    ReplenishmentOrderArgs(approvedOnly: bool)
    ReplenishmentOrderArgs(warehouseToCode: str, locationToCode: str)
    ReplenishmentOrderArgs(id: int, warehouseToCode: str, locationToCode: str, searchText: str)
    """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return ReplenishmentOrderArgs()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, warehouseToCode: str)
        __new__(cls: type, orderFilterType: ReplenishmentOrderArgsOrderFilterType)
        __new__(cls: type, approvedOnly: bool)
        __new__(cls: type, warehouseToCode: str, locationToCode: str)
        __new__(cls: type, id: int, warehouseToCode: str, locationToCode: str, searchText: str)
        """
        pass

    ApprovedOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ApprovedOnly(self: ReplenishmentOrderArgs) -> bool

Set: ApprovedOnly(self: ReplenishmentOrderArgs) = value
"""

    CustomerNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerNumber(self: ReplenishmentOrderArgs) -> str

Set: CustomerNumber(self: ReplenishmentOrderArgs) = value
"""

    Ids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Ids(self: ReplenishmentOrderArgs) -> List[int]

Set: Ids(self: ReplenishmentOrderArgs) = value
"""

    LocationToCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: LocationToCode(self: ReplenishmentOrderArgs) -> str

Set: LocationToCode(self: ReplenishmentOrderArgs) = value
"""

    OrderNumbers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderNumbers(self: ReplenishmentOrderArgs) -> List[str]

Set: OrderNumbers(self: ReplenishmentOrderArgs) = value
"""

    Paging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Paging(self: ReplenishmentOrderArgs) -> PagingParams

Set: Paging(self: ReplenishmentOrderArgs) = value
"""

    SearchText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SearchText(self: ReplenishmentOrderArgs) -> str

Set: SearchText(self: ReplenishmentOrderArgs) = value
"""

    WarehouseToCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: WarehouseToCode(self: ReplenishmentOrderArgs) -> str

Set: WarehouseToCode(self: ReplenishmentOrderArgs) = value
"""


    DaysToFuture = None
    Default = None
    Id = None
    OrderFilterType = None
    ReplenishmentOrderArgsOrderFilterType = None


class ReplenishmentOrderLinesArgs():
    """
    ReplenishmentOrderLinesArgs()
    ReplenishmentOrderLinesArgs(orderIds: List[int])
    ReplenishmentOrderLinesArgs(orderNumbers: List[str])
    ReplenishmentOrderLinesArgs(orderIds: List[int], daysToFuture: int)
    """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return ReplenishmentOrderLinesArgs()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, orderIds: List[int])
        __new__(cls: type, orderNumbers: List[str])
        __new__(cls: type, orderIds: List[int], daysToFuture: int)
        """
        pass

    Approved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Approved(self: ReplenishmentOrderLinesArgs) -> Nullable[bool]

Set: Approved(self: ReplenishmentOrderLinesArgs) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemCode(self: ReplenishmentOrderLinesArgs) -> str

Set: ItemCode(self: ReplenishmentOrderLinesArgs) = value
"""

    OrderIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderIds(self: ReplenishmentOrderLinesArgs) -> List[int]

Set: OrderIds(self: ReplenishmentOrderLinesArgs) = value
"""

    OrderNumbers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderNumbers(self: ReplenishmentOrderLinesArgs) -> List[str]

Set: OrderNumbers(self: ReplenishmentOrderLinesArgs) = value
"""

    Paging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Paging(self: ReplenishmentOrderLinesArgs) -> PagingParams

Set: Paging(self: ReplenishmentOrderLinesArgs) = value
"""

    SearchText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SearchText(self: ReplenishmentOrderLinesArgs) -> str

Set: SearchText(self: ReplenishmentOrderLinesArgs) = value
"""


    DaysToFuture = None
    Default = None


class SalesOrder(OutboundOrder):
    """
    Represents a single sales order. Contains all general information of a sales order.
                
                It doesn't contain the order lines! Those are gathered by using the Wms.RemotingObjects.Sales.SalesOrderLines and Wms.RemotingObjects.Sales.SalesOrderLine
                objects.
    
    SalesOrder()
    """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return SalesOrder()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    def Clone(self):
        """ Clone(self: SalesOrder) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    BusinessUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: BusinessUnit(self: SalesOrder) -> str

Set: BusinessUnit(self: SalesOrder) = value
"""

    SalesRepresentative = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SalesRepresentative(self: SalesOrder) -> str

Set: SalesRepresentative(self: SalesOrder) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Type(self: SalesOrder) -> OutboundOrderTypeEnum

"""



class SalesOrderArgs():
    """
    SalesOrderArgs()
    SalesOrderArgs(warehouseCode: str)
    SalesOrderArgs(orderFilterType: SalesOrderOrderFilterType)
    SalesOrderArgs(warehouseCode: str, customerNumber: str)
    SalesOrderArgs(orderNumber: str, warehouseCode: str, customerNumber: str, searchText: str)
    """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return SalesOrderArgs()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, warehouseCode: str)
        __new__(cls: type, orderFilterType: SalesOrderOrderFilterType)
        __new__(cls: type, warehouseCode: str, customerNumber: str)
        __new__(cls: type, orderNumber: str, warehouseCode: str, customerNumber: str, searchText: str)
        """
        pass

    BatchId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: BatchId(self: SalesOrderArgs) -> str

Set: BatchId(self: SalesOrderArgs) = value
"""

    CustomerNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerNumber(self: SalesOrderArgs) -> str

Set: CustomerNumber(self: SalesOrderArgs) = value
"""

    DaysToFuture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DaysToFuture(self: SalesOrderArgs) -> int

Set: DaysToFuture(self: SalesOrderArgs) = value
"""

    OnlyBatchableOrders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the orderlines should be retrieved too. Doing so will result in a quick
            stock check to determine if the items can be delivered.

Get: OnlyBatchableOrders(self: SalesOrderArgs) -> bool

Set: OnlyBatchableOrders(self: SalesOrderArgs) = value
"""

    OnlyBatchedOrders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return only orders

Get: OnlyBatchedOrders(self: SalesOrderArgs) -> bool

Set: OnlyBatchedOrders(self: SalesOrderArgs) = value
"""

    OrderFilterType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderFilterType(self: SalesOrderArgs) -> SalesOrderOrderFilterType

Set: OrderFilterType(self: SalesOrderArgs) = value
"""

    OrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderNumber(self: SalesOrderArgs) -> str

Set: OrderNumber(self: SalesOrderArgs) = value
"""

    OrderNumbers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderNumbers(self: SalesOrderArgs) -> List[str]

Set: OrderNumbers(self: SalesOrderArgs) = value
"""

    SearchText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SearchText(self: SalesOrderArgs) -> str

Set: SearchText(self: SalesOrderArgs) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: WarehouseCode(self: SalesOrderArgs) -> str

Set: WarehouseCode(self: SalesOrderArgs) = value
"""


    Default = None
    SalesOrderOrderFilterType = None


class SalesOrderLine(OutboundOrderLine):
    """
    Represents a single order line of a sales order.
    
    SalesOrderLine()
    """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return SalesOrderLine()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    def GetHashCode(self):
        """ GetHashCode(self: SalesOrderLine) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    CustomerItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerItemCode(self: SalesOrderLine) -> str

Set: CustomerItemCode(self: SalesOrderLine) = value
"""

    IsCostItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsCostItem(self: SalesOrderLine) -> bool

Set: IsCostItem(self: SalesOrderLine) = value
"""

    IsExtraItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsExtraItem(self: SalesOrderLine) -> bool

Set: IsExtraItem(self: SalesOrderLine) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Type(self: SalesOrderLine) -> OutboundOrderTypeEnum

"""



class SalesOrderLines(OutboundOrderLines):
    """
    Container for the Wms.RemotingObjects.Sales.SalesOrderLine objects.
    
    SalesOrderLines()
    """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return SalesOrderLines()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def FromIEnumerable(list):
        """ FromIEnumerable(list: IEnumerable[SalesOrderLine]) -> SalesOrderLines """
        pass

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


class SalesOrderLinesArgs():
    """
    SalesOrderLinesArgs()
    SalesOrderLinesArgs(orderNumbers: List[str])
    SalesOrderLinesArgs(orderNumbers: List[str], daysToFuture: int)
    """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return SalesOrderLinesArgs()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    @staticmethod # known case of __new__
    def __new__(self, orderNumbers=None, daysToFuture=None):
        """
        __new__(cls: type)
        __new__(cls: type, orderNumbers: List[str])
        __new__(cls: type, orderNumbers: List[str], daysToFuture: int)
        """
        pass

    DaysToFuture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DaysToFuture(self: SalesOrderLinesArgs) -> int

Set: DaysToFuture(self: SalesOrderLinesArgs) = value
"""

    OrderNumbers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderNumbers(self: SalesOrderLinesArgs) -> List[str]

Set: OrderNumbers(self: SalesOrderLinesArgs) = value
"""

    SearchText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SearchText(self: SalesOrderLinesArgs) -> str

Set: SearchText(self: SalesOrderLinesArgs) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: WarehouseCode(self: SalesOrderLinesArgs) -> str

Set: WarehouseCode(self: SalesOrderLinesArgs) = value
"""


    Default = None


class SalesOrders(OutboundOrders):
    """
    Container for the Wms.RemotingObjects.Sales.SalesOrder objects.
    
    SalesOrders()
    """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return SalesOrders()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def FromIEnumerable(list):
        """ FromIEnumerable(list: IEnumerable[OutboundOrder]) -> SalesOrders """
        pass

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


class SplitProcessedOutboundOrdersEnum:
    """ enum SplitProcessedOutboundOrdersEnum, values: IntoFirstColli (2), None (0), PerOutboundOrder (1) """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return SplitProcessedOutboundOrdersEnum()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
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

    IntoFirstColli = None
    None_ =None
    PerOutboundOrder = None
    value__ = None


class StockRegistrationForColliEnum:
    """ enum StockRegistrationForColliEnum, values: Counts (2), Disabled (0), PackageSlip (1) """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return StockRegistrationForColliEnum()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
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

    Counts = None
    Disabled = None
    PackageSlip = None
    value__ = None


