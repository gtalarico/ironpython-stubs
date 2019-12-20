from System import Object
from Wms.RemotingObjects import DbObject
from System.Collections.Generic import List
from Wms.RemotingObjects import FindableList
# encoding: utf-8
# module Wms.RemotingObjects.Outbound calls itself Outbound
# from Wms.RemotingObjects, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AllocationProfile():
    """ AllocationProfile() """
    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Description(self: AllocationProfile) -> str

Set: Description(self: AllocationProfile) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Id(self: AllocationProfile) -> int

Set: Id(self: AllocationProfile) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: AllocationProfile) -> str

Set: Name(self: AllocationProfile) = value
"""


    Instance = AllocationProfile()
    """hardcoded/returns an instance of the class"""

class AllocationProfiles(List):
    """ AllocationProfiles() """
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
    ValueMember = 'Id'

    Instance = AllocationProfiles()
    """hardcoded/returns an instance of the class"""

class GetHistoryOutboundOrderCustomersArgs():
    """ GetHistoryOutboundOrderCustomersArgs() """
    CustomerNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerNumber(self: GetHistoryOutboundOrderCustomersArgs) -> str

Set: CustomerNumber(self: GetHistoryOutboundOrderCustomersArgs) = value
"""

    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Filter(self: GetHistoryOutboundOrderCustomersArgs) -> str

Set: Filter(self: GetHistoryOutboundOrderCustomersArgs) = value
"""

    Paging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Paging(self: GetHistoryOutboundOrderCustomersArgs) -> PagingParams

Set: Paging(self: GetHistoryOutboundOrderCustomersArgs) = value
"""

    Warehouse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Warehouse(self: GetHistoryOutboundOrderCustomersArgs) -> str

Set: Warehouse(self: GetHistoryOutboundOrderCustomersArgs) = value
"""


    Instance = GetHistoryOutboundOrderCustomersArgs()
    """hardcoded/returns an instance of the class"""

class GetHistoryOutboundOrderItemArgs():
    """ GetHistoryOutboundOrderItemArgs() """
    CustomerNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerNumber(self: GetHistoryOutboundOrderItemArgs) -> str

Set: CustomerNumber(self: GetHistoryOutboundOrderItemArgs) = value
"""

    DeliveryDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DeliveryDate(self: GetHistoryOutboundOrderItemArgs) -> Nullable[DateTime]

Set: DeliveryDate(self: GetHistoryOutboundOrderItemArgs) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemCode(self: GetHistoryOutboundOrderItemArgs) -> str

Set: ItemCode(self: GetHistoryOutboundOrderItemArgs) = value
"""

    OrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderNumber(self: GetHistoryOutboundOrderItemArgs) -> str

Set: OrderNumber(self: GetHistoryOutboundOrderItemArgs) = value
"""

    Paging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Paging(self: GetHistoryOutboundOrderItemArgs) -> PagingParams

Set: Paging(self: GetHistoryOutboundOrderItemArgs) = value
"""

    SearchText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SearchText(self: GetHistoryOutboundOrderItemArgs) -> str

Set: SearchText(self: GetHistoryOutboundOrderItemArgs) = value
"""


    Instance = GetHistoryOutboundOrderItemArgs()
    """hardcoded/returns an instance of the class"""

class GetHistoryOutboundOrdersArgs():
    """ GetHistoryOutboundOrdersArgs() """
    CacheKeyOfReceipt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CacheKeyOfReceipt(self: GetHistoryOutboundOrdersArgs) -> CacheKey

Set: CacheKeyOfReceipt(self: GetHistoryOutboundOrdersArgs) = value
"""

    CustomerNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerNumber(self: GetHistoryOutboundOrdersArgs) -> str

Set: CustomerNumber(self: GetHistoryOutboundOrdersArgs) = value
"""

    DecreaseQuantitiesWithActieveAdhocRma = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DecreaseQuantitiesWithActieveAdhocRma(self: GetHistoryOutboundOrdersArgs) -> bool

Set: DecreaseQuantitiesWithActieveAdhocRma(self: GetHistoryOutboundOrdersArgs) = value
"""

    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Filter(self: GetHistoryOutboundOrdersArgs) -> str

Set: Filter(self: GetHistoryOutboundOrdersArgs) = value
"""

    IncludeOrdersThatCanBeReturned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IncludeOrdersThatCanBeReturned(self: GetHistoryOutboundOrdersArgs) -> bool

Set: IncludeOrdersThatCanBeReturned(self: GetHistoryOutboundOrdersArgs) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemCode(self: GetHistoryOutboundOrdersArgs) -> str

Set: ItemCode(self: GetHistoryOutboundOrdersArgs) = value
"""

    OrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderNumber(self: GetHistoryOutboundOrdersArgs) -> str

Set: OrderNumber(self: GetHistoryOutboundOrdersArgs) = value
"""

    Paging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Paging(self: GetHistoryOutboundOrdersArgs) -> PagingParams

