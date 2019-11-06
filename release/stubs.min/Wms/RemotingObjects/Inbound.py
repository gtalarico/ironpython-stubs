# encoding: utf-8
# module Wms.RemotingObjects.Inbound calls itself Inbound
# from Wms.RemotingObjects,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class PreReceipt(DbObject):
 """ PreReceipt() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PreReceipt()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 Date=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Date(self: PreReceipt) -> DateTime

Set: Date(self: PreReceipt)=value
"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Description(self: PreReceipt) -> str

Set: Description(self: PreReceipt)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Id(self: PreReceipt) -> int

Set: Id(self: PreReceipt)=value
"""

 Notes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Notes(self: PreReceipt) -> str

Set: Notes(self: PreReceipt)=value
"""

 NumberOfCollo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: NumberOfCollo(self: PreReceipt) -> int

Set: NumberOfCollo(self: PreReceipt)=value
"""

 PendingOrderCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PendingOrderCount(self: PreReceipt) -> int

Set: PendingOrderCount(self: PreReceipt)=value
"""

 PercentageReceived=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Percentage of Prereceipt products (quantity) that is delivered (0-100).
   Excluded the amount that was over delivered (more delivered than expected).

Get: PercentageReceived(self: PreReceipt) -> int

"""

 Status=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Status(self: PreReceipt) -> PreReceiptStatus

Set: Status(self: PreReceipt)=value
"""

 Tags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Tags(self: PreReceipt) -> str

Set: Tags(self: PreReceipt)=value
"""

 TotalOrderLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: TotalOrderLines(self: PreReceipt) -> int

Set: TotalOrderLines(self: PreReceipt)=value
"""

 TotalOrderLinesReceived=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Amount of lines that are already received/completed

Get: TotalOrderLinesReceived(self: PreReceipt) -> int

Set: TotalOrderLinesReceived(self: PreReceipt)=value
"""

 TotalOrderLinesToReceive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Amount of lines where quantityReceived reach quantity expected

Get: TotalOrderLinesToReceive(self: PreReceipt) -> int

Set: TotalOrderLinesToReceive(self: PreReceipt)=value
"""

 TotalQuantity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Total quantity expecting to receive (QuantityToReceive).

Get: TotalQuantity(self: PreReceipt) -> Decimal

Set: TotalQuantity(self: PreReceipt)=value
"""

 TotalQuantityReceived=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Total amount of Quantity received
   Excluded the amount that was received per line more than expected (see query)

Get: TotalQuantityReceived(self: PreReceipt) -> Decimal

Set: TotalQuantityReceived(self: PreReceipt)=value
"""



class CreatePreReceiptArgs(PreReceipt):
 """ CreatePreReceiptArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return CreatePreReceiptArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 Lines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Lines(self: CreatePreReceiptArgs) -> List[PreReceiptLine]

Set: Lines(self: CreatePreReceiptArgs)=value
"""

 OrderIds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderIds(self: CreatePreReceiptArgs) -> List[int]

Set: OrderIds(self: CreatePreReceiptArgs)=value
"""

 OrderLineIds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderLineIds(self: CreatePreReceiptArgs) -> List[int]

Set: OrderLineIds(self: CreatePreReceiptArgs)=value
"""

 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: WarehouseCode(self: CreatePreReceiptArgs) -> str

Set: WarehouseCode(self: CreatePreReceiptArgs)=value
"""



class ErpInboundLocationMode:
 """ enum ErpInboundLocationMode,values: DefaultItemLocation (1),DefaultWarehouseLocation (0) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ErpInboundLocationMode()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
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
 DefaultItemLocation=None
 DefaultWarehouseLocation=None
 value__=None


class ErpProcessInboundOrderResult(ErpProcessPurchaseOrderLinesResult):
 """ ErpProcessInboundOrderResult() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ErpProcessInboundOrderResult()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 CreatedOrder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CreatedOrder(self: ErpProcessInboundOrderResult) -> InboundOrder

Set: CreatedOrder(self: ErpProcessInboundOrderResult)=value
"""

 HasOrder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: HasOrder(self: ErpProcessInboundOrderResult) -> bool

"""



class InboundOrder(DbObject):
 """ InboundOrder() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return InboundOrder()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetHashCode(self):
  """ GetHashCode(self: InboundOrder) -> int """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 BusinessUnit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: BusinessUnit(self: InboundOrder) -> str

Set: BusinessUnit(self: InboundOrder)=value
"""

 DateFirstExpected=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DateFirstExpected(self: InboundOrder) -> DateTime

Set: DateFirstExpected(self: InboundOrder)=value
"""

 DateOrdered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DateOrdered(self: InboundOrder) -> DateTime

Set: DateOrdered(self: InboundOrder)=value
"""

 DeliveryMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DeliveryMethod(self: InboundOrder) -> str

Set: DeliveryMethod(self: InboundOrder)=value
"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Description(self: InboundOrder) -> str

Set: Description(self: InboundOrder)=value
"""

 GroupKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: GroupKey(self: InboundOrder) -> int

Set: GroupKey(self: InboundOrder)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Id(self: InboundOrder) -> int

Set: Id(self: InboundOrder)=value
"""

 Notes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property can be used to store notes of a PurchaseOrder.

Get: Notes(self: InboundOrder) -> str

Set: Notes(self: InboundOrder)=value
"""

 Number=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Number(self: InboundOrder) -> str

Set: Number(self: InboundOrder)=value
"""

 PendingOrderLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates how many order lines are pending.

Get: PendingOrderLines(self: InboundOrder) -> int

