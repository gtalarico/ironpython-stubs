# encoding: utf-8
# module Wms.RemotingObjects.Purchase calls itself Purchase
# from Wms.RemotingObjects, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ErpProcessPurchaseOrderLinesResult:
    """ ErpProcessPurchaseOrderLinesResult() """
    DefaultItemLocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultItemLocations(self: ErpProcessPurchaseOrderLinesResult) -> Dictionary[str, str]

Set: DefaultItemLocations(self: ErpProcessPurchaseOrderLinesResult) = value
"""

    DefaultReceiptLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultReceiptLocation(self: ErpProcessPurchaseOrderLinesResult) -> str

Set: DefaultReceiptLocation(self: ErpProcessPurchaseOrderLinesResult) = value
"""

    EntryNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntryNumber(self: ErpProcessPurchaseOrderLinesResult) -> str

Set: EntryNumber(self: ErpProcessPurchaseOrderLinesResult) = value
"""

    HasDocument = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasDocument(self: ErpProcessPurchaseOrderLinesResult) -> bool

"""

    Reports = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reports(self: ErpProcessPurchaseOrderLinesResult) -> List[Attachment]

Set: Reports(self: ErpProcessPurchaseOrderLinesResult) = value
"""



class ErpProcessReceiptResult:
    """ ErpProcessReceiptResult() """
    CreatedPurchaseOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatedPurchaseOrder(self: ErpProcessReceiptResult) -> PurchaseOrder

Set: CreatedPurchaseOrder(self: ErpProcessReceiptResult) = value
"""

    HasPurchaseOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasPurchaseOrder(self: ErpProcessReceiptResult) -> bool

"""



class GetHistoryPurchaseOrderPrintLinesArgs:
    """
    GetHistoryPurchaseOrderPrintLinesArgs()
    GetHistoryPurchaseOrderPrintLinesArgs(purchaseReceiptGuid: Guid)
    GetHistoryPurchaseOrderPrintLinesArgs(purchaseReceiptGuid: Guid, pagingParams: PagingParams)
    """
    @staticmethod # known case of __new__
    def __new__(self, purchaseReceiptGuid=None, pagingParams=None):
        """
        __new__(cls: type)
        __new__(cls: type, purchaseReceiptGuid: Guid)
        __new__(cls: type, purchaseReceiptGuid: Guid, pagingParams: PagingParams)
        """
        pass

    PagingParams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PagingParams(self: GetHistoryPurchaseOrderPrintLinesArgs) -> PagingParams

Set: PagingParams(self: GetHistoryPurchaseOrderPrintLinesArgs) = value
"""

    PurchaseReceiptGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PurchaseReceiptGuid(self: GetHistoryPurchaseOrderPrintLinesArgs) -> Guid

Set: PurchaseReceiptGuid(self: GetHistoryPurchaseOrderPrintLinesArgs) = value
"""

    SearchText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SearchText(self: GetHistoryPurchaseOrderPrintLinesArgs) -> str

Set: SearchText(self: GetHistoryPurchaseOrderPrintLinesArgs) = value
"""



class GetItemsOfVendorArgs:
    """
    GetItemsOfVendorArgs()
    GetItemsOfVendorArgs(vendorNumber: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, vendorNumber=None):
        """
        __new__(cls: type)
        __new__(cls: type, vendorNumber: str)
        """
        pass

    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filter(self: GetItemsOfVendorArgs) -> str

Set: Filter(self: GetItemsOfVendorArgs) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: GetItemsOfVendorArgs) -> str

Set: ItemCode(self: GetItemsOfVendorArgs) = value
"""

    Paging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Paging(self: GetItemsOfVendorArgs) -> PagingParams

Set: Paging(self: GetItemsOfVendorArgs) = value
"""

    VendorNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VendorNumber(self: GetItemsOfVendorArgs) -> str

Set: VendorNumber(self: GetItemsOfVendorArgs) = value
"""



class GetItemVendorsArgs:
    """
    GetItemVendorsArgs()
    GetItemVendorsArgs(itemCode: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, itemCode=None):
        """
        __new__(cls: type)
        __new__(cls: type, itemCode: str)
        """
        pass

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: GetItemVendorsArgs) -> str

Set: ItemCode(self: GetItemVendorsArgs) = value
"""


    Default = None