Set: Paging(self: GetHistoryOutboundOrdersArgs) = value
"""


    Instance = GetHistoryOutboundOrdersArgs()
    """hardcoded/returns an instance of the class"""

class GetOutboundOrdersArgs():
    """ GetOutboundOrdersArgs() """
    OrderNumbers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderNumbers(self: GetOutboundOrdersArgs) -> List[str]

Set: OrderNumbers(self: GetOutboundOrdersArgs) = value
"""

    SearchText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SearchText(self: GetOutboundOrdersArgs) -> str

Set: SearchText(self: GetOutboundOrdersArgs) = value
"""


    Instance = GetOutboundOrdersArgs()
    """hardcoded/returns an instance of the class"""

class HistoryOutboundOrder(DbObject):
    """  """
    def Clone(self):
        """ Clone(self: HistoryOutboundOrder) -> object """
        pass

    def Equals(self, obj):
        """ Equals(self: HistoryOutboundOrder, obj: object) -> bool """
        pass

    def GetHashCode(self, orderNumber=None, dateOfDelivery=None):
        """
        GetHashCode(self: HistoryOutboundOrder) -> int
        GetHashCode(orderNumber: str, dateOfDelivery: DateTime) -> int
        """
        pass

    def GetHashCodeOfCustomer(self):
        """ GetHashCodeOfCustomer(self: HistoryOutboundOrder) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    AllowPartialDelivery = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: AllowPartialDelivery(self: HistoryOutboundOrder) -> PartialDeliveryTypeEnum

Set: AllowPartialDelivery(self: HistoryOutboundOrder) = value
"""

    AllowPartialDeliveryAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: AllowPartialDeliveryAsString(self: HistoryOutboundOrder) -> str

"""

    Backorder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Backorder(self: HistoryOutboundOrder) -> bool

Set: Backorder(self: HistoryOutboundOrder) = value
"""

    CustomerAddressLine1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerAddressLine1(self: HistoryOutboundOrder) -> str

Set: CustomerAddressLine1(self: HistoryOutboundOrder) = value
"""

    CustomerAddressLine2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerAddressLine2(self: HistoryOutboundOrder) -> str

Set: CustomerAddressLine2(self: HistoryOutboundOrder) = value
"""

    CustomerAddressLine3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerAddressLine3(self: HistoryOutboundOrder) -> str

Set: CustomerAddressLine3(self: HistoryOutboundOrder) = value
"""

    CustomerCity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerCity(self: HistoryOutboundOrder) -> str

Set: CustomerCity(self: HistoryOutboundOrder) = value
"""

    CustomerContact = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerContact(self: HistoryOutboundOrder) -> str

Set: CustomerContact(self: HistoryOutboundOrder) = value
"""

    CustomerContactEmail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerContactEmail(self: HistoryOutboundOrder) -> str

Set: CustomerContactEmail(self: HistoryOutboundOrder) = value
"""

    CustomerCountryCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerCountryCode(self: HistoryOutboundOrder) -> str

Set: CustomerCountryCode(self: HistoryOutboundOrder) = value
"""

    CustomerCountryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerCountryName(self: HistoryOutboundOrder) -> str

