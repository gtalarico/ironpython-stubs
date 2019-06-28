# encoding: utf-8
# module Wms.RemotingObjects.Printing calls itself Printing
# from Wms.RemotingObjects,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class PrintLineBase:
 # no doc
 def Equals(self,obj):
  """ Equals(self: PrintLineBase,obj: object) -> bool """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: PrintLineBase) -> int """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __ne__(self,*args):
  pass
 GroupKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GroupKey(self: PrintLineBase) -> str

"""

 NumberOfCopies=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: NumberOfCopies(self: PrintLineBase) -> Decimal

Set: NumberOfCopies(self: PrintLineBase)=value
"""

 PrintLineItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PrintLineItems(self: PrintLineBase) -> PrintLinesBase

Set: PrintLineItems(self: PrintLineBase)=value
"""

 Quantity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Quantity(self: PrintLineBase) -> Decimal

Set: Quantity(self: PrintLineBase)=value
"""



class BarcodePrintLine:
 """ BarcodePrintLine(barcode: str) """
 def GetHashCode(self):
  """ GetHashCode(self: BarcodePrintLine) -> int """
  pass
 @staticmethod
 def __new__(self,barcode):
  """ __new__(cls: type,barcode: str) """
  pass
 Barcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Barcode(self: BarcodePrintLine) -> str

Set: Barcode(self: BarcodePrintLine)=value
"""

 GroupKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GroupKey(self: BarcodePrintLine) -> str

"""



class PrintLinesBase:
 # no doc
 def AddRange(self,collection):
  """ AddRange(self: PrintLinesBase,collection: IEnumerable[PrintLineBase]) -> List[PrintLineBase] """
  pass
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
 UniqueId='GroupKey'


class BarcodePrintLines:
 """
 BarcodePrintLines()
 BarcodePrintLines(collection: IEnumerable[BarcodePrintLine])
 """
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,collection=None):
  """
  __new__(cls: type)
  __new__(cls: type,collection: IEnumerable[BarcodePrintLine])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 IsDisposable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDisposable(self: BarcodePrintLines) -> bool

"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreserveState(self: BarcodePrintLines) -> bool

"""

 TotalRowsMatched=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TotalRowsMatched(self: BarcodePrintLines) -> Int64

Set: TotalRowsMatched(self: BarcodePrintLines)=value
"""


 DisplayMember=None
 ValueMember=None


class InboundOrderPrintLine:
 """ InboundOrderPrintLine() """
 def GetHashCode(self):
  """ GetHashCode(self: InboundOrderPrintLine) -> int """
  pass
 Barcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Barcode(self: InboundOrderPrintLine) -> str

Set: Barcode(self: InboundOrderPrintLine)=value
"""

 EndDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: EndDate(self: InboundOrderPrintLine) -> DateTime

"""

 GroupKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GroupKey(self: InboundOrderPrintLine) -> str

"""

 GTINCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GTINCode(self: InboundOrderPrintLine) -> str

Set: GTINCode(self: InboundOrderPrintLine)=value
"""

 IsBatchItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsBatchItem(self: InboundOrderPrintLine) -> bool

Set: IsBatchItem(self: InboundOrderPrintLine)=value
"""

 IsSerialItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsSerialItem(self: InboundOrderPrintLine) -> bool

Set: IsSerialItem(self: InboundOrderPrintLine)=value
"""

 ItemBrand=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemBrand(self: InboundOrderPrintLine) -> str

Set: ItemBrand(self: InboundOrderPrintLine)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemCode(self: InboundOrderPrintLine) -> str

Set: ItemCode(self: InboundOrderPrintLine)=value
"""

 ItemDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemDescription(self: InboundOrderPrintLine) -> str

Set: ItemDescription(self: InboundOrderPrintLine)=value
"""

 ItemIdentification=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemIdentification(self: InboundOrderPrintLine) -> str

"""

 ItemIdentifications=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemIdentifications(self: InboundOrderPrintLine) -> List[ItemIdentification]

Set: ItemIdentifications(self: InboundOrderPrintLine)=value
"""

 OrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OrderNumber(self: InboundOrderPrintLine) -> str

Set: OrderNumber(self: InboundOrderPrintLine)=value
"""

 Quantity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Quantity(self: InboundOrderPrintLine) -> Decimal

Set: Quantity(self: InboundOrderPrintLine)=value
"""

 SupplierCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SupplierCode(self: InboundOrderPrintLine) -> str

Set: SupplierCode(self: InboundOrderPrintLine)=value
"""



class ItemPrintLine:
 """ ItemPrintLine() """
 @staticmethod
 def Create(item):
  """ Create(item: Item) -> ItemPrintLine """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: ItemPrintLine) -> int """
  pass
 Barcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Barcode(self: ItemPrintLine) -> str

Set: Barcode(self: ItemPrintLine)=value
"""

 DefaultSalesPrice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DefaultSalesPrice(self: ItemPrintLine) -> Decimal

Set: DefaultSalesPrice(self: ItemPrintLine)=value
"""

 DefaultVendorName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DefaultVendorName(self: ItemPrintLine) -> str

Set: DefaultVendorName(self: ItemPrintLine)=value
"""

 DefaultVendorNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DefaultVendorNumber(self: ItemPrintLine) -> str

Set: DefaultVendorNumber(self: ItemPrintLine)=value
"""

 GroupKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GroupKey(self: ItemPrintLine) -> str

"""

 GTINCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GTINCode(self: ItemPrintLine) -> str

Set: GTINCode(self: ItemPrintLine)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemCode(self: ItemPrintLine) -> str

Set: ItemCode(self: ItemPrintLine)=value
"""

 ItemDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemDescription(self: ItemPrintLine) -> str