class GetPurchaseOrderLinesArgs:
    """
    GetPurchaseOrderLinesArgs()
    GetPurchaseOrderLinesArgs(purchaseOrderIds: IEnumerable[int])
    """
    @staticmethod # known case of __new__
    def __new__(self, purchaseOrderIds=None):
        """
        __new__(cls: type)
        __new__(cls: type, purchaseOrderIds: IEnumerable[int])
        """
        pass

    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filter(self: GetPurchaseOrderLinesArgs) -> str

Set: Filter(self: GetPurchaseOrderLinesArgs) = value
"""


    PurchaseOrderIds = None


class InboundOrderArgsBase:
    """ InboundOrderArgsBase() """
    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filter(self: InboundOrderArgsBase) -> str

Set: Filter(self: InboundOrderArgsBase) = value
"""

    FromDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FromDate(self: InboundOrderArgsBase) -> Nullable[DateTime]

"""

    TimeSpan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimeSpan(self: InboundOrderArgsBase) -> TimeFilterEnum

Set: TimeSpan(self: InboundOrderArgsBase) = value
"""

    ToDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToDate(self: InboundOrderArgsBase) -> DateTime

"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: InboundOrderArgsBase) -> str

Set: WarehouseCode(self: InboundOrderArgsBase) = value
"""



class GetPurchaseOrderVendorArgs:
    """
    GetPurchaseOrderVendorArgs()
    GetPurchaseOrderVendorArgs(warehouseCode: str, filterText: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, warehouseCode=None, filterText=None):
        """
        __new__(cls: type)
        __new__(cls: type, warehouseCode: str, filterText: str)
        """
        pass

    IncludePreReceipts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludePreReceipts(self: GetPurchaseOrderVendorArgs) -> bool

Set: IncludePreReceipts(self: GetPurchaseOrderVendorArgs) = value
"""

    IncludePurchaseOrders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludePurchaseOrders(self: GetPurchaseOrderVendorArgs) -> bool

Set: IncludePurchaseOrders(self: GetPurchaseOrderVendorArgs) = value
"""


    Default = None


class GetVendorsArgs:
    """
    GetVendorsArgs()
    GetVendorsArgs(vendorNumber: str)
    GetVendorsArgs(vendorNumber: str, filterText: str)
    GetVendorsArgs(id: int)
    GetVendorsArgs(id: int, filterText: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, vendorNumber: str)
        __new__(cls: type, vendorNumber: str, filterText: str)
        __new__(cls: type, id: int)
        __new__(cls: type, id: int, filterText: str)
        """
        pass

    FilterText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilterText(self: GetVendorsArgs) -> str

Set: FilterText(self: GetVendorsArgs) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: GetVendorsArgs) -> int

Set: Id(self: GetVendorsArgs) = value
"""

    Paging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Paging(self: GetVendorsArgs) -> PagingParams

Set: Paging(self: GetVendorsArgs) = value
"""

    VendorNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VendorNumber(self: GetVendorsArgs) -> str

Set: VendorNumber(self: GetVendorsArgs) = value
"""


    Default = None


class PurchaseOrder:
    """ PurchaseOrder() """
    @staticmethod
    def CreateDummyFromVendor(orderNumber, warehouseCode, vendor):
        """ CreateDummyFromVendor(orderNumber: str, warehouseCode: str, vendor: Vendor) -> PurchaseOrder """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: PurchaseOrder) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    HasPreReceipt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasPreReceipt(self: PurchaseOrder) -> bool

"""

    PreReceipts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreReceipts(self: PurchaseOrder) -> PreReceiptSummaries

Set: PreReceipts(self: PurchaseOrder) = value
"""

    UniquePreReceiptsAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UniquePreReceiptsAsString(self: PurchaseOrder) -> str

"""

    VendorAddressLine1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VendorAddressLine1(self: PurchaseOrder) -> str

