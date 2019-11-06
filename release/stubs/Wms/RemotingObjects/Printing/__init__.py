from System.Collections.Generic import List
from Wms.RemotingObjects import DbObject
from Wms.RemotingObjects import FindableList
from System import Object
# encoding: utf-8
# module Wms.RemotingObjects.Printing calls itself Printing
# from Wms.RemotingObjects, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class PrintLineBase():
    """  """
    def Equals(self, obj):
        """ Equals(self: PrintLineBase, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PrintLineBase) -> int
        
            Best practice to override as well if Equals is overridden
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    GroupKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: GroupKey(self: PrintLineBase) -> str

"""

    NumberOfCopies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: NumberOfCopies(self: PrintLineBase) -> Decimal

Set: NumberOfCopies(self: PrintLineBase) = value
"""

    PrintLineItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PrintLineItems(self: PrintLineBase) -> PrintLinesBase

Set: PrintLineItems(self: PrintLineBase) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Quantity(self: PrintLineBase) -> Decimal

Set: Quantity(self: PrintLineBase) = value
"""


    Instance = PrintLineBase()
    """hardcoded/returns an instance of the class"""

class BarcodePrintLine(PrintLineBase):
    """ BarcodePrintLine(barcode: str) """
    def GetHashCode(self):
        """ GetHashCode(self: BarcodePrintLine) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, barcode):
        """ __new__(cls: type, barcode: str) """
        pass

    Barcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Barcode(self: BarcodePrintLine) -> str

Set: Barcode(self: BarcodePrintLine) = value
"""

    GroupKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: GroupKey(self: BarcodePrintLine) -> str

"""


    Instance = BarcodePrintLine()
    """hardcoded/returns an instance of the class"""

class PrintLinesBase(FindableList):
    """  """
    def AddRange(self, collection):
        """ AddRange(self: PrintLinesBase, collection: IEnumerable[PrintLineBase]) -> List[PrintLineBase] """
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

    UniqueId = 'GroupKey'

    Instance = PrintLinesBase()
    """hardcoded/returns an instance of the class"""

class BarcodePrintLines(PrintLinesBase):
    """
    BarcodePrintLines()
    BarcodePrintLines(collection: IEnumerable[BarcodePrintLine])
    """
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
    def __new__(self, collection=None):
        """
        __new__(cls: type)
        __new__(cls: type, collection: IEnumerable[BarcodePrintLine])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    IsDisposable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsDisposable(self: BarcodePrintLines) -> bool

"""

    PreserveState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PreserveState(self: BarcodePrintLines) -> bool

"""

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """when paging is used this property holds the total number of rows 
            which are returned by the query

Get: TotalRowsMatched(self: BarcodePrintLines) -> Int64

Set: TotalRowsMatched(self: BarcodePrintLines) = value
"""


    DisplayMember = None
    ValueMember = None

    Instance = BarcodePrintLines()
    """hardcoded/returns an instance of the class"""

class InboundOrderPrintLine(PrintLineBase):
    """ InboundOrderPrintLine() """
    def GetHashCode(self):
        """ GetHashCode(self: InboundOrderPrintLine) -> int """
        pass

    Barcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """DEFAULT supplier barcode

Get: Barcode(self: InboundOrderPrintLine) -> str

Set: Barcode(self: InboundOrderPrintLine) = value
"""

    EndDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndDate(self: InboundOrderPrintLine) -> DateTime

"""

    GroupKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: GroupKey(self: InboundOrderPrintLine) -> str

"""

    GTINCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The GS1 GTIN code of this item

Get: GTINCode(self: InboundOrderPrintLine) -> str

Set: GTINCode(self: InboundOrderPrintLine) = value
"""

    IsBatchItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsBatchItem(self: InboundOrderPrintLine) -> bool

Set: IsBatchItem(self: InboundOrderPrintLine) = value
"""

    IsSerialItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsSerialItem(self: InboundOrderPrintLine) -> bool

Set: IsSerialItem(self: InboundOrderPrintLine) = value
"""

    ItemBrand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemBrand(self: InboundOrderPrintLine) -> str

Set: ItemBrand(self: InboundOrderPrintLine) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemCode(self: InboundOrderPrintLine) -> str

Set: ItemCode(self: InboundOrderPrintLine) = value
"""

    ItemDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemDescription(self: InboundOrderPrintLine) -> str

Set: ItemDescription(self: InboundOrderPrintLine) = value
"""

    ItemIdentification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Pure for displaying in PrintLines form.

Get: ItemIdentification(self: InboundOrderPrintLine) -> str

"""

    ItemIdentifications = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemIdentifications(self: InboundOrderPrintLine) -> List[ItemIdentification]

Set: ItemIdentifications(self: InboundOrderPrintLine) = value
"""

    OrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderNumber(self: InboundOrderPrintLine) -> str

Set: OrderNumber(self: InboundOrderPrintLine) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Quantity(self: InboundOrderPrintLine) -> Decimal

Set: Quantity(self: InboundOrderPrintLine) = value
"""

    SupplierCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """DEFAULT supplier code.

Get: SupplierCode(self: InboundOrderPrintLine) -> str

Set: SupplierCode(self: InboundOrderPrintLine) = value
"""


    Instance = InboundOrderPrintLine()
    """hardcoded/returns an instance of the class"""

class ItemPrintLine(PrintLineBase):
    """ ItemPrintLine() """
    @staticmethod
    def Create(item):
        """ Create(item: Item) -> ItemPrintLine """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ItemPrintLine) -> int """
        pass

    Barcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Barcode(self: ItemPrintLine) -> str

Set: Barcode(self: ItemPrintLine) = value
"""

    DefaultSalesPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DefaultSalesPrice(self: ItemPrintLine) -> Decimal

Set: DefaultSalesPrice(self: ItemPrintLine) = value
"""

    DefaultVendorName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DefaultVendorName(self: ItemPrintLine) -> str

Set: DefaultVendorName(self: ItemPrintLine) = value
"""

    DefaultVendorNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DefaultVendorNumber(self: ItemPrintLine) -> str

Set: DefaultVendorNumber(self: ItemPrintLine) = value
"""

    GroupKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: GroupKey(self: ItemPrintLine) -> str

"""

    GTINCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The GS1 GTIN code of this item

Get: GTINCode(self: ItemPrintLine) -> str

Set: GTINCode(self: ItemPrintLine) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemCode(self: ItemPrintLine) -> str

