# encoding: utf-8
# module Wms.RemotingObjects.ColliRegistration calls itself ColliRegistration
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ColloReference:
    """
    ColloReference()
    ColloReference(reference: str, type: ReferenceType)
    ColloReference(reference: str, type: ReferenceType, warehouseCode: str, warehouseLocationCode: str, itemCode: str, quantity: Decimal)
    ColloReference(reference: str, type: ReferenceType, warehouseCode: str, warehouseLocationCode: str, itemCode: str, quantity: Decimal, itemId: str)
    """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return ColloReference()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    def Clone(self):
        """ Clone(self: ColloReference) -> object """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ColloReference) -> int """
        pass

    def ToString(self):
        """ ToString(self: ColloReference) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, reference=None, type=None, warehouseCode=None, warehouseLocationCode=None, itemCode=None, quantity=None, itemId=None):
        """
        __new__(cls: type)
        __new__(cls: type, reference: str, type: ReferenceType)
        __new__(cls: type, reference: str, type: ReferenceType, warehouseCode: str, warehouseLocationCode: str, itemCode: str, quantity: Decimal)
        __new__(cls: type, reference: str, type: ReferenceType, warehouseCode: str, warehouseLocationCode: str, itemCode: str, quantity: Decimal, itemId: str)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ColliPresetId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The chosen preset of this reference

Get: ColliPresetId(self: ColloReference) -> str

Set: ColliPresetId(self: ColloReference) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ItemCode(self: ColloReference) -> str

Set: ItemCode(self: ColloReference) = value
"""

    ItemIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Optional. The serial or batch numbers on this reference.

Get: ItemIds(self: ColloReference) -> ItemIdentifications

Set: ItemIds(self: ColloReference) = value
"""

    OrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderNumber(self: ColloReference) -> str

Set: OrderNumber(self: ColloReference) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Parent(self: ColloReference) -> str

Set: Parent(self: ColloReference) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Quantity(self: ColloReference) -> Decimal

Set: Quantity(self: ColloReference) = value
"""

    Reference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Reference(self: ColloReference) -> str

Set: Reference(self: ColloReference) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Type(self: ColloReference) -> ReferenceType

Set: Type(self: ColloReference) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: WarehouseCode(self: ColloReference) -> str

Set: WarehouseCode(self: ColloReference) = value
"""

    WarehouseLocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: WarehouseLocationCode(self: ColloReference) -> str

Set: WarehouseLocationCode(self: ColloReference) = value
"""



class ColloReferencePair():
    """
    ColloReferencePair(itemCode: str, warehouseCode: str, warehouseLocationCode: str)
    ColloReferencePair(outer: ColloReference, inner: ColloReference)
    """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return ColloReferencePair()
    instance = ZZZ()
    """hardcoded/returns an instance of the class"""
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, itemCode: str, warehouseCode: str, warehouseLocationCode: str)
        __new__(cls: type, outer: ColloReference, inner: ColloReference)
        """
        pass

    InnerReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerReference(self: ColloReferencePair) -> str

Set: InnerReference(self: ColloReferencePair) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: ColloReferencePair) -> str

Set: ItemCode(self: ColloReferencePair) = value
"""

    ItemIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIds(self: ColloReferencePair) -> ItemIdentifications

Set: ItemIds(self: ColloReferencePair) = value
"""

    OrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderNumber(self: ColloReferencePair) -> str

Set: OrderNumber(self: ColloReferencePair) = value
"""

    OuterReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OuterReference(self: ColloReferencePair) -> str

Set: OuterReference(self: ColloReferencePair) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: ColloReferencePair) -> Decimal

Set: Quantity(self: ColloReferencePair) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: ColloReferencePair) -> str

Set: WarehouseCode(self: ColloReferencePair) = value
"""

    WarehouseLocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseLocationCode(self: ColloReferencePair) -> str

Set: WarehouseLocationCode(self: ColloReferencePair) = value
"""



class ReferenceType:
    """ enum ReferenceType, values: Inner (0), Outer (1) """
    def ZZZ(self):
        """hardcoded/mock instance of the class"""
        return ReferenceType()
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

    Inner = None
    Outer = None
    value__ = None