Set: PendingOrderLines(self: InboundOrder)=value
"""

 ProjectCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ProjectCode(self: InboundOrder) -> str

Set: ProjectCode(self: InboundOrder)=value
"""

 ProjectName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ProjectName(self: InboundOrder) -> str

Set: ProjectName(self: InboundOrder)=value
"""

 SelectionCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: SelectionCode(self: InboundOrder) -> str

Set: SelectionCode(self: InboundOrder)=value
"""

 SelectionCodeDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: SelectionCodeDescription(self: InboundOrder) -> str

Set: SelectionCodeDescription(self: InboundOrder)=value
"""

 Warehouse=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Warehouse(self: InboundOrder) -> str

Set: Warehouse(self: InboundOrder)=value
"""



class InboundOrderLine(object):
 """ InboundOrderLine() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return InboundOrderLine()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def AddReceiving(self,*__args):
  """
  AddReceiving(self: InboundOrderLine,quantity: Decimal) -> bool
  AddReceiving(self: InboundOrderLine,itemId: ItemIdentification) -> bool
  """
  pass
 def Clone(self):
  """ Clone(self: InboundOrderLine) -> object """
  pass
 @staticmethod
 def FromItem(item,itemDefaultLocation):
  """ FromItem(item: Item,itemDefaultLocation: str) -> InboundOrderLine """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: InboundOrderLine) -> int """
  pass
 def IsBatchNumberItemCheck(self,checkRegistration):
  """
  IsBatchNumberItemCheck(self: InboundOrderLine,checkRegistration: bool) -> bool
  
   Checks if the item is a batchnumber item.
  
   checkRegistration: True if the batchnumber registration should be checked,false if just the property should be returned.
   Returns: True if the check is ignored and the item is a batch item,or when the itemid registration is set to
     complete (means the numers are registered throughout the 
    whole process).
     False if the check is ignored and the item is not a batch item,or when the itemids are registered
     during delivery only.
  """
  pass
 def IsSerialNumberItemCheck(self,checkRegistration):
  """
  IsSerialNumberItemCheck(self: InboundOrderLine,checkRegistration: bool) -> bool
  
   Checks if the item is a serialnumber item.
  
   checkRegistration: True if the serialnumber registration should be checked,false if just the property should be returned.
   Returns: True if the check is ignored and the item is a serial item,or when the itemid registration is set to
     complete (means the numers are registered throughout the 
    whole process).
     False if the check is ignored and the item is not a serial item,or when the itemids are registered
     during delivery only.
  """
  pass
 def PutBack(self,*__args):
  """
  PutBack(self: InboundOrderLine,quantity: Decimal) -> Decimal
  
   quantity: Positive quantity to put back
   Returns: the amount that is put back. (positive)
  PutBack(self: InboundOrderLine,itemId: ItemIdentification) -> Decimal
   Returns: the amount that is put back. (positive)
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 CustomErpFields=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Can be used for none standard data input towards Erp (while processing) - Profit rma order only at this moment 
   Expected key: Erp field property name,e.g: "V1Cd" (Profit cost center field)
   Expected value: Erp field property value (NOTE: use same Type as eventual Erp Type to avoid conversion errors)

Get: CustomErpFields(self: InboundOrderLine) -> SerializableDictionary[str,object]

Set: CustomErpFields(self: InboundOrderLine)=value
"""

 CustomFields=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomFields(self: InboundOrderLine) -> SerializableDictionary[str,object]

Set: CustomFields(self: InboundOrderLine)=value
"""

 DateExpected=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DateExpected(self: InboundOrderLine) -> DateTime

Set: DateExpected(self: InboundOrderLine)=value
"""

 DefaultVendorBarcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DefaultVendorBarcode(self: InboundOrderLine) -> str

Set: DefaultVendorBarcode(self: InboundOrderLine)=value
"""

 DefaultVendorItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DefaultVendorItemCode(self: InboundOrderLine) -> str

Set: DefaultVendorItemCode(self: InboundOrderLine)=value
"""

 GTINCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The GS1 GTIN code of this item

Get: GTINCode(self: InboundOrderLine) -> str

Set: GTINCode(self: InboundOrderLine)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Id(self: InboundOrderLine) -> int

Set: Id(self: InboundOrderLine)=value
"""

 IsBatchNumberItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IsBatchNumberItem(self: InboundOrderLine) -> bool

Set: IsBatchNumberItem(self: InboundOrderLine)=value
"""

 IsFractionAllowed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IsFractionAllowed(self: InboundOrderLine) -> bool

Set: IsFractionAllowed(self: InboundOrderLine)=value
"""

 IsProcessed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IsProcessed(self: InboundOrderLine) -> bool

Set: IsProcessed(self: InboundOrderLine)=value
"""

 IsSerialNumberItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IsSerialNumberItem(self: InboundOrderLine) -> bool

Set: IsSerialNumberItem(self: InboundOrderLine)=value
"""

 ItemBrand=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemBrand(self: InboundOrderLine) -> str

Set: ItemBrand(self: InboundOrderLine)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemCode(self: InboundOrderLine) -> str

Set: ItemCode(self: InboundOrderLine)=value
"""

 ItemDefaultLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemDefaultLocation(self: InboundOrderLine) -> str

Set: ItemDefaultLocation(self: InboundOrderLine)=value
"""

 ItemDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemDescription(self: InboundOrderLine) -> str

Set: ItemDescription(self: InboundOrderLine)=value
"""

 ItemIdRegistration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemIdRegistration(self: InboundOrderLine) -> ItemIdentificationRegistration

