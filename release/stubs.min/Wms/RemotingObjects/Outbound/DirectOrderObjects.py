# encoding: utf-8
# module Wms.RemotingObjects.Outbound.DirectOrderObjects calls itself DirectOrderObjects
# from Wms.RemotingObjects,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class DirectOrder(CacheObject):
 """
 DirectOrder()
 DirectOrder(customer: Customer,warehouseCode: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DirectOrder()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def AddOrderLine(self,orderLine):
  """ AddOrderLine(self: DirectOrder,orderLine: DirectOrderLine) """
  pass
 def CloneHeaderOnly(self):
  """ CloneHeaderOnly(self: DirectOrder) -> DirectOrder """
  pass
 def EnsureValidLineNumber(self,orderLine):
  """ EnsureValidLineNumber(self: DirectOrder,orderLine: DirectOrderLine) """
  pass
 def IndexOf(self,lineNumber):
  """ IndexOf(self: DirectOrder,lineNumber: int) -> int """
  pass
 def TryGetOrderLineByItemAndLocation(self,itemCode,locationCode,directOrderLineFound):
  """ TryGetOrderLineByItemAndLocation(self: DirectOrder,itemCode: str,locationCode: str) -> (bool,DirectOrderLine) """
  pass
 def TryGetOrderLineByLineNumber(self,lineNumber,directOrderLineFound):
  """ TryGetOrderLineByLineNumber(self: DirectOrder,lineNumber: int) -> (bool,DirectOrderLine) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,customer=None,warehouseCode=None):
  """
  __new__(cls: type)
  __new__(cls: type,customer: Customer,warehouseCode: str)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 AllocationReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AllocationReference(self: DirectOrder) -> AllocatedStockItemReference

Set: AllocationReference(self: DirectOrder)=value
"""

 CustomerName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerName(self: DirectOrder) -> str

Set: CustomerName(self: DirectOrder)=value
"""

 CustomerNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerNumber(self: DirectOrder) -> str

Set: CustomerNumber(self: DirectOrder)=value
"""

 ErpId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ErpId(self: DirectOrder) -> str

Set: ErpId(self: DirectOrder)=value
"""

 HasLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasLines(self: DirectOrder) -> bool

"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: DirectOrder) -> Guid

Set: Id(self: DirectOrder)=value
"""

 IdAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IdAsString(self: DirectOrder) -> str

"""

 IsProcessed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsProcessed(self: DirectOrder) -> bool

Set: IsProcessed(self: DirectOrder)=value
"""

 LastLineNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LastLineNumber(self: DirectOrder) -> int

Set: LastLineNumber(self: DirectOrder)=value
"""

 Lifetime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Lifetime(self: DirectOrder) -> CacheLifeTimes

"""

 OrderDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OrderDate(self: DirectOrder) -> DateTime

Set: OrderDate(self: DirectOrder)=value
"""

 OrderLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OrderLines(self: DirectOrder) -> List[DirectOrderLine]

Set: OrderLines(self: DirectOrder)=value
"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreserveState(self: DirectOrder) -> bool

"""

 Reference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Reference(self: DirectOrder) -> str

Set: Reference(self: DirectOrder)=value
"""

 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WarehouseCode(self: DirectOrder) -> str

Set: WarehouseCode(self: DirectOrder)=value
"""


 DisplayMember='CustomerName'
 ValueMember='CustomerNumber'


class DirectOrderCrudArgs(object):
 """ DirectOrderCrudArgs(directOrder: DirectOrder) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DirectOrderCrudArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,directOrder):
  """ __new__(cls: type,directOrder: DirectOrder) """
  pass
 DirectOrder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DirectOrder(self: DirectOrderCrudArgs) -> DirectOrder

Set: DirectOrder(self: DirectOrderCrudArgs)=value
"""



class DirectOrderLine(object):
 """ DirectOrderLine(item: Item,location: Location) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DirectOrderLine()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def ConvertToOutboundOrderLine(self,parent):
  """ ConvertToOutboundOrderLine(self: DirectOrderLine,parent: DirectOrder) -> OutboundOrderLine """
  pass
 def TryGetItemIdentificationByNumber(self,itemIdentificationNumber,itemIdentification):
  """ TryGetItemIdentificationByNumber(self: DirectOrderLine,itemIdentificationNumber: str) -> (bool,ItemIdentification) """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 @staticmethod
 def __new__(self,item,location):
  """ __new__(cls: type,item: Item,location: Location) """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 ContainsBatchNumberItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Don't set directly. Setter is for serialization purpose only

Get: ContainsBatchNumberItem(self: DirectOrderLine) -> bool

Set: ContainsBatchNumberItem(self: DirectOrderLine)=value
"""

 ContainsItemIdentificationItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ContainsItemIdentificationItem(self: DirectOrderLine) -> bool

