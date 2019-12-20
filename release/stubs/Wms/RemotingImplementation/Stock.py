from Wms.RemotingImplementation.TaskScheduler import TaskBase
from System import Object
from System import Exception
# encoding: utf-8
# module Wms.RemotingImplementation.Stock calls itself Stock
# from Wms.RemotingImplementation, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AllocatedStockArgs():
    """ AllocatedStockArgs() """
    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: AllocatedStockArgs) -> str

Set: ItemCode(self: AllocatedStockArgs) = value
"""

    ItemDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemDescription(self: AllocatedStockArgs) -> str

Set: ItemDescription(self: AllocatedStockArgs) = value
"""

    ItemIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIds(self: AllocatedStockArgs) -> ItemIdentifications

Set: ItemIds(self: AllocatedStockArgs) = value
"""

    LineNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineNumber(self: AllocatedStockArgs) -> str

Set: LineNumber(self: AllocatedStockArgs) = value
"""

    OrderId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderId(self: AllocatedStockArgs) -> str

Set: OrderId(self: AllocatedStockArgs) = value
"""

    OrderLineId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderLineId(self: AllocatedStockArgs) -> str

Set: OrderLineId(self: AllocatedStockArgs) = value
"""

    OrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderNumber(self: AllocatedStockArgs) -> str

Set: OrderNumber(self: AllocatedStockArgs) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: AllocatedStockArgs) -> Decimal

Set: Quantity(self: AllocatedStockArgs) = value
"""

    ReferenceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceId(self: AllocatedStockArgs) -> AllocatedStockItemReference

Set: ReferenceId(self: AllocatedStockArgs) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: AllocatedStockArgs) -> str

Set: WarehouseCode(self: AllocatedStockArgs) = value
"""

    WarehouseLocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseLocationCode(self: AllocatedStockArgs) -> str

Set: WarehouseLocationCode(self: AllocatedStockArgs) = value
"""


    Instance = AllocatedStockArgs()
    """hardcoded/returns an instance of the class"""

class AddAllocatedStockArgs(AllocatedStockArgs):
    """ AddAllocatedStockArgs() """
    IsItemIdentificationItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsItemIdentificationItem(self: AddAllocatedStockArgs) -> bool

Set: IsItemIdentificationItem(self: AddAllocatedStockArgs) = value
"""

    ItemIdentificationRegistration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIdentificationRegistration(self: AddAllocatedStockArgs) -> ItemIdentificationRegistration

Set: ItemIdentificationRegistration(self: AddAllocatedStockArgs) = value
"""

    ItemIdentificationToAdd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIdentificationToAdd(self: AddAllocatedStockArgs) -> ItemIdentification

Set: ItemIdentificationToAdd(self: AddAllocatedStockArgs) = value
"""


    Instance = AddAllocatedStockArgs()
    """hardcoded/returns an instance of the class"""

class AllocationSettings():
    """ AllocationSettings() """
    def GetLocationsForLine(self, line, locs):
        """ GetLocationsForLine(self: AllocationSettings, line: OutboundOrderLine, locs: IEnumerable[ItemStock]) -> IEnumerable[ItemStock] """
        pass

    DecrementStock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DecrementStock(self: AllocationSettings) -> bool

Set: DecrementStock(self: AllocationSettings) = value
"""

    ExcludeBlockedItemIdentifications = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExcludeBlockedItemIdentifications(self: AllocationSettings) -> bool

Set: ExcludeBlockedItemIdentifications(self: AllocationSettings) = value
"""

    ForbiddenLocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForbiddenLocations(self: AllocationSettings) -> List[Location]

Set: ForbiddenLocations(self: AllocationSettings) = value
"""

    GetLocationsForLineDelegate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GetLocationsForLineDelegate(self: AllocationSettings) -> OnGetLocationsForLine

Set: GetLocationsForLineDelegate(self: AllocationSettings) = value
"""

    IgnoreAllocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IgnoreAllocations(self: AllocationSettings) -> bool

Set: IgnoreAllocations(self: AllocationSettings) = value
"""

    IgnoreBlockedForInboundLocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IgnoreBlockedForInboundLocations(self: AllocationSettings) -> bool

Set: IgnoreBlockedForInboundLocations(self: AllocationSettings) = value
"""

    IgnoreBlockedForOutboundLocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IgnoreBlockedForOutboundLocations(self: AllocationSettings) -> bool

Set: IgnoreBlockedForOutboundLocations(self: AllocationSettings) = value
"""

    LocationSelectionAlgorithm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationSelectionAlgorithm(self: AllocationSettings) -> LocationSelectionAlgorithmType

Set: LocationSelectionAlgorithm(self: AllocationSettings) = value
"""

    OnDecreaseStockWithAssignedStock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnDecreaseStockWithAssignedStock(self: AllocationSettings) -> DecreaseStockWithAssignedStock