Set: VendorAddressLine1(self: PurchaseOrder) = value
"""

    VendorAddressLine2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VendorAddressLine2(self: PurchaseOrder) -> str

Set: VendorAddressLine2(self: PurchaseOrder) = value
"""

    VendorAddressLine3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VendorAddressLine3(self: PurchaseOrder) -> str

Set: VendorAddressLine3(self: PurchaseOrder) = value
"""

    VendorCity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VendorCity(self: PurchaseOrder) -> str

Set: VendorCity(self: PurchaseOrder) = value
"""

    VendorContact = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VendorContact(self: PurchaseOrder) -> str

Set: VendorContact(self: PurchaseOrder) = value
"""

    VendorContactEmail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VendorContactEmail(self: PurchaseOrder) -> str

Set: VendorContactEmail(self: PurchaseOrder) = value
"""

    VendorCountryCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VendorCountryCode(self: PurchaseOrder) -> str

Set: VendorCountryCode(self: PurchaseOrder) = value
"""

    VendorCountryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VendorCountryName(self: PurchaseOrder) -> str

Set: VendorCountryName(self: PurchaseOrder) = value
"""

    VendorName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VendorName(self: PurchaseOrder) -> str

Set: VendorName(self: PurchaseOrder) = value
"""

    VendorNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VendorNumber(self: PurchaseOrder) -> str

Set: VendorNumber(self: PurchaseOrder) = value
"""

    VendorPhoneNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VendorPhoneNumber(self: PurchaseOrder) -> str

Set: VendorPhoneNumber(self: PurchaseOrder) = value
"""

    VendorState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VendorState(self: PurchaseOrder) -> str

Set: VendorState(self: PurchaseOrder) = value
"""

    VendorZipCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VendorZipCode(self: PurchaseOrder) -> str

Set: VendorZipCode(self: PurchaseOrder) = value
"""



class HistoryPurchaseOrder:
    """ HistoryPurchaseOrder() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    DateReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DateReceived(self: HistoryPurchaseOrder) -> DateTime

"""

    GroupGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupGuid(self: HistoryPurchaseOrder) -> Guid

Set: GroupGuid(self: HistoryPurchaseOrder) = value
"""

    PreReceiptDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreReceiptDescription(self: HistoryPurchaseOrder) -> str

Set: PreReceiptDescription(self: HistoryPurchaseOrder) = value
"""

    PreReceiptId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreReceiptId(self: HistoryPurchaseOrder) -> str

Set: PreReceiptId(self: HistoryPurchaseOrder) = value
"""

    PreReceiptTransactionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreReceiptTransactionId(self: HistoryPurchaseOrder) -> str

Set: PreReceiptTransactionId(self: HistoryPurchaseOrder) = value
"""

    YourReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YourReference(self: HistoryPurchaseOrder) -> str

Set: YourReference(self: HistoryPurchaseOrder) = value
"""



class HistoryPurchaseOrders:
    """ HistoryPurchaseOrders() """
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
    """Get: TotalRowsMatched(self: HistoryPurchaseOrders) -> Int64

Set: TotalRowsMatched(self: HistoryPurchaseOrders) = value
"""



class HistoryPurchaseOrdersFilter:
    """ HistoryPurchaseOrdersFilter() """
    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: HistoryPurchaseOrdersFilter) -> str

Set: WarehouseCode(self: HistoryPurchaseOrdersFilter) = value
"""



class Vendor:
    """ Vendor() """
    def GetHashCode(self):
        """ GetHashCode(self: Vendor) -> int """
        pass

    AddressLine1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AddressLine1(self: Vendor) -> str

Set: AddressLine1(self: Vendor) = value
"""

    AddressLine2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AddressLine2(self: Vendor) -> str

Set: AddressLine2(self: Vendor) = value
"""

    AddressLine3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AddressLine3(self: Vendor) -> str

Set: AddressLine3(self: Vendor) = value
"""

    City = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: City(self: Vendor) -> str

Set: City(self: Vendor) = value
"""

    Contact = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Contact(self: Vendor) -> str

Set: Contact(self: Vendor) = value
"""

    ContactEmail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContactEmail(self: Vendor) -> str

Set: ContactEmail(self: Vendor) = value
"""

    CountryCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CountryCode(self: Vendor) -> str

Set: CountryCode(self: Vendor) = value
"""

    CountryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CountryName(self: Vendor) -> str