Set: ItemDescription(self: ItemPrintLine)=value
"""

 ItemGroupCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemGroupCode(self: ItemPrintLine) -> str

Set: ItemGroupCode(self: ItemPrintLine)=value
"""

 ItemGroupDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemGroupDescription(self: ItemPrintLine) -> str

Set: ItemGroupDescription(self: ItemPrintLine)=value
"""

 SupplierCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SupplierCode(self: ItemPrintLine) -> str

Set: SupplierCode(self: ItemPrintLine)=value
"""

 UnitCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UnitCode(self: ItemPrintLine) -> str

Set: UnitCode(self: ItemPrintLine)=value
"""



class ItemPrintLines:
 """
 ItemPrintLines()
 ItemPrintLines(collection: IEnumerable[ItemPrintLine])
 """
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,collection=None):
  """
  __new__(cls: type)
  __new__(cls: type,collection: IEnumerable[ItemPrintLine])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 IsDisposable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDisposable(self: ItemPrintLines) -> bool

"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreserveState(self: ItemPrintLines) -> bool

"""

 TotalRowsMatched=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TotalRowsMatched(self: ItemPrintLines) -> Int64

Set: TotalRowsMatched(self: ItemPrintLines)=value
"""


 DisplayMember='ItemDescription'
 ValueMember='ItemCode'


class ItemWithItemIdPrintLine:
 """ ItemWithItemIdPrintLine() """
 @staticmethod
 def Create(item,itemIdentificationNumber):
  """ Create(item: Item,itemIdentificationNumber: str) -> ItemWithItemIdPrintLine """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: ItemWithItemIdPrintLine) -> int """
  pass
 Barcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Barcode(self: ItemWithItemIdPrintLine) -> str

Set: Barcode(self: ItemWithItemIdPrintLine)=value
"""

 DefaultSalesPrice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DefaultSalesPrice(self: ItemWithItemIdPrintLine) -> Decimal

Set: DefaultSalesPrice(self: ItemWithItemIdPrintLine)=value
"""

 DefaultVendorName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DefaultVendorName(self: ItemWithItemIdPrintLine) -> str

Set: DefaultVendorName(self: ItemWithItemIdPrintLine)=value
"""

 DefaultVendorNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DefaultVendorNumber(self: ItemWithItemIdPrintLine) -> str

Set: DefaultVendorNumber(self: ItemWithItemIdPrintLine)=value
"""

 ExpiryDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExpiryDate(self: ItemWithItemIdPrintLine) -> DateTime

Set: ExpiryDate(self: ItemWithItemIdPrintLine)=value
"""

 GroupKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GroupKey(self: ItemWithItemIdPrintLine) -> str

"""

 GTINCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GTINCode(self: ItemWithItemIdPrintLine) -> str

Set: GTINCode(self: ItemWithItemIdPrintLine)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemCode(self: ItemWithItemIdPrintLine) -> str

Set: ItemCode(self: ItemWithItemIdPrintLine)=value
"""

 ItemDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemDescription(self: ItemWithItemIdPrintLine) -> str

Set: ItemDescription(self: ItemWithItemIdPrintLine)=value
"""

 ItemGroupCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemGroupCode(self: ItemWithItemIdPrintLine) -> str

Set: ItemGroupCode(self: ItemWithItemIdPrintLine)=value
"""

 ItemGroupDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemGroupDescription(self: ItemWithItemIdPrintLine) -> str

Set: ItemGroupDescription(self: ItemWithItemIdPrintLine)=value
"""

 ItemIdentification=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemIdentification(self: ItemWithItemIdPrintLine) -> str

Set: ItemIdentification(self: ItemWithItemIdPrintLine)=value
"""

 StartDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: StartDate(self: ItemWithItemIdPrintLine) -> DateTime

Set: StartDate(self: ItemWithItemIdPrintLine)=value
"""

 SupplierCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SupplierCode(self: ItemWithItemIdPrintLine) -> str

Set: SupplierCode(self: ItemWithItemIdPrintLine)=value
"""

 UnitCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UnitCode(self: ItemWithItemIdPrintLine) -> str

Set: UnitCode(self: ItemWithItemIdPrintLine)=value
"""



class LabelFieldType:
 """ enum LabelFieldType,values: Barcode (2),BarcodeDescription (3),String (1),Unknown (0) """
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
 Barcode=None
 BarcodeDescription=None
 String=None
 Unknown=None
 value__=None


class LicenseOptions:
 """ LicenseOptions() """
 PdfPrintNetCompany=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PdfPrintNetCompany(self: LicenseOptions) -> str

Set: PdfPrintNetCompany(self: LicenseOptions)=value
"""

 PdfPrintNetLicenseKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PdfPrintNetLicenseKey(self: LicenseOptions) -> str

Set: PdfPrintNetLicenseKey(self: LicenseOptions)=value
"""



class LicensePlatePrintLine:
 """ LicensePlatePrintLine() """
 @staticmethod
 def Create(item):
  """ Create(item: LicensePlate) -> LicensePlatePrintLine """
  pass
 Barcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Barcode(self: LicensePlatePrintLine) -> str

"""

 BestBeforeDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BestBeforeDate(self: LicensePlatePrintLine) -> Nullable[DateTime]

Set: BestBeforeDate(self: LicensePlatePrintLine)=value
"""

 Code=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Code(self: LicensePlatePrintLine) -> str

Set: Code(self: LicensePlatePrintLine)=value
"""

 CreatedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CreatedBy(self: LicensePlatePrintLine) -> str