Set: ItemIdRegistration(self: InboundOrderLine)=value
"""

 ItemIds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemIds(self: InboundOrderLine) -> ItemIdentifications

Set: ItemIds(self: InboundOrderLine)=value
"""

 ItemWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemWeight(self: InboundOrderLine) -> Decimal

Set: ItemWeight(self: InboundOrderLine)=value
"""

 LineCurrencyCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: LineCurrencyCode(self: InboundOrderLine) -> str

Set: LineCurrencyCode(self: InboundOrderLine)=value
"""

 LineDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: LineDescription(self: InboundOrderLine) -> str

Set: LineDescription(self: InboundOrderLine)=value
"""

 LineInstruction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: LineInstruction(self: InboundOrderLine) -> str

Set: LineInstruction(self: InboundOrderLine)=value
"""

 LineNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: LineNumber(self: InboundOrderLine) -> int

Set: LineNumber(self: InboundOrderLine)=value
"""

 OrderId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderId(self: InboundOrderLine) -> int

Set: OrderId(self: InboundOrderLine)=value
"""

 OrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderNumber(self: InboundOrderLine) -> str

Set: OrderNumber(self: InboundOrderLine)=value
"""

 QuantityOrdered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: QuantityOrdered(self: InboundOrderLine) -> Decimal

Set: QuantityOrdered(self: InboundOrderLine)=value
"""

 QuantityReceived=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: QuantityReceived(self: InboundOrderLine) -> Decimal

Set: QuantityReceived(self: InboundOrderLine)=value
"""

 QuantityToReceive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: QuantityToReceive(self: InboundOrderLine) -> Decimal

Set: QuantityToReceive(self: InboundOrderLine)=value
"""

 UnitCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: UnitCode(self: InboundOrderLine) -> str

Set: UnitCode(self: InboundOrderLine)=value
"""



class InboundOrderLines(FindableList):
 """ InboundOrderLines() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return InboundOrderLines()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetHashCode(self):
  """ GetHashCode(self: InboundOrderLines) -> int """
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
 IsDisposable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IsDisposable(self: InboundOrderLines) -> bool

"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PreserveState(self: InboundOrderLines) -> bool

"""


 DisplayMember='ItemCode'
 ValueMember='Id'


class InboundOrders(FindableList):
 """ InboundOrders() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return InboundOrders()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def FromIEnumerable(list):
  """ FromIEnumerable(list: IEnumerable[InboundOrder]) -> InboundOrders """
  pass
 def GetCacheKey(self):
  """ GetCacheKey(self: InboundOrders) -> int """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: InboundOrders) -> int """
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
 DisplayMember=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DisplayMember(self: InboundOrders) -> str

"""

 ValueMember=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ValueMember(self: InboundOrders) -> str

"""



class InboundOrderTypeEnum:
 """ enum InboundOrderTypeEnum,values: AdhocPurchase (2),AdhocRma (3),AdhocRmaTouch (4),PreReceipt (5),Purchase (0),Rma (1) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return InboundOrderTypeEnum()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
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
 AdhocPurchase=None
 AdhocRma=None
 AdhocRmaTouch=None
 PreReceipt=None
 Purchase=None
 Rma=None
 value__=None


class InboundReceiveLine(object):
 """
 Contains the orderlines of the same item of inbound orders.
 
 InboundReceiveLine()
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return InboundReceiveLine()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Clone(self):
  """ Clone(self: InboundReceiveLine) -> object """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: InboundReceiveLine) -> int """
  pass
 def GetItemIdsReceived(self):
  """ GetItemIdsReceived(self: InboundReceiveLine) -> ItemIdentifications """
  pass
 def PutBack(self,*__args):
  """
  PutBack(self: InboundReceiveLine,orderNumber: str,quantity: Decimal) -> bool
  PutBack(self: InboundReceiveLine,orderId: int,quantity: Decimal) -> bool
  PutBack(self: InboundReceiveLine,orderNumber: str,itemId: ItemIdentification) -> bool
  PutBack(self: InboundReceiveLine,orderId: int,itemId: ItemIdentification) -> bool
  """
  pass
 def Receive(self,*__args):
  """
  Receive(self: InboundReceiveLine,orderNumber: str,quantity: Decimal) -> bool
   Returns: false if not all picked items have been added to the PurchaseOrderLines.
  Receive(self: InboundReceiveLine,orderId: int,quantity: Decimal) -> bool
   Returns: false if not all picked items have been added to the PurchaseOrderLines.
  Receive(self: InboundReceiveLine,orderNumber: str,itemId: ItemIdentification) -> bool
   Returns: false if not all picked items have been added to the PurchaseOrderLines.
  Receive(self: InboundReceiveLine,orderId: int,itemId: ItemIdentification) -> bool
   Returns: false if not all picked items have been added to the PurchaseOrderLines.
  """
  pass
 def ValidateOrderIdWithOrderLine(self,*args):
  """ ValidateOrderIdWithOrderLine(self: InboundReceiveLine,orderLine: InboundOrderLine,orderId: int) -> bool """
  pass
 def ValidateOrderNumberWithOrderLine(self,*args):
  """ ValidateOrderNumberWithOrderLine(self: InboundReceiveLine,orderLine: InboundOrderLine,orderNumber: str) -> bool """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 BarcodePresent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BarcodePresent(self: InboundReceiveLine) -> Nullable[bool]

Set: BarcodePresent(self: InboundReceiveLine)=value
"""

 CurrentVendorItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CurrentVendorItemCode(self: InboundReceiveLine) -> str

"""

 DefaultVendorItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DefaultVendorItemCode(self: InboundReceiveLine) -> str