Set: OnDecreaseStockWithAssignedStock(self: AllocationSettings) = value
"""

    PickTypesToInclude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickTypesToInclude(self: AllocationSettings) -> LocationPickTypeEnum

Set: PickTypesToInclude(self: AllocationSettings) = value
"""


    DecreaseStockWithAssignedStock = None
    OnGetLocationsForLine = None

    Instance = AllocationSettings()
    """hardcoded/returns an instance of the class"""

class BatchAllocationSink(Object):
    """
    BatchAllocationSink()
    BatchAllocationSink(generatePick2PlaceImage: bool, preferredColumns: int)
    BatchAllocationSink(args: BatchAllocationSinkArgs)
    """
    def AddLine(self, *__args):
        """ AddLine(self: BatchAllocationSink, line: OutboundOrderLine, loc: ItemStock)AddLine(self: BatchAllocationSink, orderLine: OutboundOrderLine, location: ItemStock, allocation: AllocatedStockItem) """
        pass

    def CommitMutations(self):
        """ CommitMutations(self: BatchAllocationSink) """
        pass

    def CreateBatch(self, tag):
        """ CreateBatch(self: BatchAllocationSink, tag: object) -> Batch """
        pass

    def GetBatch(self, line, loc):
        """ GetBatch(self: BatchAllocationSink, line: OutboundOrderLine, loc: ItemStock) -> Batch """
        pass

    def GetBatchByTag(self, tag):
        """ GetBatchByTag(self: BatchAllocationSink, tag: object) -> Batch """
        pass

    def GetReferenceId(self, line, loc):
        """ GetReferenceId(self: BatchAllocationSink, line: OutboundOrderLine, loc: ItemStock) -> AllocatedStockItemReference """
        pass

    def RemoveBatchByTag(self, tag):
        """ RemoveBatchByTag(self: BatchAllocationSink, tag: object) """
        pass

    def SyncOrderLineWithAllocation(self, orderLine, allocation):
        """ SyncOrderLineWithAllocation(self: BatchAllocationSink, orderLine: OutboundOrderLine, allocation: AllocatedStockItem) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, generatePick2PlaceImage: bool, preferredColumns: int)
        __new__(cls: type, args: BatchAllocationSinkArgs)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Batches = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Batches(self: BatchAllocationSink) -> Batches

Set: Batches(self: BatchAllocationSink) = value
"""

    DefaultBatch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultBatch(self: BatchAllocationSink) -> Batch

Set: DefaultBatch(self: BatchAllocationSink) = value
"""

    GetBatchDelegate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GetBatchDelegate(self: BatchAllocationSink) -> OnGetBatch

Set: GetBatchDelegate(self: BatchAllocationSink) = value
"""


    OnGetBatch = None

    Instance = BatchAllocationSink()
    """hardcoded/returns an instance of the class"""

class BatchAllocationSinkArgs():
    """ BatchAllocationSinkArgs() """
    GeneratePick2PlaceImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeneratePick2PlaceImage(self: BatchAllocationSinkArgs) -> bool

Set: GeneratePick2PlaceImage(self: BatchAllocationSinkArgs) = value
"""

    PreferredColumns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreferredColumns(self: BatchAllocationSinkArgs) -> int

Set: PreferredColumns(self: BatchAllocationSinkArgs) = value
"""

    ProcessingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProcessingMode(self: BatchAllocationSinkArgs) -> BatchPackProcessingModeEnum

Set: ProcessingMode(self: BatchAllocationSinkArgs) = value
"""


    Instance = BatchAllocationSinkArgs()
    """hardcoded/returns an instance of the class"""

class BatchSink(BatchAllocationSink):
    """
    BatchSink()
    BatchSink(args: BatchAllocationSinkArgs)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, args=None):
        """
        __new__(cls: type)
        __new__(cls: type, args: BatchAllocationSinkArgs)
        """
        pass

    Instance = BatchSink()
    """hardcoded/returns an instance of the class"""

class DefaultPrintAllocationSettings(AllocationSettings):
    """ DefaultPrintAllocationSettings() """
    Instance = DefaultPrintAllocationSettings()
    """hardcoded/returns an instance of the class"""