"""

 ContainsSerialNumberItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Don't set directly. Setter is for serialization purpose only

Get: ContainsSerialNumberItem(self: DirectOrderLine) -> bool

Set: ContainsSerialNumberItem(self: DirectOrderLine)=value
"""

 CustomErpFields=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomErpFields(self: DirectOrderLine) -> SerializableDictionary[str,object]

Set: CustomErpFields(self: DirectOrderLine)=value
"""

 DefaultVendorBarcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DefaultVendorBarcode(self: DirectOrderLine) -> str

Set: DefaultVendorBarcode(self: DirectOrderLine)=value
"""

 HasItemIdentifications=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasItemIdentifications(self: DirectOrderLine) -> bool

"""

 Item=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Item(self: DirectOrderLine) -> Item

Set: Item(self: DirectOrderLine)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemCode(self: DirectOrderLine) -> str

"""

 ItemDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemDescription(self: DirectOrderLine) -> str

"""

 ItemIdentifications=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemIdentifications(self: DirectOrderLine) -> ItemIdentifications

Set: ItemIdentifications(self: DirectOrderLine)=value
"""

 LineNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LineNumber(self: DirectOrderLine) -> int

Set: LineNumber(self: DirectOrderLine)=value
"""

 Location=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Location(self: DirectOrderLine) -> Location

Set: Location(self: DirectOrderLine)=value
"""

 LocationCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LocationCode(self: DirectOrderLine) -> str

"""

 Quantity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Quantity(self: DirectOrderLine) -> Decimal

Set: Quantity(self: DirectOrderLine)=value
"""


 DisplayMember='ItemDescription'
 NoLinenumberValue=-1
 ValueMember='ItemCode'


class DirectOrderLineCrudArgs(DirectOrderCrudArgs):
 """ DirectOrderLineCrudArgs(directOrder: DirectOrder,directOrderLine: DirectOrderLine) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DirectOrderLineCrudArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,directOrder,directOrderLine):
  """ __new__(cls: type,directOrder: DirectOrder,directOrderLine: DirectOrderLine) """
  pass
 DirectOrderLine=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DirectOrderLine(self: DirectOrderLineCrudArgs) -> DirectOrderLine

Set: DirectOrderLine(self: DirectOrderLineCrudArgs)=value
"""



class DirectOrderLineItemIdentificationCrudArgs(DirectOrderLineCrudArgs):
 """ DirectOrderLineItemIdentificationCrudArgs(order: DirectOrder,directOrderLine: DirectOrderLine,itemIdentification: ItemIdentification) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DirectOrderLineItemIdentificationCrudArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,order,directOrderLine,itemIdentification):
  """ __new__(cls: type,order: DirectOrder,directOrderLine: DirectOrderLine,itemIdentification: ItemIdentification) """
  pass
 ItemIdentification=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemIdentification(self: DirectOrderLineItemIdentificationCrudArgs) -> ItemIdentification

Set: ItemIdentification(self: DirectOrderLineItemIdentificationCrudArgs)=value
"""



class DirectOrderLineItemIdentificationsCrudArgs(DirectOrderLineCrudArgs):
 """ DirectOrderLineItemIdentificationsCrudArgs(directOrder: DirectOrder,directOrderLine: DirectOrderLine,itemIdentifications: ItemIdentifications) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DirectOrderLineItemIdentificationsCrudArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,directOrder,directOrderLine,itemIdentifications):
  """ __new__(cls: type,directOrder: DirectOrder,directOrderLine: DirectOrderLine,itemIdentifications: ItemIdentifications) """
  pass
 ItemIdentifications=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemIdentifications(self: DirectOrderLineItemIdentificationsCrudArgs) -> ItemIdentifications

Set: ItemIdentifications(self: DirectOrderLineItemIdentificationsCrudArgs)=value
"""



class ErpProcessDirecOrderResult(object):
 """ ErpProcessDirecOrderResult() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ErpProcessDirecOrderResult()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 OrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OrderNumber(self: ErpProcessDirecOrderResult) -> str

Set: OrderNumber(self: ErpProcessDirecOrderResult)=value
"""

 Success=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Success(self: ErpProcessDirecOrderResult) -> bool

Set: Success(self: ErpProcessDirecOrderResult)=value
"""



class HistoryDirectOrder(object):
 """ HistoryDirectOrder() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HistoryDirectOrder()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 CreatedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CreatedBy(self: HistoryDirectOrder) -> str

Set: CreatedBy(self: HistoryDirectOrder)=value
"""

 CreatedOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CreatedOn(self: HistoryDirectOrder) -> DateTime

Set: CreatedOn(self: HistoryDirectOrder)=value
"""

 CustomerName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerName(self: HistoryDirectOrder) -> str