Set: ItemCode(self: ItemPrintLine) = value
"""

    ItemDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemDescription(self: ItemPrintLine) -> str

Set: ItemDescription(self: ItemPrintLine) = value
"""

    ItemGroupCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemGroupCode(self: ItemPrintLine) -> str

Set: ItemGroupCode(self: ItemPrintLine) = value
"""

    ItemGroupDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemGroupDescription(self: ItemPrintLine) -> str

Set: ItemGroupDescription(self: ItemPrintLine) = value
"""

    SupplierCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SupplierCode(self: ItemPrintLine) -> str

Set: SupplierCode(self: ItemPrintLine) = value
"""

    UnitCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: UnitCode(self: ItemPrintLine) -> str

Set: UnitCode(self: ItemPrintLine) = value
"""


    Instance = ItemPrintLine()
    """hardcoded/returns an instance of the class"""

class ItemPrintLines(PrintLinesBase):
    """
    ItemPrintLines()
    ItemPrintLines(collection: IEnumerable[ItemPrintLine])
    """
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
    def __new__(self, collection=None):
        """
        __new__(cls: type)
        __new__(cls: type, collection: IEnumerable[ItemPrintLine])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    IsDisposable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsDisposable(self: ItemPrintLines) -> bool

"""

    PreserveState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PreserveState(self: ItemPrintLines) -> bool

"""

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """when paging is used this property holds the total number of rows 
            which are returned by the query

Get: TotalRowsMatched(self: ItemPrintLines) -> Int64

Set: TotalRowsMatched(self: ItemPrintLines) = value
"""


    DisplayMember = 'ItemDescription'
    ValueMember = 'ItemCode'

    Instance = ItemPrintLines()
    """hardcoded/returns an instance of the class"""

class ItemWithItemIdPrintLine(PrintLineBase):
    """ ItemWithItemIdPrintLine() """
    @staticmethod
    def Create(item, itemIdentificationNumber):
        """ Create(item: Item, itemIdentificationNumber: str) -> ItemWithItemIdPrintLine """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ItemWithItemIdPrintLine) -> int """
        pass

    Barcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Barcode(self: ItemWithItemIdPrintLine) -> str

Set: Barcode(self: ItemWithItemIdPrintLine) = value
"""

    DefaultSalesPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultSalesPrice(self: ItemWithItemIdPrintLine) -> Decimal

Set: DefaultSalesPrice(self: ItemWithItemIdPrintLine) = value
"""

    DefaultVendorName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultVendorName(self: ItemWithItemIdPrintLine) -> str

Set: DefaultVendorName(self: ItemWithItemIdPrintLine) = value
"""

    DefaultVendorNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultVendorNumber(self: ItemWithItemIdPrintLine) -> str

Set: DefaultVendorNumber(self: ItemWithItemIdPrintLine) = value
"""

    ExpiryDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExpiryDate(self: ItemWithItemIdPrintLine) -> DateTime

Set: ExpiryDate(self: ItemWithItemIdPrintLine) = value
"""

    GroupKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupKey(self: ItemWithItemIdPrintLine) -> str

"""

    GTINCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The GS1 GTIN code of this item

Get: GTINCode(self: ItemWithItemIdPrintLine) -> str

Set: GTINCode(self: ItemWithItemIdPrintLine) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: ItemWithItemIdPrintLine) -> str

Set: ItemCode(self: ItemWithItemIdPrintLine) = value
"""

    ItemDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemDescription(self: ItemWithItemIdPrintLine) -> str

Set: ItemDescription(self: ItemWithItemIdPrintLine) = value
"""

    ItemGroupCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemGroupCode(self: ItemWithItemIdPrintLine) -> str

Set: ItemGroupCode(self: ItemWithItemIdPrintLine) = value
"""

    ItemGroupDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemGroupDescription(self: ItemWithItemIdPrintLine) -> str

Set: ItemGroupDescription(self: ItemWithItemIdPrintLine) = value
"""

    ItemIdentification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIdentification(self: ItemWithItemIdPrintLine) -> str

Set: ItemIdentification(self: ItemWithItemIdPrintLine) = value
"""

    StartDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartDate(self: ItemWithItemIdPrintLine) -> DateTime

Set: StartDate(self: ItemWithItemIdPrintLine) = value
"""

    SupplierCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupplierCode(self: ItemWithItemIdPrintLine) -> str

Set: SupplierCode(self: ItemWithItemIdPrintLine) = value
"""

    UnitCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitCode(self: ItemWithItemIdPrintLine) -> str

Set: UnitCode(self: ItemWithItemIdPrintLine) = value
"""


    Instance = ItemWithItemIdPrintLine()
    """hardcoded/returns an instance of the class"""

class LabelFieldType(Object):
    """ enum LabelFieldType, values: Barcode (2), BarcodeDescription (3), String (1), Unknown (0) """
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

    Barcode = None
    BarcodeDescription = None
    String = None
    Unknown = None
    value__ = None

    Instance = LabelFieldType()
    """hardcoded/returns an instance of the class"""

class LicenseOptions():
    """ LicenseOptions() """
    PdfPrintNetCompany = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PdfPrintNet License company name

Get: PdfPrintNetCompany(self: LicenseOptions) -> str

Set: PdfPrintNetCompany(self: LicenseOptions) = value
"""

    PdfPrintNetLicenseKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PdfPrintNet License key

Get: PdfPrintNetLicenseKey(self: LicenseOptions) -> str

Set: PdfPrintNetLicenseKey(self: LicenseOptions) = value
"""


    Instance = LicenseOptions()
    """hardcoded/returns an instance of the class"""

class LicensePlatePrintLine(PrintLineBase):
    """ LicensePlatePrintLine() """
    @staticmethod
    def Create(item):
        """ Create(item: LicensePlate) -> LicensePlatePrintLine """
        pass

    Barcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Barcode(self: LicensePlatePrintLine) -> str

"""

    BestBeforeDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: BestBeforeDate(self: LicensePlatePrintLine) -> Nullable[DateTime]

Set: BestBeforeDate(self: LicensePlatePrintLine) = value
"""

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Code(self: LicensePlatePrintLine) -> str

Set: Code(self: LicensePlatePrintLine) = value
"""

    CreatedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CreatedBy(self: LicensePlatePrintLine) -> str

Set: CreatedBy(self: LicensePlatePrintLine) = value
"""

    CreatedOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CreatedOn(self: LicensePlatePrintLine) -> Nullable[DateTime]