"""

 HasInstructions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasInstructions(self: InboundReceiveLine) -> bool

"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: InboundReceiveLine) -> str

"""

 Instructions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Instructions(self: InboundReceiveLine) -> IEnumerable[str]

"""

 IsBatchNumberItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsBatchNumberItem(self: InboundReceiveLine) -> bool

"""

 IsSerialNumberItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsSerialNumberItem(self: InboundReceiveLine) -> bool

"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemCode(self: InboundReceiveLine) -> str

Set: ItemCode(self: InboundReceiveLine)=value
"""

 ItemDefaultLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemDefaultLocation(self: InboundReceiveLine) -> str

"""

 ItemIdRegistration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemIdRegistration(self: InboundReceiveLine) -> ItemIdentificationRegistration

Set: ItemIdRegistration(self: InboundReceiveLine)=value
"""

 LineDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LineDescription(self: InboundReceiveLine) -> str

"""

 OrderLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OrderLines(self: InboundReceiveLine) -> InboundOrderLines

"""

 QuantityLeft=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: QuantityLeft(self: InboundReceiveLine) -> Decimal

"""

 QuantityOrdered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Cumulative quantity of all the Purchaseorderlines in this object

Get: QuantityOrdered(self: InboundReceiveLine) -> Decimal

"""

 QuantityReceived=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Cumulative delivered quantity of all the Purchaseorderlines in this object

Get: QuantityReceived(self: InboundReceiveLine) -> Decimal

"""

 QuantityToReceive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: QuantityToReceive(self: InboundReceiveLine) -> Decimal

"""

 SalesUnitCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SalesUnitCode(self: InboundReceiveLine) -> str

Set: SalesUnitCode(self: InboundReceiveLine)=value
"""

 UnitCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UnitCode(self: InboundReceiveLine) -> str

Set: UnitCode(self: InboundReceiveLine)=value
"""



class InboundReceiveLines(FindableList):
 """
 InboundReceiveLines(collection: IEnumerable[InboundReceiveLine])
 InboundReceiveLines()
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return InboundReceiveLines()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def AddLinesFrom(self,orderLines):
  """ AddLinesFrom(self: InboundReceiveLines,orderLines: InboundOrderLines) """
  pass
 def AddOrUpdateLicensePlate(self,licensePlate):
  """ AddOrUpdateLicensePlate(self: InboundReceiveLines,licensePlate: LicensePlate) """
  pass
 def AddOrUpdateLicensePlateItems(self,item):
  """ AddOrUpdateLicensePlateItems(self: InboundReceiveLines,item: LicensePlateItem) """
  pass
 def Clear(self):
  """ Clear(self: InboundReceiveLines) """
  pass
 @staticmethod
 def FromIEnumerable(lines):
  """ FromIEnumerable(lines: IEnumerable[InboundReceiveLine]) -> InboundReceiveLines """
  pass
 def GetById(self,lineId):
  """ GetById(self: InboundReceiveLines,lineId: str) -> InboundReceiveLine """
  pass
 def GetIdsOfReceivedOrders(self):
  """ GetIdsOfReceivedOrders(self: InboundReceiveLines) -> List[int] """
  pass
 def GetKey(self):
  """ GetKey(self: InboundReceiveLines) -> int """
  pass
 def GetOrderLines(self):
  """
  GetOrderLines(self: InboundReceiveLines) -> InboundOrderLines
  
   Returns all orderlines,used for processing.
  """
  pass
 def GetOrderLinesByOrderId(self,orderId):
  """
  GetOrderLinesByOrderId(self: InboundReceiveLines,orderId: int) -> InboundOrderLines
  
   Returns the lines of the given order,used for processing.
  """
  pass
 def GetQuantityReceived(self,predicate):
  """ GetQuantityReceived(self: InboundReceiveLines,predicate: Predicate[InboundReceiveLine]) -> Decimal """
  pass
 def GetQuantityReceivedByItemCode(self,itemCode):
  """ GetQuantityReceivedByItemCode(self: InboundReceiveLines,itemCode: str) -> Decimal """
  pass
 def GetQuantityReceivedOfItem(self,*__args):
  """
  GetQuantityReceivedOfItem(self: InboundReceiveLines,receiveLineId: str) -> Decimal
  GetQuantityReceivedOfItem(self: InboundReceiveLines,itemCode: str,itemIdNumber: str) -> Decimal
  """
  pass
 def GetQuantityToReceiveOfItem(self,receiveLineId):
  """ GetQuantityToReceiveOfItem(self: InboundReceiveLines,receiveLineId: str) -> Decimal """
  pass
 def GetReceivedOrderLines(self):
  """
  GetReceivedOrderLines(self: InboundReceiveLines) -> InboundOrderLines
  
   Returns all received orderlines,used for processing.
  """
  pass
 def GetReceivedOrderLinesByOrderId(self,orderId):
  """
  GetReceivedOrderLinesByOrderId(self: InboundReceiveLines,orderId: int) -> InboundOrderLines
  
   Returns the received lines of the given order,used for processing.
  """
  pass
 def IndexOf(self,item,index=None,count=None):
  """ IndexOf(self: InboundReceiveLines,lineId: str) -> int """
  pass
 def MarkOrderLinesAsProcessed(self,orderId):
  """ MarkOrderLinesAsProcessed(self: InboundReceiveLines,orderId: int) """
  pass
 def RemoveLicensePlate(self,id):
  """ RemoveLicensePlate(self: InboundReceiveLines,id: int) """
  pass
 def RemoveLicensePlateItem(self,id):
  """ RemoveLicensePlateItem(self: InboundReceiveLines,id: int) """
  pass
 def SetOrderData(self,order):
  """ SetOrderData(self: InboundReceiveLines,order: InboundOrder) """
  pass
 def Sort(self,*__args):
  """ Sort(self: InboundReceiveLines,comparer: Func[InboundReceiveLine,str]) -> InboundReceiveLines """
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
  __new__(cls: type,collection: IEnumerable[InboundReceiveLine])
  __new__(cls: type)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 CustomerNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerNumber(self: InboundReceiveLines) -> str