Set: CreatedBy(self: LicensePlatePrintLine)=value
"""

 CreatedOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CreatedOn(self: LicensePlatePrintLine) -> Nullable[DateTime]

Set: CreatedOn(self: LicensePlatePrintLine)=value
"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Description(self: LicensePlatePrintLine) -> str

Set: Description(self: LicensePlatePrintLine)=value
"""

 GroupKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GroupKey(self: LicensePlatePrintLine) -> str

"""

 LocationCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LocationCode(self: LicensePlatePrintLine) -> str

Set: LocationCode(self: LicensePlatePrintLine)=value
"""

 NoOfItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: NoOfItems(self: LicensePlatePrintLine) -> int

Set: NoOfItems(self: LicensePlatePrintLine)=value
"""

 Status=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Status(self: LicensePlatePrintLine) -> LicensePlateStatusEnum

Set: Status(self: LicensePlatePrintLine)=value
"""

 StatusAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: StatusAsString(self: LicensePlatePrintLine) -> str

"""

 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WarehouseCode(self: LicensePlatePrintLine) -> str

Set: WarehouseCode(self: LicensePlatePrintLine)=value
"""



class LicensePlatePrintLines:
 """
 LicensePlatePrintLines()
 LicensePlatePrintLines(collection: IEnumerable[LicensePlatePrintLine])
 """
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,collection=None):
  """
  __new__(cls: type)
  __new__(cls: type,collection: IEnumerable[LicensePlatePrintLine])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 IsDisposable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDisposable(self: LicensePlatePrintLines) -> bool

"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreserveState(self: LicensePlatePrintLines) -> bool

"""

 TotalRowsMatched=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TotalRowsMatched(self: LicensePlatePrintLines) -> Int64

Set: TotalRowsMatched(self: LicensePlatePrintLines)=value
"""


 DisplayMember='Description'
 ValueMember='Code'


class PickbatchPrintLine:
 """ PickbatchPrintLine() """
 @staticmethod
 def Create(batch):
  """ Create(batch: Batch) -> PickbatchPrintLine """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: PickbatchPrintLine) -> int """
  pass
 Barcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Barcode(self: PickbatchPrintLine) -> str

Set: Barcode(self: PickbatchPrintLine)=value
"""

 BatchId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BatchId(self: PickbatchPrintLine) -> str

Set: BatchId(self: PickbatchPrintLine)=value
"""

 BatchName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BatchName(self: PickbatchPrintLine) -> str

Set: BatchName(self: PickbatchPrintLine)=value
"""

 CreatedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CreatedBy(self: PickbatchPrintLine) -> str

Set: CreatedBy(self: PickbatchPrintLine)=value
"""

 CreatedOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CreatedOn(self: PickbatchPrintLine) -> DateTime

Set: CreatedOn(self: PickbatchPrintLine)=value
"""

 GroupKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GroupKey(self: PickbatchPrintLine) -> str

"""

 Notes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Notes(self: PickbatchPrintLine) -> str

Set: Notes(self: PickbatchPrintLine)=value
"""

 PickProcessedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PickProcessedBy(self: PickbatchPrintLine) -> str

Set: PickProcessedBy(self: PickbatchPrintLine)=value
"""

 PickProcessedOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PickProcessedOn(self: PickbatchPrintLine) -> DateTime

Set: PickProcessedOn(self: PickbatchPrintLine)=value
"""

 Tags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Tags(self: PickbatchPrintLine) -> str

Set: Tags(self: PickbatchPrintLine)=value
"""



class PickbatchPrintLines:
 """
 PickbatchPrintLines()
 PickbatchPrintLines(collection: IEnumerable[PickbatchPrintLine])
 """
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,collection=None):
  """
  __new__(cls: type)
  __new__(cls: type,collection: IEnumerable[PickbatchPrintLine])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 IsDisposable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDisposable(self: PickbatchPrintLines) -> bool

"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreserveState(self: PickbatchPrintLines) -> bool

"""

 TotalRowsMatched=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TotalRowsMatched(self: PickbatchPrintLines) -> Int64

Set: TotalRowsMatched(self: PickbatchPrintLines)=value
"""


 DisplayMember='BatchName'
 ValueMember='BatchId'


class PrintBaseArgs:
 """
 PrintBaseArgs()
 PrintBaseArgs(printerName: str,options: PrintingOptions)
 """
 @staticmethod
 def __new__(self,printerName=None,options=None):
  """
  __new__(cls: type)
  __new__(cls: type,printerName: str,options: PrintingOptions)
  """
  pass
 Label=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Label(self: PrintBaseArgs) -> str

Set: Label(self: PrintBaseArgs)=value
"""

 PrinterName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PrinterName(self: PrintBaseArgs) -> str

Set: PrinterName(self: PrintBaseArgs)=value
"""

 PrintingOptions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PrintingOptions(self: PrintBaseArgs) -> PrintingOptions

Set: PrintingOptions(self: PrintBaseArgs)=value
"""



class PrintDuplicateLabelArgs:
 """ PrintDuplicateLabelArgs() """
 ShipmentId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ShipmentId(self: PrintDuplicateLabelArgs) -> int

Set: ShipmentId(self: PrintDuplicateLabelArgs)=value
"""



class PrintLabel:
 """ PrintLabel() """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 DatasetTypeFullName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DatasetTypeFullName(self: PrintLabel) -> str

Set: DatasetTypeFullName(self: PrintLabel)=value
"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Description(self: PrintLabel) -> str

Set: Description(self: PrintLabel)=value
"""

 DisplayName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DisplayName(self: PrintLabel) -> str