Set: CreatedOn(self: LicensePlatePrintLine) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Description(self: LicensePlatePrintLine) -> str

Set: Description(self: LicensePlatePrintLine) = value
"""

    GroupKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: GroupKey(self: LicensePlatePrintLine) -> str

"""

    LocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: LocationCode(self: LicensePlatePrintLine) -> str

Set: LocationCode(self: LicensePlatePrintLine) = value
"""

    NoOfItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: NoOfItems(self: LicensePlatePrintLine) -> int

Set: NoOfItems(self: LicensePlatePrintLine) = value
"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Status(self: LicensePlatePrintLine) -> LicensePlateStatusEnum

Set: Status(self: LicensePlatePrintLine) = value
"""

    StatusAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: StatusAsString(self: LicensePlatePrintLine) -> str

"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: WarehouseCode(self: LicensePlatePrintLine) -> str

Set: WarehouseCode(self: LicensePlatePrintLine) = value
"""


    Instance = LicensePlatePrintLine()
    """hardcoded/returns an instance of the class"""

class LicensePlatePrintLines(PrintLinesBase):
    """
    LicensePlatePrintLines()
    LicensePlatePrintLines(collection: IEnumerable[LicensePlatePrintLine])
    """
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
    def __new__(self, collection=None):
        """
        __new__(cls: type)
        __new__(cls: type, collection: IEnumerable[LicensePlatePrintLine])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    IsDisposable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsDisposable(self: LicensePlatePrintLines) -> bool

"""

    PreserveState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PreserveState(self: LicensePlatePrintLines) -> bool

"""

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """when paging is used this property holds the total number of rows 
            which are returned by the query

Get: TotalRowsMatched(self: LicensePlatePrintLines) -> Int64

Set: TotalRowsMatched(self: LicensePlatePrintLines) = value
"""


    DisplayMember = 'Description'
    ValueMember = 'Code'

    Instance = LicensePlatePrintLines()
    """hardcoded/returns an instance of the class"""

class PickbatchPrintLine(PrintLineBase):
    """ PickbatchPrintLine() """
    @staticmethod
    def Create(batch):
        """ Create(batch: Batch) -> PickbatchPrintLine """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: PickbatchPrintLine) -> int """
        pass

    Barcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Barcode(self: PickbatchPrintLine) -> str

Set: Barcode(self: PickbatchPrintLine) = value
"""

    BatchId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BatchId(self: PickbatchPrintLine) -> str

Set: BatchId(self: PickbatchPrintLine) = value
"""

    BatchName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BatchName(self: PickbatchPrintLine) -> str

Set: BatchName(self: PickbatchPrintLine) = value
"""

    CreatedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatedBy(self: PickbatchPrintLine) -> str

Set: CreatedBy(self: PickbatchPrintLine) = value
"""

    CreatedOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatedOn(self: PickbatchPrintLine) -> DateTime

Set: CreatedOn(self: PickbatchPrintLine) = value
"""

    GroupKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: GroupKey(self: PickbatchPrintLine) -> str

"""

    Notes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Notes(self: PickbatchPrintLine) -> str

Set: Notes(self: PickbatchPrintLine) = value
"""

    PickProcessedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickProcessedBy(self: PickbatchPrintLine) -> str

Set: PickProcessedBy(self: PickbatchPrintLine) = value
"""

    PickProcessedOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickProcessedOn(self: PickbatchPrintLine) -> DateTime

Set: PickProcessedOn(self: PickbatchPrintLine) = value
"""

    Tags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tags(self: PickbatchPrintLine) -> str

Set: Tags(self: PickbatchPrintLine) = value
"""


    Instance = PickbatchPrintLine()
    """hardcoded/returns an instance of the class"""

class PickbatchPrintLines(PrintLinesBase):
    """
    PickbatchPrintLines()
    PickbatchPrintLines(collection: IEnumerable[PickbatchPrintLine])
    """
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
    def __new__(self, collection=None):
        """
        __new__(cls: type)
        __new__(cls: type, collection: IEnumerable[PickbatchPrintLine])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    IsDisposable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsDisposable(self: PickbatchPrintLines) -> bool

"""

    PreserveState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PreserveState(self: PickbatchPrintLines) -> bool

"""

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """when paging is used this property holds the total number of rows 
            which are returned by the query

Get: TotalRowsMatched(self: PickbatchPrintLines) -> Int64

Set: TotalRowsMatched(self: PickbatchPrintLines) = value
"""


    DisplayMember = 'BatchName'
    ValueMember = 'BatchId'

    Instance = PickbatchPrintLines()
    """hardcoded/returns an instance of the class"""

class PrintBaseArgs():
    """
    Base class for requesting a print of some document.
    
    PrintBaseArgs()
    PrintBaseArgs(printerName: str, options: PrintingOptions)
    """
    @staticmethod # known case of __new__
    def __new__(self, printerName=None, options=None):
        """
        __new__(cls: type)
        __new__(cls: type, printerName: str, options: PrintingOptions)
        """
        pass

    Label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A descriptive label for print job

Get: Label(self: PrintBaseArgs) -> str

Set: Label(self: PrintBaseArgs) = value
"""

    PrinterName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Override: id of printer to print from.
            Leave empty to let the Print rule engine decide the printer.

Get: PrinterName(self: PrintBaseArgs) -> str

Set: PrinterName(self: PrintBaseArgs) = value
"""

    PrintingOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Printing options for printing.
            Overrides the print rule printer options and the default printer options.

Get: PrintingOptions(self: PrintBaseArgs) -> PrintingOptions

Set: PrintingOptions(self: PrintBaseArgs) = value
"""


    Instance = PrintBaseArgs()
    """hardcoded/returns an instance of the class"""

class PrintDuplicateLabelArgs(PrintBaseArgs):
    """ PrintDuplicateLabelArgs() """
    ShipmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ShipmentId(self: PrintDuplicateLabelArgs) -> int

Set: ShipmentId(self: PrintDuplicateLabelArgs) = value
"""


    Instance = PrintDuplicateLabelArgs()
    """hardcoded/returns an instance of the class"""

class PrintLabel(DbObject):
    """ PrintLabel() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    DatasetTypeFullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DatasetTypeFullName(self: PrintLabel) -> str

Set: DatasetTypeFullName(self: PrintLabel) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: PrintLabel) -> str

Set: Description(self: PrintLabel) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DisplayName(self: PrintLabel) -> str

"""

    FieldRegEx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FieldRegEx(self: PrintLabel) -> str