Set: CustomerNumber(self: InboundReceiveLines)=value
"""

 GroupGuid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: GroupGuid(self: InboundReceiveLines) -> Guid

Set: GroupGuid(self: InboundReceiveLines)=value
"""

 HasLicensePlates=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: HasLicensePlates(self: InboundReceiveLines) -> bool

"""

 IsDisposable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IsDisposable(self: InboundReceiveLines) -> bool

"""

 LicensePlateItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: LicensePlateItems(self: InboundReceiveLines) -> LicensePlateItems

"""

 LicensePlates=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: LicensePlates(self: InboundReceiveLines) -> LicensePlates

"""

 Notes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Notes(self: InboundReceiveLines) -> str

Set: Notes(self: InboundReceiveLines)=value
"""

 OrderIds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """key is the orderID,value is orderNumber

Get: OrderIds(self: InboundReceiveLines) -> Dictionary[int,str]

"""

 OrderNumberList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderNumberList(self: InboundReceiveLines) -> str

"""

 OrderType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderType(self: InboundReceiveLines) -> InboundOrderTypeEnum

Set: OrderType(self: InboundReceiveLines)=value
"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PreserveState(self: InboundReceiveLines) -> bool

"""

 ProcessState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ProcessState(self: InboundReceiveLines) -> ProcessReceiveLinesStepsEnum

Set: ProcessState(self: InboundReceiveLines)=value
"""

 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: WarehouseCode(self: InboundReceiveLines) -> str

Set: WarehouseCode(self: InboundReceiveLines)=value
"""


 ValueMember='Id'


class PrepareAdhocRmaReceiveLinesArgs(object):
 """ PrepareAdhocRmaReceiveLinesArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PrepareAdhocRmaReceiveLinesArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetHashCode(self):
  """ GetHashCode(self: PrepareAdhocRmaReceiveLinesArgs) -> int """
  pass
 def ToPrepareInboundReceiveLinesArgs(self):
  """ ToPrepareInboundReceiveLinesArgs(self: PrepareAdhocRmaReceiveLinesArgs) -> PrepareInboundReceiveLinesArgs """
  pass
 Customer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Customer(self: PrepareAdhocRmaReceiveLinesArgs) -> Customer

Set: Customer(self: PrepareAdhocRmaReceiveLinesArgs)=value
"""

 HistoryOutboundOrders=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: HistoryOutboundOrders(self: PrepareAdhocRmaReceiveLinesArgs) -> HistoryOutboundOrders

Set: HistoryOutboundOrders(self: PrepareAdhocRmaReceiveLinesArgs)=value
"""

 OrderType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderType(self: PrepareAdhocRmaReceiveLinesArgs) -> InboundOrderTypeEnum

"""

 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: WarehouseCode(self: PrepareAdhocRmaReceiveLinesArgs) -> str

Set: WarehouseCode(self: PrepareAdhocRmaReceiveLinesArgs)=value
"""



class PrepareInboundReceiveLinesArgs(object):
 """ PrepareInboundReceiveLinesArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PrepareInboundReceiveLinesArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 CustomerNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerNumber(self: PrepareInboundReceiveLinesArgs) -> str

Set: CustomerNumber(self: PrepareInboundReceiveLinesArgs)=value
"""

 OrderType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderType(self: PrepareInboundReceiveLinesArgs) -> InboundOrderTypeEnum

Set: OrderType(self: PrepareInboundReceiveLinesArgs)=value
"""

 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: WarehouseCode(self: PrepareInboundReceiveLinesArgs) -> str

Set: WarehouseCode(self: PrepareInboundReceiveLinesArgs)=value
"""



class PreReceiptArgs:
 """ PreReceiptArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PreReceiptArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 IncludeCompleted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IncludeCompleted(self: PreReceiptArgs) -> bool

Set: IncludeCompleted(self: PreReceiptArgs)=value
"""

 Paging=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Paging(self: PreReceiptArgs) -> PagingParams

Set: Paging(self: PreReceiptArgs)=value
"""

 StatusFlags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: StatusFlags(self: PreReceiptArgs) -> PreReceiptStatus

Set: StatusFlags(self: PreReceiptArgs)=value
"""



class PreReceiptLine(object):
 """ PreReceiptLine() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PreReceiptLine()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 CurrentVendorItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CurrentVendorItemCode(self: PreReceiptLine) -> str

Set: CurrentVendorItemCode(self: PreReceiptLine)=value
"""

 DateReceipt=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DateReceipt(self: PreReceiptLine) -> DateTime

Set: DateReceipt(self: PreReceiptLine)=value
"""

 DefaultVendorItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DefaultVendorItemCode(self: PreReceiptLine) -> str

Set: DefaultVendorItemCode(self: PreReceiptLine)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Id of the prereceipt line. Unqiue for every line.

Get: Id(self: PreReceiptLine) -> int

Set: Id(self: PreReceiptLine)=value
"""

 IsBatchNumberItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IsBatchNumberItem(self: PreReceiptLine) -> bool

