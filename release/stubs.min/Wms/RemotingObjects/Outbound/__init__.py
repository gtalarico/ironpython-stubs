# encoding: utf-8
# module Wms.RemotingObjects.Outbound calls itself Outbound
# from Wms.RemotingObjects,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from System.Collections.Generic import *
from ..__init__ import *

# no functions
# classes

class AllocationProfile(object):
 """ AllocationProfile() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return AllocationProfile()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Description(self: AllocationProfile) -> str

Set: Description(self: AllocationProfile)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Id(self: AllocationProfile) -> int

Set: Id(self: AllocationProfile)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Name(self: AllocationProfile) -> str

Set: Name(self: AllocationProfile)=value
"""



class AllocationProfiles(List):
 """ AllocationProfiles() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return AllocationProfiles()
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
 DisplayMember='Name'
 ValueMember='Id'


class GetHistoryOutboundOrderCustomersArgs(object):
 """ GetHistoryOutboundOrderCustomersArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return GetHistoryOutboundOrderCustomersArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 CustomerNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerNumber(self: GetHistoryOutboundOrderCustomersArgs) -> str

Set: CustomerNumber(self: GetHistoryOutboundOrderCustomersArgs)=value
"""

 Filter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Filter(self: GetHistoryOutboundOrderCustomersArgs) -> str

Set: Filter(self: GetHistoryOutboundOrderCustomersArgs)=value
"""

 Paging=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Paging(self: GetHistoryOutboundOrderCustomersArgs) -> PagingParams

Set: Paging(self: GetHistoryOutboundOrderCustomersArgs)=value
"""

 Warehouse=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Warehouse(self: GetHistoryOutboundOrderCustomersArgs) -> str

Set: Warehouse(self: GetHistoryOutboundOrderCustomersArgs)=value
"""



class GetHistoryOutboundOrderItemArgs(object):
 """ GetHistoryOutboundOrderItemArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return GetHistoryOutboundOrderItemArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 CustomerNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerNumber(self: GetHistoryOutboundOrderItemArgs) -> str

Set: CustomerNumber(self: GetHistoryOutboundOrderItemArgs)=value
"""

 DeliveryDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DeliveryDate(self: GetHistoryOutboundOrderItemArgs) -> Nullable[DateTime]

Set: DeliveryDate(self: GetHistoryOutboundOrderItemArgs)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemCode(self: GetHistoryOutboundOrderItemArgs) -> str

Set: ItemCode(self: GetHistoryOutboundOrderItemArgs)=value
"""

 OrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderNumber(self: GetHistoryOutboundOrderItemArgs) -> str

Set: OrderNumber(self: GetHistoryOutboundOrderItemArgs)=value
"""

 Paging=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Paging(self: GetHistoryOutboundOrderItemArgs) -> PagingParams

Set: Paging(self: GetHistoryOutboundOrderItemArgs)=value
"""

 SearchText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: SearchText(self: GetHistoryOutboundOrderItemArgs) -> str

Set: SearchText(self: GetHistoryOutboundOrderItemArgs)=value
"""



class GetHistoryOutboundOrdersArgs(object):
 """ GetHistoryOutboundOrdersArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return GetHistoryOutboundOrdersArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 CacheKeyOfReceipt=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CacheKeyOfReceipt(self: GetHistoryOutboundOrdersArgs) -> CacheKey

Set: CacheKeyOfReceipt(self: GetHistoryOutboundOrdersArgs)=value
"""

 CustomerNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerNumber(self: GetHistoryOutboundOrdersArgs) -> str

Set: CustomerNumber(self: GetHistoryOutboundOrdersArgs)=value
"""

 DecreaseQuantitiesWithActieveAdhocRma=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DecreaseQuantitiesWithActieveAdhocRma(self: GetHistoryOutboundOrdersArgs) -> bool

Set: DecreaseQuantitiesWithActieveAdhocRma(self: GetHistoryOutboundOrdersArgs)=value
"""

 Filter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Filter(self: GetHistoryOutboundOrdersArgs) -> str

Set: Filter(self: GetHistoryOutboundOrdersArgs)=value
"""

 IncludeOrdersThatCanBeReturned=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IncludeOrdersThatCanBeReturned(self: GetHistoryOutboundOrdersArgs) -> bool

Set: IncludeOrdersThatCanBeReturned(self: GetHistoryOutboundOrdersArgs)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemCode(self: GetHistoryOutboundOrdersArgs) -> str

Set: ItemCode(self: GetHistoryOutboundOrdersArgs)=value
"""

 OrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderNumber(self: GetHistoryOutboundOrdersArgs) -> str

Set: OrderNumber(self: GetHistoryOutboundOrdersArgs)=value
"""

 Paging=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Paging(self: GetHistoryOutboundOrdersArgs) -> PagingParams

Set: Paging(self: GetHistoryOutboundOrdersArgs)=value
"""