Set: CustomerCountryName(self: HistoryOutboundOrder) = value
"""

    CustomerEoriNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerEoriNumber(self: HistoryOutboundOrder) -> str

Set: CustomerEoriNumber(self: HistoryOutboundOrder) = value
"""

    CustomerInvoiceAddressLine1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceAddressLine1(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceAddressLine1(self: HistoryOutboundOrder) = value
"""

    CustomerInvoiceAddressLine2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceAddressLine2(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceAddressLine2(self: HistoryOutboundOrder) = value
"""

    CustomerInvoiceAddressLine3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceAddressLine3(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceAddressLine3(self: HistoryOutboundOrder) = value
"""

    CustomerInvoiceCity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceCity(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceCity(self: HistoryOutboundOrder) = value
"""

    CustomerInvoiceContact = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceContact(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceContact(self: HistoryOutboundOrder) = value
"""

    CustomerInvoiceContactEmail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceContactEmail(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceContactEmail(self: HistoryOutboundOrder) = value
"""

    CustomerInvoiceCountryCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceCountryCode(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceCountryCode(self: HistoryOutboundOrder) = value
"""

    CustomerInvoiceCountryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceCountryName(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceCountryName(self: HistoryOutboundOrder) = value
"""

    CustomerInvoiceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceName(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceName(self: HistoryOutboundOrder) = value
"""

    CustomerInvoiceNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceNumber(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceNumber(self: HistoryOutboundOrder) = value
"""

    CustomerInvoicePhoneNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoicePhoneNumber(self: HistoryOutboundOrder) -> str

Set: CustomerInvoicePhoneNumber(self: HistoryOutboundOrder) = value
"""

    CustomerInvoiceState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceState(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceState(self: HistoryOutboundOrder) = value
"""

    CustomerInvoiceZipCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceZipCode(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceZipCode(self: HistoryOutboundOrder) = value
"""

    CustomerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerName(self: HistoryOutboundOrder) -> str

Set: CustomerName(self: HistoryOutboundOrder) = value
"""

    CustomerNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerNumber(self: HistoryOutboundOrder) -> str

Set: CustomerNumber(self: HistoryOutboundOrder) = value
"""

    CustomerPackageSlipLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerPackageSlipLayout(self: HistoryOutboundOrder) -> str

Set: CustomerPackageSlipLayout(self: HistoryOutboundOrder) = value
"""

    CustomerPhoneNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerPhoneNumber(self: HistoryOutboundOrder) -> str

Set: CustomerPhoneNumber(self: HistoryOutboundOrder) = value
"""

    CustomerReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerReference(self: HistoryOutboundOrder) -> str

Set: CustomerReference(self: HistoryOutboundOrder) = value
"""

    CustomerState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerState(self: HistoryOutboundOrder) -> str

Set: CustomerState(self: HistoryOutboundOrder) = value
"""

    CustomerZipCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerZipCode(self: HistoryOutboundOrder) -> str

Set: CustomerZipCode(self: HistoryOutboundOrder) = value
"""

    DateOfDelivery = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DateOfDelivery(self: HistoryOutboundOrder) -> DateTime

Set: DateOfDelivery(self: HistoryOutboundOrder) = value
"""

    DateOrdered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DateOrdered(self: HistoryOutboundOrder) -> DateTime

Set: DateOrdered(self: HistoryOutboundOrder) = value
"""

    DbKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DbKey(self: HistoryOutboundOrder) -> int

Set: DbKey(self: HistoryOutboundOrder) = value
"""

    DeliveryMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DeliveryMethod(self: HistoryOutboundOrder) -> str

Set: DeliveryMethod(self: HistoryOutboundOrder) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Description(self: HistoryOutboundOrder) -> str

Set: Description(self: HistoryOutboundOrder) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Id(self: HistoryOutboundOrder) -> int

"""

    Notes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Notes(self: HistoryOutboundOrder) -> str

Set: Notes(self: HistoryOutboundOrder) = value
"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Number(self: HistoryOutboundOrder) -> str

Set: Number(self: HistoryOutboundOrder) = value
"""

    NumberOfItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: NumberOfItems(self: HistoryOutboundOrder) -> int

Set: NumberOfItems(self: HistoryOutboundOrder) = value
"""

    OrderAmountDelivered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderAmountDelivered(self: HistoryOutboundOrder) -> Decimal

Set: OrderAmountDelivered(self: HistoryOutboundOrder) = value
"""

    OrderAmountTotal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderAmountTotal(self: HistoryOutboundOrder) -> Decimal

Set: OrderAmountTotal(self: HistoryOutboundOrder) = value
"""

    ProjectCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ProjectCode(self: HistoryOutboundOrder) -> str

Set: ProjectCode(self: HistoryOutboundOrder) = value
"""

    ProjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ProjectName(self: HistoryOutboundOrder) -> str

Set: ProjectName(self: HistoryOutboundOrder) = value
"""

    QuantityDelivered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: QuantityDelivered(self: HistoryOutboundOrder) -> Decimal

Set: QuantityDelivered(self: HistoryOutboundOrder) = value
"""

    QuantityOrdered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: QuantityOrdered(self: HistoryOutboundOrder) -> Decimal

Set: QuantityOrdered(self: HistoryOutboundOrder) = value
"""

    RoutingCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: RoutingCode(self: HistoryOutboundOrder) -> str

Set: RoutingCode(self: HistoryOutboundOrder) = value
"""

    SelectionCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SelectionCode(self: HistoryOutboundOrder) -> str

Set: SelectionCode(self: HistoryOutboundOrder) = value
"""

    SelectionCodeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SelectionCodeDescription(self: HistoryOutboundOrder) -> str

Set: SelectionCodeDescription(self: HistoryOutboundOrder) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Type(self: HistoryOutboundOrder) -> OutboundOrderTypeEnum

"""

    Warehouse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Warehouse(self: HistoryOutboundOrder) -> str

Set: Warehouse(self: HistoryOutboundOrder) = value
"""


    Instance = HistoryOutboundOrder()
    """hardcoded/returns an instance of the class"""

class OutboundOrderLine(DbObject):
    """  """
    def Clone(self):
        """ Clone(self: OutboundOrderLine) -> object """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: OutboundOrderLine) -> int """
        pass

    def IsBatchNumberItemCheck(self, checkRegistration):
        """
        IsBatchNumberItemCheck(self: OutboundOrderLine, checkRegistration: bool) -> bool
        
            Checks if the item is a batchnumber item.
        
            checkRegistration: True if the batchnumber registration should be checked, false if just the 
             property should be returned.
        
            Returns: True if the check is ignored and the item is a batch item, or when the itemid 
             registration is set to
                    complete (means the numers are registered 
             throughout the whole process).
                    False if the check is ignored and 
             the item is not a batch item, or when the itemids are registered
                    
             during delivery only.
        """
        pass

    def IsSerialNumberItemCheck(self, checkRegistration):
        """
        IsSerialNumberItemCheck(self: OutboundOrderLine, checkRegistration: bool) -> bool
        
            Checks if the item is a serialnumber item.
        
            checkRegistration: True if the serialnumber registration should be checked, false if just the 
             property should be returned.
        
            Returns: True if the check is ignored and the item is a serial item, or when the itemid 
             registration is set to
                    complete (means the numers are registered 
             throughout the whole process).
                    False if the check is ignored and 
             the item is not a serial item, or when the itemids are registered
                    
             during delivery only.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    BatchId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: BatchId(self: OutboundOrderLine) -> Guid

Set: BatchId(self: OutboundOrderLine) = value
"""

    CustomerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerName(self: OutboundOrderLine) -> str

Set: CustomerName(self: OutboundOrderLine) = value
"""

    CustomFields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomFields(self: OutboundOrderLine) -> SerializableDictionary[str, object]

Set: CustomFields(self: OutboundOrderLine) = value
"""

    DateOfDelivery = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DateOfDelivery(self: OutboundOrderLine) -> DateTime

Set: DateOfDelivery(self: OutboundOrderLine) = value
"""

    DefaultVendorBarcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DefaultVendorBarcode(self: OutboundOrderLine) -> str

Set: DefaultVendorBarcode(self: OutboundOrderLine) = value
"""

    DefaultVendorItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DefaultVendorItemCode(self: OutboundOrderLine) -> str

Set: DefaultVendorItemCode(self: OutboundOrderLine) = value
"""

    GTINCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The GS1 GTIN code of this item

Get: GTINCode(self: OutboundOrderLine) -> str

Set: GTINCode(self: OutboundOrderLine) = value
"""

    HistoryId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HistoryId(self: OutboundOrderLine) -> int

Set: HistoryId(self: OutboundOrderLine) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Id(self: OutboundOrderLine) -> int

Set: Id(self: OutboundOrderLine) = value
"""

    IsBatchNumberItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsBatchNumberItem(self: OutboundOrderLine) -> bool

Set: IsBatchNumberItem(self: OutboundOrderLine) = value
"""

    IsFractionAllowed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsFractionAllowed(self: OutboundOrderLine) -> bool

Set: IsFractionAllowed(self: OutboundOrderLine) = value
"""

    IsSerialNumberItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsSerialNumberItem(self: OutboundOrderLine) -> bool

Set: IsSerialNumberItem(self: OutboundOrderLine) = value
"""

    ItemBrand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Necessary for Userinterface BOXwise Mobile

Get: ItemBrand(self: OutboundOrderLine) -> str

Set: ItemBrand(self: OutboundOrderLine) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Necessary for Userinterface BOXwise Mobile

Get: ItemCode(self: OutboundOrderLine) -> str

Set: ItemCode(self: OutboundOrderLine) = value
"""

    ItemDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Necessary for Userinterface BOXwise Mobile

Get: ItemDescription(self: OutboundOrderLine) -> str

Set: ItemDescription(self: OutboundOrderLine) = value
"""

    ItemDimensions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemDimensions(self: OutboundOrderLine) -> Dimensions

Set: ItemDimensions(self: OutboundOrderLine) = value
"""

    ItemIdentifierAssigned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemIdentifierAssigned(self: OutboundOrderLine) -> bool

Set: ItemIdentifierAssigned(self: OutboundOrderLine) = value
"""

    ItemIdRegistration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemIdRegistration(self: OutboundOrderLine) -> ItemIdentificationRegistration

Set: ItemIdRegistration(self: OutboundOrderLine) = value
"""

    ItemLongDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemLongDescription(self: OutboundOrderLine) -> str

Set: ItemLongDescription(self: OutboundOrderLine) = value
"""

    ItemPackLocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemPackLocations(self: OutboundOrderLine) -> ItemPackLocations

Set: ItemPackLocations(self: OutboundOrderLine) = value
"""

    ItemPickLocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemPickLocations(self: OutboundOrderLine) -> ItemPickLocations

Set: ItemPickLocations(self: OutboundOrderLine) = value
"""

    ItemPurchasePrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemPurchasePrice(self: OutboundOrderLine) -> Decimal

Set: ItemPurchasePrice(self: OutboundOrderLine) = value
"""

    ItemSalesPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemSalesPrice(self: OutboundOrderLine) -> Decimal

Set: ItemSalesPrice(self: OutboundOrderLine) = value
"""

    ItemSalesPriceSingleWithVat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemSalesPriceSingleWithVat(self: OutboundOrderLine) -> Decimal

Set: ItemSalesPriceSingleWithVat(self: OutboundOrderLine) = value
"""

    ItemSalesPriceSumPickable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemSalesPriceSumPickable(self: OutboundOrderLine) -> Decimal

"""

    ItemSalesPriceSumToDeliver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemSalesPriceSumToDeliver(self: OutboundOrderLine) -> Decimal

"""

    ItemWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemWeight(self: OutboundOrderLine) -> Decimal

Set: ItemWeight(self: OutboundOrderLine) = value
"""

    LineCurrencyCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: LineCurrencyCode(self: OutboundOrderLine) -> str

Set: LineCurrencyCode(self: OutboundOrderLine) = value
"""

    LineDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: LineDescription(self: OutboundOrderLine) -> str

Set: LineDescription(self: OutboundOrderLine) = value
"""

    LineInstruction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Necessary for Userinterface BOXwise Mobile

Get: LineInstruction(self: OutboundOrderLine) -> str

Set: LineInstruction(self: OutboundOrderLine) = value
"""

    LineItemIdentifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: LineItemIdentifier(self: OutboundOrderLine) -> str

Set: LineItemIdentifier(self: OutboundOrderLine) = value
"""

    LineNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: LineNumber(self: OutboundOrderLine) -> int

Set: LineNumber(self: OutboundOrderLine) = value
"""

    OrderId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderId(self: OutboundOrderLine) -> int

Set: OrderId(self: OutboundOrderLine) = value
"""

    OrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Necessary for Userinterface BOXwise Mobile

Get: OrderNumber(self: OutboundOrderLine) -> str

Set: OrderNumber(self: OutboundOrderLine) = value
"""

    PercentageItemSalesPriceSumPickable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PercentageItemSalesPriceSumPickable(self: OutboundOrderLine) -> int

"""

    QuantityAllocated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: QuantityAllocated(self: OutboundOrderLine) -> Decimal

"""

    QuantityLocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Quantity locked by external ERP program. 
            This quantity is not included in stock allocation but shown in %Batchable and CheckPartialDelivery
            
            * assigned to purchase order from Profit (wmspro-3531). 
            * Potential order waiting as an Afas option added here too.
            
            These amounts are not in Wms.RemotingObjects.Outbound.OutboundOrderLine.QuantityToDeliver but are actually part of the order
            and thus the order cannot be Completely Delivered.

Get: QuantityLocked(self: OutboundOrderLine) -> Decimal

Set: QuantityLocked(self: OutboundOrderLine) = value
"""

    QuantityOrdered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Necessary for Userinterface BOXwise Mobile

Get: QuantityOrdered(self: OutboundOrderLine) -> Decimal

Set: QuantityOrdered(self: OutboundOrderLine) = value
"""

    QuantityPackable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: QuantityPackable(self: OutboundOrderLine) -> Decimal

"""

    QuantityPacked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: QuantityPacked(self: OutboundOrderLine) -> Decimal

"""

    QuantityPickable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The quantity that is pickable. This is calculated when the batchable salesorders are retrieved.
            After that the line will be batched and the property QuantityAllocated can be used.

Get: QuantityPickable(self: OutboundOrderLine) -> Decimal

Set: QuantityPickable(self: OutboundOrderLine) = value
"""

    QuantityPicked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The quantity left to be picked.

Get: QuantityPicked(self: OutboundOrderLine) -> Decimal

"""

    QuantityProcessed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: QuantityProcessed(self: OutboundOrderLine) -> Decimal

"""

    QuantityToDeliver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Necessary for Userinterface BOXwise Mobile

Get: QuantityToDeliver(self: OutboundOrderLine) -> Decimal

Set: QuantityToDeliver(self: OutboundOrderLine) = value
"""

    QuantityToDeliverOriginal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is used by picking process to be able to revert a pick to original state.

Get: QuantityToDeliverOriginal(self: OutboundOrderLine) -> Decimal

Set: QuantityToDeliverOriginal(self: OutboundOrderLine) = value
"""

    RequestedDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: RequestedDate(self: OutboundOrderLine) -> DateTime

Set: RequestedDate(self: OutboundOrderLine) = value
"""

    ShowInBatch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ShowInBatch(self: OutboundOrderLine) -> bool

Set: ShowInBatch(self: OutboundOrderLine) = value
"""

    StockAssigned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: StockAssigned(self: OutboundOrderLine) -> bool

Set: StockAssigned(self: OutboundOrderLine) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Type(self: OutboundOrderLine) -> OutboundOrderTypeEnum

"""

    UnitCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: UnitCode(self: OutboundOrderLine) -> str

Set: UnitCode(self: OutboundOrderLine) = value
"""

    VatCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: VatCode(self: OutboundOrderLine) -> str

Set: VatCode(self: OutboundOrderLine) = value
"""

    Warehouse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Warehouse(self: OutboundOrderLine) -> str

Set: Warehouse(self: OutboundOrderLine) = value
"""

    WarehouseLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: WarehouseLocation(self: OutboundOrderLine) -> str

Set: WarehouseLocation(self: OutboundOrderLine) = value
"""


    Instance = OutboundOrderLine()
    """hardcoded/returns an instance of the class"""

class HistoryOutboundOrderLine(OutboundOrderLine):
    """ HistoryOutboundOrderLine() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    OrderId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderId(self: HistoryOutboundOrderLine) -> int

Set: OrderId(self: HistoryOutboundOrderLine) = value
"""

    QuantityDelivered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: QuantityDelivered(self: HistoryOutboundOrderLine) -> Decimal

Set: QuantityDelivered(self: HistoryOutboundOrderLine) = value
"""

    ShipmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ShipmentId(self: HistoryOutboundOrderLine) -> int

Set: ShipmentId(self: HistoryOutboundOrderLine) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Type(self: HistoryOutboundOrderLine) -> OutboundOrderTypeEnum

"""


    Instance = HistoryOutboundOrderLine()
    """hardcoded/returns an instance of the class"""

class OutboundOrderLines(FindableList):
    """ OutboundOrderLines() """
    def Clone(self):
        """ Clone(self: OutboundOrderLines) -> object """
        pass

    @staticmethod
    def FromIEnumerable(list):
        """ FromIEnumerable(list: IEnumerable[OutboundOrderLine]) -> OutboundOrderLines """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: OutboundOrderLines) -> int """
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
    """

Get: IsDisposable(self: OutboundOrderLines) -> bool

"""

    PreserveState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PreserveState(self: OutboundOrderLines) -> bool

"""


    DisplayMember = 'ItemCode'
    ValueMember = 'Id'

    Instance = OutboundOrderLines()
    """hardcoded/returns an instance of the class"""

class HistoryOutboundOrderLines(OutboundOrderLines):
    """ HistoryOutboundOrderLines() """
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

    DisplayMember = 'ItemCode'
    ValueMember = 'Id'

    Instance = HistoryOutboundOrderLines()
    """hardcoded/returns an instance of the class"""

class HistoryOutboundOrders(FindableList):
    """ HistoryOutboundOrders() """
    def Add(self, *__args):
        """
        Add(self: HistoryOutboundOrders, order: HistoryOutboundOrder) -> FindableList[HistoryOutboundOrder]
        Add(self: HistoryOutboundOrders, order: HistoryOutboundOrder, predicate: Predicate[HistoryOutboundOrder])
        """
        pass

    def Clone(self):
        """ Clone(self: HistoryOutboundOrders) -> object """
        pass

    @staticmethod
    def FromIEnumerable(list):
        """ FromIEnumerable(list: IEnumerable[HistoryOutboundOrder]) -> HistoryOutboundOrders """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: HistoryOutboundOrders) -> int """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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
    """

Get: TotalRowsMatched(self: HistoryOutboundOrders) -> Int64

Set: TotalRowsMatched(self: HistoryOutboundOrders) = value
"""


    DisplayMember = 'Number'
    ValueMember = 'DbKey'

    Instance = HistoryOutboundOrders()
    """hardcoded/returns an instance of the class"""

class OutboundOrder(DbObject):
    """  """
    def Clone(self):
        """ Clone(self: OutboundOrder) -> object """
        pass

    def Equals(self, obj):
        """ Equals(self: OutboundOrder, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: OutboundOrder) -> int """
        pass

    def GetHashCodeOfCustomer(self):
        """ GetHashCodeOfCustomer(self: OutboundOrder) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    AllowPartialDelivery = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: AllowPartialDelivery(self: OutboundOrder) -> PartialDeliveryTypeEnum

Set: AllowPartialDelivery(self: OutboundOrder) = value
"""

    AllowPartialDeliveryAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: AllowPartialDeliveryAsString(self: OutboundOrder) -> str

"""

    Backorder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Backorder(self: OutboundOrder) -> bool

Set: Backorder(self: OutboundOrder) = value
"""

    CustomerAddressLine1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerAddressLine1(self: OutboundOrder) -> str

Set: CustomerAddressLine1(self: OutboundOrder) = value
"""

    CustomerAddressLine2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerAddressLine2(self: OutboundOrder) -> str

Set: CustomerAddressLine2(self: OutboundOrder) = value
"""

    CustomerAddressLine3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerAddressLine3(self: OutboundOrder) -> str

Set: CustomerAddressLine3(self: OutboundOrder) = value
"""

    CustomerCity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Necessary for Userinterface BOXwise Mobile

Get: CustomerCity(self: OutboundOrder) -> str

Set: CustomerCity(self: OutboundOrder) = value
"""

    CustomerContact = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerContact(self: OutboundOrder) -> str

Set: CustomerContact(self: OutboundOrder) = value
"""

    CustomerContactEmail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerContactEmail(self: OutboundOrder) -> str

Set: CustomerContactEmail(self: OutboundOrder) = value
"""

    CustomerCountryCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Necessary for Userinterface BOXwise Mobile

Get: CustomerCountryCode(self: OutboundOrder) -> str

Set: CustomerCountryCode(self: OutboundOrder) = value
"""

    CustomerCountryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerCountryName(self: OutboundOrder) -> str

Set: CustomerCountryName(self: OutboundOrder) = value
"""

    CustomerEoriNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerEoriNumber(self: OutboundOrder) -> str

Set: CustomerEoriNumber(self: OutboundOrder) = value
"""

    CustomerInvoiceAddressLine1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceAddressLine1(self: OutboundOrder) -> str

Set: CustomerInvoiceAddressLine1(self: OutboundOrder) = value
"""

    CustomerInvoiceAddressLine2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceAddressLine2(self: OutboundOrder) -> str

Set: CustomerInvoiceAddressLine2(self: OutboundOrder) = value
"""

    CustomerInvoiceAddressLine3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceAddressLine3(self: OutboundOrder) -> str

Set: CustomerInvoiceAddressLine3(self: OutboundOrder) = value
"""

    CustomerInvoiceCity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceCity(self: OutboundOrder) -> str

Set: CustomerInvoiceCity(self: OutboundOrder) = value
"""

    CustomerInvoiceContact = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceContact(self: OutboundOrder) -> str

Set: CustomerInvoiceContact(self: OutboundOrder) = value
"""

    CustomerInvoiceContactEmail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceContactEmail(self: OutboundOrder) -> str

Set: CustomerInvoiceContactEmail(self: OutboundOrder) = value
"""

    CustomerInvoiceCountryCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceCountryCode(self: OutboundOrder) -> str

Set: CustomerInvoiceCountryCode(self: OutboundOrder) = value
"""

    CustomerInvoiceCountryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceCountryName(self: OutboundOrder) -> str

Set: CustomerInvoiceCountryName(self: OutboundOrder) = value
"""

    CustomerInvoiceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceName(self: OutboundOrder) -> str

Set: CustomerInvoiceName(self: OutboundOrder) = value
"""

    CustomerInvoiceNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceNumber(self: OutboundOrder) -> str

Set: CustomerInvoiceNumber(self: OutboundOrder) = value
"""

    CustomerInvoicePhoneNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoicePhoneNumber(self: OutboundOrder) -> str

Set: CustomerInvoicePhoneNumber(self: OutboundOrder) = value
"""

    CustomerInvoiceState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceState(self: OutboundOrder) -> str

Set: CustomerInvoiceState(self: OutboundOrder) = value
"""

    CustomerInvoiceZipCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceZipCode(self: OutboundOrder) -> str

Set: CustomerInvoiceZipCode(self: OutboundOrder) = value
"""

    CustomerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Necessary for Userinterface BOXwise Mobile

Get: CustomerName(self: OutboundOrder) -> str

Set: CustomerName(self: OutboundOrder) = value
"""

    CustomerNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerNumber(self: OutboundOrder) -> str

Set: CustomerNumber(self: OutboundOrder) = value
"""

    CustomerPackageSlipLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerPackageSlipLayout(self: OutboundOrder) -> str

Set: CustomerPackageSlipLayout(self: OutboundOrder) = value
"""

    CustomerPhoneNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerPhoneNumber(self: OutboundOrder) -> str

Set: CustomerPhoneNumber(self: OutboundOrder) = value
"""

    CustomerReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerReference(self: OutboundOrder) -> str

Set: CustomerReference(self: OutboundOrder) = value
"""

    CustomerState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerState(self: OutboundOrder) -> str

Set: CustomerState(self: OutboundOrder) = value
"""

    CustomerZipCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerZipCode(self: OutboundOrder) -> str

Set: CustomerZipCode(self: OutboundOrder) = value
"""

    CustomFields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomFields(self: OutboundOrder) -> SerializableDictionary[str, object]

Set: CustomFields(self: OutboundOrder) = value
"""

    DateOfDelivery = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DateOfDelivery(self: OutboundOrder) -> DateTime

Set: DateOfDelivery(self: OutboundOrder) = value
"""

    DateOrdered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DateOrdered(self: OutboundOrder) -> DateTime

Set: DateOrdered(self: OutboundOrder) = value
"""

    DeliverableOrderlines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DeliverableOrderlines(self: OutboundOrder) -> int

Set: DeliverableOrderlines(self: OutboundOrder) = value
"""

    DeliveryMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Necessary for Userinterface BOXwise Mobile

Get: DeliveryMethod(self: OutboundOrder) -> str

Set: DeliveryMethod(self: OutboundOrder) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Description(self: OutboundOrder) -> str

Set: Description(self: OutboundOrder) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Necessary for Userinterface BOXwise Mobile

Get: Id(self: OutboundOrder) -> int

Set: Id(self: OutboundOrder) = value
"""

    LineBackColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: LineBackColor(self: OutboundOrder) -> str

Set: LineBackColor(self: OutboundOrder) = value
"""

    LineForeColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: LineForeColor(self: OutboundOrder) -> str

Set: LineForeColor(self: OutboundOrder) = value
"""

    Notes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Notes(self: OutboundOrder) -> str

Set: Notes(self: OutboundOrder) = value
"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Necessary for Userinterface BOXwise Mobile

Get: Number(self: OutboundOrder) -> str

Set: Number(self: OutboundOrder) = value
"""

    OrderAmountDeliverable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderAmountDeliverable(self: OutboundOrder) -> Decimal

Set: OrderAmountDeliverable(self: OutboundOrder) = value
"""

    OrderAmountTotal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderAmountTotal(self: OutboundOrder) -> Decimal

Set: OrderAmountTotal(self: OutboundOrder) = value
"""

    PendingItemCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PendingItemCount(self: OutboundOrder) -> int

"""

    PendingItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PendingItems(self: OutboundOrder) -> Dictionary[str, Decimal]

Set: PendingItems(self: OutboundOrder) = value
"""

    PendingItemUnitCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PendingItemUnitCount(self: OutboundOrder) -> Decimal

"""

    PendingOrderLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PendingOrderLines(self: OutboundOrder) -> int

Set: PendingOrderLines(self: OutboundOrder) = value
"""

    PercentageDeliverableAmount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PercentageDeliverableAmount(self: OutboundOrder) -> int

Set: PercentageDeliverableAmount(self: OutboundOrder) = value
"""

    PercentageDeliverableLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PercentageDeliverableLines(self: OutboundOrder) -> int

Set: PercentageDeliverableLines(self: OutboundOrder) = value
"""

    PercentDeliverable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Percentage of the QuantityToDeliver that is deliverable

Get: PercentDeliverable(self: OutboundOrder) -> int

Set: PercentDeliverable(self: OutboundOrder) = value
"""

    ProjectCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ProjectCode(self: OutboundOrder) -> str

Set: ProjectCode(self: OutboundOrder) = value
"""

    ProjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ProjectName(self: OutboundOrder) -> str

Set: ProjectName(self: OutboundOrder) = value
"""

    RoutingCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: RoutingCode(self: OutboundOrder) -> str

Set: RoutingCode(self: OutboundOrder) = value
"""

    SelectionCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SelectionCode(self: OutboundOrder) -> str

Set: SelectionCode(self: OutboundOrder) = value
"""

    SelectionCodeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SelectionCodeDescription(self: OutboundOrder) -> str

Set: SelectionCodeDescription(self: OutboundOrder) = value
"""

    Tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Tag(self: OutboundOrder) -> Tag

Set: Tag(self: OutboundOrder) = value
"""

    TotalOrderlines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: TotalOrderlines(self: OutboundOrder) -> int

Set: TotalOrderlines(self: OutboundOrder) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Type(self: OutboundOrder) -> OutboundOrderTypeEnum

"""

    Warehouse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Necessary for Userinterface BOXwise Mobile

Get: Warehouse(self: OutboundOrder) -> str

Set: Warehouse(self: OutboundOrder) = value
"""


    Instance = OutboundOrder()
    """hardcoded/returns an instance of the class"""

class OutboundOrderLineEqualityComparer(Object):
    """ OutboundOrderLineEqualityComparer() """
    def Equals(self, *__args):
        """ Equals(self: OutboundOrderLineEqualityComparer, x: OutboundOrderLine, y: OutboundOrderLine) -> bool """
        pass

    def GetHashCode(self, obj=None):
        """ GetHashCode(self: OutboundOrderLineEqualityComparer, obj: OutboundOrderLine) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Instance = OutboundOrderLineEqualityComparer()
    """hardcoded/returns an instance of the class"""

class OutboundOrders(FindableList):
    """
    OutboundOrders()
    OutboundOrders(Capacity: int)
    """
    def Add(self, *__args):
        """
        Add(self: OutboundOrders, order: OutboundOrder) -> FindableList[OutboundOrder]
        Add(self: OutboundOrders, order: OutboundOrder, predicate: Predicate[OutboundOrder])
        """
        pass

    def Clone(self):
        """ Clone(self: OutboundOrders) -> object """
        pass

    @staticmethod
    def FromIEnumerable(list):
        """ FromIEnumerable(list: IEnumerable[OutboundOrder]) -> OutboundOrders """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: OutboundOrders) -> int """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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

    @staticmethod # known case of __new__
    def __new__(self, Capacity=None):
        """
        __new__(cls: type)
        __new__(cls: type, Capacity: int)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalRowsMatched(self: OutboundOrders) -> Int64

Set: TotalRowsMatched(self: OutboundOrders) = value
"""


    DisplayMember = 'Number'
    ValueMember = 'Id'

    Instance = OutboundOrders()
    """hardcoded/returns an instance of the class"""

class OutboundOrderTypeEnum(Object):
    """ enum OutboundOrderTypeEnum, values: ReplenishmentOrder (2), RtvOrder (3), SalesOrder (1) """
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

    ReplenishmentOrder = None
    RtvOrder = None
    SalesOrder = None
    value__ = None

    Instance = OutboundOrderTypeEnum()
    """hardcoded/returns an instance of the class"""

class PickDifferenceOptionsEnum(Object):
    """ enum PickDifferenceOptionsEnum, values: BasedOnMarkAsPicked (1), BasedOnNonePickedItems (2), None (0) """
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

    BasedOnMarkAsPicked = None
    BasedOnNonePickedItems = None
    None_ =None
    value__ = None

    Instance = PickDifferenceOptionsEnum()
    """hardcoded/returns an instance of the class"""

class ValidateItemIdentificationArgs():
    """
    ValidateItemIdentificationArgs()
    ValidateItemIdentificationArgs(itemCode: str, number: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, itemCode=None, number=None):
        """
        __new__(cls: type)
        __new__(cls: type, itemCode: str, number: str)
        """
        pass

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: ValidateItemIdentificationArgs) -> str

Set: ItemCode(self: ValidateItemIdentificationArgs) = value
"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Number(self: ValidateItemIdentificationArgs) -> str

Set: Number(self: ValidateItemIdentificationArgs) = value
"""


    Instance = ValidateItemIdentificationArgs()
    """hardcoded/returns an instance of the class"""

# variables with complex values