Set: FieldRegEx(self: PrintLabel) = value
"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The height of the label in dots (dpi). So far it's only implemented for colli labels.

Get: Height(self: PrintLabel) -> int

Set: Height(self: PrintLabel) = value
"""

    ID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ID(self: PrintLabel) -> int

Set: ID(self: PrintLabel) = value
"""

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Image(self: PrintLabel) -> Array[Byte]

Set: Image(self: PrintLabel) = value
"""

    IsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsActive(self: PrintLabel) -> bool

Set: IsActive(self: PrintLabel) = value
"""

    Mappings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The keys are the fields in the label, the values are the properties of the dataset.

Get: Mappings(self: PrintLabel) -> Mappings[str, str, str]

Set: Mappings(self: PrintLabel) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: PrintLabel) -> str

Set: Name(self: PrintLabel) = value
"""

    OneLabelPerPrintAction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Instead of that the entered qty is used for nr Of Labels,
            1 label is printed with the possibility to add the input qty on the label.

Get: OneLabelPerPrintAction(self: PrintLabel) -> bool

Set: OneLabelPerPrintAction(self: PrintLabel) = value
"""

    PrinterCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrinterCode(self: PrintLabel) -> str

Set: PrinterCode(self: PrintLabel) = value
"""

    SingleLabelDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SingleLabelDescription(self: PrintLabel) -> str

Set: SingleLabelDescription(self: PrintLabel) = value
"""

    Sys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Sys(self: PrintLabel) -> bool

Set: Sys(self: PrintLabel) = value
"""


    Instance = PrintLabel()
    """hardcoded/returns an instance of the class"""

class PrintLabelArgs():
    """ PrintLabelArgs() """
    PrintLabels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PrintLabels(self: PrintLabelArgs) -> bool

Set: PrintLabels(self: PrintLabelArgs) = value
"""

    SelectedLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SelectedLabel(self: PrintLabelArgs) -> PrintLabel

Set: SelectedLabel(self: PrintLabelArgs) = value
"""


    Instance = PrintLabelArgs()
    """hardcoded/returns an instance of the class"""

class PrintLabelItemProperties():
    """ PrintLabelItemProperties() """
    EndElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: EndElement(self: PrintLabelItemProperties) -> Match

Set: EndElement(self: PrintLabelItemProperties) = value
"""

    EndPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: EndPosition(self: PrintLabelItemProperties) -> int

Set: EndPosition(self: PrintLabelItemProperties) = value
"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Height(self: PrintLabelItemProperties) -> int

"""

    StartElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: StartElement(self: PrintLabelItemProperties) -> Match

Set: StartElement(self: PrintLabelItemProperties) = value
"""

    StartPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: StartPosition(self: PrintLabelItemProperties) -> int

Set: StartPosition(self: PrintLabelItemProperties) = value
"""


    Instance = PrintLabelItemProperties()
    """hardcoded/returns an instance of the class"""

class PrintLabelMapping():
    """
    PrintLabelMapping(placeholder: str, datasetField: str, transformation: str)
    PrintLabelMapping()
    """
    @staticmethod # known case of __new__
    def __new__(self, placeholder=None, datasetField=None, transformation=None):
        """
        __new__(cls: type, placeholder: str, datasetField: str, transformation: str)
        __new__(cls: type)
        """
        pass

    DatasetField = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DatasetField(self: PrintLabelMapping) -> str

Set: DatasetField(self: PrintLabelMapping) = value
"""

    Placeholder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Placeholder(self: PrintLabelMapping) -> str

Set: Placeholder(self: PrintLabelMapping) = value
"""

    Transformation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Transformation(self: PrintLabelMapping) -> str

Set: Transformation(self: PrintLabelMapping) = value
"""


    Instance = PrintLabelMapping()
    """hardcoded/returns an instance of the class"""

class PrintLabelMappings(FindableList):
    """ PrintLabelMappings() """
    @staticmethod
    def ConstructFrom(mappings):
        """ ConstructFrom(mappings: Mappings[str, str, str]) -> PrintLabelMappings """
        pass

    def ConvertTo(self, mappings=None):
        """
        ConvertTo(self: PrintLabelMappings) -> Mappings[str, str, str]
        ConvertTo(mappings: PrintLabelMappings) -> Mappings[str, str, str]
        """
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

    DisplayMember = 'DatasetField'
    ValueMember = 'Placeholder'

    Instance = PrintLabelMappings()
    """hardcoded/returns an instance of the class"""

class PrintLabels(FindableList):
    """ PrintLabels() """
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

    DisplayMember = 'DisplayName'
    ValueMember = 'ID'

    Instance = PrintLabels()
    """hardcoded/returns an instance of the class"""

class PrintPackageSlipArgs(PrintBaseArgs):
    """ PrintPackageSlipArgs() """
    ShipmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of the shipment to print the package slip for.

Get: ShipmentId(self: PrintPackageSlipArgs) -> int

Set: ShipmentId(self: PrintPackageSlipArgs) = value
"""


    Instance = PrintPackageSlipArgs()
    """hardcoded/returns an instance of the class"""

class PrintPickbatchLabelArgs(PrintBaseArgs):
    """ PrintPickbatchLabelArgs() """
    BatchIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Ids of the Wms.RemotingObjects.BatchPicking.Batch to print the label for

Get: BatchIds(self: PrintPickbatchLabelArgs) -> List[Guid]

Set: BatchIds(self: PrintPickbatchLabelArgs) = value
"""

    PrintLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of the Pickbatch Label layout

Get: PrintLabel(self: PrintPickbatchLabelArgs) -> PrintLabel

Set: PrintLabel(self: PrintPickbatchLabelArgs) = value
"""


    Instance = PrintPickbatchLabelArgs()
    """hardcoded/returns an instance of the class"""

class PrintPickingListArgs(PrintBaseArgs):
    """
    Options for requesting a print of a picklist
    
    PrintPickingListArgs()
    """
    BatchIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Ids of the batches to print a picklist for.

Get: BatchIds(self: PrintPickingListArgs) -> List[Guid]

Set: BatchIds(self: PrintPickingListArgs) = value
"""

    Report = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Report used to generate the picklist

Get: Report(self: PrintPickingListArgs) -> ReportItem

