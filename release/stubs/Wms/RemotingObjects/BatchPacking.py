from System import Object
# encoding: utf-8
# module Wms.RemotingObjects.BatchPacking calls itself BatchPacking
# from Wms.RemotingObjects, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ItemPackScanArgs():
    """ ItemPackScanArgs(cacheKey: CacheKey, barcode: str, packageGuid: Guid) """
    @staticmethod # known case of __new__
    def __new__(self, cacheKey, barcode, packageGuid):
        """ __new__(cls: type, cacheKey: CacheKey, barcode: str, packageGuid: Guid) """
        pass

    Barcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Barcode(self: ItemPackScanArgs) -> str

"""

    CacheKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CacheKey(self: ItemPackScanArgs) -> CacheKey

"""

    PackageGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PackageGuid(self: ItemPackScanArgs) -> Guid

"""


    Instance = ItemPackScanArgs()
    """hardcoded/returns an instance of the class"""

class MoveAction(Object):
    """ enum MoveAction, values: Ignore (0), MoveBetweenColli (3), Pack (1), Unpack (2) """
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

    Ignore = None
    MoveBetweenColli = None
    Pack = None
    Unpack = None
    value__ = None

    Instance = MoveAction()
    """hardcoded/returns an instance of the class"""

class MoveTransportItemsBetweenTransportPackagesArgs():
    """
    MoveTransportItemsBetweenTransportPackagesArgs()
    MoveTransportItemsBetweenTransportPackagesArgs(moveArgs: MoveTransportPackageItemsArgs, itemsToPackArgs: GetItemsToPackArgs)
    """
    @staticmethod # known case of __new__
    def __new__(self, moveArgs=None, itemsToPackArgs=None):
        """
        __new__(cls: type)
        __new__(cls: type, moveArgs: MoveTransportPackageItemsArgs, itemsToPackArgs: GetItemsToPackArgs)
        """
        pass

    Action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Action(self: MoveTransportItemsBetweenTransportPackagesArgs) -> MoveAction

Set: Action(self: MoveTransportItemsBetweenTransportPackagesArgs) = value
"""

    ItemsPacked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemsPacked(self: MoveTransportItemsBetweenTransportPackagesArgs) -> TransportPackages

Set: ItemsPacked(self: MoveTransportItemsBetweenTransportPackagesArgs) = value
"""

    ItemsToPack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemsToPack(self: MoveTransportItemsBetweenTransportPackagesArgs) -> TransportItems

Set: ItemsToPack(self: MoveTransportItemsBetweenTransportPackagesArgs) = value
"""

    ItemsToPackArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemsToPackArgs(self: MoveTransportItemsBetweenTransportPackagesArgs) -> GetItemsToPackArgs

Set: ItemsToPackArgs(self: MoveTransportItemsBetweenTransportPackagesArgs) = value
"""

    MoveArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MoveArgs(self: MoveTransportItemsBetweenTransportPackagesArgs) -> MoveTransportPackageItemsArgs

Set: MoveArgs(self: MoveTransportItemsBetweenTransportPackagesArgs) = value
"""


    Instance = MoveTransportItemsBetweenTransportPackagesArgs()
    """hardcoded/returns an instance of the class"""

class MoveTransportPackageItemsArgs():
    """
    MoveTransportPackageItemsArgs()
    MoveTransportPackageItemsArgs(cacheKey: CacheKey, fromBoxGuid: Guid, toBoxGuid: Guid)
    MoveTransportPackageItemsArgs(cacheKey: CacheKey, fromBoxGuid: Guid, toBoxGuid: Guid, transportItems: TransportItems)
    """
    @staticmethod
    def Validate(args):
        """ Validate(args: MoveTransportPackageItemsArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cacheKey=None, fromBoxGuid=None, toBoxGuid=None, transportItems=None):
        """
        __new__(cls: type)
        __new__(cls: type, cacheKey: CacheKey, fromBoxGuid: Guid, toBoxGuid: Guid)
        __new__(cls: type, cacheKey: CacheKey, fromBoxGuid: Guid, toBoxGuid: Guid, transportItems: TransportItems)
        """
        pass

    CacheKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CacheKey(self: MoveTransportPackageItemsArgs) -> CacheKey

Set: CacheKey(self: MoveTransportPackageItemsArgs) = value
"""

    FromBoxGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FromBoxGuid(self: MoveTransportPackageItemsArgs) -> Guid

Set: FromBoxGuid(self: MoveTransportPackageItemsArgs) = value
"""

    OrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderNumber(self: MoveTransportPackageItemsArgs) -> str

Set: OrderNumber(self: MoveTransportPackageItemsArgs) = value
"""

    ToBoxGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToBoxGuid(self: MoveTransportPackageItemsArgs) -> Guid

Set: ToBoxGuid(self: MoveTransportPackageItemsArgs) = value
"""

    TransportItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransportItems(self: MoveTransportPackageItemsArgs) -> TransportItems

Set: TransportItems(self: MoveTransportPackageItemsArgs) = value
"""


    Instance = MoveTransportPackageItemsArgs()
    """hardcoded/returns an instance of the class"""

class ProcessBatchPackingArgs():
    """ ProcessBatchPackingArgs() """
    CacheKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CacheKey(self: ProcessBatchPackingArgs) -> CacheKey

Set: CacheKey(self: ProcessBatchPackingArgs) = value
"""

    ValidateStock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ValidateStock(self: ProcessBatchPackingArgs) -> Nullable[bool]

Set: ValidateStock(self: ProcessBatchPackingArgs) = value
"""


    Instance = ProcessBatchPackingArgs()
    """hardcoded/returns an instance of the class"""

class ScanItemPackArgsResult():
    """ ScanItemPackArgsResult() """
    BarcodeStructure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BarcodeStructure(self: ScanItemPackArgsResult) -> BarcodeStructure

Set: BarcodeStructure(self: ScanItemPackArgsResult) = value
"""

    ResultType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResultType(self: ScanItemPackArgsResult) -> ScanItemPackResultType

Set: ResultType(self: ScanItemPackArgsResult) = value
"""

    ScanResult = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScanResult(self: ScanItemPackArgsResult) -> BarcodeStructureResultEnum

Set: ScanResult(self: ScanItemPackArgsResult) = value
"""


    Instance = ScanItemPackArgsResult()
    """hardcoded/returns an instance of the class"""

class ScanItemPackResultType(Object):
    """ enum ScanItemPackResultType, values: InnerReference (1), Item (0) """
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

    InnerReference = None
    Item = None
    value__ = None

    Instance = ScanItemPackResultType()
    """hardcoded/returns an instance of the class"""

class TransportPackageScanEnum(Object):
    """ enum TransportPackageScanEnum, values: None (0), Serial (2), SSCC (1) """
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

    None_ =None
    Serial = None
    SSCC = None
    value__ = None

    Instance = TransportPackageScanEnum()
    """hardcoded/returns an instance of the class"""

class TransportPackageScanResult():
    """ TransportPackageScanResult() """
    Barcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Barcode(self: TransportPackageScanResult) -> str

Set: Barcode(self: TransportPackageScanResult) = value
"""

    FaultMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FaultMessage(self: TransportPackageScanResult) -> str

Set: FaultMessage(self: TransportPackageScanResult) = value
"""

    MatchedScanOfType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MatchedScanOfType(self: TransportPackageScanResult) -> TransportPackageScanEnum

Set: MatchedScanOfType(self: TransportPackageScanResult) = value
"""


    Instance = TransportPackageScanResult()
    """hardcoded/returns an instance of the class"""
