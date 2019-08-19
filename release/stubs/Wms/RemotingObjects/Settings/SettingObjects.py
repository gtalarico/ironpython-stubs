from System.Collections.Generic import *
from Wms.RemotingObjects import *
# encoding: utf-8
# module Wms.RemotingObjects.Settings.SettingObjects calls itself SettingObjects
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class MyList(FindableList):
    """ MyList() """
    def ToString(self):
        """ ToString(self: MyList) -> str """
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

    def __str__(self, *args): #cannot find CLR method
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return MyList()

class OrderFlowLink():
    """ OrderFlowLink(orderFlowOption: OrderFlowOption, orderSelectionCode: str, orderSelectionDescription: str, Color: str) """
    @staticmethod # known case of __new__
    def __new__(self, orderFlowOption, orderSelectionCode, orderSelectionDescription, Color):
        """ __new__(cls: type, orderFlowOption: OrderFlowOption, orderSelectionCode: str, orderSelectionDescription: str, Color: str) """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Color(self: OrderFlowLink) -> str

Set: Color(self: OrderFlowLink) = value
"""

    OrderFlowOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderFlowOption(self: OrderFlowLink) -> OrderFlowOption

Set: OrderFlowOption(self: OrderFlowLink) = value
"""

    OrderSelectionCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderSelectionCode(self: OrderFlowLink) -> str

Set: OrderSelectionCode(self: OrderFlowLink) = value
"""

    OrderSelectionDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderSelectionDescription(self: OrderFlowLink) -> str

Set: OrderSelectionDescription(self: OrderFlowLink) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return OrderFlowLink()

class OrderFlowLinks(List):
    """ OrderFlowLinks() """
    def DeleteLinksThatAreNotEqual(self, SelectionCodes):
        """ DeleteLinksThatAreNotEqual(self: OrderFlowLinks, SelectionCodes: Array[str]) """
        pass

    def GetLinkBySelectionCode(self, Code):
        """ GetLinkBySelectionCode(self: OrderFlowLinks, Code: str) -> OrderFlowLink """
        pass

    def ToString(self):
        """ ToString(self: OrderFlowLinks) -> str """
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

    def __str__(self, *args): #cannot find CLR method
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return OrderFlowLinks()

class OrderFlowOption:
    """ enum OrderFlowOption, values: FulFill (2), FulFillPrintInvoice (1), PrintInvoiceFulFill (0) """
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

    FulFill = None
    FulFillPrintInvoice = None
    PrintInvoiceFulFill = None
    value__ = None

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return OrderFlowOption()

class ShippperServiceLink():
    """ ShippperServiceLink(ShipperId: str, ServiceId: str, DeliveryMethodCode: str, DeliveryMethodName: str, Color: str) """
    @staticmethod # known case of __new__
    def __new__(self, ShipperId, ServiceId, DeliveryMethodCode, DeliveryMethodName, Color):
        """ __new__(cls: type, ShipperId: str, ServiceId: str, DeliveryMethodCode: str, DeliveryMethodName: str, Color: str) """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Color(self: ShippperServiceLink) -> str

Set: Color(self: ShippperServiceLink) = value
"""

    DeliveryMethodCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DeliveryMethodCode(self: ShippperServiceLink) -> str

Set: DeliveryMethodCode(self: ShippperServiceLink) = value
"""

    DeliveryMethodName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DeliveryMethodName(self: ShippperServiceLink) -> str

Set: DeliveryMethodName(self: ShippperServiceLink) = value
"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Enabled(self: ShippperServiceLink) -> bool

Set: Enabled(self: ShippperServiceLink) = value
"""

    ServiceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ServiceId(self: ShippperServiceLink) -> str

Set: ServiceId(self: ShippperServiceLink) = value
"""

    ShipperId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ShipperId(self: ShippperServiceLink) -> str

Set: ShipperId(self: ShippperServiceLink) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ShippperServiceLink()

class ShippperServiceLinks(List):
    """ ShippperServiceLinks() """
    def DeliveryMethodCodes(self):
        """ DeliveryMethodCodes(self: ShippperServiceLinks) -> List[str] """
        pass

    def DisableLinksWithServiceIds(self, ServiceIds):
        """ DisableLinksWithServiceIds(self: ShippperServiceLinks, ServiceIds: List[str]) """
        pass

    def GetByDeliveryMethodCode(self, DeliveryMethodCode):
        """ GetByDeliveryMethodCode(self: ShippperServiceLinks, DeliveryMethodCode: str) -> ShippperServiceLink """
        pass

    def GetColorForService(self, ServiceId):
        """ GetColorForService(self: ShippperServiceLinks, ServiceId: str) -> str """
        pass

    def ServiceIds(self, ShipperId):
        """ ServiceIds(self: ShippperServiceLinks, ShipperId: str) -> List[str] """
        pass

    def ShipperIds(self):
        """ ShipperIds(self: ShippperServiceLinks) -> List[str] """
        pass

    def ToString(self):
        """ ToString(self: ShippperServiceLinks) -> str """
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

    def __str__(self, *args): #cannot find CLR method
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ShippperServiceLinks()