Set: IsBatchNumberItem(self: PreReceiptLine)=value
"""

 IsFullyReceived=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsFullyReceived(self: PreReceiptLine) -> bool

"""

 IsSerialNumberItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IsSerialNumberItem(self: PreReceiptLine) -> bool

Set: IsSerialNumberItem(self: PreReceiptLine)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Product for this line.

Get: ItemCode(self: PreReceiptLine) -> str

Set: ItemCode(self: PreReceiptLine)=value
"""

 ItemDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemDescription(self: PreReceiptLine) -> str

Set: ItemDescription(self: PreReceiptLine)=value
"""

 ItemIdRegistration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemIdRegistration(self: PreReceiptLine) -> ItemIdentificationRegistration

Set: ItemIdRegistration(self: PreReceiptLine)=value
"""

 ItemIds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemIds(self: PreReceiptLine) -> ItemIdentifications

Set: ItemIds(self: PreReceiptLine)=value
"""

 ItemPurchasePrice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemPurchasePrice(self: PreReceiptLine) -> Decimal

Set: ItemPurchasePrice(self: PreReceiptLine)=value
"""

 LineCurrencyCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LineCurrencyCode(self: PreReceiptLine) -> str

Set: LineCurrencyCode(self: PreReceiptLine)=value
"""

 LineInstruction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LineInstruction(self: PreReceiptLine) -> str

Set: LineInstruction(self: PreReceiptLine)=value
"""

 PercentageReceived=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PercentageReceived(self: PreReceiptLine) -> int

"""

 PreReceiptId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Id that identifies from which Wms.RemotingObjects.Inbound.PreReceipt this line is from.

Get: PreReceiptId(self: PreReceiptLine) -> int

Set: PreReceiptId(self: PreReceiptLine)=value
"""

 PurchaseOrderId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PurchaseOrderId(self: PreReceiptLine) -> int

Set: PurchaseOrderId(self: PreReceiptLine)=value
"""

 PurchaseOrderLineId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PurchaseOrderLineId(self: PreReceiptLine) -> int

Set: PurchaseOrderLineId(self: PreReceiptLine)=value
"""

 PurchaseOrderLineNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PurchaseOrderLineNumber(self: PreReceiptLine) -> int

Set: PurchaseOrderLineNumber(self: PreReceiptLine)=value
"""

 PurchaseOrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PurchaseOrderNumber(self: PreReceiptLine) -> str

Set: PurchaseOrderNumber(self: PreReceiptLine)=value
"""

 Quantity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Quantity(self: PreReceiptLine) -> Decimal

Set: Quantity(self: PreReceiptLine)=value
"""

 QuantityOrdered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: QuantityOrdered(self: PreReceiptLine) -> Decimal

Set: QuantityOrdered(self: PreReceiptLine)=value
"""

 QuantitySupplierPackageSlip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: QuantitySupplierPackageSlip(self: PreReceiptLine) -> Decimal

Set: QuantitySupplierPackageSlip(self: PreReceiptLine)=value
"""

 QuantityToReceive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: QuantityToReceive(self: PreReceiptLine) -> Decimal

"""

 SalesUnitCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: SalesUnitCode(self: PreReceiptLine) -> str

Set: SalesUnitCode(self: PreReceiptLine)=value
"""

 SalesUnitFactor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: SalesUnitFactor(self: PreReceiptLine) -> Decimal

Set: SalesUnitFactor(self: PreReceiptLine)=value
"""

 SupplierCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: SupplierCode(self: PreReceiptLine) -> str

Set: SupplierCode(self: PreReceiptLine)=value
"""

 SupplierName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: SupplierName(self: PreReceiptLine) -> str

Set: SupplierName(self: PreReceiptLine)=value
"""

 UnitCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: UnitCode(self: PreReceiptLine) -> str

Set: UnitCode(self: PreReceiptLine)=value
"""

 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: WarehouseCode(self: PreReceiptLine) -> str

Set: WarehouseCode(self: PreReceiptLine)=value
"""



class PreReceiptLinesArgs(object):
 """
 Mdoel to retreive Wms.RemotingObjects.Inbound.PreReceiptLines
 
 PreReceiptLinesArgs()
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PreReceiptLinesArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Filter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Filters out all receipt lines not containing this filter. in code,description etc

Get: Filter(self: PreReceiptLinesArgs) -> str

Set: Filter(self: PreReceiptLinesArgs)=value
"""

 IncludeCompleted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If you want to include already completed prereceipts.
   (Wms.RemotingObjects.Inbound.PreReceiptLine.QuantitySupplierPackageSlip - Wms.RemotingObjects.Inbound.PreReceiptLine.Quantity > 0)

Get: IncludeCompleted(self: PreReceiptLinesArgs) -> bool

Set: IncludeCompleted(self: PreReceiptLinesArgs)=value
"""

 PreReceiptIds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Filters,only returns Lines that are part of one of these PreReceipts.

Get: PreReceiptIds(self: PreReceiptLinesArgs) -> Array[int]

Set: PreReceiptIds(self: PreReceiptLinesArgs)=value
"""

 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Filter,only show lines with this warehousecode.

Get: WarehouseCode(self: PreReceiptLinesArgs) -> str

Set: WarehouseCode(self: PreReceiptLinesArgs)=value
"""