Set: CountryName(self: Vendor) = value
"""

    GroupKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupKey(self: Vendor) -> int

Set: GroupKey(self: Vendor) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: Vendor) -> int

Set: Id(self: Vendor) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Vendor) -> str

Set: Name(self: Vendor) = value
"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Number(self: Vendor) -> str

Set: Number(self: Vendor) = value
"""

    PhoneNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhoneNumber(self: Vendor) -> str

Set: PhoneNumber(self: Vendor) = value
"""

    ReceiptType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReceiptType(self: Vendor) -> ReceiptTypeEnum

Set: ReceiptType(self: Vendor) = value
"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: State(self: Vendor) -> str

Set: State(self: Vendor) = value
"""

    UniqueId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UniqueId(self: Vendor) -> str

"""

    ZipCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZipCode(self: Vendor) -> str

Set: ZipCode(self: Vendor) = value
"""



class ItemVendor:
    """ ItemVendor() """
    def GetHashCode(self):
        """ GetHashCode(self: ItemVendor) -> int """
        pass

    Barcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Barcode(self: ItemVendor) -> str

Set: Barcode(self: ItemVendor) = value
"""

    IsMainVendor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMainVendor(self: ItemVendor) -> bool

Set: IsMainVendor(self: ItemVendor) = value
"""

    PurchaseUnitCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PurchaseUnitCode(self: ItemVendor) -> str

Set: PurchaseUnitCode(self: ItemVendor) = value
"""

    SalesUnitFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SalesUnitFactor(self: ItemVendor) -> Decimal

Set: SalesUnitFactor(self: ItemVendor) = value
"""



class ItemVendors:
    """ ItemVendors() """
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


class ProcessPurchaseOrderLinesArgs:
    """ ProcessPurchaseOrderLinesArgs() """
    DefaultInboundLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultInboundLocation(self: ProcessPurchaseOrderLinesArgs) -> str

Set: DefaultInboundLocation(self: ProcessPurchaseOrderLinesArgs) = value
"""

    YourReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YourReference(self: ProcessPurchaseOrderLinesArgs) -> str

Set: YourReference(self: ProcessPurchaseOrderLinesArgs) = value
"""



class ProcessReceiptArgs:
    """ ProcessReceiptArgs() """
    DocumentPrinter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DocumentPrinter(self: ProcessReceiptArgs) -> str

Set: DocumentPrinter(self: ProcessReceiptArgs) = value
"""

    OrderDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderDescription(self: ProcessReceiptArgs) -> str

Set: OrderDescription(self: ProcessReceiptArgs) = value
"""

    VendorNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VendorNumber(self: ProcessReceiptArgs) -> str

Set: VendorNumber(self: ProcessReceiptArgs) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: ProcessReceiptArgs) -> str

Set: WarehouseCode(self: ProcessReceiptArgs) = value
"""

    YourReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YourReference(self: ProcessReceiptArgs) -> str

Set: YourReference(self: ProcessReceiptArgs) = value
"""



class PurchaseOrderArgs:
    """
    PurchaseOrderArgs()
    PurchaseOrderArgs(id: int)
    PurchaseOrderArgs(warehouseCode: str)
    PurchaseOrderArgs(warehouseCode: str, vendorNumber: str)
    PurchaseOrderArgs(warehouseCode: str, vendorNumber: str, groupkey: int)
    PurchaseOrderArgs(warehouseCode: str, vendorNumber: str, searchText: str)
    PurchaseOrderArgs(warehouseCode: str, vendorNumber: str, searchText: str, timeSpan: TimeFilterEnum)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, id: int)
        __new__(cls: type, warehouseCode: str)
        __new__(cls: type, warehouseCode: str, vendorNumber: str)
        __new__(cls: type, warehouseCode: str, vendorNumber: str, groupkey: int)
        __new__(cls: type, warehouseCode: str, vendorNumber: str, searchText: str)
        __new__(cls: type, warehouseCode: str, vendorNumber: str, searchText: str, timeSpan: TimeFilterEnum)
        """
        pass

    Paging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Paging(self: PurchaseOrderArgs) -> PagingParams