Set: CustomerName(self: HistoryDirectOrder)=value
"""

 CustomerNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerNumber(self: HistoryDirectOrder) -> str

Set: CustomerNumber(self: HistoryDirectOrder)=value
"""

 DirectOrders_pk=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DirectOrders_pk(self: HistoryDirectOrder) -> int

Set: DirectOrders_pk(self: HistoryDirectOrder)=value
"""

 ErpId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ErpId(self: HistoryDirectOrder) -> str

Set: ErpId(self: HistoryDirectOrder)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: HistoryDirectOrder) -> str

Set: Id(self: HistoryDirectOrder)=value
"""

 ModifiedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ModifiedBy(self: HistoryDirectOrder) -> str

Set: ModifiedBy(self: HistoryDirectOrder)=value
"""

 ModifiedOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ModifiedOn(self: HistoryDirectOrder) -> DateTime

Set: ModifiedOn(self: HistoryDirectOrder)=value
"""

 OrderDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OrderDate(self: HistoryDirectOrder) -> DateTime

Set: OrderDate(self: HistoryDirectOrder)=value
"""

 Reference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Reference(self: HistoryDirectOrder) -> str

Set: Reference(self: HistoryDirectOrder)=value
"""

 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WarehouseCode(self: HistoryDirectOrder) -> str

Set: WarehouseCode(self: HistoryDirectOrder)=value
"""



class HistoryDirectOrderLine(object):
 """ HistoryDirectOrderLine() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HistoryDirectOrderLine()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 CreatedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CreatedBy(self: HistoryDirectOrderLine) -> str

Set: CreatedBy(self: HistoryDirectOrderLine)=value
"""

 CreatedOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CreatedOn(self: HistoryDirectOrderLine) -> DateTime

Set: CreatedOn(self: HistoryDirectOrderLine)=value
"""

 DirectOrderLines_pk=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DirectOrderLines_pk(self: HistoryDirectOrderLine) -> int

Set: DirectOrderLines_pk(self: HistoryDirectOrderLine)=value
"""

 DirectOrder_fk=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DirectOrder_fk(self: HistoryDirectOrderLine) -> int

Set: DirectOrder_fk(self: HistoryDirectOrderLine)=value
"""

 ErpId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ErpId(self: HistoryDirectOrderLine) -> str

Set: ErpId(self: HistoryDirectOrderLine)=value
"""

 IsBatchNumberItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsBatchNumberItem(self: HistoryDirectOrderLine) -> bool

Set: IsBatchNumberItem(self: HistoryDirectOrderLine)=value
"""

 IsSerialNumberItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsSerialNumberItem(self: HistoryDirectOrderLine) -> bool

Set: IsSerialNumberItem(self: HistoryDirectOrderLine)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemCode(self: HistoryDirectOrderLine) -> str

Set: ItemCode(self: HistoryDirectOrderLine)=value
"""

 ItemDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemDescription(self: HistoryDirectOrderLine) -> str

Set: ItemDescription(self: HistoryDirectOrderLine)=value
"""

 Linenumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Linenumber(self: HistoryDirectOrderLine) -> int

Set: Linenumber(self: HistoryDirectOrderLine)=value
"""

 ModifiedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ModifiedBy(self: HistoryDirectOrderLine) -> str

Set: ModifiedBy(self: HistoryDirectOrderLine)=value
"""

 ModifiedOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ModifiedOn(self: HistoryDirectOrderLine) -> DateTime

Set: ModifiedOn(self: HistoryDirectOrderLine)=value
"""

 Quantity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Quantity(self: HistoryDirectOrderLine) -> Decimal

Set: Quantity(self: HistoryDirectOrderLine)=value
"""

 WarehouseLocationCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WarehouseLocationCode(self: HistoryDirectOrderLine) -> str

Set: WarehouseLocationCode(self: HistoryDirectOrderLine)=value
"""



class HistoryDirectOrderLinesFilter(object):
 """ HistoryDirectOrderLinesFilter() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HistoryDirectOrderLinesFilter()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 DirectOrderKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DirectOrderKey(self: HistoryDirectOrderLinesFilter) -> int

Set: DirectOrderKey(self: HistoryDirectOrderLinesFilter)=value
"""

 SearchText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SearchText(self: HistoryDirectOrderLinesFilter) -> str

Set: SearchText(self: HistoryDirectOrderLinesFilter)=value
"""



class HistoryDirectOrdersFilter(HistoryFilterBase):
 """ HistoryDirectOrdersFilter() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HistoryDirectOrdersFilter()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WarehouseCode(self: HistoryDirectOrdersFilter) -> str

Set: WarehouseCode(self: HistoryDirectOrdersFilter)=value
"""