class GetOutboundOrdersArgs(object):
 """ GetOutboundOrdersArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return GetOutboundOrdersArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 OrderNumbers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderNumbers(self: GetOutboundOrdersArgs) -> List[str]

Set: OrderNumbers(self: GetOutboundOrdersArgs)=value
"""

 SearchText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: SearchText(self: GetOutboundOrdersArgs) -> str

Set: SearchText(self: GetOutboundOrdersArgs)=value
"""



class HistoryOutboundOrder(DbObject):
 """  """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HistoryOutboundOrder()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Clone(self):
  """ Clone(self: HistoryOutboundOrder) -> object """
  pass
 def Equals(self,obj):
  """ Equals(self: HistoryOutboundOrder,obj: object) -> bool """
  pass
 def GetHashCode(self,orderNumber=None,dateOfDelivery=None):
  """
  GetHashCode(self: HistoryOutboundOrder) -> int
  GetHashCode(orderNumber: str,dateOfDelivery: DateTime) -> int
  """
  pass
 def GetHashCodeOfCustomer(self):
  """ GetHashCodeOfCustomer(self: HistoryOutboundOrder) -> int """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 AllowPartialDelivery=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: AllowPartialDelivery(self: HistoryOutboundOrder) -> PartialDeliveryTypeEnum

Set: AllowPartialDelivery(self: HistoryOutboundOrder)=value
"""

 AllowPartialDeliveryAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: AllowPartialDeliveryAsString(self: HistoryOutboundOrder) -> str

"""

 Backorder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Backorder(self: HistoryOutboundOrder) -> bool

Set: Backorder(self: HistoryOutboundOrder)=value
"""

 CustomerAddressLine1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerAddressLine1(self: HistoryOutboundOrder) -> str

Set: CustomerAddressLine1(self: HistoryOutboundOrder)=value
"""

 CustomerAddressLine2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerAddressLine2(self: HistoryOutboundOrder) -> str

Set: CustomerAddressLine2(self: HistoryOutboundOrder)=value
"""

 CustomerAddressLine3=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerAddressLine3(self: HistoryOutboundOrder) -> str

Set: CustomerAddressLine3(self: HistoryOutboundOrder)=value
"""

 CustomerCity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerCity(self: HistoryOutboundOrder) -> str

Set: CustomerCity(self: HistoryOutboundOrder)=value
"""

 CustomerContact=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerContact(self: HistoryOutboundOrder) -> str

Set: CustomerContact(self: HistoryOutboundOrder)=value
"""

 CustomerContactEmail=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerContactEmail(self: HistoryOutboundOrder) -> str

Set: CustomerContactEmail(self: HistoryOutboundOrder)=value
"""

 CustomerCountryCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerCountryCode(self: HistoryOutboundOrder) -> str

Set: CustomerCountryCode(self: HistoryOutboundOrder)=value
"""

 CustomerCountryName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerCountryName(self: HistoryOutboundOrder) -> str

Set: CustomerCountryName(self: HistoryOutboundOrder)=value
"""

 CustomerEoriNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerEoriNumber(self: HistoryOutboundOrder) -> str