"""

 FieldRegEx=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FieldRegEx(self: PrintLabel) -> str

Set: FieldRegEx(self: PrintLabel)=value
"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Height(self: PrintLabel) -> int

Set: Height(self: PrintLabel)=value
"""

 ID=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ID(self: PrintLabel) -> int

Set: ID(self: PrintLabel)=value
"""

 Image=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Image(self: PrintLabel) -> Array[Byte]

Set: Image(self: PrintLabel)=value
"""

 IsActive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsActive(self: PrintLabel) -> bool

Set: IsActive(self: PrintLabel)=value
"""

 Mappings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Mappings(self: PrintLabel) -> Mappings[str,str,str]

Set: Mappings(self: PrintLabel)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: PrintLabel) -> str

Set: Name(self: PrintLabel)=value
"""

 OneLabelPerPrintAction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OneLabelPerPrintAction(self: PrintLabel) -> bool

Set: OneLabelPerPrintAction(self: PrintLabel)=value
"""

 PrinterCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PrinterCode(self: PrintLabel) -> str

Set: PrinterCode(self: PrintLabel)=value
"""

 SingleLabelDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SingleLabelDescription(self: PrintLabel) -> str

Set: SingleLabelDescription(self: PrintLabel)=value
"""

 Sys=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Sys(self: PrintLabel) -> bool

Set: Sys(self: PrintLabel)=value
"""



class PrintLabelArgs:
 """ PrintLabelArgs() """
 PrintLabels=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PrintLabels(self: PrintLabelArgs) -> bool

Set: PrintLabels(self: PrintLabelArgs)=value
"""

 SelectedLabel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SelectedLabel(self: PrintLabelArgs) -> PrintLabel

Set: SelectedLabel(self: PrintLabelArgs)=value
"""



class PrintLabelItemProperties:
 """ PrintLabelItemProperties() """
 EndElement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: EndElement(self: PrintLabelItemProperties) -> Match

Set: EndElement(self: PrintLabelItemProperties)=value
"""

 EndPosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: EndPosition(self: PrintLabelItemProperties) -> int

Set: EndPosition(self: PrintLabelItemProperties)=value
"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Height(self: PrintLabelItemProperties) -> int

"""

 StartElement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: StartElement(self: PrintLabelItemProperties) -> Match

Set: StartElement(self: PrintLabelItemProperties)=value
"""

 StartPosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: StartPosition(self: PrintLabelItemProperties) -> int

Set: StartPosition(self: PrintLabelItemProperties)=value
"""



class PrintLabelMapping:
 """
 PrintLabelMapping(placeholder: str,datasetField: str,transformation: str)
 PrintLabelMapping()
 """
 @staticmethod
 def __new__(self,placeholder=None,datasetField=None,transformation=None):
  """
  __new__(cls: type,placeholder: str,datasetField: str,transformation: str)
  __new__(cls: type)
  """
  pass
 DatasetField=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DatasetField(self: PrintLabelMapping) -> str

Set: DatasetField(self: PrintLabelMapping)=value
"""

 Placeholder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Placeholder(self: PrintLabelMapping) -> str

Set: Placeholder(self: PrintLabelMapping)=value
"""

 Transformation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Transformation(self: PrintLabelMapping) -> str

Set: Transformation(self: PrintLabelMapping)=value
"""



class PrintLabelMappings:
 """ PrintLabelMappings() """
 @staticmethod
 def ConstructFrom(mappings):
  """ ConstructFrom(mappings: Mappings[str,str,str]) -> PrintLabelMappings """
  pass
 def ConvertTo(self,mappings=None):
  """
  ConvertTo(self: PrintLabelMappings) -> Mappings[str,str,str]
  ConvertTo(mappings: PrintLabelMappings) -> Mappings[str,str,str]
  """
  pass
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
 DisplayMember='DatasetField'
 ValueMember='Placeholder'


class PrintLabels:
 """ PrintLabels() """
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
 DisplayMember='DisplayName'
 ValueMember='ID'


class PrintPackageSlipArgs:
 """ PrintPackageSlipArgs() """
 ShipmentId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ShipmentId(self: PrintPackageSlipArgs) -> int

Set: ShipmentId(self: PrintPackageSlipArgs)=value
"""



class PrintPickbatchLabelArgs:
 """ PrintPickbatchLabelArgs() """
 BatchIds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BatchIds(self: PrintPickbatchLabelArgs) -> List[Guid]

Set: BatchIds(self: PrintPickbatchLabelArgs)=value
"""

 PrintLabel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PrintLabel(self: PrintPickbatchLabelArgs) -> PrintLabel

Set: PrintLabel(self: PrintPickbatchLabelArgs)=value
"""



class PrintPickingListArgs:
 """ PrintPickingListArgs() """
 BatchIds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BatchIds(self: PrintPickingListArgs) -> List[Guid]

Set: BatchIds(self: PrintPickingListArgs)=value
"""

 Report=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Report(self: PrintPickingListArgs) -> ReportItem

Set: Report(self: PrintPickingListArgs)=value
"""



class PrintShipmentDocumentArgs:
 """ PrintShipmentDocumentArgs() """
 ShipmentId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ShipmentId(self: PrintShipmentDocumentArgs) -> int

Set: ShipmentId(self: PrintShipmentDocumentArgs)=value
"""



class PrintSSCCLabelsArgs:
 """ PrintSSCCLabelsArgs() """
 CacheKeyOfTransportPackages=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CacheKeyOfTransportPackages(self: PrintSSCCLabelsArgs) -> CacheKey

Set: CacheKeyOfTransportPackages(self: PrintSSCCLabelsArgs)=value
"""

 LabelHomogeneousPallet=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LabelHomogeneousPallet(self: PrintSSCCLabelsArgs) -> str

