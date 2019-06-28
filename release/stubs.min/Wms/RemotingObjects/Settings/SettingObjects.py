# encoding: utf-8
# module Wms.RemotingObjects.Settings.SettingObjects calls itself SettingObjects
# from Wms.RemotingObjects,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class MyList:
 """ MyList() """
 def ToString(self):
  """ ToString(self: MyList) -> str """
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
 def __str__(self,*args):
  pass

class OrderFlowLink:
 """ OrderFlowLink(orderFlowOption: OrderFlowOption,orderSelectionCode: str,orderSelectionDescription: str,Color: str) """
 @staticmethod
 def __new__(self,orderFlowOption,orderSelectionCode,orderSelectionDescription,Color):
  """ __new__(cls: type,orderFlowOption: OrderFlowOption,orderSelectionCode: str,orderSelectionDescription: str,Color: str) """
  pass
 Color=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Color(self: OrderFlowLink) -> str

Set: Color(self: OrderFlowLink)=value
"""

 OrderFlowOption=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OrderFlowOption(self: OrderFlowLink) -> OrderFlowOption

Set: OrderFlowOption(self: OrderFlowLink)=value
"""

 OrderSelectionCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OrderSelectionCode(self: OrderFlowLink) -> str

Set: OrderSelectionCode(self: OrderFlowLink)=value
"""

 OrderSelectionDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OrderSelectionDescription(self: OrderFlowLink) -> str

Set: OrderSelectionDescription(self: OrderFlowLink)=value
"""



class OrderFlowLinks:
 """ OrderFlowLinks() """
 def DeleteLinksThatAreNotEqual(self,SelectionCodes):
  """ DeleteLinksThatAreNotEqual(self: OrderFlowLinks,SelectionCodes: Array[str]) """
  pass
 def GetLinkBySelectionCode(self,Code):
  """ GetLinkBySelectionCode(self: OrderFlowLinks,Code: str) -> OrderFlowLink """
  pass
 def ToString(self):
  """ ToString(self: OrderFlowLinks) -> str """
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
 def __str__(self,*args):
  pass

class OrderFlowOption:
 """ enum OrderFlowOption,values: FulFill (2),FulFillPrintInvoice (1),PrintInvoiceFulFill (0) """
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
 FulFill=None
 FulFillPrintInvoice=None
 PrintInvoiceFulFill=None
 value__=None


class ShippperServiceLink:
 """ ShippperServiceLink(ShipperId: str,ServiceId: str,DeliveryMethodCode: str,DeliveryMethodName: str,Color: str) """
 @staticmethod
 def __new__(self,ShipperId,ServiceId,DeliveryMethodCode,DeliveryMethodName,Color):
  """ __new__(cls: type,ShipperId: str,ServiceId: str,DeliveryMethodCode: str,DeliveryMethodName: str,Color: str) """
  pass
 Color=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Color(self: ShippperServiceLink) -> str

Set: Color(self: ShippperServiceLink)=value
"""

 DeliveryMethodCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DeliveryMethodCode(self: ShippperServiceLink) -> str

Set: DeliveryMethodCode(self: ShippperServiceLink)=value
"""

 DeliveryMethodName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DeliveryMethodName(self: ShippperServiceLink) -> str

Set: DeliveryMethodName(self: ShippperServiceLink)=value
"""

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Enabled(self: ShippperServiceLink) -> bool

Set: Enabled(self: ShippperServiceLink)=value
"""

 ServiceId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ServiceId(self: ShippperServiceLink) -> str

Set: ServiceId(self: ShippperServiceLink)=value
"""

 ShipperId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ShipperId(self: ShippperServiceLink) -> str

Set: ShipperId(self: ShippperServiceLink)=value
"""



class ShippperServiceLinks:
 """ ShippperServiceLinks() """
 def DeliveryMethodCodes(self):
  """ DeliveryMethodCodes(self: ShippperServiceLinks) -> List[str] """
  pass
 def DisableLinksWithServiceIds(self,ServiceIds):
  """ DisableLinksWithServiceIds(self: ShippperServiceLinks,ServiceIds: List[str]) """
  pass
 def GetByDeliveryMethodCode(self,DeliveryMethodCode):
  """ GetByDeliveryMethodCode(self: ShippperServiceLinks,DeliveryMethodCode: str) -> ShippperServiceLink """
  pass
 def GetColorForService(self,ServiceId):
  """ GetColorForService(self: ShippperServiceLinks,ServiceId: str) -> str """
  pass
 def ServiceIds(self,ShipperId):
  """ ServiceIds(self: ShippperServiceLinks,ShipperId: str) -> List[str] """
  pass
 def ShipperIds(self):
  """ ShipperIds(self: ShippperServiceLinks) -> List[str] """
  pass
 def ToString(self):
  """ ToString(self: ShippperServiceLinks) -> str """
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
 def __str__(self,*args):
  pass