class EnhancedStockAllocater(Object):
    """
    EnhancedStockAllocater(stockManager: IStockManager)
    EnhancedStockAllocater(stockManager: IStockManager, settings: AllocationSettings, allocationSink: IAllocationSink)
    """
    def AllocateLine(self, line):
        """ AllocateLine(self: EnhancedStockAllocater, line: OutboundOrderLine) -> bool """
        pass

    def AllocateLines(self, lines):
        """ AllocateLines(self: EnhancedStockAllocater, lines: IEnumerable[OutboundOrderLine]) """
        pass

    def DeAllocateStockAllocation(self, allocation):
        """ DeAllocateStockAllocation(self: EnhancedStockAllocater, allocation: ItemStockAllocation) """
        pass

    def Dispose(self):
        """ Dispose(self: EnhancedStockAllocater) """
        pass

    def ReAllocateItems(self, referenceId, itemCode, warehouseCode, outboundOrderLines, overwriteAllocation):
        """ ReAllocateItems(self: EnhancedStockAllocater, referenceId: AllocatedStockItemReference, itemCode: str, warehouseCode: str, outboundOrderLines: OutboundOrderLines, overwriteAllocation: bool) """
        pass

    def UpdateAllocationForLine(self, line, warehouseLocationCode, deltaQuantity, itemIdNumber, useAssignedNumber):
        """ UpdateAllocationForLine(self: EnhancedStockAllocater, line: OutboundOrderLine, warehouseLocationCode: str, deltaQuantity: Decimal, itemIdNumber: str, useAssignedNumber: bool) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, stockManager, settings=None, allocationSink=None):
        """
        __new__(cls: type, stockManager: IStockManager)
        __new__(cls: type, stockManager: IStockManager, settings: AllocationSettings, allocationSink: IAllocationSink)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AllocationSink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllocationSink(self: EnhancedStockAllocater) -> IAllocationSink

Set: AllocationSink(self: EnhancedStockAllocater) = value
"""

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Settings(self: EnhancedStockAllocater) -> AllocationSettings

Set: Settings(self: EnhancedStockAllocater) = value
"""


    Instance = EnhancedStockAllocater()
    """hardcoded/returns an instance of the class"""