Set: LabelHomogeneousPallet(self: PrintSSCCLabelsArgs)=value
"""

 LabelMixedPallet=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LabelMixedPallet(self: PrintSSCCLabelsArgs) -> str

Set: LabelMixedPallet(self: PrintSSCCLabelsArgs)=value
"""

 SelectedPackageId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SelectedPackageId(self: PrintSSCCLabelsArgs) -> Guid

Set: SelectedPackageId(self: PrintSSCCLabelsArgs)=value
"""



class PurchaseOrderPrintLine:
 """ PurchaseOrderPrintLine() """
 CurrentBarcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CurrentBarcode(self: PurchaseOrderPrintLine) -> str

Set: CurrentBarcode(self: PurchaseOrderPrintLine)=value
"""

 CurrentSupplierCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CurrentSupplierCode(self: PurchaseOrderPrintLine) -> str

Set: CurrentSupplierCode(self: PurchaseOrderPrintLine)=value
"""

 InboundLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: InboundLocation(self: PurchaseOrderPrintLine) -> str

Set: InboundLocation(self: PurchaseOrderPrintLine)=value
"""

 YourReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: YourReference(self: PurchaseOrderPrintLine) -> str

Set: YourReference(self: PurchaseOrderPrintLine)=value
"""



class PurchaseOrderPrintLines:
 """
 PurchaseOrderPrintLines()
 PurchaseOrderPrintLines(collection: IEnumerable[PurchaseOrderPrintLine])
 """
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,collection=None):
  """
  __new__(cls: type)
  __new__(cls: type,collection: IEnumerable[PurchaseOrderPrintLine])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 IsDisposable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDisposable(self: PurchaseOrderPrintLines) -> bool

"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreserveState(self: PurchaseOrderPrintLines) -> bool

"""

 TotalRowsMatched=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TotalRowsMatched(self: PurchaseOrderPrintLines) -> Int64

Set: TotalRowsMatched(self: PurchaseOrderPrintLines)=value
"""


 DisplayMember='ItemDescription'
 ValueMember='ItemCode'


class ReportItem:
 """ ReportItem() """
 DataSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DataSource(self: ReportItem) -> str

Set: DataSource(self: ReportItem)=value
"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Description(self: ReportItem) -> str

Set: Description(self: ReportItem)=value
"""

 FileName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FileName(self: ReportItem) -> str

Set: FileName(self: ReportItem)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: ReportItem) -> str

Set: Name(self: ReportItem)=value
"""



class ReportItems:
 """ ReportItems() """
 @staticmethod
 def FromIEnumerable(list):
  """ FromIEnumerable(list: IEnumerable[ReportItem]) -> ReportItems """
  pass
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
 DisplayMember='Description'
 ValueMember='Name'


class RmaOrderPrintLine:
 """ RmaOrderPrintLine() """
 def GetHashCode(self):
  """ GetHashCode(self: RmaOrderPrintLine) -> int """
  pass
 Reason=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Reason(self: RmaOrderPrintLine) -> str

Set: Reason(self: RmaOrderPrintLine)=value
"""



class RmaOrderPrintLines:
 """ RmaOrderPrintLines() """
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
 IsDisposable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDisposable(self: RmaOrderPrintLines) -> bool

"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreserveState(self: RmaOrderPrintLines) -> bool

"""


 DisplayMember='ItemDescription'


class SSCCBasePrintLine:
 """ SSCCBasePrintLine(barcode: str,barcodeReadable: str) """
 def GetHashCode(self):
  """ GetHashCode(self: SSCCBasePrintLine) -> int """
  pass
 @staticmethod
 def __new__(self,barcode,barcodeReadable):
  """ __new__(cls: type,barcode: str,barcodeReadable: str) """
  pass
 Barcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Barcode(self: SSCCBasePrintLine) -> str

Set: Barcode(self: SSCCBasePrintLine)=value
"""

 BarcodeReadable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BarcodeReadable(self: SSCCBasePrintLine) -> str

Set: BarcodeReadable(self: SSCCBasePrintLine)=value
"""

 GroupKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GroupKey(self: SSCCBasePrintLine) -> str

"""



class SSCCBasePrintLines:
 """
 SSCCBasePrintLines()
 SSCCBasePrintLines(collection: IEnumerable[SSCCBasePrintLine])
 """
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,collection=None):
  """
  __new__(cls: type)
  __new__(cls: type,collection: IEnumerable[SSCCBasePrintLine])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 IsDisposable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDisposable(self: SSCCBasePrintLines) -> bool

"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreserveState(self: SSCCBasePrintLines) -> bool

"""

 TotalRowsMatched=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TotalRowsMatched(self: SSCCBasePrintLines) -> Int64

Set: TotalRowsMatched(self: SSCCBasePrintLines)=value
"""


 DisplayMember=None
 ValueMember=None


class SSCCHeterogeneousPrintLine:
 """
 SSCCHeterogeneousPrintLine(barcode: str,barcodeReadable: str)
 SSCCHeterogeneousPrintLine(barcode: str,barcodeReadable: str,packages: TransportPackages)
 """
 def GetHashCode(self):
  """ GetHashCode(self: SSCCHeterogeneousPrintLine) -> int """
  pass
 @staticmethod
 def __new__(self,barcode,barcodeReadable,packages=None):
  """
  __new__(cls: type,barcode: str,barcodeReadable: str)
  __new__(cls: type,barcode: str,barcodeReadable: str,packages: TransportPackages)
  """
  pass
 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Description(self: SSCCHeterogeneousPrintLine) -> str