Set: Report(self: PrintPickingListArgs) = value
"""


    Instance = PrintPickingListArgs()
    """hardcoded/returns an instance of the class"""

class PrintShipmentDocumentArgs(PrintBaseArgs):
    """ PrintShipmentDocumentArgs() """
    ShipmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ShipmentId(self: PrintShipmentDocumentArgs) -> int

Set: ShipmentId(self: PrintShipmentDocumentArgs) = value
"""


    Instance = PrintShipmentDocumentArgs()
    """hardcoded/returns an instance of the class"""

class PrintSSCCLabelsArgs():
    """ PrintSSCCLabelsArgs() """
    CacheKeyOfTransportPackages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Wms.RemotingObjects.Caching.CacheKey of the Wms.RemotingObjects.ShippingLayers.TransportPackages to print the labels for

Get: CacheKeyOfTransportPackages(self: PrintSSCCLabelsArgs) -> CacheKey

Set: CacheKeyOfTransportPackages(self: PrintSSCCLabelsArgs) = value
"""

    LabelHomogeneousPallet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of the homogeneous pallet label layout

Get: LabelHomogeneousPallet(self: PrintSSCCLabelsArgs) -> str

Set: LabelHomogeneousPallet(self: PrintSSCCLabelsArgs) = value
"""

    LabelMixedPallet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of the mixed pallet layout

Get: LabelMixedPallet(self: PrintSSCCLabelsArgs) -> str

Set: LabelMixedPallet(self: PrintSSCCLabelsArgs) = value
"""

    SelectedPackageId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The System.Guid of a Wms.RemotingObjects.ShippingLayers.TransportPackage if you want to print the label of a specific package />

Get: SelectedPackageId(self: PrintSSCCLabelsArgs) -> Guid

Set: SelectedPackageId(self: PrintSSCCLabelsArgs) = value
"""


    Instance = PrintSSCCLabelsArgs()
    """hardcoded/returns an instance of the class"""

class PurchaseOrderPrintLine(Object):
    """ PurchaseOrderPrintLine() """
    CurrentBarcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """CURRENT vendor Barcode

Get: CurrentBarcode(self: PurchaseOrderPrintLine) -> str

Set: CurrentBarcode(self: PurchaseOrderPrintLine) = value
"""

    CurrentSupplierCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Current vendor code.

Get: CurrentSupplierCode(self: PurchaseOrderPrintLine) -> str

Set: CurrentSupplierCode(self: PurchaseOrderPrintLine) = value
"""

    InboundLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InboundLocation(self: PurchaseOrderPrintLine) -> str

Set: InboundLocation(self: PurchaseOrderPrintLine) = value
"""

    YourReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: YourReference(self: PurchaseOrderPrintLine) -> str

Set: YourReference(self: PurchaseOrderPrintLine) = value
"""


    Instance = PurchaseOrderPrintLine()
    """hardcoded/returns an instance of the class"""

class PurchaseOrderPrintLines(PrintLinesBase):
    """
    PurchaseOrderPrintLines()
    PurchaseOrderPrintLines(collection: IEnumerable[PurchaseOrderPrintLine])
    """
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
    def __new__(self, collection=None):
        """
        __new__(cls: type)
        __new__(cls: type, collection: IEnumerable[PurchaseOrderPrintLine])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    IsDisposable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsDisposable(self: PurchaseOrderPrintLines) -> bool

"""

    PreserveState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PreserveState(self: PurchaseOrderPrintLines) -> bool

"""

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """when paging is used this property holds the total number of rows 
            which are returned by the query

Get: TotalRowsMatched(self: PurchaseOrderPrintLines) -> Int64

Set: TotalRowsMatched(self: PurchaseOrderPrintLines) = value
"""


    DisplayMember = 'ItemDescription'
    ValueMember = 'ItemCode'

    Instance = PurchaseOrderPrintLines()
    """hardcoded/returns an instance of the class"""

class ReportItem():
    """ ReportItem() """
    DataSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DataSource(self: ReportItem) -> str

Set: DataSource(self: ReportItem) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Description(self: ReportItem) -> str

Set: Description(self: ReportItem) = value
"""

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: FileName(self: ReportItem) -> str

Set: FileName(self: ReportItem) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: ReportItem) -> str

Set: Name(self: ReportItem) = value
"""


    Instance = ReportItem()
    """hardcoded/returns an instance of the class"""

class ReportItems(List):
    """ ReportItems() """
    @staticmethod
    def FromIEnumerable(list):
        """ FromIEnumerable(list: IEnumerable[ReportItem]) -> ReportItems """
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

    DisplayMember = 'Description'
    ValueMember = 'Name'

    Instance = ReportItems()
    """hardcoded/returns an instance of the class"""

class RmaOrderPrintLine(Object):
    """ RmaOrderPrintLine() """
    def GetHashCode(self):
        """ GetHashCode(self: RmaOrderPrintLine) -> int """
        pass

    Reason = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Reason(self: RmaOrderPrintLine) -> str

Set: Reason(self: RmaOrderPrintLine) = value
"""


    Instance = RmaOrderPrintLine()
    """hardcoded/returns an instance of the class"""

class RmaOrderPrintLines(PrintLinesBase):
    """ RmaOrderPrintLines() """
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

Get: IsDisposable(self: RmaOrderPrintLines) -> bool

"""

    PreserveState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PreserveState(self: RmaOrderPrintLines) -> bool

"""


    DisplayMember = 'ItemDescription'

    Instance = RmaOrderPrintLines()
    """hardcoded/returns an instance of the class"""

class SSCCBasePrintLine(PrintLineBase):
    """ SSCCBasePrintLine(barcode: str, barcodeReadable: str) """
    def GetHashCode(self):
        """ GetHashCode(self: SSCCBasePrintLine) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, barcode, barcodeReadable):
        """ __new__(cls: type, barcode: str, barcodeReadable: str) """
        pass

    Barcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Barcode(self: SSCCBasePrintLine) -> str

Set: Barcode(self: SSCCBasePrintLine) = value
"""

    BarcodeReadable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: BarcodeReadable(self: SSCCBasePrintLine) -> str

Set: BarcodeReadable(self: SSCCBasePrintLine) = value
"""

    GroupKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: GroupKey(self: SSCCBasePrintLine) -> str