class EnhancedStockManager(Object):
    """
    EnhancedStockManager(messaging: IMessaging)
    EnhancedStockManager()
    """
    def AllocateOutboundOrderLine(self, item, allocationSettings, allocationSink):
        """ AllocateOutboundOrderLine(self: EnhancedStockManager, item: KeyValuePair[str, List[OutboundOrderLine]], allocationSettings: AllocationSettings, allocationSink: IAllocationSink) """
        pass

    def AllocateOutboundOrderLines(self, orderLines, allocationSettings, allocationSink):
        """ AllocateOutboundOrderLines(self: EnhancedStockManager, orderLines: IEnumerable[OutboundOrderLine], allocationSettings: AllocationSettings, allocationSink: IAllocationSink) -> bool """
        pass

    def ChangeStock(self, itemCode, location, qty, *__args):
        """ ChangeStock(self: EnhancedStockManager, itemCode: str, location: Location, qty: Decimal, swallowErrors: bool)ChangeStock(self: EnhancedStockManager, itemCode: str, location: Location, qty: Decimal, itemIds: ItemIdentifications, swallowErrors: bool) """
        pass

    def ClearAllocatedStock(self):
        """ ClearAllocatedStock(self: EnhancedStockManager) """
        pass

    def ConsolidateAllocations(self, oldReferenceId, newReferenceId, orderLine, itemLocation):
        """ ConsolidateAllocations(self: EnhancedStockManager, oldReferenceId: AllocatedStockItemReference, newReferenceId: AllocatedStockItemReference, orderLine: OutboundOrderLine, itemLocation: BatchItemLocationBase) """
        pass

    def DeAllocateStock(self, *__args):
        """
        DeAllocateStock(self: EnhancedStockManager, referenceId: AllocatedStockItemReference) -> int
        DeAllocateStock(self: EnhancedStockManager, referenceId: AllocatedStockItemReference, orderLine: OutboundOrderLine, itemLocation: BatchItemLocationBase)DeAllocateStock(self: EnhancedStockManager, allocation: ItemStockAllocation)DeAllocateStock(self: EnhancedStockManager, args: AllocatedStockArgs) -> int
        """
        pass

    def FindFreeStock(self, itemCode, selector, excludeBlockedItemIds, type, referenceId, includeAssignedLines):
        """ FindFreeStock(self: EnhancedStockManager, itemCode: str, selector: Func[ItemStock, bool], excludeBlockedItemIds: bool, type: AssignedItemIdsFilterType, referenceId: AllocatedStockItemReference, includeAssignedLines: bool) -> List[ItemStock] """
        pass

    def FindItemStockAllocations(self, itemCode, selector):
        """ FindItemStockAllocations(self: EnhancedStockManager, itemCode: str, selector: Func[AllocatedStockItem, bool]) -> ItemStockAllocationList """
        pass

    def FindStockAndAllocations(self, *__args):
        """
        FindStockAndAllocations(self: EnhancedStockManager, itemCode: str, stockSelector: Func[ItemStock, bool]) -> List[ItemStockWithAllocations]
        FindStockAndAllocations(self: EnhancedStockManager, filterBy: GetStockManagerListArgs) -> IEnumerable[ItemStockWithAllocations]
        """
        pass

    def FulfillDirectOrderLines(self, directOrder):
        """ FulfillDirectOrderLines(self: EnhancedStockManager, directOrder: DirectOrder) """
        pass

    def FulfillOutboundOrderLines(self, lines, deAllocateStock, adjustStock):
        """ FulfillOutboundOrderLines(self: EnhancedStockManager, lines: IEnumerable[OutboundOrderLine], deAllocateStock: bool, adjustStock: bool) """
        pass

    def GetAllItemIdentifications(self, filterBy):
        """ GetAllItemIdentifications(self: EnhancedStockManager, filterBy: GetAllItemIdentificationsArgs) -> ItemIdentifications """
        pass

    def GetAvailableItemIdsOnLocationIncludingAllocated(self, referenceId, args):
        """ GetAvailableItemIdsOnLocationIncludingAllocated(self: EnhancedStockManager, referenceId: AllocatedStockItemReference, args: GetItemIdentificationArgs) -> ItemIdentifications """
        pass

    def GetBatchableOrderLines(self, input, settings, batchable, nonBatchable):
        """ GetBatchableOrderLines(self: EnhancedStockManager, input: IEnumerable[OutboundOrderLine], settings: AllocationSettings) -> (List[OutboundOrderLine], List[OutboundOrderLine]) """
        pass

    def GetStockAllocator(self, settings, allocationSink):
        """ GetStockAllocator(self: EnhancedStockManager, settings: AllocationSettings, allocationSink: IAllocationSink) -> IStockAllocater """
        pass

    def GetStockByFilter(self, filterBy):
        """ GetStockByFilter(self: EnhancedStockManager, filterBy: GetStockManagerListArgs) -> IEnumerable[ItemStock] """
        pass

    def GetStockOnMatchingFilter(self, filterBy):
        """ GetStockOnMatchingFilter(self: EnhancedStockManager, filterBy: GetStockManagerListArgs) -> IEnumerable[ItemStock] """
        pass

    def GetStockTotals(self, itemCode, warehouseCode):
        """ GetStockTotals(self: EnhancedStockManager, itemCode: str, warehouseCode: str) -> ItemStockTotals """
        pass

    def GetValidPickLocations(self, settings, warehouseCode, itemCode):
        """ GetValidPickLocations(self: EnhancedStockManager, settings: AllocationSettings, warehouseCode: str, itemCode: str) -> ItemStockList """
        pass

    def IsAllocated(self, orderId, lineId, itemCode, referenceIds):
        """ IsAllocated(self: EnhancedStockManager, orderId: Nullable[int], lineId: Nullable[int], itemCode: str) -> (bool, List[AllocatedStockItemReference]) """
        pass

    def MergeErpStock(self, list):
        """ MergeErpStock(self: EnhancedStockManager, list: IEnumerable[ItemStock]) """
        pass

    def ReAllocateItems(self, referenceId, itemCode, warehouseCode, outboundOrderLines, overwriteAllocation):
        """ ReAllocateItems(self: EnhancedStockManager, referenceId: AllocatedStockItemReference, itemCode: str, warehouseCode: str, outboundOrderLines: OutboundOrderLines, overwriteAllocation: bool) """
        pass

    def ReAllocateStock(self, args):
        """ ReAllocateStock(self: EnhancedStockManager, args: ReallocateStockArgs) """
        pass

    def SetGeneral(self, general):
        """ SetGeneral(self: EnhancedStockManager, general: IGeneral) """
        pass

    def TransferItems(self, transfer):
        """ TransferItems(self: EnhancedStockManager, transfer: WarehouseTransfer) """
        pass

    def TryAllocateItemOnLocation(self, args, errorMessage):
        """ TryAllocateItemOnLocation(self: EnhancedStockManager, args: AddAllocatedStockArgs) -> (bool, str) """
        pass

    def UpdateAllocationForOutboundOrderLine(self, line, warehouseLocationCode, quantity, itemIdNumber, useAssignedNumber, allocationSink, allocationSettings):
        """ UpdateAllocationForOutboundOrderLine(self: EnhancedStockManager, line: OutboundOrderLine, warehouseLocationCode: str, quantity: Decimal, itemIdNumber: str, useAssignedNumber: bool, allocationSink: IAllocationSink, allocationSettings: AllocationSettings) -> bool """
        pass

    def ValidateLocation(self, referenceId, warehouseCode, warehouseLocationCode, itemCode, itemIdNumber):
        """ ValidateLocation(self: EnhancedStockManager, referenceId: AllocatedStockItemReference, warehouseCode: str, warehouseLocationCode: str, itemCode: str, itemIdNumber: str) -> Decimal """
        pass

    def ValidateProcessQuantity(self, orderLinesPairs, message):
        """ ValidateProcessQuantity(self: EnhancedStockManager, orderLinesPairs: Dictionary[OutboundOrder, OutboundOrderLines]) -> (bool, str) """
        pass

    def ValidateStockForTransferQuantityOnLocationFrom(self, item, referenceId, message):
        """ ValidateStockForTransferQuantityOnLocationFrom(self: EnhancedStockManager, item: WarehouseTransferItem, referenceId: AllocatedStockItemReference) -> (bool, str) """
        pass

    def Where(self, *__args):
        """
        Where(self: EnhancedStockManager, selector: Func[ItemStock, bool]) -> List[ItemStock]
        Where(self: EnhancedStockManager, filterBy: GetStockManagerListArgs) -> List[ItemStock]
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, messaging=None):
        """
        __new__(cls: type, messaging: IMessaging)
        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Instance = EnhancedStockManager()
    """hardcoded/returns an instance of the class"""