Set: Description(self: SSCCHeterogeneousPrintLine)=value
"""

 FromAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FromAddress(self: SSCCHeterogeneousPrintLine) -> str

Set: FromAddress(self: SSCCHeterogeneousPrintLine)=value
"""

 FromCity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FromCity(self: SSCCHeterogeneousPrintLine) -> str

Set: FromCity(self: SSCCHeterogeneousPrintLine)=value
"""

 FromCountry=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FromCountry(self: SSCCHeterogeneousPrintLine) -> str

Set: FromCountry(self: SSCCHeterogeneousPrintLine)=value
"""

 FromName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FromName(self: SSCCHeterogeneousPrintLine) -> str

Set: FromName(self: SSCCHeterogeneousPrintLine)=value
"""

 FromZipCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FromZipCode(self: SSCCHeterogeneousPrintLine) -> str

Set: FromZipCode(self: SSCCHeterogeneousPrintLine)=value
"""

 GroupKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GroupKey(self: SSCCHeterogeneousPrintLine) -> str

"""

 PackageNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PackageNumber(self: SSCCHeterogeneousPrintLine) -> int

Set: PackageNumber(self: SSCCHeterogeneousPrintLine)=value
"""

 ToAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ToAddress(self: SSCCHeterogeneousPrintLine) -> str

Set: ToAddress(self: SSCCHeterogeneousPrintLine)=value
"""

 ToCity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ToCity(self: SSCCHeterogeneousPrintLine) -> str

Set: ToCity(self: SSCCHeterogeneousPrintLine)=value
"""

 ToCountry=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ToCountry(self: SSCCHeterogeneousPrintLine) -> str

Set: ToCountry(self: SSCCHeterogeneousPrintLine)=value
"""

 ToName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ToName(self: SSCCHeterogeneousPrintLine) -> str

Set: ToName(self: SSCCHeterogeneousPrintLine)=value
"""

 TotalAmountOfPackages=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TotalAmountOfPackages(self: SSCCHeterogeneousPrintLine) -> int

Set: TotalAmountOfPackages(self: SSCCHeterogeneousPrintLine)=value
"""

 ToZipCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ToZipCode(self: SSCCHeterogeneousPrintLine) -> str

Set: ToZipCode(self: SSCCHeterogeneousPrintLine)=value
"""



class SSCCHeterogeneousPrintLines:
 """
 SSCCHeterogeneousPrintLines()
 SSCCHeterogeneousPrintLines(collection: IEnumerable[SSCCHeterogeneousPrintLine])
 """
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,collection=None):
  """
  __new__(cls: type)
  __new__(cls: type,collection: IEnumerable[SSCCHeterogeneousPrintLine])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 IsDisposable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDisposable(self: SSCCHeterogeneousPrintLines) -> bool

"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreserveState(self: SSCCHeterogeneousPrintLines) -> bool

"""

 TotalRowsMatched=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TotalRowsMatched(self: SSCCHeterogeneousPrintLines) -> Int64

Set: TotalRowsMatched(self: SSCCHeterogeneousPrintLines)=value
"""


 DisplayMember=None
 ValueMember=None


class SSCCHomogeneousPrintLine:
 """
 SSCCHomogeneousPrintLine(barcode: str,barcodeReadable: str)
 SSCCHomogeneousPrintLine(barcode: str,barcodeReadable: str,packages: TransportPackages)
 """
 def GetHashCode(self):
  """ GetHashCode(self: SSCCHomogeneousPrintLine) -> int """
  pass
 @staticmethod
 def __new__(self,barcode,barcodeReadable,packages=None):
  """
  __new__(cls: type,barcode: str,barcodeReadable: str)
  __new__(cls: type,barcode: str,barcodeReadable: str,packages: TransportPackages)
  """
  pass
 Batch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Batch(self: SSCCHomogeneousPrintLine) -> str

Set: Batch(self: SSCCHomogeneousPrintLine)=value
"""

 ExpiryDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExpiryDate(self: SSCCHomogeneousPrintLine) -> DateTime

Set: ExpiryDate(self: SSCCHomogeneousPrintLine)=value
"""

 GTIN=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GTIN(self: SSCCHomogeneousPrintLine) -> str

Set: GTIN(self: SSCCHomogeneousPrintLine)=value
"""

 ItemWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemWeight(self: SSCCHomogeneousPrintLine) -> Decimal

Set: ItemWeight(self: SSCCHomogeneousPrintLine)=value
"""

 Serial=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Serial(self: SSCCHomogeneousPrintLine) -> str

Set: Serial(self: SSCCHomogeneousPrintLine)=value
"""

 UnitCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UnitCount(self: SSCCHomogeneousPrintLine) -> int

Set: UnitCount(self: SSCCHomogeneousPrintLine)=value
"""



class SSCCHomogeneousPrintLines:
 """
 SSCCHomogeneousPrintLines()
 SSCCHomogeneousPrintLines(collection: IEnumerable[SSCCHomogeneousPrintLine])
 """
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,collection=None):
  """
  __new__(cls: type)
  __new__(cls: type,collection: IEnumerable[SSCCHomogeneousPrintLine])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 IsDisposable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDisposable(self: SSCCHomogeneousPrintLines) -> bool

"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreserveState(self: SSCCHomogeneousPrintLines) -> bool