"""


    Instance = SSCCBasePrintLine()
    """hardcoded/returns an instance of the class"""

class SSCCBasePrintLines(PrintLinesBase):
    """
    SSCCBasePrintLines()
    SSCCBasePrintLines(collection: IEnumerable[SSCCBasePrintLine])
    """
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
    def __new__(self, collection=None):
        """
        __new__(cls: type)
        __new__(cls: type, collection: IEnumerable[SSCCBasePrintLine])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    IsDisposable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsDisposable(self: SSCCBasePrintLines) -> bool

"""

    PreserveState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PreserveState(self: SSCCBasePrintLines) -> bool

"""

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """when paging is used this property holds the total number of rows 
            which are returned by the query

Get: TotalRowsMatched(self: SSCCBasePrintLines) -> Int64

Set: TotalRowsMatched(self: SSCCBasePrintLines) = value
"""


    DisplayMember = None
    ValueMember = None

    Instance = SSCCBasePrintLines()
    """hardcoded/returns an instance of the class"""

class SSCCHeterogeneousPrintLine(SSCCBasePrintLine):
    """
    SSCCHeterogeneousPrintLine(barcode: str, barcodeReadable: str)
    SSCCHeterogeneousPrintLine(barcode: str, barcodeReadable: str, packages: TransportPackages)
    """
    def GetHashCode(self):
        """ GetHashCode(self: SSCCHeterogeneousPrintLine) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, barcode, barcodeReadable, packages=None):
        """
        __new__(cls: type, barcode: str, barcodeReadable: str)
        __new__(cls: type, barcode: str, barcodeReadable: str, packages: TransportPackages)
        """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: SSCCHeterogeneousPrintLine) -> str

Set: Description(self: SSCCHeterogeneousPrintLine) = value
"""

    FromAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FromAddress(self: SSCCHeterogeneousPrintLine) -> str

Set: FromAddress(self: SSCCHeterogeneousPrintLine) = value
"""

    FromCity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FromCity(self: SSCCHeterogeneousPrintLine) -> str

Set: FromCity(self: SSCCHeterogeneousPrintLine) = value
"""

    FromCountry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FromCountry(self: SSCCHeterogeneousPrintLine) -> str

Set: FromCountry(self: SSCCHeterogeneousPrintLine) = value
"""

    FromName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FromName(self: SSCCHeterogeneousPrintLine) -> str

Set: FromName(self: SSCCHeterogeneousPrintLine) = value
"""

    FromZipCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FromZipCode(self: SSCCHeterogeneousPrintLine) -> str

Set: FromZipCode(self: SSCCHeterogeneousPrintLine) = value
"""

    GroupKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: GroupKey(self: SSCCHeterogeneousPrintLine) -> str

"""

    PackageNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PackageNumber(self: SSCCHeterogeneousPrintLine) -> int

Set: PackageNumber(self: SSCCHeterogeneousPrintLine) = value
"""

    ToAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToAddress(self: SSCCHeterogeneousPrintLine) -> str

Set: ToAddress(self: SSCCHeterogeneousPrintLine) = value
"""

    ToCity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToCity(self: SSCCHeterogeneousPrintLine) -> str

Set: ToCity(self: SSCCHeterogeneousPrintLine) = value
"""

    ToCountry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToCountry(self: SSCCHeterogeneousPrintLine) -> str

Set: ToCountry(self: SSCCHeterogeneousPrintLine) = value
"""

    ToName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToName(self: SSCCHeterogeneousPrintLine) -> str

Set: ToName(self: SSCCHeterogeneousPrintLine) = value
"""

    TotalAmountOfPackages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalAmountOfPackages(self: SSCCHeterogeneousPrintLine) -> int

Set: TotalAmountOfPackages(self: SSCCHeterogeneousPrintLine) = value
"""

    ToZipCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToZipCode(self: SSCCHeterogeneousPrintLine) -> str

Set: ToZipCode(self: SSCCHeterogeneousPrintLine) = value
"""


    Instance = SSCCHeterogeneousPrintLine()
    """hardcoded/returns an instance of the class"""

class SSCCHeterogeneousPrintLines(PrintLinesBase):
    """
    SSCCHeterogeneousPrintLines()
    SSCCHeterogeneousPrintLines(collection: IEnumerable[SSCCHeterogeneousPrintLine])
    """
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
    def __new__(self, collection=None):
        """
        __new__(cls: type)
        __new__(cls: type, collection: IEnumerable[SSCCHeterogeneousPrintLine])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    IsDisposable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsDisposable(self: SSCCHeterogeneousPrintLines) -> bool

"""

    PreserveState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PreserveState(self: SSCCHeterogeneousPrintLines) -> bool

"""

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """when paging is used this property holds the total number of rows 
            which are returned by the query

Get: TotalRowsMatched(self: SSCCHeterogeneousPrintLines) -> Int64

Set: TotalRowsMatched(self: SSCCHeterogeneousPrintLines) = value
"""


    DisplayMember = None
    ValueMember = None

    Instance = SSCCHeterogeneousPrintLines()
    """hardcoded/returns an instance of the class"""

class SSCCHomogeneousPrintLine(SSCCHeterogeneousPrintLine):
    """
    SSCCHomogeneousPrintLine(barcode: str, barcodeReadable: str)
    SSCCHomogeneousPrintLine(barcode: str, barcodeReadable: str, packages: TransportPackages)
    """
    def GetHashCode(self):
        """ GetHashCode(self: SSCCHomogeneousPrintLine) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, barcode, barcodeReadable, packages=None):
        """
        __new__(cls: type, barcode: str, barcodeReadable: str)
        __new__(cls: type, barcode: str, barcodeReadable: str, packages: TransportPackages)
        """
        pass

    Batch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Batch(self: SSCCHomogeneousPrintLine) -> str

Set: Batch(self: SSCCHomogeneousPrintLine) = value
"""

    ExpiryDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExpiryDate(self: SSCCHomogeneousPrintLine) -> DateTime

Set: ExpiryDate(self: SSCCHomogeneousPrintLine) = value
"""

    GTIN = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GTIN(self: SSCCHomogeneousPrintLine) -> str

Set: GTIN(self: SSCCHomogeneousPrintLine) = value
"""

    ItemWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemWeight(self: SSCCHomogeneousPrintLine) -> Decimal

Set: ItemWeight(self: SSCCHomogeneousPrintLine) = value
"""

    Serial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Serial(self: SSCCHomogeneousPrintLine) -> str

Set: Serial(self: SSCCHomogeneousPrintLine) = value
"""

    UnitCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitCount(self: SSCCHomogeneousPrintLine) -> int