class IAllocationSink(Object):
    # no doc
    def AddLine(self, *__args):
        """ AddLine(self: IAllocationSink, line: OutboundOrderLine, loc: ItemStock)AddLine(self: IAllocationSink, orderLine: OutboundOrderLine, location: ItemStock, allocation: AllocatedStockItem) """
        pass

    def CommitMutations(self):
        """ CommitMutations(self: IAllocationSink) """
        pass

    def GetReferenceId(self, line, loc):
        """ GetReferenceId(self: IAllocationSink, line: OutboundOrderLine, loc: ItemStock) -> AllocatedStockItemReference """
        pass

    def SyncOrderLineWithAllocation(self, orderLine, allocation):
        """ SyncOrderLineWithAllocation(self: IAllocationSink, orderLine: OutboundOrderLine, allocation: AllocatedStockItem) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Instance = IAllocationSink()
    """hardcoded/returns an instance of the class"""

class IStockAllocater(Object):
    # no doc
    def AllocateLines(self, lines):
        """ AllocateLines(self: IStockAllocater, lines: IEnumerable[OutboundOrderLine]) """
        pass

    def DeAllocateStockAllocation(self, allocation):
        """ DeAllocateStockAllocation(self: IStockAllocater, allocation: ItemStockAllocation) """
        pass

    def ReAllocateItems(self, referenceId, itemCode, warehouseCode, outboundOrderLines, overwriteAllocation):
        """ ReAllocateItems(self: IStockAllocater, referenceId: AllocatedStockItemReference, itemCode: str, warehouseCode: str, outboundOrderLines: OutboundOrderLines, overwriteAllocation: bool) """
        pass

    def UpdateAllocationForLine(self, line, warehouseLocationCode, deltaQuantity, itemIdNumber, useAssignedNumber):
        """ UpdateAllocationForLine(self: IStockAllocater, line: OutboundOrderLine, warehouseLocationCode: str, deltaQuantity: Decimal, itemIdNumber: str, useAssignedNumber: bool) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AllocationSink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllocationSink(self: IStockAllocater) -> IAllocationSink

Set: AllocationSink(self: IStockAllocater) = value
"""

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Settings(self: IStockAllocater) -> AllocationSettings

Set: Settings(self: IStockAllocater) = value
"""


    Instance = IStockAllocater()
    """hardcoded/returns an instance of the class"""