"""

 TotalRowsMatched=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TotalRowsMatched(self: SSCCHomogeneousPrintLines) -> Int64

Set: TotalRowsMatched(self: SSCCHomogeneousPrintLines)=value
"""


 DisplayMember=None
 ValueMember=None


class TransportPackageItemPrintLine:
 """ TransportPackageItemPrintLine() """
 Barcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Barcode(self: TransportPackageItemPrintLine) -> str

Set: Barcode(self: TransportPackageItemPrintLine)=value
"""

 GroupKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GroupKey(self: TransportPackageItemPrintLine) -> str

"""

 GTINCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GTINCode(self: TransportPackageItemPrintLine) -> str

Set: GTINCode(self: TransportPackageItemPrintLine)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemCode(self: TransportPackageItemPrintLine) -> str

Set: ItemCode(self: TransportPackageItemPrintLine)=value
"""

 ItemDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemDescription(self: TransportPackageItemPrintLine) -> str

Set: ItemDescription(self: TransportPackageItemPrintLine)=value
"""

 ItemQuantity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemQuantity(self: TransportPackageItemPrintLine) -> Decimal

Set: ItemQuantity(self: TransportPackageItemPrintLine)=value
"""

 UnitCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UnitCode(self: TransportPackageItemPrintLine) -> str

Set: UnitCode(self: TransportPackageItemPrintLine)=value
"""



class TransportPackageItemsPrintLine:
 """
 TransportPackageItemsPrintLine()
 TransportPackageItemsPrintLine(collection: IEnumerable[TransportPackageItemPrintLine])
 """
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,collection=None):
  """
  __new__(cls: type)
  __new__(cls: type,collection: IEnumerable[TransportPackageItemPrintLine])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 IsDisposable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDisposable(self: TransportPackageItemsPrintLine) -> bool

"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreserveState(self: TransportPackageItemsPrintLine) -> bool

"""

 TotalRowsMatched=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TotalRowsMatched(self: TransportPackageItemsPrintLine) -> Int64