Set: UnitCount(self: SSCCHomogeneousPrintLine) = value
"""


    Instance = SSCCHomogeneousPrintLine()
    """hardcoded/returns an instance of the class"""

class SSCCHomogeneousPrintLines(PrintLinesBase):
    """
    SSCCHomogeneousPrintLines()
    SSCCHomogeneousPrintLines(collection: IEnumerable[SSCCHomogeneousPrintLine])
    """
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
    def __new__(self, collection=None):
        """
        __new__(cls: type)
        __new__(cls: type, collection: IEnumerable[SSCCHomogeneousPrintLine])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    IsDisposable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsDisposable(self: SSCCHomogeneousPrintLines) -> bool

"""

    PreserveState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PreserveState(self: SSCCHomogeneousPrintLines) -> bool

"""

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """when paging is used this property holds the total number of rows 
            which are returned by the query

Get: TotalRowsMatched(self: SSCCHomogeneousPrintLines) -> Int64

Set: TotalRowsMatched(self: SSCCHomogeneousPrintLines) = value
"""


    DisplayMember = None
    ValueMember = None

    Instance = SSCCHomogeneousPrintLines()
    """hardcoded/returns an instance of the class"""

class TransportPackageItemPrintLine(PrintLineBase):
    """ TransportPackageItemPrintLine() """
    Barcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Barcode(self: TransportPackageItemPrintLine) -> str

Set: Barcode(self: TransportPackageItemPrintLine) = value
"""

    GroupKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: GroupKey(self: TransportPackageItemPrintLine) -> str

"""

    GTINCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The GS1 GTIN code of this item

Get: GTINCode(self: TransportPackageItemPrintLine) -> str

Set: GTINCode(self: TransportPackageItemPrintLine) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemCode(self: TransportPackageItemPrintLine) -> str

Set: ItemCode(self: TransportPackageItemPrintLine) = value
"""

    ItemDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemDescription(self: TransportPackageItemPrintLine) -> str

Set: ItemDescription(self: TransportPackageItemPrintLine) = value
"""

    ItemQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemQuantity(self: TransportPackageItemPrintLine) -> Decimal

Set: ItemQuantity(self: TransportPackageItemPrintLine) = value
"""

    UnitCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: UnitCode(self: TransportPackageItemPrintLine) -> str

Set: UnitCode(self: TransportPackageItemPrintLine) = value
"""


    Instance = TransportPackageItemPrintLine()
    """hardcoded/returns an instance of the class"""

class TransportPackageItemsPrintLine(PrintLinesBase):
    """
    TransportPackageItemsPrintLine()
    TransportPackageItemsPrintLine(collection: IEnumerable[TransportPackageItemPrintLine])
    """
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
    def __new__(self, collection=None):
        """
        __new__(cls: type)
        __new__(cls: type, collection: IEnumerable[TransportPackageItemPrintLine])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    IsDisposable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsDisposable(self: TransportPackageItemsPrintLine) -> bool

"""

    PreserveState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PreserveState(self: TransportPackageItemsPrintLine) -> bool

"""

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """when paging is used this property holds the total number of rows 
            which are returned by the query

Get: TotalRowsMatched(self: TransportPackageItemsPrintLine) -> Int64