class PreReceiptReceiveLines:
 """ PreReceiptReceiveLines() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PreReceiptReceiveLines()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetIdsOfReceivedOrders(self):
  """ GetIdsOfReceivedOrders(self: PreReceiptReceiveLines) -> List[int] """
  pass
 def IndexOf(self,item,index=None,count=None):
  """ IndexOf(self: InboundReceiveLines,lineId: str) -> int """
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
 PreReceiptId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PreReceiptId(self: PreReceiptReceiveLines) -> int

Set: PreReceiptId(self: PreReceiptReceiveLines)=value
"""



class PreReceipts(PagedList):
 """ PreReceipts() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PreReceipts()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def FromIEnumerable(list):
  """ FromIEnumerable(list: IEnumerable[PreReceipt]) -> PreReceipts """
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

class PreReceiptStatus:
 """ enum (flags) PreReceiptStatus,values: Active (2),Archived (16),InProcess (4),PartiallyReceived (8),Pending (1) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PreReceiptStatus()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
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
 Active=None
 Archived=None
 InProcess=None
 PartiallyReceived=None
 Pending=None
 value__=None


class PreReceiptSummaries(List):
 """ PreReceiptSummaries() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PreReceiptSummaries()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
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
 UniquePreReceiptsAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: UniquePreReceiptsAsString(self: PreReceiptSummaries) -> str

"""


 Delimiter=None


class PreReceiptSummary(object):
 """ PreReceiptSummary() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PreReceiptSummary()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Id(self: PreReceiptSummary) -> int

Set: Id(self: PreReceiptSummary)=value
"""

 IdAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IdAsString(self: PreReceiptSummary) -> str

"""

 OrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderNumber(self: PreReceiptSummary) -> str

Set: OrderNumber(self: PreReceiptSummary)=value
"""



class ProcessInboundReceiveLinesArgs(object):
 """ ProcessInboundReceiveLinesArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ProcessInboundReceiveLinesArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 CacheKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Cachekey of the cached ReceiveLines

Get: CacheKey(self: ProcessInboundReceiveLinesArgs) -> CacheKey

Set: CacheKey(self: ProcessInboundReceiveLinesArgs)=value
"""

 CacheKeyOfResults=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CacheKeyOfResults(self: ProcessInboundReceiveLinesArgs) -> CacheKey

Set: CacheKeyOfResults(self: ProcessInboundReceiveLinesArgs)=value
"""

 DefaultReceiptLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DefaultReceiptLocation(self: ProcessInboundReceiveLinesArgs) -> str

Set: DefaultReceiptLocation(self: ProcessInboundReceiveLinesArgs)=value
"""

 OrderDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Order description used for FreeReceipt inboundorder creation.

Get: OrderDescription(self: ProcessInboundReceiveLinesArgs) -> str

Set: OrderDescription(self: ProcessInboundReceiveLinesArgs)=value
"""

 PreReceiptId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """PreReceipt id is only available for PreReceipts. It's needed for lookup after processing

Get: PreReceiptId(self: ProcessInboundReceiveLinesArgs) -> int

Set: PreReceiptId(self: ProcessInboundReceiveLinesArgs)=value
"""

 PrintLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The print lines of the received items,these can be used for labelprinting.

Get: PrintLines(self: ProcessInboundReceiveLinesArgs) -> PrintLinesBase

Set: PrintLines(self: ProcessInboundReceiveLinesArgs)=value
"""

 YourReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The user's reference for this receipt.

Get: YourReference(self: ProcessInboundReceiveLinesArgs) -> str

Set: YourReference(self: ProcessInboundReceiveLinesArgs)=value
"""



class ProcessInboundReceiveLinesResult(CacheObject):
 """ ProcessInboundReceiveLinesResult() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ProcessInboundReceiveLinesResult()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetKey(self):
  """ GetKey(self: ProcessInboundReceiveLinesResult) -> str """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 Lifetime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Lifetime(self: ProcessInboundReceiveLinesResult) -> CacheLifeTimes

"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Make sure state is preserved for this object

Get: PreserveState(self: ProcessInboundReceiveLinesResult) -> bool

"""

 Results=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Results(self: ProcessInboundReceiveLinesResult) -> Dictionary[InboundOrder,ErpProcessPurchaseOrderLinesResult]

Set: Results(self: ProcessInboundReceiveLinesResult)=value
"""



class ProcessReceiveLinesStepsEnum:
 """ enum ProcessReceiveLinesStepsEnum,values: CreatePrintLines (2),Done (7),LogReceiveLines (1),PrintErpReceipt (5),PrintReceipt (6),ProcessReceiveLines (0),UpdateLicensePlates (4),UpdateStock (3) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ProcessReceiveLinesStepsEnum()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
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
 CreatePrintLines=None
 Done=None
 LogReceiveLines=None
 PrintErpReceipt=None
 PrintReceipt=None
 ProcessReceiveLines=None
 UpdateLicensePlates=None
 UpdateStock=None
 value__=None


class ReceiptTypeEnum:
 """ enum ReceiptTypeEnum,values: PreReceipt (0),Purchase (1) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReceiptTypeEnum()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
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
 PreReceipt=None
 Purchase=None
 value__=None


class ReceiveArgs(object):
 """ ReceiveArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReceiveArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 CacheKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CacheKey(self: ReceiveArgs) -> CacheKey

Set: CacheKey(self: ReceiveArgs)=value
"""

 EndDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: EndDate(self: ReceiveArgs) -> Nullable[DateTime]

Set: EndDate(self: ReceiveArgs)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemCode(self: ReceiveArgs) -> str