class IStockManager(Object):
    # no doc
    def AllocateOutboundOrderLines(self, orderLines, allocationSettings, allocationSink):
        """ AllocateOutboundOrderLines(self: IStockManager, orderLines: IEnumerable[OutboundOrderLine], allocationSettings: AllocationSettings, allocationSink: IAllocationSink) -> bool """
        pass

    def ChangeStock(self, itemCode, location, qty, *__args):
        """ ChangeStock(self: IStockManager, itemCode: str, location: Location, qty: Decimal, swallowErrors: bool)ChangeStock(self: IStockManager, itemCode: str, location: Location, qty: Decimal, itemIds: ItemIdentifications, swallowErrors: bool) """
        pass

    def ClearAllocatedStock(self):
        """ ClearAllocatedStock(self: IStockManager) """
        pass

    def ConsolidateAllocations(self, oldReferenceId, newReferenceId, orderLine, itemLocation):
        """ ConsolidateAllocations(self: IStockManager, oldReferenceId: AllocatedStockItemReference, newReferenceId: AllocatedStockItemReference, orderLine: OutboundOrderLine, itemLocation: BatchItemLocationBase) """
        pass

    def DeAllocateStock(self, *__args):
        """
        DeAllocateStock(self: IStockManager, referenceId: AllocatedStockItemReference) -> int
        DeAllocateStock(self: IStockManager, referenceId: AllocatedStockItemReference, orderLine: OutboundOrderLine, itemLocation: BatchItemLocationBase)DeAllocateStock(self: IStockManager, allocation: ItemStockAllocation)DeAllocateStock(self: IStockManager, args: AllocatedStockArgs) -> int
        """
        pass

    def FindFreeStock(self, itemCode, selector, excludeBlockedItemIds, type, referenceId, includeAssignedLines):
        """ FindFreeStock(self: IStockManager, itemCode: str, selector: Func[ItemStock, bool], excludeBlockedItemIds: bool, type: AssignedItemIdsFilterType, referenceId: AllocatedStockItemReference, includeAssignedLines: bool) -> List[ItemStock] """
        pass

    def FindItemStockAllocations(self, itemCode, selector):
        """ FindItemStockAllocations(self: IStockManager, itemCode: str, selector: Func[AllocatedStockItem, bool]) -> ItemStockAllocationList """
        pass

    def FindStockAndAllocations(self, *__args):
        """
        FindStockAndAllocations(self: IStockManager, filterBy: GetStockManagerListArgs) -> IEnumerable[ItemStockWithAllocations]
        FindStockAndAllocations(self: IStockManager, itemCode: str, stockSelector: Func[ItemStock, bool]) -> List[ItemStockWithAllocations]
        """
        pass

    def FulfillDirectOrderLines(self, directOrder):
        """ FulfillDirectOrderLines(self: IStockManager, directOrder: DirectOrder) """
        pass

    def FulfillOutboundOrderLines(self, lines, deAllocateStock, adjustStock):
        """ FulfillOutboundOrderLines(self: IStockManager, lines: IEnumerable[OutboundOrderLine], deAllocateStock: bool, adjustStock: bool) """
        pass

    def GetAllItemIdentifications(self, filterBy):
        """ GetAllItemIdentifications(self: IStockManager, filterBy: GetAllItemIdentificationsArgs) -> ItemIdentifications """
        pass

    def GetAvailableItemIdsOnLocationIncludingAllocated(self, referenceId, args):
        """ GetAvailableItemIdsOnLocationIncludingAllocated(self: IStockManager, referenceId: AllocatedStockItemReference, args: GetItemIdentificationArgs) -> ItemIdentifications """
        pass

    def GetBatchableOrderLines(self, input, settings, batchable, nonBatchable):
        """ GetBatchableOrderLines(self: IStockManager, input: IEnumerable[OutboundOrderLine], settings: AllocationSettings) -> (List[OutboundOrderLine], List[OutboundOrderLine]) """
        pass

    def GetStockAllocator(self, settings, allocationSink):
        """ GetStockAllocator(self: IStockManager, settings: AllocationSettings, allocationSink: IAllocationSink) -> IStockAllocater """
        pass

    def GetStockByFilter(self, filterBy):
        """ GetStockByFilter(self: IStockManager, filterBy: GetStockManagerListArgs) -> IEnumerable[ItemStock] """
        pass

    def GetStockOnMatchingFilter(self, args):
        """ GetStockOnMatchingFilter(self: IStockManager, args: GetStockManagerListArgs) -> IEnumerable[ItemStock] """
        pass

    def GetStockTotals(self, itemCode, warehouseCode):
        """ GetStockTotals(self: IStockManager, itemCode: str, warehouseCode: str) -> ItemStockTotals """
        pass

    def GetValidPickLocations(self, settings, warehouseCode, itemCode):
        """ GetValidPickLocations(self: IStockManager, settings: AllocationSettings, warehouseCode: str, itemCode: str) -> ItemStockList """
        pass

    def IsAllocated(self, orderId, lineId, itemCode, referenceIds):
        """ IsAllocated(self: IStockManager, orderId: Nullable[int], lineId: Nullable[int], itemCode: str) -> (bool, List[AllocatedStockItemReference]) """
        pass

    def MergeErpStock(self, list):
        """ MergeErpStock(self: IStockManager, list: IEnumerable[ItemStock]) """
        pass

    def ReAllocateItems(self, referenceId, itemCode, warehouseCode, outboundOrderLines, overwriteAllocation):
        """ ReAllocateItems(self: IStockManager, referenceId: AllocatedStockItemReference, itemCode: str, warehouseCode: str, outboundOrderLines: OutboundOrderLines, overwriteAllocation: bool) """
        pass

    def ReAllocateStock(self, args):
        """ ReAllocateStock(self: IStockManager, args: ReallocateStockArgs) """
        pass

    def SetGeneral(self, general):
        """ SetGeneral(self: IStockManager, general: IGeneral) """
        pass

    def TransferItems(self, transfer):
        """ TransferItems(self: IStockManager, transfer: WarehouseTransfer) """
        pass

    def TryAllocateItemOnLocation(self, args, errorMessage):
        """ TryAllocateItemOnLocation(self: IStockManager, args: AddAllocatedStockArgs) -> (bool, str) """
        pass

    def UpdateAllocationForOutboundOrderLine(self, line, warehouseLocationCode, deltaQuantity, itemIdNumber, useAssignedNumber, allocationSink, allocationSettings):
        """ UpdateAllocationForOutboundOrderLine(self: IStockManager, line: OutboundOrderLine, warehouseLocationCode: str, deltaQuantity: Decimal, itemIdNumber: str, useAssignedNumber: bool, allocationSink: IAllocationSink, allocationSettings: AllocationSettings) -> bool """
        pass

    def ValidateLocation(self, referenceId, warehouseCode, warehouseLocationCode, itemCode, itemIdNumber):
        """ ValidateLocation(self: IStockManager, referenceId: AllocatedStockItemReference, warehouseCode: str, warehouseLocationCode: str, itemCode: str, itemIdNumber: str) -> Decimal """
        pass

    def ValidateProcessQuantity(self, orderLinesPairs, message):
        """ ValidateProcessQuantity(self: IStockManager, orderLinesPairs: Dictionary[OutboundOrder, OutboundOrderLines]) -> (bool, str) """
        pass

    def ValidateStockForTransferQuantityOnLocationFrom(self, item, referenceId, message):
        """ ValidateStockForTransferQuantityOnLocationFrom(self: IStockManager, item: WarehouseTransferItem, referenceId: AllocatedStockItemReference) -> (bool, str) """
        pass

    def Where(self, selector):
        """ Where(self: IStockManager, selector: Func[ItemStock, bool]) -> List[ItemStock] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Instance = IStockManager()
    """hardcoded/returns an instance of the class"""

class ItemStockAllocationExtensions():
    # no doc
    @staticmethod
    def EnrichWithBatchData(this, batchNames, orderNumbers, lineNumbers, barcodes):
        """ EnrichWithBatchData(this: ItemStockAllocationList, batchNames: Dictionary[str, str], orderNumbers: Dictionary[str, str], lineNumbers: Dictionary[str, str], barcodes: Dictionary[str, str]) """
        pass

    @staticmethod
    def EnrichWithDirectOrderData(this):
        """ EnrichWithDirectOrderData(this: ItemStockAllocationList) """
        pass

    @staticmethod
    def EnrichWithMessageQueueData(this):
        """ EnrichWithMessageQueueData(this: ItemStockAllocationList) """
        pass

    __all__ = [
        'EnrichWithBatchData',
        'EnrichWithDirectOrderData',
        'EnrichWithMessageQueueData',
    ]

    Instance = ItemStockAllocationExtensions()
    """hardcoded/returns an instance of the class"""

class LocationSelectionAlgorithmType(Object):
    """ enum LocationSelectionAlgorithmType, values: AlphabeticSort (1), AlphabeticSortBulkFirst (2), LeastLocations (0), LeastLocationsBulkFirst (3) """
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

    AlphabeticSort = None
    AlphabeticSortBulkFirst = None
    LeastLocations = None
    LeastLocationsBulkFirst = None
    value__ = None

    Instance = LocationSelectionAlgorithmType()
    """hardcoded/returns an instance of the class"""

class LockException(Exception):
    """ LockException(message: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message):
        """ __new__(cls: type, message: str) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None

    Instance = LockException()
    """hardcoded/returns an instance of the class"""

class MessageQueueAllocationSink(Object):
    """ MessageQueueAllocationSink(messageReferenceId: Nullable[Guid]) """
    def AddLine(self, *__args):
        """ AddLine(self: MessageQueueAllocationSink, line: OutboundOrderLine, loc: ItemStock)AddLine(self: MessageQueueAllocationSink, orderLine: OutboundOrderLine, location: ItemStock, allocation: AllocatedStockItem) """
        pass

    def CommitMutations(self):
        """ CommitMutations(self: MessageQueueAllocationSink) """
        pass

    def GetReferenceId(self, line, loc):
        """ GetReferenceId(self: MessageQueueAllocationSink, line: OutboundOrderLine, loc: ItemStock) -> AllocatedStockItemReference """
        pass

    def SyncOrderLineWithAllocation(self, orderLine, allocation):
        """ SyncOrderLineWithAllocation(self: MessageQueueAllocationSink, orderLine: OutboundOrderLine, allocation: AllocatedStockItem) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, messageReferenceId):
        """ __new__(cls: type, messageReferenceId: Nullable[Guid]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Instance = MessageQueueAllocationSink()
    """hardcoded/returns an instance of the class"""

class MessageQueueStockAllocater(Object):
    """ MessageQueueStockAllocater(stockManager: IStockManager, settings: AllocationSettings, allocationSink: IAllocationSink) """
    def AllocateLine(self, line):
        """ AllocateLine(self: MessageQueueStockAllocater, line: OutboundOrderLine) -> bool """
        pass

    def AllocateLines(self, lines):
        """ AllocateLines(self: MessageQueueStockAllocater, lines: IEnumerable[OutboundOrderLine]) """
        pass

    def DeAllocateStockAllocation(self, allocation):
        """ DeAllocateStockAllocation(self: MessageQueueStockAllocater, allocation: ItemStockAllocation) """
        pass

    def Dispose(self):
        """ Dispose(self: MessageQueueStockAllocater) """
        pass

    def ReAllocateItems(self, referenceId, itemCode, warehouseCode, outboundOrderLines, overwriteAllocation):
        """ ReAllocateItems(self: MessageQueueStockAllocater, referenceId: AllocatedStockItemReference, itemCode: str, warehouseCode: str, outboundOrderLines: OutboundOrderLines, overwriteAllocation: bool) """
        pass

    def UpdateAllocationForLine(self, line, warehouseLocationCode, deltaQuantity, itemIdNumber, useAssignedNumber):
        """ UpdateAllocationForLine(self: MessageQueueStockAllocater, line: OutboundOrderLine, warehouseLocationCode: str, deltaQuantity: Decimal, itemIdNumber: str, useAssignedNumber: bool) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, stockManager, settings, allocationSink):
        """ __new__(cls: type, stockManager: IStockManager, settings: AllocationSettings, allocationSink: IAllocationSink) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AllocationSink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllocationSink(self: MessageQueueStockAllocater) -> IAllocationSink

Set: AllocationSink(self: MessageQueueStockAllocater) = value
"""

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Settings(self: MessageQueueStockAllocater) -> AllocationSettings