Set: TotalRowsMatched(self: TransportPackageItemsPrintLine)=value
"""


 DisplayMember='ItemCode'
 ValueMember='GroupKey'


class TransportPackagePrintLine:
 """ TransportPackagePrintLine() """
 @staticmethod
 def Create(transportPackage):
  """ Create(transportPackage: TransportPackage) -> TransportPackagePrintLine """
  pass
 CustomerDeliveryAddresLine1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerDeliveryAddresLine1(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryAddresLine1(self: TransportPackagePrintLine)=value
"""

 CustomerDeliveryAddresLine2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerDeliveryAddresLine2(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryAddresLine2(self: TransportPackagePrintLine)=value
"""

 CustomerDeliveryAddresLine3=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerDeliveryAddresLine3(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryAddresLine3(self: TransportPackagePrintLine)=value
"""

 CustomerDeliveryCity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerDeliveryCity(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryCity(self: TransportPackagePrintLine)=value
"""

 CustomerDeliveryCountryCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerDeliveryCountryCode(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryCountryCode(self: TransportPackagePrintLine)=value
"""

 CustomerDeliveryCountryName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerDeliveryCountryName(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryCountryName(self: TransportPackagePrintLine)=value
"""

 CustomerDeliveryEmail=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerDeliveryEmail(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryEmail(self: TransportPackagePrintLine)=value
"""

 CustomerDeliveryName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerDeliveryName(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryName(self: TransportPackagePrintLine)=value
"""

 CustomerDeliveryName2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerDeliveryName2(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryName2(self: TransportPackagePrintLine)=value
"""

 CustomerDeliveryPhoneNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerDeliveryPhoneNumber(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryPhoneNumber(self: TransportPackagePrintLine)=value
"""

 CustomerDeliveryStateCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerDeliveryStateCode(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryStateCode(self: TransportPackagePrintLine)=value
"""

 CustomerDeliveryZipCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerDeliveryZipCode(self: TransportPackagePrintLine) -> str

Set: CustomerDeliveryZipCode(self: TransportPackagePrintLine)=value
"""

 CustomerInvoiceAddresLine1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerInvoiceAddresLine1(self: TransportPackagePrintLine) -> str

Set: CustomerInvoiceAddresLine1(self: TransportPackagePrintLine)=value
"""

 CustomerInvoiceAddresLine2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerInvoiceAddresLine2(self: TransportPackagePrintLine) -> str

Set: CustomerInvoiceAddresLine2(self: TransportPackagePrintLine)=value
"""

 CustomerInvoiceAddresLine3=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerInvoiceAddresLine3(self: TransportPackagePrintLine) -> str

Set: CustomerInvoiceAddresLine3(self: TransportPackagePrintLine)=value
"""

 CustomerInvoiceCity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerInvoiceCity(self: TransportPackagePrintLine) -> str

Set: CustomerInvoiceCity(self: TransportPackagePrintLine)=value
"""

 CustomerInvoiceCountryCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerInvoiceCountryCode(self: TransportPackagePrintLine) -> str

Set: CustomerInvoiceCountryCode(self: TransportPackagePrintLine)=value
"""

 CustomerInvoiceCountryName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerInvoiceCountryName(self: TransportPackagePrintLine) -> str

Set: CustomerInvoiceCountryName(self: TransportPackagePrintLine)=value
"""

 CustomerInvoiceEmail=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerInvoiceEmail(self: TransportPackagePrintLine) -> str

Set: CustomerInvoiceEmail(self: TransportPackagePrintLine)=value
"""

 CustomerInvoiceName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerInvoiceName(self: TransportPackagePrintLine) -> str

Set: CustomerInvoiceName(self: TransportPackagePrintLine)=value
"""

 CustomerInvoiceName2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerInvoiceName2(self: TransportPackagePrintLine) -> str

Set: CustomerInvoiceName2(self: TransportPackagePrintLine)=value
"""

 CustomerInvoicePhoneNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerInvoicePhoneNumber(self: TransportPackagePrintLine) -> str

Set: CustomerInvoicePhoneNumber(self: TransportPackagePrintLine)=value
"""

 CustomerInvoiceStateCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerInvoiceStateCode(self: TransportPackagePrintLine) -> str

Set: CustomerInvoiceStateCode(self: TransportPackagePrintLine)=value
"""

 CustomerInvoiceZipCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerInvoiceZipCode(self: TransportPackagePrintLine) -> str

Set: CustomerInvoiceZipCode(self: TransportPackagePrintLine)=value
"""

 CustomerReferences=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerReferences(self: TransportPackagePrintLine) -> str

Set: CustomerReferences(self: TransportPackagePrintLine)=value
"""

 GroupKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GroupKey(self: TransportPackagePrintLine) -> str

"""

 ItemBarcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemBarcode(self: TransportPackagePrintLine) -> str

"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemCode(self: TransportPackagePrintLine) -> str

"""

 ItemDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemDescription(self: TransportPackagePrintLine) -> str

"""

 OurReferences=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OurReferences(self: TransportPackagePrintLine) -> str

Set: OurReferences(self: TransportPackagePrintLine)=value
"""

 PackageBarcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PackageBarcode(self: TransportPackagePrintLine) -> str

Set: PackageBarcode(self: TransportPackagePrintLine)=value
"""

 PackageDimensions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PackageDimensions(self: TransportPackagePrintLine) -> str

Set: PackageDimensions(self: TransportPackagePrintLine)=value
"""

 PackageGuid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PackageGuid(self: TransportPackagePrintLine) -> str

Set: PackageGuid(self: TransportPackagePrintLine)=value
"""

 PackageIdentification=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PackageIdentification(self: TransportPackagePrintLine) -> str

Set: PackageIdentification(self: TransportPackagePrintLine)=value
"""

 PackageItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PackageItemCode(self: TransportPackagePrintLine) -> str

Set: PackageItemCode(self: TransportPackagePrintLine)=value
"""

 PackageNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PackageNumber(self: TransportPackagePrintLine) -> str

Set: PackageNumber(self: TransportPackagePrintLine)=value
"""

 PackageType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PackageType(self: TransportPackagePrintLine) -> str

Set: PackageType(self: TransportPackagePrintLine)=value
"""

 PackageWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PackageWeight(self: TransportPackagePrintLine) -> str

Set: PackageWeight(self: TransportPackagePrintLine)=value
"""

 SenderAddresLine1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SenderAddresLine1(self: TransportPackagePrintLine) -> str

Set: SenderAddresLine1(self: TransportPackagePrintLine)=value
"""

 SenderAddresLine2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SenderAddresLine2(self: TransportPackagePrintLine) -> str

Set: SenderAddresLine2(self: TransportPackagePrintLine)=value
"""

 SenderAddresLine3=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SenderAddresLine3(self: TransportPackagePrintLine) -> str

Set: SenderAddresLine3(self: TransportPackagePrintLine)=value
"""

 SenderCity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SenderCity(self: TransportPackagePrintLine) -> str

Set: SenderCity(self: TransportPackagePrintLine)=value
"""

 SenderCountryCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SenderCountryCode(self: TransportPackagePrintLine) -> str

Set: SenderCountryCode(self: TransportPackagePrintLine)=value
"""

 SenderCountryName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SenderCountryName(self: TransportPackagePrintLine) -> str

Set: SenderCountryName(self: TransportPackagePrintLine)=value
"""

 SenderEmail=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SenderEmail(self: TransportPackagePrintLine) -> str

Set: SenderEmail(self: TransportPackagePrintLine)=value
"""

 SenderName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SenderName(self: TransportPackagePrintLine) -> str

Set: SenderName(self: TransportPackagePrintLine)=value
"""

 SenderPhoneNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SenderPhoneNumber(self: TransportPackagePrintLine) -> str

Set: SenderPhoneNumber(self: TransportPackagePrintLine)=value
"""

 SenderStateCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SenderStateCode(self: TransportPackagePrintLine) -> str

Set: SenderStateCode(self: TransportPackagePrintLine)=value
"""

 SenderZipCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SenderZipCode(self: TransportPackagePrintLine) -> str

Set: SenderZipCode(self: TransportPackagePrintLine)=value
"""

 UnitCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UnitCode(self: TransportPackagePrintLine) -> str

"""



class TransportPackagePrintLines:
 """
 TransportPackagePrintLines()
 TransportPackagePrintLines(collection: IEnumerable[TransportPackagePrintLine])
 """
 @staticmethod
 def Create(transportPackages):
  """ Create(transportPackages: TransportPackages) -> TransportPackagePrintLines """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,collection=None):
  """
  __new__(cls: type)
  __new__(cls: type,collection: IEnumerable[TransportPackagePrintLine])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 IsDisposable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDisposable(self: TransportPackagePrintLines) -> bool

"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreserveState(self: TransportPackagePrintLines) -> bool

"""

 TotalRowsMatched=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TotalRowsMatched(self: TransportPackagePrintLines) -> Int64

Set: TotalRowsMatched(self: TransportPackagePrintLines)=value
"""


 DisplayMember='PackageNumber'
 ValueMember='PackageGuid'


# variables with complex values