Set: Paging(self: PurchaseOrderArgs) = value
"""


    GroupKey = None
    OrderIds = None
    VendorNumber = None


class PurchaseOrderLine:
    """ PurchaseOrderLine() """
    @staticmethod
    def FromItem(item, itemDefaultLocation):
        """ FromItem(item: Item, itemDefaultLocation: str) -> PurchaseOrderLine """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: PurchaseOrderLine) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    CurrentVendorBarcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentVendorBarcode(self: PurchaseOrderLine) -> str

Set: CurrentVendorBarcode(self: PurchaseOrderLine) = value
"""

    CurrentVendorItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentVendorItemCode(self: PurchaseOrderLine) -> str

Set: CurrentVendorItemCode(self: PurchaseOrderLine) = value
"""

    CurrentVendorNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentVendorNumber(self: PurchaseOrderLine) -> str

Set: CurrentVendorNumber(self: PurchaseOrderLine) = value
"""

    DefaultVendorNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultVendorNumber(self: PurchaseOrderLine) -> str

Set: DefaultVendorNumber(self: PurchaseOrderLine) = value
"""

    HasPreReceipt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasPreReceipt(self: PurchaseOrderLine) -> bool

"""

    ItemPurchasePrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemPurchasePrice(self: PurchaseOrderLine) -> Decimal

Set: ItemPurchasePrice(self: PurchaseOrderLine) = value
"""

    PreReceipts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreReceipts(self: PurchaseOrderLine) -> List[PreReceiptSummary]

Set: PreReceipts(self: PurchaseOrderLine) = value
"""

    SalesUnitCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SalesUnitCode(self: PurchaseOrderLine) -> str

Set: SalesUnitCode(self: PurchaseOrderLine) = value
"""

    SalesUnitFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SalesUnitFactor(self: PurchaseOrderLine) -> Decimal

Set: SalesUnitFactor(self: PurchaseOrderLine) = value
"""

    UniquePreReceiptsAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UniquePreReceiptsAsString(self: PurchaseOrderLine) -> List[str]

"""



class PurchaseOrderLines:
    """ PurchaseOrderLines() """
    @staticmethod
    def FromIEnumerable(inboundOrderLines):
        """ FromIEnumerable(inboundOrderLines: IEnumerable[InboundOrderLine]) -> PurchaseOrderLines """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: PurchaseOrderLines) -> int """
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

    IsDisposable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDisposable(self: PurchaseOrderLines) -> bool

"""

    PreserveState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreserveState(self: PurchaseOrderLines) -> bool

"""


    DisplayMember = 'ItemCode'
    ValueMember = 'Id'


class PurchaseOrders:
    """ PurchaseOrders() """
    @staticmethod
    def FromIEnumerable(list):
        """ FromIEnumerable(list: IEnumerable[InboundOrder]) -> PurchaseOrders """
        pass

    def GetCacheKey(self):
        """ GetCacheKey(self: PurchaseOrders) -> int """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: PurchaseOrders) -> int """
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

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalRowsMatched(self: PurchaseOrders) -> Int64

Set: TotalRowsMatched(self: PurchaseOrders) = value
"""


    DisplayMember = 'Number'
    ValueMember = 'Id'


class PurchaseOrderVendor:
    """ PurchaseOrderVendor() """
    Barcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Barcode(self: PurchaseOrderVendor) -> str

Set: Barcode(self: PurchaseOrderVendor) = value
"""

    DateOldestPurchaseOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DateOldestPurchaseOrder(self: PurchaseOrderVendor) -> DateTime

Set: DateOldestPurchaseOrder(self: PurchaseOrderVendor) = value
"""

    NumberOfCollo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfCollo(self: PurchaseOrderVendor) -> int

Set: NumberOfCollo(self: PurchaseOrderVendor) = value
"""

    PendingOrderCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PendingOrderCount(self: PurchaseOrderVendor) -> int

Set: PendingOrderCount(self: PurchaseOrderVendor) = value
"""



class PurchaseOrderVendors:
    """ PurchaseOrderVendors() """
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


class Vendors:
    """ Vendors() """
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