Set: TotalRowsMatched(self: TransportPackageItemsPrintLine) = value
"""


    DisplayMember = 'ItemCode'
    ValueMember = 'GroupKey'

    Instance = TransportPackageItemsPrintLine()
    """hardcoded/returns an instance of the class"""

class TransportPackagePrintLine(PrintLineBase):
    """ TransportPackagePrintLine() """
    @staticmethod
    def Create(transportPackage):
        """ Create(transportPackage: TransportPackage) -> TransportPackagePrintLine """
        pass

    CustomerDeliveryAddresLine1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerDeliveryAddresLine1(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryAddresLine1(self: TransportPackagePrintLine) = value
"""

    CustomerDeliveryAddresLine2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerDeliveryAddresLine2(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryAddresLine2(self: TransportPackagePrintLine) = value
"""

    CustomerDeliveryAddresLine3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerDeliveryAddresLine3(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryAddresLine3(self: TransportPackagePrintLine) = value
"""

    CustomerDeliveryCity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerDeliveryCity(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryCity(self: TransportPackagePrintLine) = value
"""

    CustomerDeliveryCountryCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerDeliveryCountryCode(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryCountryCode(self: TransportPackagePrintLine) = value
"""

    CustomerDeliveryCountryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerDeliveryCountryName(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryCountryName(self: TransportPackagePrintLine) = value
"""

    CustomerDeliveryEmail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerDeliveryEmail(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryEmail(self: TransportPackagePrintLine) = value
"""

    CustomerDeliveryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerDeliveryName(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryName(self: TransportPackagePrintLine) = value
"""

    CustomerDeliveryName2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerDeliveryName2(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryName2(self: TransportPackagePrintLine) = value
"""

    CustomerDeliveryPhoneNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerDeliveryPhoneNumber(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryPhoneNumber(self: TransportPackagePrintLine) = value
"""

    CustomerDeliveryStateCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerDeliveryStateCode(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryStateCode(self: TransportPackagePrintLine) = value
"""

    CustomerDeliveryZipCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerDeliveryZipCode(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryZipCode(self: TransportPackagePrintLine) = value
"""

    CustomerInvoiceAddresLine1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceAddresLine1(self: TransportPackagePrintLine) -> str

Set: CustomerInvoiceAddresLine1(self: TransportPackagePrintLine) = value
"""

    CustomerInvoiceAddresLine2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceAddresLine2(self: TransportPackagePrintLine) -> str

Set: CustomerInvoiceAddresLine2(self: TransportPackagePrintLine) = value
"""

    CustomerInvoiceAddresLine3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceAddresLine3(self: TransportPackagePrintLine) -> str

Set: CustomerInvoiceAddresLine3(self: TransportPackagePrintLine) = value
"""

    CustomerInvoiceCity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceCity(self: TransportPackagePrintLine) -> str

Set: CustomerInvoiceCity(self: TransportPackagePrintLine) = value
"""

    CustomerInvoiceCountryCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceCountryCode(self: TransportPackagePrintLine) -> str

Set: CustomerInvoiceCountryCode(self: TransportPackagePrintLine) = value
"""

    CustomerInvoiceCountryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceCountryName(self: TransportPackagePrintLine) -> str

Set: CustomerInvoiceCountryName(self: TransportPackagePrintLine) = value
"""

    CustomerInvoiceEmail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceEmail(self: TransportPackagePrintLine) -> str

Set: CustomerInvoiceEmail(self: TransportPackagePrintLine) = value
"""

    CustomerInvoiceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceName(self: TransportPackagePrintLine) -> str

Set: CustomerInvoiceName(self: TransportPackagePrintLine) = value
"""

    CustomerInvoiceName2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceName2(self: TransportPackagePrintLine) -> str

Set: CustomerInvoiceName2(self: TransportPackagePrintLine) = value
"""

    CustomerInvoicePhoneNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoicePhoneNumber(self: TransportPackagePrintLine) -> str

Set: CustomerInvoicePhoneNumber(self: TransportPackagePrintLine) = value
"""

    CustomerInvoiceStateCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceStateCode(self: TransportPackagePrintLine) -> str

Set: CustomerInvoiceStateCode(self: TransportPackagePrintLine) = value
"""

    CustomerInvoiceZipCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerInvoiceZipCode(self: TransportPackagePrintLine) -> str

Set: CustomerInvoiceZipCode(self: TransportPackagePrintLine) = value
"""

    CustomerReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CustomerReferences(self: TransportPackagePrintLine) -> str

Set: CustomerReferences(self: TransportPackagePrintLine) = value
"""

    GroupKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: GroupKey(self: TransportPackagePrintLine) -> str

"""

    ItemBarcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Only here to map the print line to the dataset

Get: ItemBarcode(self: TransportPackagePrintLine) -> str

"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Only here to map the print line to the dataset

Get: ItemCode(self: TransportPackagePrintLine) -> str

"""

    ItemDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Only here to map the print line to the dataset

Get: ItemDescription(self: TransportPackagePrintLine) -> str

"""

    OurReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OurReferences(self: TransportPackagePrintLine) -> str

Set: OurReferences(self: TransportPackagePrintLine) = value
"""

    PackageBarcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PackageBarcode(self: TransportPackagePrintLine) -> str

Set: PackageBarcode(self: TransportPackagePrintLine) = value
"""

    PackageDimensions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PackageDimensions(self: TransportPackagePrintLine) -> str

Set: PackageDimensions(self: TransportPackagePrintLine) = value
"""

    PackageGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PackageGuid(self: TransportPackagePrintLine) -> str

Set: PackageGuid(self: TransportPackagePrintLine) = value
"""

    PackageIdentification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PackageIdentification(self: TransportPackagePrintLine) -> str

Set: PackageIdentification(self: TransportPackagePrintLine) = value
"""

    PackageItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PackageItemCode(self: TransportPackagePrintLine) -> str

Set: PackageItemCode(self: TransportPackagePrintLine) = value
"""

    PackageNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PackageNumber(self: TransportPackagePrintLine) -> str

Set: PackageNumber(self: TransportPackagePrintLine) = value
"""

    PackageType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PackageType(self: TransportPackagePrintLine) -> str

Set: PackageType(self: TransportPackagePrintLine) = value
"""

    PackageWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PackageWeight(self: TransportPackagePrintLine) -> str

Set: PackageWeight(self: TransportPackagePrintLine) = value
"""

    SenderAddresLine1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SenderAddresLine1(self: TransportPackagePrintLine) -> str

Set: SenderAddresLine1(self: TransportPackagePrintLine) = value
"""

    SenderAddresLine2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SenderAddresLine2(self: TransportPackagePrintLine) -> str

Set: SenderAddresLine2(self: TransportPackagePrintLine) = value
"""

    SenderAddresLine3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SenderAddresLine3(self: TransportPackagePrintLine) -> str

Set: SenderAddresLine3(self: TransportPackagePrintLine) = value
"""

    SenderCity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SenderCity(self: TransportPackagePrintLine) -> str

Set: SenderCity(self: TransportPackagePrintLine) = value
"""

    SenderCountryCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SenderCountryCode(self: TransportPackagePrintLine) -> str

Set: SenderCountryCode(self: TransportPackagePrintLine) = value
"""

    SenderCountryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SenderCountryName(self: TransportPackagePrintLine) -> str

Set: SenderCountryName(self: TransportPackagePrintLine) = value
"""

    SenderEmail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SenderEmail(self: TransportPackagePrintLine) -> str

Set: SenderEmail(self: TransportPackagePrintLine) = value
"""

    SenderName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SenderName(self: TransportPackagePrintLine) -> str

Set: SenderName(self: TransportPackagePrintLine) = value
"""

    SenderPhoneNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SenderPhoneNumber(self: TransportPackagePrintLine) -> str

Set: SenderPhoneNumber(self: TransportPackagePrintLine) = value
"""

    SenderStateCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SenderStateCode(self: TransportPackagePrintLine) -> str

Set: SenderStateCode(self: TransportPackagePrintLine) = value
"""

    SenderZipCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SenderZipCode(self: TransportPackagePrintLine) -> str

Set: SenderZipCode(self: TransportPackagePrintLine) = value
"""

    UnitCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Only here to map the print line to the dataset

Get: UnitCode(self: TransportPackagePrintLine) -> str

"""


    Instance = TransportPackagePrintLine()
    """hardcoded/returns an instance of the class"""

class TransportPackagePrintLines(PrintLinesBase):
    """
    TransportPackagePrintLines()
    TransportPackagePrintLines(collection: IEnumerable[TransportPackagePrintLine])
    """
    @staticmethod
    def Create(transportPackages):
        """ Create(transportPackages: TransportPackages) -> TransportPackagePrintLines """
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
    def __new__(self, collection=None):
        """
        __new__(cls: type)
        __new__(cls: type, collection: IEnumerable[TransportPackagePrintLine])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    IsDisposable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsDisposable(self: TransportPackagePrintLines) -> bool

"""

    PreserveState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PreserveState(self: TransportPackagePrintLines) -> bool

"""

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """when paging is used this property holds the total number of rows 
            which are returned by the query

Get: TotalRowsMatched(self: TransportPackagePrintLines) -> Int64

Set: TotalRowsMatched(self: TransportPackagePrintLines) = value
"""


    DisplayMember = 'PackageNumber'
    ValueMember = 'PackageGuid'

    Instance = TransportPackagePrintLines()
    """hardcoded/returns an instance of the class"""

# variables with complex values