Set: CustomerEoriNumber(self: HistoryOutboundOrder)=value
"""

 CustomerInvoiceAddressLine1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceAddressLine1(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceAddressLine1(self: HistoryOutboundOrder)=value
"""

 CustomerInvoiceAddressLine2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceAddressLine2(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceAddressLine2(self: HistoryOutboundOrder)=value
"""

 CustomerInvoiceAddressLine3=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceAddressLine3(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceAddressLine3(self: HistoryOutboundOrder)=value
"""

 CustomerInvoiceCity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceCity(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceCity(self: HistoryOutboundOrder)=value
"""

 CustomerInvoiceContact=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceContact(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceContact(self: HistoryOutboundOrder)=value
"""

 CustomerInvoiceContactEmail=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceContactEmail(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceContactEmail(self: HistoryOutboundOrder)=value
"""

 CustomerInvoiceCountryCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceCountryCode(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceCountryCode(self: HistoryOutboundOrder)=value
"""

 CustomerInvoiceCountryName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceCountryName(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceCountryName(self: HistoryOutboundOrder)=value
"""

 CustomerInvoiceName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceName(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceName(self: HistoryOutboundOrder)=value
"""

 CustomerInvoiceNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceNumber(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceNumber(self: HistoryOutboundOrder)=value
"""

 CustomerInvoicePhoneNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoicePhoneNumber(self: HistoryOutboundOrder) -> str

Set: CustomerInvoicePhoneNumber(self: HistoryOutboundOrder)=value
"""

 CustomerInvoiceState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceState(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceState(self: HistoryOutboundOrder)=value
"""

 CustomerInvoiceZipCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceZipCode(self: HistoryOutboundOrder) -> str

Set: CustomerInvoiceZipCode(self: HistoryOutboundOrder)=value
"""

 CustomerName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerName(self: HistoryOutboundOrder) -> str

Set: CustomerName(self: HistoryOutboundOrder)=value
"""

 CustomerNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerNumber(self: HistoryOutboundOrder) -> str

Set: CustomerNumber(self: HistoryOutboundOrder)=value
"""

 CustomerPackageSlipLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerPackageSlipLayout(self: HistoryOutboundOrder) -> str

Set: CustomerPackageSlipLayout(self: HistoryOutboundOrder)=value
"""

 CustomerPhoneNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerPhoneNumber(self: HistoryOutboundOrder) -> str

Set: CustomerPhoneNumber(self: HistoryOutboundOrder)=value
"""

 CustomerReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerReference(self: HistoryOutboundOrder) -> str

Set: CustomerReference(self: HistoryOutboundOrder)=value
"""

 CustomerState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerState(self: HistoryOutboundOrder) -> str

Set: CustomerState(self: HistoryOutboundOrder)=value
"""

 CustomerZipCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerZipCode(self: HistoryOutboundOrder) -> str

Set: CustomerZipCode(self: HistoryOutboundOrder)=value
"""

 DateOfDelivery=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DateOfDelivery(self: HistoryOutboundOrder) -> DateTime

Set: DateOfDelivery(self: HistoryOutboundOrder)=value
"""

 DateOrdered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DateOrdered(self: HistoryOutboundOrder) -> DateTime

Set: DateOrdered(self: HistoryOutboundOrder)=value
"""

 DbKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DbKey(self: HistoryOutboundOrder) -> int

Set: DbKey(self: HistoryOutboundOrder)=value
"""

 DeliveryMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DeliveryMethod(self: HistoryOutboundOrder) -> str

Set: DeliveryMethod(self: HistoryOutboundOrder)=value
"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Description(self: HistoryOutboundOrder) -> str

Set: Description(self: HistoryOutboundOrder)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Id(self: HistoryOutboundOrder) -> int

"""

 Notes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Notes(self: HistoryOutboundOrder) -> str

Set: Notes(self: HistoryOutboundOrder)=value
"""

 Number=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Number(self: HistoryOutboundOrder) -> str

Set: Number(self: HistoryOutboundOrder)=value
"""

 NumberOfItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: NumberOfItems(self: HistoryOutboundOrder) -> int

Set: NumberOfItems(self: HistoryOutboundOrder)=value
"""

 OrderAmountDelivered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderAmountDelivered(self: HistoryOutboundOrder) -> Decimal

Set: OrderAmountDelivered(self: HistoryOutboundOrder)=value
"""

 OrderAmountTotal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderAmountTotal(self: HistoryOutboundOrder) -> Decimal

Set: OrderAmountTotal(self: HistoryOutboundOrder)=value
"""

 ProjectCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ProjectCode(self: HistoryOutboundOrder) -> str

Set: ProjectCode(self: HistoryOutboundOrder)=value
"""

 ProjectName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ProjectName(self: HistoryOutboundOrder) -> str

Set: ProjectName(self: HistoryOutboundOrder)=value
"""

 QuantityDelivered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: QuantityDelivered(self: HistoryOutboundOrder) -> Decimal

Set: QuantityDelivered(self: HistoryOutboundOrder)=value
"""

 QuantityOrdered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: QuantityOrdered(self: HistoryOutboundOrder) -> Decimal

Set: QuantityOrdered(self: HistoryOutboundOrder)=value
"""

 RoutingCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: RoutingCode(self: HistoryOutboundOrder) -> str

Set: RoutingCode(self: HistoryOutboundOrder)=value
"""

 SelectionCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: SelectionCode(self: HistoryOutboundOrder) -> str

Set: SelectionCode(self: HistoryOutboundOrder)=value
"""

 SelectionCodeDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: SelectionCodeDescription(self: HistoryOutboundOrder) -> str

Set: SelectionCodeDescription(self: HistoryOutboundOrder)=value
"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Type(self: HistoryOutboundOrder) -> OutboundOrderTypeEnum

"""

 Warehouse=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Warehouse(self: HistoryOutboundOrder) -> str

Set: Warehouse(self: HistoryOutboundOrder)=value
"""



class OutboundOrderLine(DbObject):
 """  """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return OutboundOrderLine()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Clone(self):
  """ Clone(self: OutboundOrderLine) -> object """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: OutboundOrderLine) -> int """
  pass
 def IsBatchNumberItemCheck(self,checkRegistration):
  """
  IsBatchNumberItemCheck(self: OutboundOrderLine,checkRegistration: bool) -> bool
  
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
  IsSerialNumberItemCheck(self: OutboundOrderLine,checkRegistration: bool) -> bool
  
   Checks if the item is a serialnumber item.
  
   checkRegistration: True if the serialnumber registration should be checked,false if just the property should be returned.
   Returns: True if the check is ignored and the item is a serial item,or when the itemid registration is set to
     complete (means the numers are registered throughout the 
    whole process).
     False if the check is ignored and the item is not a serial item,or when the itemids are registered
     during delivery only.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 BatchId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: BatchId(self: OutboundOrderLine) -> Guid

Set: BatchId(self: OutboundOrderLine)=value
"""

 CustomerName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerName(self: OutboundOrderLine) -> str

Set: CustomerName(self: OutboundOrderLine)=value
"""

 CustomFields=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomFields(self: OutboundOrderLine) -> SerializableDictionary[str,object]

Set: CustomFields(self: OutboundOrderLine)=value
"""

 DateOfDelivery=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DateOfDelivery(self: OutboundOrderLine) -> DateTime

Set: DateOfDelivery(self: OutboundOrderLine)=value
"""

 DefaultVendorBarcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DefaultVendorBarcode(self: OutboundOrderLine) -> str

Set: DefaultVendorBarcode(self: OutboundOrderLine)=value
"""

 DefaultVendorItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DefaultVendorItemCode(self: OutboundOrderLine) -> str

Set: DefaultVendorItemCode(self: OutboundOrderLine)=value
"""

 GTINCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The GS1 GTIN code of this item

Get: GTINCode(self: OutboundOrderLine) -> str

Set: GTINCode(self: OutboundOrderLine)=value
"""

 HistoryId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: HistoryId(self: OutboundOrderLine) -> int

Set: HistoryId(self: OutboundOrderLine)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Id(self: OutboundOrderLine) -> int

Set: Id(self: OutboundOrderLine)=value
"""

 IsBatchNumberItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IsBatchNumberItem(self: OutboundOrderLine) -> bool

Set: IsBatchNumberItem(self: OutboundOrderLine)=value
"""

 IsFractionAllowed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IsFractionAllowed(self: OutboundOrderLine) -> bool

Set: IsFractionAllowed(self: OutboundOrderLine)=value
"""

 IsSerialNumberItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IsSerialNumberItem(self: OutboundOrderLine) -> bool

Set: IsSerialNumberItem(self: OutboundOrderLine)=value
"""

 ItemBrand=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Necessary for Userinterface BOXwise Mobile

Get: ItemBrand(self: OutboundOrderLine) -> str

Set: ItemBrand(self: OutboundOrderLine)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Necessary for Userinterface BOXwise Mobile

Get: ItemCode(self: OutboundOrderLine) -> str

Set: ItemCode(self: OutboundOrderLine)=value
"""

 ItemDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Necessary for Userinterface BOXwise Mobile

Get: ItemDescription(self: OutboundOrderLine) -> str

Set: ItemDescription(self: OutboundOrderLine)=value
"""

 ItemDimensions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemDimensions(self: OutboundOrderLine) -> Dimensions

Set: ItemDimensions(self: OutboundOrderLine)=value
"""

 ItemIdentifierAssigned=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemIdentifierAssigned(self: OutboundOrderLine) -> bool

Set: ItemIdentifierAssigned(self: OutboundOrderLine)=value
"""

 ItemIdRegistration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemIdRegistration(self: OutboundOrderLine) -> ItemIdentificationRegistration

Set: ItemIdRegistration(self: OutboundOrderLine)=value
"""

 ItemLongDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemLongDescription(self: OutboundOrderLine) -> str

Set: ItemLongDescription(self: OutboundOrderLine)=value
"""

 ItemPackLocations=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemPackLocations(self: OutboundOrderLine) -> ItemPackLocations

Set: ItemPackLocations(self: OutboundOrderLine)=value
"""

 ItemPickLocations=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemPickLocations(self: OutboundOrderLine) -> ItemPickLocations

Set: ItemPickLocations(self: OutboundOrderLine)=value
"""

 ItemPurchasePrice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemPurchasePrice(self: OutboundOrderLine) -> Decimal

Set: ItemPurchasePrice(self: OutboundOrderLine)=value
"""

 ItemSalesPrice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemSalesPrice(self: OutboundOrderLine) -> Decimal

Set: ItemSalesPrice(self: OutboundOrderLine)=value
"""

 ItemSalesPriceSingleWithVat=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemSalesPriceSingleWithVat(self: OutboundOrderLine) -> Decimal

Set: ItemSalesPriceSingleWithVat(self: OutboundOrderLine)=value
"""

 ItemSalesPriceSumPickable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemSalesPriceSumPickable(self: OutboundOrderLine) -> Decimal

"""

 ItemSalesPriceSumToDeliver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemSalesPriceSumToDeliver(self: OutboundOrderLine) -> Decimal

"""

 ItemWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemWeight(self: OutboundOrderLine) -> Decimal

Set: ItemWeight(self: OutboundOrderLine)=value
"""

 LineCurrencyCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: LineCurrencyCode(self: OutboundOrderLine) -> str

Set: LineCurrencyCode(self: OutboundOrderLine)=value
"""

 LineDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: LineDescription(self: OutboundOrderLine) -> str

Set: LineDescription(self: OutboundOrderLine)=value
"""

 LineInstruction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Necessary for Userinterface BOXwise Mobile

Get: LineInstruction(self: OutboundOrderLine) -> str

Set: LineInstruction(self: OutboundOrderLine)=value
"""

 LineItemIdentifier=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: LineItemIdentifier(self: OutboundOrderLine) -> str

Set: LineItemIdentifier(self: OutboundOrderLine)=value
"""

 LineNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: LineNumber(self: OutboundOrderLine) -> int

Set: LineNumber(self: OutboundOrderLine)=value
"""

 OrderId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderId(self: OutboundOrderLine) -> int

Set: OrderId(self: OutboundOrderLine)=value
"""

 OrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Necessary for Userinterface BOXwise Mobile

Get: OrderNumber(self: OutboundOrderLine) -> str

Set: OrderNumber(self: OutboundOrderLine)=value
"""

 PercentageItemSalesPriceSumPickable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PercentageItemSalesPriceSumPickable(self: OutboundOrderLine) -> int

"""

 QuantityAllocated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: QuantityAllocated(self: OutboundOrderLine) -> Decimal

"""

 QuantityLocked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Quantity locked by external ERP program. 
   This quantity is not included in stock allocation but shown in %Batchable and CheckPartialDelivery
   
   * assigned to purchase order from Profit (wmspro-3531). 
   * Potential order waiting as an Afas option added here too.
   
   These amounts are not in Wms.RemotingObjects.Outbound.OutboundOrderLine.QuantityToDeliver but are actually part of the order
   and thus the order cannot be Completely Delivered.

Get: QuantityLocked(self: OutboundOrderLine) -> Decimal

Set: QuantityLocked(self: OutboundOrderLine)=value
"""

 QuantityOrdered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Necessary for Userinterface BOXwise Mobile

Get: QuantityOrdered(self: OutboundOrderLine) -> Decimal

Set: QuantityOrdered(self: OutboundOrderLine)=value
"""

 QuantityPackable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: QuantityPackable(self: OutboundOrderLine) -> Decimal

"""

 QuantityPacked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: QuantityPacked(self: OutboundOrderLine) -> Decimal

"""

 QuantityPickable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The quantity that is pickable. This is calculated when the batchable salesorders are retrieved.
   After that the line will be batched and the property QuantityAllocated can be used.

Get: QuantityPickable(self: OutboundOrderLine) -> Decimal

Set: QuantityPickable(self: OutboundOrderLine)=value
"""

 QuantityPicked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The quantity left to be picked.

Get: QuantityPicked(self: OutboundOrderLine) -> Decimal

"""

 QuantityProcessed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: QuantityProcessed(self: OutboundOrderLine) -> Decimal

"""

 QuantityToDeliver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Necessary for Userinterface BOXwise Mobile

Get: QuantityToDeliver(self: OutboundOrderLine) -> Decimal

Set: QuantityToDeliver(self: OutboundOrderLine)=value
"""

 QuantityToDeliverOriginal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is used by picking process to be able to revert a pick to original state.

Get: QuantityToDeliverOriginal(self: OutboundOrderLine) -> Decimal

Set: QuantityToDeliverOriginal(self: OutboundOrderLine)=value
"""

 RequestedDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: RequestedDate(self: OutboundOrderLine) -> DateTime

Set: RequestedDate(self: OutboundOrderLine)=value
"""

 ShowInBatch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ShowInBatch(self: OutboundOrderLine) -> bool

Set: ShowInBatch(self: OutboundOrderLine)=value
"""

 StockAssigned=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: StockAssigned(self: OutboundOrderLine) -> bool

Set: StockAssigned(self: OutboundOrderLine)=value
"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Type(self: OutboundOrderLine) -> OutboundOrderTypeEnum

"""

 UnitCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: UnitCode(self: OutboundOrderLine) -> str

Set: UnitCode(self: OutboundOrderLine)=value
"""

 VatCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: VatCode(self: OutboundOrderLine) -> str

Set: VatCode(self: OutboundOrderLine)=value
"""

 Warehouse=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Warehouse(self: OutboundOrderLine) -> str

Set: Warehouse(self: OutboundOrderLine)=value
"""

 WarehouseLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: WarehouseLocation(self: OutboundOrderLine) -> str

Set: WarehouseLocation(self: OutboundOrderLine)=value
"""



class HistoryOutboundOrderLine(OutboundOrderLine):
 """ HistoryOutboundOrderLine() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HistoryOutboundOrderLine()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 OrderId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderId(self: HistoryOutboundOrderLine) -> int

Set: OrderId(self: HistoryOutboundOrderLine)=value
"""

 QuantityDelivered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: QuantityDelivered(self: HistoryOutboundOrderLine) -> Decimal

Set: QuantityDelivered(self: HistoryOutboundOrderLine)=value
"""

 ShipmentId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ShipmentId(self: HistoryOutboundOrderLine) -> int

Set: ShipmentId(self: HistoryOutboundOrderLine)=value
"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Type(self: HistoryOutboundOrderLine) -> OutboundOrderTypeEnum

"""



class OutboundOrderLines(FindableList):
 """ OutboundOrderLines() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return OutboundOrderLines()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
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

Get: IsDisposable(self: OutboundOrderLines) -> bool

"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PreserveState(self: OutboundOrderLines) -> bool

"""


 DisplayMember='ItemCode'
 ValueMember='Id'


class HistoryOutboundOrderLines(OutboundOrderLines):
 """ HistoryOutboundOrderLines() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HistoryOutboundOrderLines()
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
 DisplayMember='ItemCode'
 ValueMember='Id'


class HistoryOutboundOrders(FindableList):
 """ HistoryOutboundOrders() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HistoryOutboundOrders()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Add(self,*__args):
  """
  Add(self: HistoryOutboundOrders,order: HistoryOutboundOrder) -> FindableList[HistoryOutboundOrder]
  Add(self: HistoryOutboundOrders,order: HistoryOutboundOrder,predicate: Predicate[HistoryOutboundOrder])
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
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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
 TotalRowsMatched=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: TotalRowsMatched(self: HistoryOutboundOrders) -> Int64

Set: TotalRowsMatched(self: HistoryOutboundOrders)=value
"""


 DisplayMember='Number'
 ValueMember='DbKey'


class OutboundOrder(DbObject):
 """  """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return OutboundOrder()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Clone(self):
  """ Clone(self: OutboundOrder) -> object """
  pass
 def Equals(self,obj):
  """ Equals(self: OutboundOrder,obj: object) -> bool """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: OutboundOrder) -> int """
  pass
 def GetHashCodeOfCustomer(self):
  """ GetHashCodeOfCustomer(self: OutboundOrder) -> int """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 AllowPartialDelivery=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: AllowPartialDelivery(self: OutboundOrder) -> PartialDeliveryTypeEnum

Set: AllowPartialDelivery(self: OutboundOrder)=value
"""

 AllowPartialDeliveryAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: AllowPartialDeliveryAsString(self: OutboundOrder) -> str

"""

 Backorder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Backorder(self: OutboundOrder) -> bool

Set: Backorder(self: OutboundOrder)=value
"""

 CustomerAddressLine1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerAddressLine1(self: OutboundOrder) -> str

Set: CustomerAddressLine1(self: OutboundOrder)=value
"""

 CustomerAddressLine2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerAddressLine2(self: OutboundOrder) -> str

Set: CustomerAddressLine2(self: OutboundOrder)=value
"""

 CustomerAddressLine3=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerAddressLine3(self: OutboundOrder) -> str

Set: CustomerAddressLine3(self: OutboundOrder)=value
"""

 CustomerCity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Necessary for Userinterface BOXwise Mobile

Get: CustomerCity(self: OutboundOrder) -> str

Set: CustomerCity(self: OutboundOrder)=value
"""

 CustomerContact=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerContact(self: OutboundOrder) -> str

Set: CustomerContact(self: OutboundOrder)=value
"""

 CustomerContactEmail=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerContactEmail(self: OutboundOrder) -> str

Set: CustomerContactEmail(self: OutboundOrder)=value
"""

 CustomerCountryCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Necessary for Userinterface BOXwise Mobile

Get: CustomerCountryCode(self: OutboundOrder) -> str

Set: CustomerCountryCode(self: OutboundOrder)=value
"""

 CustomerCountryName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerCountryName(self: OutboundOrder) -> str

Set: CustomerCountryName(self: OutboundOrder)=value
"""

 CustomerEoriNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerEoriNumber(self: OutboundOrder) -> str

Set: CustomerEoriNumber(self: OutboundOrder)=value
"""

 CustomerInvoiceAddressLine1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceAddressLine1(self: OutboundOrder) -> str

Set: CustomerInvoiceAddressLine1(self: OutboundOrder)=value
"""

 CustomerInvoiceAddressLine2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceAddressLine2(self: OutboundOrder) -> str

Set: CustomerInvoiceAddressLine2(self: OutboundOrder)=value
"""

 CustomerInvoiceAddressLine3=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceAddressLine3(self: OutboundOrder) -> str

Set: CustomerInvoiceAddressLine3(self: OutboundOrder)=value
"""

 CustomerInvoiceCity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceCity(self: OutboundOrder) -> str

Set: CustomerInvoiceCity(self: OutboundOrder)=value
"""

 CustomerInvoiceContact=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceContact(self: OutboundOrder) -> str

Set: CustomerInvoiceContact(self: OutboundOrder)=value
"""

 CustomerInvoiceContactEmail=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceContactEmail(self: OutboundOrder) -> str

Set: CustomerInvoiceContactEmail(self: OutboundOrder)=value
"""

 CustomerInvoiceCountryCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceCountryCode(self: OutboundOrder) -> str

Set: CustomerInvoiceCountryCode(self: OutboundOrder)=value
"""

 CustomerInvoiceCountryName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceCountryName(self: OutboundOrder) -> str

Set: CustomerInvoiceCountryName(self: OutboundOrder)=value
"""

 CustomerInvoiceName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceName(self: OutboundOrder) -> str

Set: CustomerInvoiceName(self: OutboundOrder)=value
"""

 CustomerInvoiceNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceNumber(self: OutboundOrder) -> str

Set: CustomerInvoiceNumber(self: OutboundOrder)=value
"""

 CustomerInvoicePhoneNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoicePhoneNumber(self: OutboundOrder) -> str

Set: CustomerInvoicePhoneNumber(self: OutboundOrder)=value
"""

 CustomerInvoiceState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceState(self: OutboundOrder) -> str

Set: CustomerInvoiceState(self: OutboundOrder)=value
"""

 CustomerInvoiceZipCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerInvoiceZipCode(self: OutboundOrder) -> str

Set: CustomerInvoiceZipCode(self: OutboundOrder)=value
"""

 CustomerName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Necessary for Userinterface BOXwise Mobile

Get: CustomerName(self: OutboundOrder) -> str

Set: CustomerName(self: OutboundOrder)=value
"""

 CustomerNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerNumber(self: OutboundOrder) -> str

Set: CustomerNumber(self: OutboundOrder)=value
"""

 CustomerPackageSlipLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerPackageSlipLayout(self: OutboundOrder) -> str

Set: CustomerPackageSlipLayout(self: OutboundOrder)=value
"""

 CustomerPhoneNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerPhoneNumber(self: OutboundOrder) -> str

Set: CustomerPhoneNumber(self: OutboundOrder)=value
"""

 CustomerReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerReference(self: OutboundOrder) -> str

Set: CustomerReference(self: OutboundOrder)=value
"""

 CustomerState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerState(self: OutboundOrder) -> str

Set: CustomerState(self: OutboundOrder)=value
"""

 CustomerZipCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerZipCode(self: OutboundOrder) -> str

Set: CustomerZipCode(self: OutboundOrder)=value
"""

 CustomFields=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomFields(self: OutboundOrder) -> SerializableDictionary[str,object]

Set: CustomFields(self: OutboundOrder)=value
"""

 DateOfDelivery=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DateOfDelivery(self: OutboundOrder) -> DateTime

Set: DateOfDelivery(self: OutboundOrder)=value
"""

 DateOrdered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DateOrdered(self: OutboundOrder) -> DateTime

Set: DateOrdered(self: OutboundOrder)=value
"""

 DeliverableOrderlines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DeliverableOrderlines(self: OutboundOrder) -> int

Set: DeliverableOrderlines(self: OutboundOrder)=value
"""

 DeliveryMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Necessary for Userinterface BOXwise Mobile

Get: DeliveryMethod(self: OutboundOrder) -> str

Set: DeliveryMethod(self: OutboundOrder)=value
"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Description(self: OutboundOrder) -> str

Set: Description(self: OutboundOrder)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Necessary for Userinterface BOXwise Mobile

Get: Id(self: OutboundOrder) -> int

Set: Id(self: OutboundOrder)=value
"""

 LineBackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: LineBackColor(self: OutboundOrder) -> str

Set: LineBackColor(self: OutboundOrder)=value
"""

 LineForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: LineForeColor(self: OutboundOrder) -> str

Set: LineForeColor(self: OutboundOrder)=value
"""

 Notes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Notes(self: OutboundOrder) -> str

Set: Notes(self: OutboundOrder)=value
"""

 Number=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Necessary for Userinterface BOXwise Mobile

Get: Number(self: OutboundOrder) -> str

Set: Number(self: OutboundOrder)=value
"""

 OrderAmountDeliverable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderAmountDeliverable(self: OutboundOrder) -> Decimal

Set: OrderAmountDeliverable(self: OutboundOrder)=value
"""

 OrderAmountTotal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderAmountTotal(self: OutboundOrder) -> Decimal

Set: OrderAmountTotal(self: OutboundOrder)=value
"""

 PendingItemCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PendingItemCount(self: OutboundOrder) -> int

"""

 PendingItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PendingItems(self: OutboundOrder) -> Dictionary[str,Decimal]

Set: PendingItems(self: OutboundOrder)=value
"""

 PendingItemUnitCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PendingItemUnitCount(self: OutboundOrder) -> Decimal

"""

 PendingOrderLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PendingOrderLines(self: OutboundOrder) -> int

Set: PendingOrderLines(self: OutboundOrder)=value
"""

 PercentageDeliverableAmount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PercentageDeliverableAmount(self: OutboundOrder) -> int

Set: PercentageDeliverableAmount(self: OutboundOrder)=value
"""

 PercentageDeliverableLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PercentageDeliverableLines(self: OutboundOrder) -> int

Set: PercentageDeliverableLines(self: OutboundOrder)=value
"""

 PercentDeliverable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Percentage of the QuantityToDeliver that is deliverable

Get: PercentDeliverable(self: OutboundOrder) -> int

Set: PercentDeliverable(self: OutboundOrder)=value
"""

 ProjectCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ProjectCode(self: OutboundOrder) -> str

Set: ProjectCode(self: OutboundOrder)=value
"""

 ProjectName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ProjectName(self: OutboundOrder) -> str

Set: ProjectName(self: OutboundOrder)=value
"""

 RoutingCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: RoutingCode(self: OutboundOrder) -> str

Set: RoutingCode(self: OutboundOrder)=value
"""

 SelectionCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: SelectionCode(self: OutboundOrder) -> str

Set: SelectionCode(self: OutboundOrder)=value
"""

 SelectionCodeDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: SelectionCodeDescription(self: OutboundOrder) -> str

Set: SelectionCodeDescription(self: OutboundOrder)=value
"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Tag(self: OutboundOrder) -> Tag

Set: Tag(self: OutboundOrder)=value
"""

 TotalOrderlines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: TotalOrderlines(self: OutboundOrder) -> int

Set: TotalOrderlines(self: OutboundOrder)=value
"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Type(self: OutboundOrder) -> OutboundOrderTypeEnum

"""

 Warehouse=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Necessary for Userinterface BOXwise Mobile

Get: Warehouse(self: OutboundOrder) -> str

Set: Warehouse(self: OutboundOrder)=value
"""



class OutboundOrderLineEqualityComparer(object):
 """ OutboundOrderLineEqualityComparer() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return OutboundOrderLineEqualityComparer()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Equals(self,*__args):
  """ Equals(self: OutboundOrderLineEqualityComparer,x: OutboundOrderLine,y: OutboundOrderLine) -> bool """
  pass
 def GetHashCode(self,obj=None):
  """ GetHashCode(self: OutboundOrderLineEqualityComparer,obj: OutboundOrderLine) -> int """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass

class OutboundOrders(FindableList):
 """ OutboundOrders() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return OutboundOrders()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Add(self,*__args):
  """
  Add(self: OutboundOrders,order: OutboundOrder) -> FindableList[OutboundOrder]
  Add(self: OutboundOrders,order: OutboundOrder,predicate: Predicate[OutboundOrder])
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
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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
 TotalRowsMatched=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: TotalRowsMatched(self: OutboundOrders) -> Int64

Set: TotalRowsMatched(self: OutboundOrders)=value
"""


 DisplayMember='Number'
 ValueMember='Id'


class OutboundOrderTypeEnum:
 """ enum OutboundOrderTypeEnum,values: ReplenishmentOrder (2),RtvOrder (3),SalesOrder (1) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return OutboundOrderTypeEnum()
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
 ReplenishmentOrder=None
 RtvOrder=None
 SalesOrder=None
 value__=None


class PickDifferenceOptionsEnum:
 """ enum PickDifferenceOptionsEnum,values: BasedOnMarkAsPicked (1),BasedOnNonePickedItems (2),None (0) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PickDifferenceOptionsEnum()
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
 BasedOnMarkAsPicked=None
 BasedOnNonePickedItems=None
 None_ =None
 value__=None


class ValidateItemIdentificationArgs(object):
 """
 ValidateItemIdentificationArgs()
 ValidateItemIdentificationArgs(itemCode: str,number: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ValidateItemIdentificationArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,itemCode=None,number=None):
  """
  __new__(cls: type)
  __new__(cls: type,itemCode: str,number: str)
  """
  pass
 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemCode(self: ValidateItemIdentificationArgs) -> str

Set: ItemCode(self: ValidateItemIdentificationArgs)=value
"""

 Number=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Number(self: ValidateItemIdentificationArgs) -> str

Set: Number(self: ValidateItemIdentificationArgs)=value
"""



# variables with complex values