Set: Settings(self: MessageQueueStockAllocater) = value
"""


    Instance = MessageQueueStockAllocater()
    """hardcoded/returns an instance of the class"""

class ReallocateStockArgs():
    """ ReallocateStockArgs() """
    AllocationSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllocationSettings(self: ReallocateStockArgs) -> AllocationSettings

Set: AllocationSettings(self: ReallocateStockArgs) = value
"""

    OrderLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderLine(self: ReallocateStockArgs) -> OutboundOrderLine

Set: OrderLine(self: ReallocateStockArgs) = value
"""

    PickLoc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickLoc(self: ReallocateStockArgs) -> ItemPickLocation

Set: PickLoc(self: ReallocateStockArgs) = value
"""

    ReferenceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceId(self: ReallocateStockArgs) -> str

Set: ReferenceId(self: ReallocateStockArgs) = value
"""

    WarehouseCodeTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCodeTo(self: ReallocateStockArgs) -> str

Set: WarehouseCodeTo(self: ReallocateStockArgs) = value
"""

    WarehouseLocationCodeTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseLocationCodeTo(self: ReallocateStockArgs) -> str

Set: WarehouseLocationCodeTo(self: ReallocateStockArgs) = value
"""


    Instance = ReallocateStockArgs()
    """hardcoded/returns an instance of the class"""

class StockLock(Object):
    """
    StockLock()
    StockLock(exclusive: bool)
    """
    def Dispose(self):
        """ Dispose(self: StockLock) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, exclusive=None):
        """
        __new__(cls: type)
        __new__(cls: type, exclusive: bool)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Instance = StockLock()
    """hardcoded/returns an instance of the class"""

class StockStreamTask(TaskBase):
    """ StockStreamTask(settings: SystemSettings) """
    def Run(self):
        """ Run(self: StockStreamTask) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, settings):
        """ __new__(cls: type, settings: SystemSettings) """
        pass

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Settings(self: StockStreamTask) -> SystemSettings

Set: Settings(self: StockStreamTask) = value
"""


    Instance = StockStreamTask()
    """hardcoded/returns an instance of the class"""