Set: ItemCode(self: ReceiveArgs)=value
"""

 ItemIdNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemIdNumber(self: ReceiveArgs) -> str

Set: ItemIdNumber(self: ReceiveArgs)=value
"""

 LabelArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: LabelArgs(self: ReceiveArgs) -> PrintLabelArgs

Set: LabelArgs(self: ReceiveArgs)=value
"""

 OrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderNumber(self: ReceiveArgs) -> str

Set: OrderNumber(self: ReceiveArgs)=value
"""

 Quantity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Quantity(self: ReceiveArgs) -> Decimal

Set: Quantity(self: ReceiveArgs)=value
"""

 ReceiveLineId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ReceiveLineId(self: ReceiveArgs) -> str

Set: ReceiveLineId(self: ReceiveArgs)=value
"""

 UnitCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: UnitCode(self: ReceiveArgs) -> str

Set: UnitCode(self: ReceiveArgs)=value
"""



class ReceiveItemIdMultiArgs(object):
 """ ReceiveItemIdMultiArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReceiveItemIdMultiArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 CacheKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CacheKey(self: ReceiveItemIdMultiArgs) -> CacheKey

Set: CacheKey(self: ReceiveItemIdMultiArgs)=value
"""

 InboundReceiveLineUpdatet=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: InboundReceiveLineUpdatet(self: ReceiveItemIdMultiArgs) -> InboundReceiveLine

Set: InboundReceiveLineUpdatet(self: ReceiveItemIdMultiArgs)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemCode(self: ReceiveItemIdMultiArgs) -> str

Set: ItemCode(self: ReceiveItemIdMultiArgs)=value
"""

 ItemIds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemIds(self: ReceiveItemIdMultiArgs) -> ItemIdentifications

Set: ItemIds(self: ReceiveItemIdMultiArgs)=value
"""

 OrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderNumber(self: ReceiveItemIdMultiArgs) -> str

Set: OrderNumber(self: ReceiveItemIdMultiArgs)=value
"""

 ReceiveArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ReceiveArgs(self: ReceiveItemIdMultiArgs) -> ReceiveArgs

"""

 ReceiveLineId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ReceiveLineId(self: ReceiveItemIdMultiArgs) -> str

Set: ReceiveLineId(self: ReceiveItemIdMultiArgs)=value
"""



class ReceiveItemIdRangeArgs:
 """ ReceiveItemIdRangeArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReceiveItemIdRangeArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 CacheKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CacheKey(self: ReceiveItemIdRangeArgs) -> CacheKey

Set: CacheKey(self: ReceiveItemIdRangeArgs)=value
"""

 OrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderNumber(self: ReceiveItemIdRangeArgs) -> str

Set: OrderNumber(self: ReceiveItemIdRangeArgs)=value
"""

 ReceiveArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ReceiveArgs(self: ReceiveItemIdRangeArgs) -> ReceiveArgs

Set: ReceiveArgs(self: ReceiveItemIdRangeArgs)=value
"""

 ReceiveLineId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ReceiveLineId(self: ReceiveItemIdRangeArgs) -> str

Set: ReceiveLineId(self: ReceiveItemIdRangeArgs)=value
"""



class ReceiveLinesForPreReceiptArgs(object):
 """ ReceiveLinesForPreReceiptArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReceiveLinesForPreReceiptArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 PreReceiptId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PreReceiptId(self: ReceiveLinesForPreReceiptArgs) -> int

Set: PreReceiptId(self: ReceiveLinesForPreReceiptArgs)=value
"""

 Result=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Result(self: ReceiveLinesForPreReceiptArgs) -> InboundReceiveLines

Set: Result(self: ReceiveLinesForPreReceiptArgs)=value
"""

 VendorNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: VendorNumber(self: ReceiveLinesForPreReceiptArgs) -> str

Set: VendorNumber(self: ReceiveLinesForPreReceiptArgs)=value
"""

 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: WarehouseCode(self: ReceiveLinesForPreReceiptArgs) -> str

Set: WarehouseCode(self: ReceiveLinesForPreReceiptArgs)=value
"""



class ReceiveWithLicensePlateArgs(ReceiveArgs):
 """ ReceiveWithLicensePlateArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReceiveWithLicensePlateArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 AddNewLicensePlate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: AddNewLicensePlate(self: ReceiveWithLicensePlateArgs) -> bool

Set: AddNewLicensePlate(self: ReceiveWithLicensePlateArgs)=value
"""

 LicensePlateId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: LicensePlateId(self: ReceiveWithLicensePlateArgs) -> int

Set: LicensePlateId(self: ReceiveWithLicensePlateArgs)=value
"""

 ModifiedLicensePlateItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ModifiedLicensePlateItems(self: ReceiveWithLicensePlateArgs) -> LicensePlateItems

Set: ModifiedLicensePlateItems(self: ReceiveWithLicensePlateArgs)=value
"""

 NewLicensePlates=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: NewLicensePlates(self: ReceiveWithLicensePlateArgs) -> LicensePlates

Set: NewLicensePlates(self: ReceiveWithLicensePlateArgs)=value
"""



class UpdatePreReceiptStatusArgs(object):
 """ UpdatePreReceiptStatusArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return UpdatePreReceiptStatusArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 NewStatus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: NewStatus(self: UpdatePreReceiptStatusArgs) -> PreReceiptStatus

Set: NewStatus(self: UpdatePreReceiptStatusArgs)=value
"""

 PreReceiptId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreReceiptId(self: UpdatePreReceiptStatusArgs) -> int

Set: PreReceiptId(self: UpdatePreReceiptStatusArgs)=value
"""



