from System import *
# encoding: utf-8
# module Wms.RemotingInterface calls itself RemotingInterface
# from Wms.RemotingInterface, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DataChangedEventHandler(MulticastDelegate):
    """ DataChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, callback, object):
        """ BeginInvoke(self: DataChangedEventHandler, sender: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not require arguments.
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DataChangedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender):
        """ Invoke(self: DataChangedEventHandler, sender: object) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return DataChangedEventHandler()

class IClientService:
    # no doc
    def BeepContinuous(self):
        """ BeepContinuous(self: IClientService) """
        pass

    def GetDeviceInformation(self):
        """ GetDeviceInformation(self: IClientService) -> DeviceInformation """
        pass

    def GetScreenshot(self):
        """ GetScreenshot(self: IClientService) -> Array[Byte] """
        pass

    def Ping(self):
        """ Ping(self: IClientService) """
        pass

    def ReceiveMessage(self, message):
        """ ReceiveMessage(self: IClientService, message: str) """
        pass

    def ReceiveQuestion(self, question, possibleAnswers):
        """ ReceiveQuestion(self: IClientService, question: str, possibleAnswers: int) -> AnswerOptionsEnum """
        pass

    def SendKey(self, key):
        """ SendKey(self: IClientService, key: str) """
        pass

    def SendMouseClick(self, x, y):
        """ SendMouseClick(self: IClientService, x: int, y: int) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return IClientService()

class IDefaultItemLocationHelper:
    # no doc
    def GetDefaultItemLocationsByItemCode(self, itemCode):
        """ GetDefaultItemLocationsByItemCode(self: IDefaultItemLocationHelper, itemCode: str) -> ResultObject[FindableList[WarehouseItemLocation]] """
        pass

    def GetItemLocationsByItemCode(self, itemCode, filter, defaultLocationsOnly):
        """ GetItemLocationsByItemCode(self: IDefaultItemLocationHelper, itemCode: str, filter: str, defaultLocationsOnly: bool) -> ResultObject[FindableList[WarehouseItemLocation]] """
        pass

    def UpdateDefaultItemLocation(self, dfObject):
        """ UpdateDefaultItemLocation(self: IDefaultItemLocationHelper, dfObject: DataFlowObject[UpdateItemDefaultLocationArgs]) -> DataFlowObject[UpdateItemDefaultLocationArgs] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return IDefaultItemLocationHelper()

class IDocumentQueue:
    # no doc
    def CopyPrintRule(self, printRuleId):
        """ CopyPrintRule(self: IDocumentQueue, printRuleId: int) -> PrintRule """
        pass

    def DeletePrintJobs(self, jobIds):
        """ DeletePrintJobs(self: IDocumentQueue, jobIds: Array[Guid]) """
        pass

    def DeletePrintRule(self, printRuleId):
        """ DeletePrintRule(self: IDocumentQueue, printRuleId: int) """
        pass

    def DeletePrintRules(self, ruleIds):
        """ DeletePrintRules(self: IDocumentQueue, ruleIds: List[int]) """
        pass

    def GetBlobContent(self, blobId):
        """ GetBlobContent(self: IDocumentQueue, blobId: int) -> BlobContent """
        pass

    def GetFileTypes(self):
        """ GetFileTypes(self: IDocumentQueue) -> List[DocumentTypeEnum] """
        pass

    def GetMatchingPrintRules(self, attributes):
        """ GetMatchingPrintRules(self: IDocumentQueue, attributes: SerializableDictionary[str, str]) -> List[int] """
        pass

    def GetOperators(self):
        """ GetOperators(self: IDocumentQueue) -> List[Operator] """
        pass

    def GetPrinterRules(self, args):
        """ GetPrinterRules(self: IDocumentQueue, args: GetPrinterRulesArgs) -> List[PrintRule] """
        pass

    def GetPrinters(self):
        """ GetPrinters(self: IDocumentQueue) -> List[Printer] """
        pass

    def GetPrintJobAttributes(self, printJobId):
        """ GetPrintJobAttributes(self: IDocumentQueue, printJobId: Guid) -> SerializableDictionary[str, str] """
        pass

    def GetPrintJobAuditLog(self, printJobId, paging):
        """ GetPrintJobAuditLog(self: IDocumentQueue, printJobId: Guid, paging: PagingParams) -> PagedList[PrintJobAuditLogEntry] """
        pass

    def GetPrintJobs(self, args, paging):
        """ GetPrintJobs(self: IDocumentQueue, args: GetPrintJobsArgs, paging: PagingParams) -> PagedList[QueuedPrintJob] """
        pass

    def GetPrintJobTypes(self):
        """ GetPrintJobTypes(self: IDocumentQueue) -> List[PrintJobType] """
        pass

    def GetPrintJobTypesOfConfiguredPrintRules(self):
        """ GetPrintJobTypesOfConfiguredPrintRules(self: IDocumentQueue) -> List[PrintJobType] """
        pass

    def GetPrintRuleConditions(self, printRuleId):
        """ GetPrintRuleConditions(self: IDocumentQueue, printRuleId: int) -> List[PrintRuleLine] """
        pass

    def GetUsedAttributeNames(self, args):
        """ GetUsedAttributeNames(self: IDocumentQueue, args: GetPrintJobAttributesArgs) -> List[PrintJobAttribute] """
        pass

    def GetUsedAttributeValues(self, attributeName):
        """ GetUsedAttributeValues(self: IDocumentQueue, attributeName: str) -> List[str] """
        pass

    def GetUsedAttributeValuesAsObject(self, attributeName):
        """ GetUsedAttributeValuesAsObject(self: IDocumentQueue, attributeName: str) -> List[AttributeValue] """
        pass

    def GetUsedPrintJobTypes(self):
        """ GetUsedPrintJobTypes(self: IDocumentQueue) -> List[PrintJobType] """
        pass

    def RedispatchPrintJob(self, jobId):
        """ RedispatchPrintJob(self: IDocumentQueue, jobId: Guid) """
        pass

    def RedispatchPrintJobWithPrinter(self, args):
        """ RedispatchPrintJobWithPrinter(self: IDocumentQueue, args: RedispatchPrintJobArgs) """
        pass

    def SavePrintRule(self, args):
        """ SavePrintRule(self: IDocumentQueue, args: PrintRule) -> PrintRule """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return IDocumentQueue()

class IGeneral:
    # no doc
    def AddOrUpdateErpLock(self, lock):
        """ AddOrUpdateErpLock(self: IGeneral, lock: ErpLock) -> int """
        pass

    def AddOrUpdateErpLockDirect(self, lock):
        """ AddOrUpdateErpLockDirect(self: IGeneral, lock: ErpLock) -> int """
        pass

    def AddUserToZone(self, zone, user):
        """ AddUserToZone(self: IGeneral, zone: Zone, user: User) -> bool """
        pass

    def AttachClient(self, endPoint):
        """ AttachClient(self: IGeneral, endPoint: str) """
        pass

    def AuthenticateUser(self, args, barcodeSettings):
        """ AuthenticateUser(self: IGeneral, args: AuthenticationArgs) -> (RemotingIdentity, BarcodeTypes) """
        pass

    def AuthenticateUserForFirstZone(self, remId):
        """ AuthenticateUserForFirstZone(self: IGeneral) -> (bool, RemotingIdentity) """
        pass

    def AuthenticateUserForZone(self, selectedZone, remId):
        """ AuthenticateUserForZone(self: IGeneral, selectedZone: Zone) -> (bool, RemotingIdentity) """
        pass

    def BeepContinuous(self, endPoint):
        """ BeepContinuous(self: IGeneral, endPoint: str) """
        pass

    def ChangeItemBarcode(self, args):
        """ ChangeItemBarcode(self: IGeneral, args: ChangeBarcodeArgs) -> bool """
        pass

    def CheckLicenseFile(self, xml, errors, license):
        """ CheckLicenseFile(self: IGeneral, xml: str) -> (bool, List[str], License) """
        pass

    def CheckServerHealth(self):
        """ CheckServerHealth(self: IGeneral) -> ServerHealthEnum """
        pass

    def CheckZoneRightAddReferenceOnTransfer(self, warehouseTransferKey):
        """ CheckZoneRightAddReferenceOnTransfer(self: IGeneral, warehouseTransferKey: CacheKey) -> bool """
        pass

    def CleanupUserCacheData(self):
        """ CleanupUserCacheData(self: IGeneral) """
        pass

    def ClearResourceCache(self):
        """ ClearResourceCache(self: IGeneral) """
        pass

    def CompileScript(self, script):
        """ CompileScript(self: IGeneral, script: str) -> List[PythonError] """
        pass

    def CreateBarcodeStructureDefinition(self, arg):
        """ CreateBarcodeStructureDefinition(self: IGeneral, arg: DataFlowObject[BarcodeStructureDefinition]) -> DataFlowObject[BarcodeStructureDefinition] """
        pass

    def CreateColliPreset(self, arg):
        """ CreateColliPreset(self: IGeneral, arg: DataFlowObject[ColliPreset]) -> DataFlowObject[ColliPreset] """
        pass

    def CreateDatabase(self, message):
        """ CreateDatabase(self: IGeneral) -> (bool, str) """
        pass

    def CreateLocationClassification(self, arg):
        """ CreateLocationClassification(self: IGeneral, arg: DataFlowObject[LocationClassification]) -> DataFlowObject[LocationClassification] """
        pass

    def CreateModule(self, arg):
        """ CreateModule(self: IGeneral, arg: ModuleArgs) -> bool """
        pass

    def CreateOrUpdateBackgroundAgent(self, arg):
        """ CreateOrUpdateBackgroundAgent(self: IGeneral, arg: DataFlowObject[BackgroundAgent]) -> DataFlowObject[BackgroundAgent] """
        pass

    def CreatePrintLabel(self, arg):
        """ CreatePrintLabel(self: IGeneral, arg: DataFlowObject[PrintLabel]) -> DataFlowObject[PrintLabel] """
        pass

    def CreateScript(self, arg):
        """ CreateScript(self: IGeneral, arg: DataFlowObject[ZoneScript]) -> DataFlowObject[ZoneScript] """
        pass

    def CreateScriptTask(self, arg):
        """ CreateScriptTask(self: IGeneral, arg: DataFlowObject[ScriptTask]) -> DataFlowObject[ScriptTask] """
        pass

    def CreateShipperServiceLink(self, arg):
        """ CreateShipperServiceLink(self: IGeneral, arg: DataFlowObject[ShipperServiceLink]) -> DataFlowObject[ShipperServiceLink] """
        pass

    def CreateSnippetModule(self, arg):
        """ CreateSnippetModule(self: IGeneral, arg: ModuleArgs) -> bool """
        pass

    def CreateStorageAssignmentClassification(self, arg):
        """ CreateStorageAssignmentClassification(self: IGeneral, arg: DataFlowObject[StorageAssignmentClassification]) -> DataFlowObject[StorageAssignmentClassification] """
        pass

    def CreateTag(self, arg):
        """ CreateTag(self: IGeneral, arg: DataFlowObject[Tag]) -> DataFlowObject[Tag] """
        pass

    def CreateUser(self, arg):
        """ CreateUser(self: IGeneral, arg: DataFlowObject[User]) -> DataFlowObject[User] """
        pass

    def CreateWarehouseLayoutSetting(self, arg):
        """ CreateWarehouseLayoutSetting(self: IGeneral, arg: DataFlowObject[WarehouseLayoutSetting]) -> DataFlowObject[WarehouseLayoutSetting] """
        pass

    def CreateZone(self, arg):
        """ CreateZone(self: IGeneral, arg: DataFlowObject[Zone]) -> DataFlowObject[Zone] """
        pass

    def DeleteBackgroundAgent(self, arg):
        """ DeleteBackgroundAgent(self: IGeneral, arg: DataFlowObject[BackgroundAgent]) -> DataFlowObject[BackgroundAgent] """
        pass

    def DeleteBarcodeStructureDefinition(self, arg):
        """ DeleteBarcodeStructureDefinition(self: IGeneral, arg: DataFlowObject[BarcodeStructureDefinition]) -> DataFlowObject[BarcodeStructureDefinition] """
        pass

    def DeleteColliPreset(self, arg):
        """ DeleteColliPreset(self: IGeneral, arg: DataFlowObject[ColliPreset]) -> DataFlowObject[ColliPreset] """
        pass

    def DeleteErpLock(self, lock):
        """ DeleteErpLock(self: IGeneral, lock: ErpLock) """
        pass

    def DeleteLocationClassification(self, arg):
        """ DeleteLocationClassification(self: IGeneral, arg: DataFlowObject[LocationClassification]) -> DataFlowObject[LocationClassification] """
        pass

    def DeleteModule(self, args):
        """ DeleteModule(self: IGeneral, args: ModuleArgs) -> bool """
        pass

    def DeletePrintLabel(self, arg):
        """ DeletePrintLabel(self: IGeneral, arg: DataFlowObject[PrintLabel]) -> DataFlowObject[PrintLabel] """
        pass

    def DeleteScript(self, arg):
        """ DeleteScript(self: IGeneral, arg: DataFlowObject[ZoneScript]) -> DataFlowObject[ZoneScript] """
        pass

    def DeleteScriptTask(self, arg):
        """ DeleteScriptTask(self: IGeneral, arg: DataFlowObject[ScriptTask]) -> DataFlowObject[ScriptTask] """
        pass

    def DeleteShipperServiceLink(self, arg):
        """ DeleteShipperServiceLink(self: IGeneral, arg: DataFlowObject[ShipperServiceLink]) -> DataFlowObject[ShipperServiceLink] """
        pass

    def DeleteStorageAssignmentClassification(self, arg):
        """ DeleteStorageAssignmentClassification(self: IGeneral, arg: DataFlowObject[StorageAssignmentClassification]) -> DataFlowObject[StorageAssignmentClassification] """
        pass

    def DeleteTag(self, arg):
        """ DeleteTag(self: IGeneral, arg: DataFlowObject[Tag]) -> DataFlowObject[Tag] """
        pass

    def DeleteUser(self, arg):
        """ DeleteUser(self: IGeneral, arg: DataFlowObject[User]) -> DataFlowObject[User] """
        pass

    def DeleteWarehouseLayoutSetting(self, arg):
        """ DeleteWarehouseLayoutSetting(self: IGeneral, arg: DataFlowObject[WarehouseLayoutSetting]) -> DataFlowObject[WarehouseLayoutSetting] """
        pass

    def DeleteZone(self, arg):
        """ DeleteZone(self: IGeneral, arg: DataFlowObject[Zone]) -> DataFlowObject[Zone] """
        pass

    def DiscardPrintLines(self, key):
        """ DiscardPrintLines(self: IGeneral, key: CacheKey) """
        pass

    def DisposeCachedObject(self, hashCode):
        """ DisposeCachedObject(self: IGeneral, hashCode: int) -> DataFlowObject[object] """
        pass

    def DisposeCachedObjects(self):
        """ DisposeCachedObjects(self: IGeneral) """
        pass

    def DisposeCachedObjectWhenUnchanged(self, key):
        """ DisposeCachedObjectWhenUnchanged(self: IGeneral, key: CacheKey) """
        pass

    def ExecuteScript(self, script):
        """ ExecuteScript(self: IGeneral, script: str) -> object """
        pass

    def ExecuteScriptTaskOnce(self, pythonScriptId):
        """ ExecuteScriptTaskOnce(self: IGeneral, pythonScriptId: int) -> object """
        pass

    def ExecuteScriptWithCacheObjectScope(self, script, cacheKey):
        """ ExecuteScriptWithCacheObjectScope(self: IGeneral, script: str, cacheKey: int) -> object """
        pass

    def ExecuteScriptWithScope(self, script, scope):
        """ ExecuteScriptWithScope(self: IGeneral, script: str, scope: Dictionary[str, object]) -> object """
        pass

    def FinishUploadModule(self, arg):
        """ FinishUploadModule(self: IGeneral, arg: ModuleArgs) -> bool """
        pass

    def GenerateSerialNumbers(self, dfObject, numbersGenerated):
        """ GenerateSerialNumbers(self: IGeneral, dfObject: DataFlowObject[ItemIdGenerateArgs]) -> (DataFlowObject[ItemIdGenerateArgs], List[str]) """
        pass

    def GetActiveColliPresets(self, colliPresets):
        """ GetActiveColliPresets(self: IGeneral) -> (int, ColliPresets) """
        pass

    def GetAppDomainList(self):
        """ GetAppDomainList(self: IGeneral) -> List[AppDomainInformation] """
        pass

    def GetBackgroundAgentById(self, id, agent):
        """ GetBackgroundAgentById(self: IGeneral, id: str) -> (bool, BackgroundAgent) """
        pass

    def GetBackgroundAgentsAll(self, agents):
        """ GetBackgroundAgentsAll(self: IGeneral) -> (int, BackgroundAgents) """
        pass

    def GetBackgroundAgentsByType(self, type, agents):
        """ GetBackgroundAgentsByType(self: IGeneral, type: BackgroundAgentType) -> (int, BackgroundAgents) """
        pass

    def GetBackgroundAgentStatusByType(self, type):
        """ GetBackgroundAgentStatusByType(self: IGeneral, type: BackgroundAgentType) -> BackgroundAgentStatus """
        pass

    def GetBarcodeSettingsAll(self, types):
        """ GetBarcodeSettingsAll(self: IGeneral) -> (int, BarcodeTypes) """
        pass

    def GetBarcodeStructure(self, value, expectedScan, barcodeStructure):
        """ GetBarcodeStructure(self: IGeneral, value: str, expectedScan: ExpectScanOfEnum) -> (BarcodeStructureResultEnum, BarcodeStructure) """
        pass

    def GetBarcodeStructureActive(self, definitions):
        """ GetBarcodeStructureActive(self: IGeneral) -> (int, BarcodeStructureDefinitions) """
        pass

    def GetBarcodeStructureDefinitionById(self, countId, definition):
        """ GetBarcodeStructureDefinitionById(self: IGeneral, countId: int) -> (bool, BarcodeStructureDefinition) """
        pass

    def GetBarcodeStructureDefinitions(self, filterBy, pagingParams, definitions):
        """ GetBarcodeStructureDefinitions(self: IGeneral, filterBy: BarcodeStructureDefinitionFilter, pagingParams: PagingParams) -> (int, BarcodeStructureDefinitions) """
        pass

    def GetBarcodeStructureInOrder(self, value, expectedScans, barcodeStructure):
        """ GetBarcodeStructureInOrder(self: IGeneral, value: str, expectedScans: List[ExpectScanOfEnum]) -> (BarcodeStructureResultEnum, BarcodeStructure) """
        pass

    def GetCacheObject(self, hashCode):
        """ GetCacheObject(self: IGeneral, hashCode: int) -> ICachable """
        pass

    def GetCacheObjectAsXml(self, hashCode):
        """ GetCacheObjectAsXml(self: IGeneral, hashCode: int) -> str """
        pass

    def GetChacheStatus(self):
        """ GetChacheStatus(self: IGeneral) -> str """
        pass

    def GetColliPresetById(self, id, colliPreset):
        """ GetColliPresetById(self: IGeneral, id: int) -> (bool, ColliPreset) """
        pass

    def GetColliPresetsAll(self, colliPresets):
        """ GetColliPresetsAll(self: IGeneral) -> (int, ColliPresets) """
        pass

    def GetColliPresetSpecificationCodes(self, searchText, colliPresets):
        """ GetColliPresetSpecificationCodes(self: IGeneral, searchText: str) -> (int, List[str]) """
        pass

    def GetCopyOfCache(self):
        """ GetCopyOfCache(self: IGeneral) -> List[ICachable] """
        pass

    def GetCountriesActive(self, countries):
        """ GetCountriesActive(self: IGeneral) -> (int, Countries) """
        pass

    def GetCurrentIdentity(self):
        """ GetCurrentIdentity(self: IGeneral) -> RemotingIdentity """
        pass

    def GetDefaultColliPreset(self, colliPreset):
        """ GetDefaultColliPreset(self: IGeneral) -> (bool, ColliPreset) """
        pass

    def GetDefaultInboundLocations(self, warehouseCode, locations):
        """ GetDefaultInboundLocations(self: IGeneral, warehouseCode: str) -> (bool, Locations) """
        pass

    def GetDeviceInformation(self, endPoint, deviceInfo):
        """ GetDeviceInformation(self: IGeneral, endPoint: str) -> (bool, DeviceInformation) """
        pass

    def GetDevicesAll(self, devices):
        """ GetDevicesAll(self: IGeneral) -> (int, Devices) """
        pass

    def GetErpLocks(self, locks):
        """ GetErpLocks(self: IGeneral) -> (int, List[ErpLock]) """
        pass

    def GetErpName(self):
        """ GetErpName(self: IGeneral) -> str """
        pass

    def GetErpSettings(self):
        """ GetErpSettings(self: IGeneral) -> SystemSettings """
        pass

    def GetErpSettingsTable(self):
        """ GetErpSettingsTable(self: IGeneral) -> SystemSettingsTable """
        pass

    def GetExecutionContexts(self):
        """ GetExecutionContexts(self: IGeneral) -> List[SafeRpcExecutionContext] """
        pass

    def GetGeneratedScriptComment(self, script):
        """ GetGeneratedScriptComment(self: IGeneral, script: ZoneScript) -> str """
        pass

    def GetImplementedMethods(self):
        """ GetImplementedMethods(self: IGeneral) -> ImplementedFunctionalities """
        pass

    def GetItem(self, itemCode, item):
        """ GetItem(self: IGeneral, itemCode: str) -> (bool, Item) """
        pass

    def GetItemExists(self, itemCode):
        """ GetItemExists(self: IGeneral, itemCode: str) -> bool """
        pass

    def GetItemExistsOnDefaultInboundLocation(self, itemCode, warehouseCode, item):
        """ GetItemExistsOnDefaultInboundLocation(self: IGeneral, itemCode: str, warehouseCode: str) -> (bool, LocationItem) """
        pass

    def GetItemExistsOnLocation(self, itemCode, warehouseCode, warehouseLocationCode, item):
        """ GetItemExistsOnLocation(self: IGeneral, itemCode: str, warehouseCode: str, warehouseLocationCode: str) -> (bool, LocationItem) """
        pass

    def GetItemIdentificationExists(self, itemCode, itemId):
        """ GetItemIdentificationExists(self: IGeneral, itemCode: str, itemId: str) -> bool """
        pass

    def GetItemIdentificationExistsMulti(self, itemCode, itemIds):
        """ GetItemIdentificationExistsMulti(self: IGeneral, itemCode: str, itemIds: List[str]) -> bool """
        pass

    def GetItemIdentifications(self, args, selected, itemIdentifications):
        """ GetItemIdentifications(self: IGeneral, args: GetItemIdentificationArgs, selected: ItemIdentifications) -> (int, ItemIdentifications) """
        pass

    def GetItemIdentificationsAvailable(self, args, itemIds):
        """ GetItemIdentificationsAvailable(self: IGeneral, args: GetItemIdentificationArgs) -> (int, ItemIdentifications) """
        pass

    def GetItemIdentificationsAvailableIncludingBatches(self, cacheKeyOfBatch, args, itemIdentifications):
        """ GetItemIdentificationsAvailableIncludingBatches(self: IGeneral, cacheKeyOfBatch: CacheKey, args: GetItemIdentificationArgs) -> (int, ItemIdentifications) """
        pass

    def GetItemImageLarge(self, itemCode):
        """ GetItemImageLarge(self: IGeneral, itemCode: str) -> Array[Byte] """
        pass

    def GetItemImageSmall(self, itemCode):
        """ GetItemImageSmall(self: IGeneral, itemCode: str) -> Array[Byte] """
        pass

    def GetItemInfoFromBarcode(self, barcode, itemInfo):
        """ GetItemInfoFromBarcode(self: IGeneral, barcode: str) -> (bool, ItemInfo) """
        pass

    def GetItemLocationDefault(self, args, location):
        """ GetItemLocationDefault(self: IGeneral, args: GetItemLocationsArgs) -> (bool, ItemLocation) """
        pass

    def GetItemLocations(self, args, locations):
        """ GetItemLocations(self: IGeneral, args: GetItemLocationsArgs) -> (int, ItemLocations) """
        pass

    def GetItems(self, args, paging, items):
        """ GetItems(self: IGeneral, args: GetItemsArgs, paging: PagingParams) -> (int, Items) """
        pass

    def GetItemsAll(self, args, items):
        """ GetItemsAll(self: IGeneral, args: GetItemsOnLocationArgs) -> (int, LocationItems) """
        pass

    def GetItemsOnDefaultInboundLocation(self, warehouseCode, filter, items):
        """ GetItemsOnDefaultInboundLocation(self: IGeneral, warehouseCode: str, filter: str) -> (int, LocationItems) """
        pass

    def GetItemsOnLocation(self, args, items):
        """ GetItemsOnLocation(self: IGeneral, args: GetItemsOnLocationArgs) -> (int, LocationItems) """
        pass

    def GetItemsOnTransportLocation(self, filter, items):
        """ GetItemsOnTransportLocation(self: IGeneral, filter: str) -> (int, LocationItems) """
        pass

    def GetItemStockAvailableIncludingBatches(self, cacheKeyOfBatch, args, itemStock):
        """ GetItemStockAvailableIncludingBatches(self: IGeneral, cacheKeyOfBatch: CacheKey, args: GetItemStockListArgs) -> (int, List[ItemStock]) """
        pass

    def GetItemStockList(self, args, itemStockLocationList):
        """ GetItemStockList(self: IGeneral, args: GetItemStockListArgs) -> (int, ItemStockLocationList) """
        pass

    def GetItemStockTotals(self, args, totals):
        """ GetItemStockTotals(self: IGeneral, args: GetItemStockTotalsArgs) -> (bool, ItemStockTotals) """
        pass

    def GetLibContent(self, arg, contents):
        """ GetLibContent(self: IGeneral, arg: GetLibArgs) -> (int, LibContents) """
        pass

    def GetLocationClassificationById(self, id, locationClassification):
        """ GetLocationClassificationById(self: IGeneral, id: int) -> (bool, LocationClassification) """
        pass

    def GetLocationClassifications(self, filterBy, locationClassifications):
        """ GetLocationClassifications(self: IGeneral, filterBy: LocationClassificationsFilter) -> (int, LocationClassifications) """
        pass

    def GetLocationsByCountGroup(self, countGroup, locations):
        """ GetLocationsByCountGroup(self: IGeneral, countGroup: CountGroup) -> (int, Locations) """
        pass

    def GetLocationsByLocationClassification(self, locationClassification, locations):
        """ GetLocationsByLocationClassification(self: IGeneral, locationClassification: LocationClassification) -> (int, Locations) """
        pass

    def GetLocationsByStorageAssignmentClassification(self, storageAssignmentClassification, locations):
        """ GetLocationsByStorageAssignmentClassification(self: IGeneral, storageAssignmentClassification: StorageAssignmentClassification) -> (int, Locations) """
        pass

    def GetLogLines(self, args):
        """ GetLogLines(self: IGeneral, args: GetLogLinesArgs) -> PagedList[LogLine] """
        pass

    def GetModule(self, arg, module):
        """ GetModule(self: IGeneral, arg: ModuleArgs) -> (bool, PythonModule) """
        pass

    def GetPendingPrintLineCount(self, key):
        """ GetPendingPrintLineCount(self: IGeneral, key: CacheKey) -> int """
        pass

    def GetPrintDatasetInstance(self, datasetFullTypeName, dataset):
        """ GetPrintDatasetInstance(self: IGeneral, datasetFullTypeName: str) -> (bool, PrintDatasetBase) """
        pass

    def GetPrintDatasets(self, datasets):
        """ GetPrintDatasets(self: IGeneral) -> (int, List[PrintDatasetBase]) """
        pass

    def GetPrintLabelByName(self, name, label):
        """ GetPrintLabelByName(self: IGeneral, name: str) -> (bool, PrintLabel) """
        pass

    def GetPrintLabelImage(self, labelId):
        """ GetPrintLabelImage(self: IGeneral, labelId: str) -> Array[Byte] """
        pass

    def GetPrintLabelMappings(self, labelId, mappings):
        """ GetPrintLabelMappings(self: IGeneral, labelId: int) -> (bool, Mappings[str, str, str]) """
        pass

    def GetPrintLabels(self, labels):
        """ GetPrintLabels(self: IGeneral) -> (int, PrintLabels) """
        pass

    def GetPrintLabelsOfDataset(self, datasetTypeFullName, labels):
        """ GetPrintLabelsOfDataset(self: IGeneral, datasetTypeFullName: str) -> (int, PrintLabels) """
        pass

    def GetPrintLabelsOfPrintLines(self, printLinesTypes, labels):
        """ GetPrintLabelsOfPrintLines(self: IGeneral, printLinesTypes: IEnumerable[Type]) -> (int, PrintLabels) """
        pass

    def GetProfilingLogEntries(self, userKey, previousMethod, endTime, elapsedMiliSeconds, entries):
        """ GetProfilingLogEntries(self: IGeneral, userKey: int, previousMethod: int, endTime: Nullable[DateTime], elapsedMiliSeconds: int) -> (int, ProfilingLogEntries) """
        pass

    def GetProfilingUserNodes(self, userNodes):
        """ GetProfilingUserNodes(self: IGeneral) -> (int, ProfilingUserNodes) """
        pass

    def GetProgressOfActivity(self, args, activity):
        """ GetProgressOfActivity(self: IGeneral, args: GetActivityProgressArgs) -> (bool, Activity) """
        pass

    def GetProgressUpdate(self, args, progress):
        """ GetProgressUpdate(self: IGeneral, args: GetActivityProgressArgs) -> (bool, Progress) """
        pass

    def GetResourcesOfTranslation(self, resourceSet, culture, translation):
        """ GetResourcesOfTranslation(self: IGeneral, resourceSet: str, culture: str) -> (bool, Translation) """
        pass

    def GetScreenshot(self, accessId):
        """ GetScreenshot(self: IGeneral, accessId: str) -> Array[Byte] """
        pass

    def GetScriptIntellisenseOptions(self, hint):
        """ GetScriptIntellisenseOptions(self: IGeneral, hint: str) -> Array[str] """
        pass

    def GetScripts(self, arg, script):
        """ GetScripts(self: IGeneral, arg: GetScriptArgs) -> (int, ZoneScripts) """
        pass

    def GetScriptSnippets(self, snippets):
        """ GetScriptSnippets(self: IGeneral) -> (int, List[ScriptSnippet]) """
        pass

    def GetScriptTaskById(self, id, task):
        """ GetScriptTaskById(self: IGeneral, id: int) -> (bool, ScriptTask) """
        pass

    def GetScriptTaskByName(self, name, task):
        """ GetScriptTaskByName(self: IGeneral, name: str) -> (bool, ScriptTask) """
        pass

    def GetScriptTaskProjectedSchedule(self, id, schedule, firstOccurrence):
        """ GetScriptTaskProjectedSchedule(self: IGeneral, id: int) -> (bool, Array[DateTime], DateTime) """
        pass

    def GetScriptTasksActive(self, tasks):
        """ GetScriptTasksActive(self: IGeneral) -> (int, ScriptTasks) """
        pass

    def GetScriptTasksAll(self, tasks):
        """ GetScriptTasksAll(self: IGeneral) -> (int, ScriptTasks) """
        pass

    def GetScriptTasksInActive(self, tasks):
        """ GetScriptTasksInActive(self: IGeneral) -> (int, ScriptTasks) """
        pass

    def GetServerDate(self):
        """ GetServerDate(self: IGeneral) -> DateTime """
        pass

    def GetSessions(self, sessions):
        """ GetSessions(self: IGeneral) -> (int, Sessions) """
        pass

    def GetSettings(self):
        """ GetSettings(self: IGeneral) -> SystemSettings """
        pass

    def GetSettingsTable(self):
        """ GetSettingsTable(self: IGeneral) -> SystemSettingsTable """
        pass

    def GetShipperServiceLinkByErpDeliveryMethodCode(self, erpDeliveryMethodCode, shipperServiceLink):
        """ GetShipperServiceLinkByErpDeliveryMethodCode(self: IGeneral, erpDeliveryMethodCode: str) -> (bool, ShipperServiceLink) """
        pass

    def GetShipperServiceLinksAll(self, shipperServiceLinks):
        """ GetShipperServiceLinksAll(self: IGeneral) -> (int, ShipperServiceLinks) """
        pass

    def GetSortedItemLocations(self, args, filterOptions, locations):
        """ GetSortedItemLocations(self: IGeneral, args: GetItemLocationsArgs, filterOptions: FilterOptions) -> (int, ItemLocations) """
        pass

    def GetStorageAssignmentClassificationById(self, id, storageAssignmentClassification):
        """ GetStorageAssignmentClassificationById(self: IGeneral, id: int) -> (bool, StorageAssignmentClassification) """
        pass

    def GetStorageAssignmentClassifications(self, filterBy, storageAssignmentClassifications):
        """ GetStorageAssignmentClassifications(self: IGeneral, filterBy: StorageAssignmentClassificationsFilter) -> (int, StorageAssignmentClassifications) """
        pass

    def GetTagById(self, id, tag):
        """ GetTagById(self: IGeneral, id: int) -> (bool, Tag) """
        pass

    def GetTagsAll(self, tags):
        """ GetTagsAll(self: IGeneral) -> (int, Tags) """
        pass

    def GetTagsByDescription(self, filter, tags):
        """ GetTagsByDescription(self: IGeneral, filter: str) -> (int, Tags) """
        pass

    def GetTagsByType(self, target, tags):
        """ GetTagsByType(self: IGeneral, target: TagTarget) -> (int, Tags) """
        pass

    def GetTranslationsAvailable(self, translations):
        """ GetTranslationsAvailable(self: IGeneral) -> (int, Translations) """
        pass

    def GetTranslationsAvailablePerSet(self, resourseSet, translations):
        """ GetTranslationsAvailablePerSet(self: IGeneral, resourseSet: str) -> (int, Translations) """
        pass

    def GetUserByUserId(self, userId, user):
        """ GetUserByUserId(self: IGeneral, userId: int) -> (bool, User) """
        pass

    def GetUserByUserName(self, username, user):
        """ GetUserByUserName(self: IGeneral, username: str) -> (bool, User) """
        pass

    def GetUserCacheData(self, tag):
        """ GetUserCacheData(self: IGeneral, tag: str) -> str """
        pass

    def GetUsersActive(self, users):
        """ GetUsersActive(self: IGeneral) -> (int, Users) """
        pass

    def GetUsersAll(self, users):
        """ GetUsersAll(self: IGeneral) -> (int, Users) """
        pass

    def GetUsersInactive(self, users):
        """ GetUsersInactive(self: IGeneral) -> (int, Users) """
        pass

    def GetUsersInZone(self, zoneId, users):
        """ GetUsersInZone(self: IGeneral, zoneId: int) -> (int, Users) """
        pass

    def GetVersion(self):
        """ GetVersion(self: IGeneral) -> str """
        pass

    def GetWarehouseByCode(self, warehouseCode, warehouse):
        """ GetWarehouseByCode(self: IGeneral, warehouseCode: str) -> (bool, Warehouse) """
        pass

    def GetWarehouseExists(self, warehouseCode):
        """ GetWarehouseExists(self: IGeneral, warehouseCode: str) -> bool """
        pass

    def GetWarehouseLayoutBySetting(self, warehouseLocation, warehouseLayoutSetting, warehouseLayout):
        """ GetWarehouseLayoutBySetting(self: IGeneral, warehouseLocation: str, warehouseLayoutSetting: WarehouseLayoutSetting) -> (bool, WarehouseLayout) """
        pass

    def GetWarehouseLayoutsBySetting(self, warehouseLayoutSetting, warehouseLayouts):
        """ GetWarehouseLayoutsBySetting(self: IGeneral, warehouseLayoutSetting: WarehouseLayoutSetting) -> (int, WarehouseLayouts) """
        pass

    def GetWarehouseLayoutSettingById(self, id, warehouseLayoutSetting):
        """ GetWarehouseLayoutSettingById(self: IGeneral, id: int) -> (bool, WarehouseLayoutSetting) """
        pass

    def GetWarehouseLayoutSettings(self, filterBy, warehouseLayoutSettings):
        """ GetWarehouseLayoutSettings(self: IGeneral, filterBy: WarehouseLayoutSettingFilter) -> (int, WarehouseLayoutSettings) """
        pass

    def GetWarehouseLocationExists(self, warehouseCode, warehouseLocationCode):
        """ GetWarehouseLocationExists(self: IGeneral, warehouseCode: str, warehouseLocationCode: str) -> bool """
        pass

    def GetWarehouseLocationIfExists(self, warehouseCode, warehouseLocationCode, location):
        """ GetWarehouseLocationIfExists(self: IGeneral, warehouseCode: str, warehouseLocationCode: str) -> (bool, Location) """
        pass

    def GetWarehouseLocations(self, args, locations):
        """ GetWarehouseLocations(self: IGeneral, args: GetWarehouseLocationsArgs) -> (int, Locations) """
        pass

    def GetWarehousesActive(self, warehouses):
        """ GetWarehousesActive(self: IGeneral) -> (int, Warehouses) """
        pass

    def GetWarehousesActiveByLocation(self, warehouseLocationCode, warehouses):
        """ GetWarehousesActiveByLocation(self: IGeneral, warehouseLocationCode: str) -> (int, Warehouses) """
        pass

    def GetWarehousesActiveWithDefaultInboundLocation(self, warehouses):
        """ GetWarehousesActiveWithDefaultInboundLocation(self: IGeneral) -> (int, Warehouses) """
        pass

    def GetWarehousesAll(self, warehouses):
        """ GetWarehousesAll(self: IGeneral) -> (int, Warehouses) """
        pass

    def GetWarehousesInactive(self, warehouses):
        """ GetWarehousesInactive(self: IGeneral) -> (int, Warehouses) """
        pass

    def GetZoneById(self, zoneId, zone):
        """ GetZoneById(self: IGeneral, zoneId: int) -> (bool, Zone) """
        pass

    def GetZoneByName(self, zoneName, zone):
        """ GetZoneByName(self: IGeneral, zoneName: str) -> (bool, Zone) """
        pass

    def GetZoneRightsOfZone(self, zoneId, zoneRights):
        """ GetZoneRightsOfZone(self: IGeneral, zoneId: int) -> (bool, ZoneRights) """
        pass

    def GetZonesActive(self, active, zones):
        """ GetZonesActive(self: IGeneral, active: bool) -> (int, Zones) """
        pass

    def GetZonesActiveOfCurrentUser(self, zones):
        """ GetZonesActiveOfCurrentUser(self: IGeneral) -> (int, Zones) """
        pass

    def GetZonesActiveOfUser(self, user, zones):
        """ GetZonesActiveOfUser(self: IGeneral, user: User) -> (int, Zones) """
        pass

    def GetZonesAll(self, zones):
        """ GetZonesAll(self: IGeneral) -> (int, Zones) """
        pass

    def GetZoneScriptHook(self, arg, script):
        """ GetZoneScriptHook(self: IGeneral, arg: GetScriptArgs) -> (bool, ZoneScript) """
        pass

    def GetZoneScripts(self, args, scripts):
        """ GetZoneScripts(self: IGeneral, args: GetScriptArgs) -> (int, ZoneScripts) """
        pass

    def GetZoneScriptsOrphan(self, arg, scripts):
        """ GetZoneScriptsOrphan(self: IGeneral, arg: GetScriptArgs) -> (int, ZoneScripts) """
        pass

    def GetZonesOfUser(self, user, addActiveOnly, zones):
        """ GetZonesOfUser(self: IGeneral, user: User, addActiveOnly: bool) -> (int, Zones) """
        pass

    def GetZoneUsers(self, zoneId, zoneUsers):
        """ GetZoneUsers(self: IGeneral, zoneId: int) -> (int, ZoneUsers) """
        pass

    def IsProfilerRunning(self):
        """ IsProfilerRunning(self: IGeneral) -> bool """
        pass

    def KillAppDomain(self, arg):
        """ KillAppDomain(self: IGeneral, arg: DataFlowObject[AppDomainInformation]) -> DataFlowObject[AppDomainInformation] """
        pass

    def LogoutClient(self):
        """ LogoutClient(self: IGeneral) """
        pass

    def LogoutUser(self):
        """ LogoutUser(self: IGeneral) """
        pass

    def MoveModuleOrDirectory(self, isFile, name, fromDir, toDir):
        """ MoveModuleOrDirectory(self: IGeneral, isFile: bool, name: str, fromDir: str, toDir: str) -> bool """
        pass

    def OutputCacheStatusToLog(self):
        """ OutputCacheStatusToLog(self: IGeneral) """
        pass

    def PrintPrintLine(self, line, label):
        """ PrintPrintLine(self: IGeneral, line: PrintLineBase, label: PrintLabel) -> bool """
        pass

    def PrintPrintLines(self, key, label):
        """ PrintPrintLines(self: IGeneral, key: CacheKey, label: PrintLabel) -> bool """
        pass

    def PrintPrintLinesByObject(self, lines, label):
        """ PrintPrintLinesByObject(self: IGeneral, lines: PrintLinesBase, label: PrintLabel) -> bool """
        pass

    def PrintPrintLinesByObjectAndPrinter(self, lines, label, printArgs):
        """ PrintPrintLinesByObjectAndPrinter(self: IGeneral, lines: PrintLinesBase, label: PrintLabel, printArgs: PrintBaseArgs) -> bool """
        pass

    def PrintTestLabel(self, labelId, testRun):
        """ PrintTestLabel(self: IGeneral, labelId: int, testRun: bool) """
        pass

    def PurgeProfilingLog(self):
        """ PurgeProfilingLog(self: IGeneral) """
        pass

    def RegisterBackgroundAgentLastSeen(self, agent):
        """ RegisterBackgroundAgentLastSeen(self: IGeneral, agent: BackgroundAgent) """
        pass

    def RemoveUserFromZone(self, zone, user):
        """ RemoveUserFromZone(self: IGeneral, zone: Zone, user: User) -> bool """
        pass

    def ResetBarcodeSettingsToDefault(self):
        """ ResetBarcodeSettingsToDefault(self: IGeneral) -> bool """
        pass

    def ResetPrintLines(self, key, printLines):
        """ ResetPrintLines(self: IGeneral, key: CacheKey) -> (bool, PrintLinesBase) """
        pass

    def RestartScriptEngine(self):
        """ RestartScriptEngine(self: IGeneral) """
        pass

    def SaveDefaultInboundLocation(self, warehouse):
        """ SaveDefaultInboundLocation(self: IGeneral, warehouse: DataFlowObject[Warehouse]) -> DataFlowObject[Warehouse] """
        pass

    def SaveErpSetting(self, memberName, value):
        """ SaveErpSetting(self: IGeneral, memberName: str, value: object) """
        pass

    def SaveModule(self, module):
        """ SaveModule(self: IGeneral, module: PythonModule) -> bool """
        pass

    def SavePrintLabelMappings(self, labelId, mappings):
        """ SavePrintLabelMappings(self: IGeneral, labelId: int, mappings: Mappings[str, str, str]) -> bool """
        pass

    def SaveSetting(self, memberName, value):
        """ SaveSetting(self: IGeneral, memberName: str, value: object) """
        pass

    def SaveTranslations(self, translations):
        """ SaveTranslations(self: IGeneral, *translations: Array[SaveTranslationArgs]) """
        pass

    def SendBroadcastMessage(self, message):
        """ SendBroadcastMessage(self: IGeneral, message: str) """
        pass

    def SendBroadcastQuestion(self, question, possibleAnswers):
        """ SendBroadcastQuestion(self: IGeneral, question: str, possibleAnswers: int) -> Answers """
        pass

    def SendKey(self, endPoint, key):
        """ SendKey(self: IGeneral, endPoint: str, key: str) """
        pass

    def SendMessage(self, endPoint, message):
        """ SendMessage(self: IGeneral, endPoint: str, message: str) """
        pass

    def SendMouseClick(self, endPoint, x, y):
        """ SendMouseClick(self: IGeneral, endPoint: str, x: int, y: int) """
        pass

    def SetPrintLinesQuantitiesAtMax(self, key, printLines):
        """ SetPrintLinesQuantitiesAtMax(self: IGeneral, key: CacheKey) -> (bool, PrintLinesBase) """
        pass

    def SetUserCacheData(self, tag, data):
        """ SetUserCacheData(self: IGeneral, tag: str, data: str) """
        pass

    def SetZoneRightsOfZone(self, zoneId, zoneRights):
        """ SetZoneRightsOfZone(self: IGeneral, zoneId: int, zoneRights: ZoneRightViews) -> bool """
        pass

    def Sleep(self, seconds):
        """ Sleep(self: IGeneral, seconds: int) -> str """
        pass

    def StartDiscoveryServer(self):
        """ StartDiscoveryServer(self: IGeneral) """
        pass

    def StartProfiler(self):
        """ StartProfiler(self: IGeneral) """
        pass

    def StopDiscoveryServer(self):
        """ StopDiscoveryServer(self: IGeneral) """
        pass

    def StopProfiler(self):
        """ StopProfiler(self: IGeneral) """
        pass

    def TouchGetSortedItemLocations(self, args, filterOptions, locations):
        """ TouchGetSortedItemLocations(self: IGeneral, args: GetItemLocationsArgs, filterOptions: FilterOptions) -> (int, ItemLocations) """
        pass

    def UpdateBarcodeSettings(self, dfObject):
        """ UpdateBarcodeSettings(self: IGeneral, dfObject: DataFlowObject[BarcodeTypes]) -> DataFlowObject[BarcodeTypes] """
        pass

    def UpdateCultureOfUserSession(self):
        """ UpdateCultureOfUserSession(self: IGeneral) """
        pass

    def UpdateDatabase(self, message):
        """ UpdateDatabase(self: IGeneral) -> (bool, str) """
        pass

    def UpdatePrintLine(self, key, line):
        """ UpdatePrintLine(self: IGeneral, key: CacheKey, line: PrintLineBase) -> bool """
        pass

    def UploadModule(self, args):
        """ UploadModule(self: IGeneral, args: AddModuleArgs) -> bool """
        pass

    def UploadNewLicense(self, xml, license):
        """ UploadNewLicense(self: IGeneral, xml: str) -> (bool, License) """
        pass

    def ValidateColliReferences(self, dfObject):
        """ ValidateColliReferences(self: IGeneral, dfObject: DataFlowObject[ValidateColliReferencesArgs]) -> DataFlowObject[ValidateColliReferencesArgs] """
        pass

    def ValidateColliReferenceScan(self, barcode, result):
        """ ValidateColliReferenceScan(self: IGeneral, barcode: str) -> (bool, ColliBarcodeResult) """
        pass

    def ValidateItemIdentification(self, itemCode, serialNumber, isBatchNumber, errorMessage):
        """ ValidateItemIdentification(self: IGeneral, itemCode: str, serialNumber: str, isBatchNumber: bool) -> (bool, str) """
        pass

    def ValidateItemIdentificationForDelivery(self, dfObject):
        """ ValidateItemIdentificationForDelivery(self: IGeneral, dfObject: DataFlowObject[ValidateItemIdentificationArgs]) -> DataFlowObject[ValidateItemIdentificationArgs] """
        pass

    def ValidateOrder(self, orderNumber, orderType):
        """ ValidateOrder(self: IGeneral, orderNumber: str, orderType: OrderTypeEnum) -> OrderValidationResult """
        pass

    def ValidateTransportPackageScan(self, barcode, result):
        """ ValidateTransportPackageScan(self: IGeneral, barcode: str) -> (bool, TransportPackageScanResult) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CurrentLicense = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentLicense(self: IGeneral) -> License

Set: CurrentLicense(self: IGeneral) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return IGeneral()

class IInbound:
    # no doc
    def AddOrUpdateLicensePlateToReceipt(self, cacheKey, licensePlate):
        """ AddOrUpdateLicensePlateToReceipt(self: IInbound, cacheKey: CacheKey, licensePlate: LicensePlate) -> LicensePlate """
        pass

    def CancelPendingInboundReceiveLines(self, warehouseCode, customerNumber, orderType):
        """ CancelPendingInboundReceiveLines(self: IInbound, warehouseCode: str, customerNumber: str, orderType: InboundOrderTypeEnum) -> bool """
        pass

    def CancelPendingPurchaseOrderReceipts(self, purchaseOrders):
        """ CancelPendingPurchaseOrderReceipts(self: IInbound, purchaseOrders: PurchaseOrders) """
        pass

    def CancelPendingRmaOrderReceipts(self, rmaOrders):
        """ CancelPendingRmaOrderReceipts(self: IInbound, rmaOrders: RmaOrders) """
        pass

    def CreatePreReceipt(self, dfObject):
        """ CreatePreReceipt(self: IInbound, dfObject: DataFlowObject[CreatePreReceiptArgs]) -> DataFlowObject[CreatePreReceiptArgs] """
        pass

    def CreatePreReceiptLines(self, dfObject):
        """ CreatePreReceiptLines(self: IInbound, dfObject: DataFlowObject[CreatePreReceiptArgs]) -> DataFlowObject[CreatePreReceiptArgs] """
        pass

    def DeletePreReceipLines(self, dfObject):
        """ DeletePreReceipLines(self: IInbound, dfObject: DataFlowObject[List[int]]) -> DataFlowObject[List[int]] """
        pass

    def DeletePreReceipt(self, dfObject):
        """ DeletePreReceipt(self: IInbound, dfObject: DataFlowObject[int]) -> DataFlowObject[int] """
        pass

    def DisposeReceiptWhenUnchanged(self, dfObject):
        """ DisposeReceiptWhenUnchanged(self: IInbound, dfObject: DataFlowObject[CacheKey]) -> DataFlowObject[CacheKey] """
        pass

    def GetAdhocRmaCustomersByFilter(self, args, customers):
        """ GetAdhocRmaCustomersByFilter(self: IInbound, args: GetHistoryOutboundOrderCustomersArgs) -> (int, Customers) """
        pass

    def GetHistoryPurchaseOrderPrintLines(self, filter, lines):
        """ GetHistoryPurchaseOrderPrintLines(self: IInbound, filter: GetHistoryPurchaseOrderPrintLinesArgs) -> (int, PurchaseOrderPrintLines) """
        pass

    def GetHistoryPurchaseOrdersByFilter(self, filter, pagingParams, purchaseOrders):
        """ GetHistoryPurchaseOrdersByFilter(self: IInbound, filter: HistoryPurchaseOrdersFilter, pagingParams: PagingParams) -> (int, HistoryPurchaseOrders) """
        pass

    def GetHistoryPurchaseReceiptsByFilter(self, filter, pagingParams, purchaseOrders):
        """ GetHistoryPurchaseReceiptsByFilter(self: IInbound, filter: HistoryPurchaseOrdersFilter, pagingParams: PagingParams) -> (int, HistoryPurchaseOrders) """
        pass

    def GetHistoryRmaOrderLines(self, args, orderLines):
        """ GetHistoryRmaOrderLines(self: IInbound, args: GetHistoryRmaOrderLinesArgs) -> (int, HistoryRmaOrderLines) """
        pass

    def GetHistoryRmaOrdersByFilter(self, filter, pagingParams, rmaOrders):
        """ GetHistoryRmaOrdersByFilter(self: IInbound, filter: HistoryPurchaseOrdersFilter, pagingParams: PagingParams) -> (int, HistoryRmaOrders) """
        pass

    def GetInboundReceiveLinesByKey(self, cacheKey, receiveLines):
        """ GetInboundReceiveLinesByKey(self: IInbound, cacheKey: CacheKey) -> (bool, InboundReceiveLines) """
        pass

    def GetItemsOfVendor(self, args, items):
        """ GetItemsOfVendor(self: IInbound, args: GetItemsOfVendorArgs) -> (int, Items) """
        pass

    def GetItemVendors(self, args, vendors):
        """ GetItemVendors(self: IInbound, args: GetItemVendorsArgs) -> (int, ItemVendors) """
        pass

    def GetPreReceiptLines(self, args, lines):
        """ GetPreReceiptLines(self: IInbound, args: PreReceiptLinesArgs) -> (int, PagedList[PreReceiptLine]) """
        pass

    def GetPreReceiptReceiveLines(self, dfObject):
        """ GetPreReceiptReceiveLines(self: IInbound, dfObject: DataFlowObject[ReceiveLinesForPreReceiptArgs]) -> DataFlowObject[ReceiveLinesForPreReceiptArgs] """
        pass

    def GetPreReceipts(self, args, preReceipts):
        """ GetPreReceipts(self: IInbound, args: PreReceiptArgs) -> (int, PreReceipts) """
        pass

    def GetPurchaseOrder(self, filterBy, purchaseOrder):
        """ GetPurchaseOrder(self: IInbound, filterBy: PurchaseOrderArgs) -> (bool, PurchaseOrder) """
        pass

    def GetPurchaseOrderLines(self, args, purchaseOrderLines):
        """ GetPurchaseOrderLines(self: IInbound, args: GetPurchaseOrderLinesArgs) -> (int, PurchaseOrderLines) """
        pass

    def GetPurchaseOrderPrintLines(self, key, lines):
        """ GetPurchaseOrderPrintLines(self: IInbound, key: CacheKey) -> (int, PurchaseOrderPrintLines) """
        pass

    def GetPurchaseOrdersAll(self, purchaseOrders):
        """ GetPurchaseOrdersAll(self: IInbound) -> (int, PurchaseOrders) """
        pass

    def GetPurchaseOrdersByFilter(self, args, purchaseOrders):
        """ GetPurchaseOrdersByFilter(self: IInbound, args: PurchaseOrderArgs) -> (int, PurchaseOrders) """
        pass

    def GetPurchaseReceiveLines(self, purchaseOrders, warehouseCode, inboundReceiveLines):
        """ GetPurchaseReceiveLines(self: IInbound, purchaseOrders: DataFlowObject[PurchaseOrders], warehouseCode: str) -> (DataFlowObject[PurchaseOrders], InboundReceiveLines) """
        pass

    def GetPurchaseReceiveLinesByKey(self, cacheKey, inboundReceiveLines):
        """ GetPurchaseReceiveLinesByKey(self: IInbound, cacheKey: CacheKey) -> (int, InboundReceiveLines) """
        pass

    def GetRmaCustomersExpected(self, customers):
        """ GetRmaCustomersExpected(self: IInbound) -> (int, Customers) """
        pass

    def GetRmaCustomersExpectedByFilter(self, args, customers):
        """ GetRmaCustomersExpectedByFilter(self: IInbound, args: GetRmaOrderCustomersArgs) -> (int, Customers) """
        pass

    def GetRmaOrder(self, filterBy, rmaOrder):
        """ GetRmaOrder(self: IInbound, filterBy: RmaOrderArgs) -> (bool, RmaOrder) """
        pass

    def GetRmaOrderItemIdentifications(self, rmaOrderId, orderLineId, itemIds):
        """ GetRmaOrderItemIdentifications(self: IInbound, rmaOrderId: int, orderLineId: int) -> (int, ItemIdentifications) """
        pass

    def GetRmaOrderLines(self, args, rmaOrderLines):
        """ GetRmaOrderLines(self: IInbound, args: GetRmaOrderLinesArgs) -> (int, RmaOrderLines) """
        pass

    def GetRmaOrderPrintLines(self, key, lines):
        """ GetRmaOrderPrintLines(self: IInbound, key: CacheKey) -> (int, RmaOrderPrintLines) """
        pass

    def GetRmaOrdersAll(self, rmaOrders):
        """ GetRmaOrdersAll(self: IInbound) -> (int, RmaOrders) """
        pass

    def GetRmaOrdersByFilter(self, filterBy, rmaOrders):
        """ GetRmaOrdersByFilter(self: IInbound, filterBy: RmaOrderArgs) -> (int, RmaOrders) """
        pass

    def GetRmaReasons(self, reasons):
        """ GetRmaReasons(self: IInbound) -> (int, RmaReasons) """
        pass

    def GetRmaReceiveLines(self, rmaOrders, warehouseCode, rmaReceiveLines):
        """ GetRmaReceiveLines(self: IInbound, rmaOrders: DataFlowObject[RmaOrders], warehouseCode: str) -> (DataFlowObject[RmaOrders], InboundReceiveLines) """
        pass

    def GetRmaReceiveLinesByKey(self, cacheKey, rmaReceiveLines):
        """ GetRmaReceiveLinesByKey(self: IInbound, cacheKey: CacheKey) -> (int, InboundReceiveLines) """
        pass

    def GetRmaReceiveLinesUsingOutboundOrders(self, dfObject, rmaReceiveLines):
        """ GetRmaReceiveLinesUsingOutboundOrders(self: IInbound, dfObject: DataFlowObject[PrepareAdhocRmaReceiveLinesArgs]) -> (DataFlowObject[PrepareAdhocRmaReceiveLinesArgs], InboundReceiveLines) """
        pass

    def GetVendors(self, args, vendors):
        """ GetVendors(self: IInbound, args: GetVendorsArgs) -> (int, Vendors) """
        pass

    def GetVendorsExpected(self, vendors):
        """ GetVendorsExpected(self: IInbound) -> (int, PurchaseOrderVendors) """
        pass

    def GetVendorsExpectedByFilter(self, vendors, args):
        """ GetVendorsExpectedByFilter(self: IInbound, args: GetPurchaseOrderVendorArgs) -> (int, PurchaseOrderVendors) """
        pass

    def PrepareInboundReceiveLines(self, args, cacheKey):
        """ PrepareInboundReceiveLines(self: IInbound, args: PrepareInboundReceiveLinesArgs) -> CacheKey """
        pass

    def PrintPurchaseReceipt(self, groupGuid, printer, printingOptions):
        """ PrintPurchaseReceipt(self: IInbound, groupGuid: Guid, printer: str, printingOptions: PrintingOptions) -> bool """
        pass

    def PrintReceiveLabels(self, line, quantity, label):
        """ PrintReceiveLabels(self: IInbound, line: InboundReceiveLine, quantity: Decimal, label: PrintLabel) """
        pass

    def ProcessPendingReceiveLines(self, dfObject):
        """ ProcessPendingReceiveLines(self: IInbound, dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs]) -> DataFlowObject[ProcessInboundReceiveLinesArgs] """
        pass

    def ReceiveItemIdMulti(self, dfObject):
        """ ReceiveItemIdMulti(self: IInbound, dfObject: DataFlowObject[ReceiveItemIdMultiArgs]) -> DataFlowObject[ReceiveItemIdMultiArgs] """
        pass

    def ReceiveItemIdRange(self, dfObject):
        """ ReceiveItemIdRange(self: IInbound, dfObject: DataFlowObject[ReceiveItemIdRangeArgs]) -> DataFlowObject[ReceiveItemIdRangeArgs] """
        pass

    def RemoveInboundReceiveLine(self, cacheKey, receiveLineId):
        """ RemoveInboundReceiveLine(self: IInbound, cacheKey: CacheKey, receiveLineId: str) -> bool """
        pass

    def RemoveLicensePlateFromReceipt(self, cacheKey, licensePlateId):
        """ RemoveLicensePlateFromReceipt(self: IInbound, cacheKey: CacheKey, licensePlateId: int) """
        pass

    def UpdatePreReceiptStatus(self, dfObject):
        """ UpdatePreReceiptStatus(self: IInbound, dfObject: DataFlowObject[UpdatePreReceiptStatusArgs]) -> DataFlowObject[UpdatePreReceiptStatusArgs] """
        pass

    def UpdateQuantityReceiveLine(self, dfObject, receiveLine):
        """ UpdateQuantityReceiveLine(self: IInbound, dfObject: DataFlowObject[ReceiveArgs]) -> (DataFlowObject[ReceiveArgs], InboundReceiveLine) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return IInbound()

class IInventory:
    # no doc
    def AddCountItemIdentitification(self, key, itemId, overwriteIfExists):
        """ AddCountItemIdentitification(self: IInventory, key: CacheKey, itemId: ItemIdentification, overwriteIfExists: bool) -> bool """
        pass

    def AddCountItemIdentitificationMulti(self, key, itemIds, overwriteIfExists):
        """ AddCountItemIdentitificationMulti(self: IInventory, key: CacheKey, itemIds: ItemIdentifications, overwriteIfExists: bool) -> bool """
        pass

    def AddCountQuantity(self, key, quantity, overwriteIfExists):
        """ AddCountQuantity(self: IInventory, key: CacheKey, quantity: Decimal, overwriteIfExists: bool) -> bool """
        pass

    def AddWarehouseTransferItemIdentitifications(self, key, args):
        """ AddWarehouseTransferItemIdentitifications(self: IInventory, key: CacheKey, args: AddWarehouseTransferItemIdentitificationArgs) -> bool """
        pass

    def AddWarehouseTransferItems(self, key, itemCodes, overwriteIfExists):
        """ AddWarehouseTransferItems(self: IInventory, key: CacheKey, itemCodes: List[str], overwriteIfExists: bool) -> bool """
        pass

    def AddWarehouseTransferQuantities(self, key, items, overwriteIfExists):
        """ AddWarehouseTransferQuantities(self: IInventory, key: CacheKey, items: WarehouseTransferItems, overwriteIfExists: bool) -> bool """
        pass

    def AddWarehouseTransferQuantity(self, key, args):
        """ AddWarehouseTransferQuantity(self: IInventory, key: CacheKey, args: AddWarehouseTransferQuantityArgs) -> bool """
        pass

    def BatchChangeCountType(self, filterBy, type):
        """ BatchChangeCountType(self: IInventory, filterBy: CountFilter, type: CountTypeEnum) -> int """
        pass

    def CancelProcessCounts(self):
        """ CancelProcessCounts(self: IInventory) """
        pass

    def ChangeLicensePlateStatus(self, args):
        """ ChangeLicensePlateStatus(self: IInventory, args: ChangeLicensePlateStatusArgs) """
        pass

    def CheckLicensePlateIntegrity(self, args):
        """ CheckLicensePlateIntegrity(self: IInventory, args: CheckLicensePlateIntegrityArgs) -> CheckLicensePlateIntegrityResult """
        pass

    def CreateCount(self, arg):
        """ CreateCount(self: IInventory, arg: DataFlowObject[Count]) -> DataFlowObject[Count] """
        pass

    def CreateCountFromCache(self, arg):
        """ CreateCountFromCache(self: IInventory, arg: DataFlowObject[CacheKey]) -> DataFlowObject[CacheKey] """
        pass

    def CreateCountGroup(self, arg):
        """ CreateCountGroup(self: IInventory, arg: DataFlowObject[CountGroup]) -> DataFlowObject[CountGroup] """
        pass

    def CreateLicensePlate(self, lp):
        """ CreateLicensePlate(self: IInventory, lp: LicensePlate) -> LicensePlate """
        pass

    def CreateLicensePlateAuditLogEntry(self, lpAuditEntry):
        """ CreateLicensePlateAuditLogEntry(self: IInventory, lpAuditEntry: LicensePlateAuditLog) -> LicensePlateAuditLog """
        pass

    def CreateLicensePlateFromReceipt(self, args):
        """ CreateLicensePlateFromReceipt(self: IInventory, args: CreateLicensePlateFromReceiptArgs) -> LicensePlate """
        pass

    def CreateOneCount(self, itemBarcode, warehouseCode, locationCode, countGroupId, itemId):
        """ CreateOneCount(self: IInventory, itemBarcode: str, warehouseCode: str, locationCode: str, countGroupId: int, itemId: str) -> bool """
        pass

    def CreateOrUpdateLicensePlateItem(self, licensePlateId, item):
        """ CreateOrUpdateLicensePlateItem(self: IInventory, licensePlateId: int, item: LicensePlateItem) -> LicensePlateItem """
        pass

    def CreateOrUpdateLicensePlateItems(self, licensePlateId, items):
        """ CreateOrUpdateLicensePlateItems(self: IInventory, licensePlateId: int, items: List[LicensePlateItem]) """
        pass

    def CreateOrUpdateReplenishmentOrderLine(self, line, skipAllocationCheck):
        """ CreateOrUpdateReplenishmentOrderLine(self: IInventory, line: DataFlowObject[ReplenishmentOrderLine], skipAllocationCheck: bool) -> DataFlowObject[ReplenishmentOrderLine] """
        pass

    def CreateReplenishmentOrder(self, order):
        """ CreateReplenishmentOrder(self: IInventory, order: DataFlowObject[ReplenishmentOrder]) -> DataFlowObject[ReplenishmentOrder] """
        pass

    def CreateReplenishmentOrders(self, dfObject):
        """ CreateReplenishmentOrders(self: IInventory, dfObject: DataFlowObject[ReplenishmentOrders]) -> DataFlowObject[ReplenishmentOrders] """
        pass

    def CreateZeroCount(self, arg):
        """ CreateZeroCount(self: IInventory, arg: DataFlowObject[Count]) -> DataFlowObject[Count] """
        pass

    def CreateZeroCountByCountGroup(self, countGroupId):
        """ CreateZeroCountByCountGroup(self: IInventory, countGroupId: int) """
        pass

    def DeleteCountFromCache(self, arg):
        """ DeleteCountFromCache(self: IInventory, arg: DataFlowObject[CacheKey]) -> DataFlowObject[CacheKey] """
        pass

    def DeleteCountFromCacheAndTable(self, cacheKey):
        """ DeleteCountFromCacheAndTable(self: IInventory, cacheKey: CacheKey) """
        pass

    def DeleteCountFromTable(self, arg):
        """ DeleteCountFromTable(self: IInventory, arg: DataFlowObject[Count]) -> DataFlowObject[Count] """
        pass

    def DeleteCountGroup(self, arg):
        """ DeleteCountGroup(self: IInventory, arg: DataFlowObject[CountGroup]) -> DataFlowObject[CountGroup] """
        pass

    def DeleteLicensePlateById(self, licensePlateId):
        """ DeleteLicensePlateById(self: IInventory, licensePlateId: int) """
        pass

    def DeleteLicensePlateItemById(self, itemId):
        """ DeleteLicensePlateItemById(self: IInventory, itemId: int) """
        pass

    def DeleteReplenishmentOrder(self, order):
        """ DeleteReplenishmentOrder(self: IInventory, order: DataFlowObject[ReplenishmentOrder]) -> DataFlowObject[ReplenishmentOrder] """
        pass

    def DeleteReplenishmentOrderLines(self, dfObject):
        """ DeleteReplenishmentOrderLines(self: IInventory, dfObject: DataFlowObject[ReplenishmentOrderLines]) -> DataFlowObject[ReplenishmentOrderLines] """
        pass

    def DeleteReplenishmentOrders(self, dfObject):
        """ DeleteReplenishmentOrders(self: IInventory, dfObject: DataFlowObject[ReplenishmentOrders]) -> DataFlowObject[ReplenishmentOrders] """
        pass

    def GenerateReplenishmentOrder(self, warehouseToCode):
        """ GenerateReplenishmentOrder(self: IInventory, warehouseToCode: str) -> bool """
        pass

    def GenerateReplenishmentOrders(self, args):
        """ GenerateReplenishmentOrders(self: IInventory, args: GenerateReplenishmentOrdersArgs) -> bool """
        pass

    def GetAllItemIdentifications(self, filterBy):
        """ GetAllItemIdentifications(self: IInventory, filterBy: GetAllItemIdentificationsArgs) -> ItemIdentifications """
        pass

    def GetCount(self, *__args):
        """
        GetCount(self: IInventory, itemCode: str, warehouseCode: str, warehouseLocationCode: str, countGroupId: int, itemId: str) -> (bool, Count)
        GetCount(self: IInventory, key: CacheKey) -> (bool, Count)
        """
        pass

    def GetCountByCountId(self, countId, count):
        """ GetCountByCountId(self: IInventory, countId: int) -> (bool, Count) """
        pass

    def GetCountGroupIdByType(self, type):
        """ GetCountGroupIdByType(self: IInventory, type: CountGroupTypeEnum) -> int """
        pass

    def GetCountGroups(self, filter, countGroups):
        """ GetCountGroups(self: IInventory, filter: str) -> (int, CountGroups) """
        pass

    def GetCountGroupsAll(self, countGroups):
        """ GetCountGroupsAll(self: IInventory) -> (int, CountGroups) """
        pass

    def GetCountGroupsById(self, id):
        """ GetCountGroupsById(self: IInventory, id: int) -> CountGroup """
        pass

    def GetCountGroupsByType(self, type):
        """ GetCountGroupsByType(self: IInventory, type: CountGroupTypeEnum) -> CountGroup """
        pass

    def GetCounts(self, filterBy, pagingParams, counts):
        """ GetCounts(self: IInventory, filterBy: CountFilter, pagingParams: PagingParams) -> (int, Counts) """
        pass

    def GetItemsOnLocationLeftToAddToLp(self, args):
        """ GetItemsOnLocationLeftToAddToLp(self: IInventory, args: GetItemsOnLocationLeftToAddToLpArgs) -> List[LpLocationItem] """
        pass

    def GetItemStockAllocations(self, filterBy, allocations):
        """ GetItemStockAllocations(self: IInventory, filterBy: GetAllocationsArgs) -> (int, ItemStockAllocationList) """
        pass

    def GetLicensePlateAuditLogEntries(self, args, pagingParams, logEntries):
        """ GetLicensePlateAuditLogEntries(self: IInventory, args: GetLicensePlateItemAuditLogEntriesArgs, pagingParams: PagingParams) -> (int, LicensePlateAuditLogs) """
        pass

    def GetLicensePlateByCode(self, args, licensePlate):
        """ GetLicensePlateByCode(self: IInventory, args: GetLicensePlateByCodeArgs) -> (bool, LicensePlate) """
        pass

    def GetLicensePlateById(self, licensePlateId, licensePlate):
        """ GetLicensePlateById(self: IInventory, licensePlateId: int) -> (bool, LicensePlate) """
        pass

    def GetLicensePlateItems(self, args, pagingParams, items):
        """ GetLicensePlateItems(self: IInventory, args: GetLicensePlateItemsArgs, pagingParams: PagingParams) -> (int, LicensePlateItems) """
        pass

    def GetLicensePlates(self, args, pagingParams, licensePlates):
        """ GetLicensePlates(self: IInventory, args: GetLicensePlatesArgs, pagingParams: PagingParams) -> (int, LicensePlates) """
        pass

    def GetProcessCountsProgress(self, percentageComplete, message):
        """ GetProcessCountsProgress(self: IInventory) -> (int, str) """
        pass

    def GetReplenishmentOrder(self, args, replenishmentOrder):
        """ GetReplenishmentOrder(self: IInventory, args: ReplenishmentOrderArgs) -> (bool, ReplenishmentOrder) """
        pass

    def GetReplenishmentOrderLines(self, args, replenishmentOrderLines):
        """ GetReplenishmentOrderLines(self: IInventory, args: ReplenishmentOrderLinesArgs) -> (int, ReplenishmentOrderLines) """
        pass

    def GetReplenishmentOrders(self, filterBy, replenishmentOrders):
        """ GetReplenishmentOrders(self: IInventory, filterBy: ReplenishmentOrderArgs) -> (int, ReplenishmentOrders) """
        pass

    def GetStockManagerList(self, filterBy, pagingParams, stockList):
        """ GetStockManagerList(self: IInventory, filterBy: GetStockManagerListArgs, pagingParams: PagingParams) -> (int, ItemStockWithAllocationsList) """
        pass

    def GetStockOnMatchingFilter(self, args):
        """ GetStockOnMatchingFilter(self: IInventory, args: GetStockManagerListArgs) -> FindableList[ItemStockWithLocations] """
        pass

    def GetWarehousesWithPendingCounts(self, warehouses):
        """ GetWarehousesWithPendingCounts(self: IInventory) -> (int, Warehouses) """
        pass

    def GetWarehouseTransfer(self, key):
        """ GetWarehouseTransfer(self: IInventory, key: CacheKey) -> WarehouseTransfer """
        pass

    def GetWarehouseTransferItems(self, key):
        """ GetWarehouseTransferItems(self: IInventory, key: CacheKey) -> WarehouseTransferItems """
        pass

    def IsValidItemInCountGroup(self, itemBarcode, countGroup, quantity):
        """ IsValidItemInCountGroup(self: IInventory, itemBarcode: str, countGroup: CountGroup) -> (bool, Decimal) """
        pass

    def IsValidLocationInCountGroup(self, warehouseCode, locationBarcode, countGroup, location):
        """ IsValidLocationInCountGroup(self: IInventory, warehouseCode: str, locationBarcode: str, countGroup: CountGroup) -> (bool, Location) """
        pass

    def ItemBelongsToLicensePlate(self, args):
        """ ItemBelongsToLicensePlate(self: IInventory, args: ItemBelongsToLicensePlateArgs) -> bool """
        pass

    def PreCreateReplenishmentOrderLineForItem(self, replenishmentOrderId, itemcode, quantity, line):
        """ PreCreateReplenishmentOrderLineForItem(self: IInventory, replenishmentOrderId: int, itemcode: str, quantity: Decimal) -> (bool, ReplenishmentOrderLine) """
        pass

    def PrepareCount(self, itemCode, warehouseCode, warehouseLocationCode, countGroupId):
        """ PrepareCount(self: IInventory, itemCode: str, warehouseCode: str, warehouseLocationCode: str, countGroupId: int) -> CacheKey """
        pass

    def PrepareCountWithType(self, itemCode, warehouseCode, warehouseLocationCode, countGroupType):
        """ PrepareCountWithType(self: IInventory, itemCode: str, warehouseCode: str, warehouseLocationCode: str, countGroupType: CountGroupTypeEnum) -> CacheKey """
        pass

    def PrepareWarehouseTransfer(self, warehouseCodeFrom, warehouseLocationCodeFrom, warehouseCodeTo, warehouseLocationCodeTo, type):
        """ PrepareWarehouseTransfer(self: IInventory, warehouseCodeFrom: str, warehouseLocationCodeFrom: str, warehouseCodeTo: str, warehouseLocationCodeTo: str, type: WarehouseTransferType) -> CacheKey """
        pass

    def PrepareWarehouseTransferFrom(self, itemCode, warehouseCodeFrom, warehouseLocationCodeFrom):
        """ PrepareWarehouseTransferFrom(self: IInventory, itemCode: str, warehouseCodeFrom: str, warehouseLocationCodeFrom: str) -> CacheKey """
        pass

    def PrepareWarehouseTransferFromInterBranch(self, warehouseCodeFrom, warehouseLocationCodeFrom, transferType):
        """ PrepareWarehouseTransferFromInterBranch(self: IInventory, warehouseCodeFrom: str, warehouseLocationCodeFrom: str, transferType: Nullable[WarehouseTransferType]) -> CacheKey """
        pass

    def PrepareWarehouseTransferItem(self, itemCode, warehouseCodeFrom, warehouseLocationCodeFrom, warehouseCodeTo, warehouseLocationCodeTo):
        """ PrepareWarehouseTransferItem(self: IInventory, itemCode: str, warehouseCodeFrom: str, warehouseLocationCodeFrom: str, warehouseCodeTo: str, warehouseLocationCodeTo: str) -> CacheKey """
        pass

    def PrepareWarehouseTransferReceived(self, itemCode, warehouseCodeFrom, warehouseCodeTo, warehouseLocationCodeTo):
        """ PrepareWarehouseTransferReceived(self: IInventory, itemCode: str, warehouseCodeFrom: str, warehouseCodeTo: str, warehouseLocationCodeTo: str) -> CacheKey """
        pass

    def PrepareWarehouseTransferTo(self, itemCode, warehouseCodeTo, warehouseLocationCodeTo):
        """ PrepareWarehouseTransferTo(self: IInventory, itemCode: str, warehouseCodeTo: str, warehouseLocationCodeTo: str) -> CacheKey """
        pass

    def PrepareWarehouseTransferToMulti(self, itemCodes, warehouseCodeFrom, warehouseLocationCodeFrom, warehouseCodeTo, warehouseLocationTo):
        """ PrepareWarehouseTransferToMulti(self: IInventory, itemCodes: List[str], warehouseCodeFrom: str, warehouseLocationCodeFrom: str, warehouseCodeTo: str, warehouseLocationTo: str) -> CacheKey """
        pass

    def PrepareWarehouseTransferToMultiReceived(self, itemCodes, warehouseCodeFrom, warehouseCodeTo, warehouseLocationTo):
        """ PrepareWarehouseTransferToMultiReceived(self: IInventory, itemCodes: List[str], warehouseCodeFrom: str, warehouseCodeTo: str, warehouseLocationTo: str) -> CacheKey """
        pass

    def PrepareWarehouseTransferToMultiTransport(self, itemCodes, warehouseCodeTo, warehouseLocationTo):
        """ PrepareWarehouseTransferToMultiTransport(self: IInventory, itemCodes: List[str], warehouseCodeTo: str, warehouseLocationTo: str) -> CacheKey """
        pass

    def PrintLicensePlateLabels(self, args):
        """ PrintLicensePlateLabels(self: IInventory, args: PrintLicensePlateLabelArgs) """
        pass

    def ProcessCounts(self, warehouseCode, countGroup, description, date, ledgerCode, started):
        """ ProcessCounts(self: IInventory, warehouseCode: str, countGroup: int, description: str, date: DateTime, ledgerCode: str) -> bool """
        pass

    def ProcessWarehouseTransfer(self, dfObject):
        """ ProcessWarehouseTransfer(self: IInventory, dfObject: DataFlowObject[ProcessWarehouseTransferArgs]) -> DataFlowObject[ProcessWarehouseTransferArgs] """
        pass

    def RemoveCountItemIdentification(self, key, itemId):
        """ RemoveCountItemIdentification(self: IInventory, key: CacheKey, itemId: str) -> bool """
        pass

    def RemoveWarehouseTransfer(self, key):
        """ RemoveWarehouseTransfer(self: IInventory, key: CacheKey) -> bool """
        pass

    def RemoveWarehouseTransferItemCompletely(self, key, itemCode):
        """ RemoveWarehouseTransferItemCompletely(self: IInventory, key: CacheKey, itemCode: str) -> bool """
        pass

    def RemoveWarehouseTransferItemIdentification(self, key, itemCode, itemId):
        """ RemoveWarehouseTransferItemIdentification(self: IInventory, key: CacheKey, itemCode: str, itemId: str) -> bool """
        pass

    def SubtractWarehouseTransferItemQuantity(self, key, itemCode, quantity):
        """ SubtractWarehouseTransferItemQuantity(self: IInventory, key: CacheKey, itemCode: str, quantity: Decimal) -> bool """
        pass

    def SubtractWarehouseTransferQuantities(self, key, items):
        """ SubtractWarehouseTransferQuantities(self: IInventory, key: CacheKey, items: WarehouseTransferItems) -> bool """
        pass

    def SyncStock(self):
        """ SyncStock(self: IInventory) """
        pass

    def TransferItems(self, arg):
        """ TransferItems(self: IInventory, arg: DataFlowObject[WarehouseTransfer]) -> DataFlowObject[WarehouseTransfer] """
        pass

    def UpdateLicensePlate(self, lp):
        """ UpdateLicensePlate(self: IInventory, lp: LicensePlate) """
        pass

    def UpdateWarehouseTransfer(self, key, warehouseCodeFrom, warehouseLocationCodeFrom, warehouseCodeTo, warehouseLocationTo):
        """ UpdateWarehouseTransfer(self: IInventory, key: CacheKey, warehouseCodeFrom: str, warehouseLocationCodeFrom: str, warehouseCodeTo: str, warehouseLocationTo: str) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return IInventory()

class IMessaging:
    # no doc
    def ChangeMessagesStatus(self, messageIds, newStatus):
        """ ChangeMessagesStatus(self: IMessaging, messageIds: List[Guid], newStatus: MessageStatus) """
        pass

    def ChangeMessageStatus(self, messageId, newStatus):
        """ ChangeMessageStatus(self: IMessaging, messageId: Guid, newStatus: MessageStatus) """
        pass

    def CreateMessage(self, message):
        """ CreateMessage(self: IMessaging, message: IMessage) """
        pass

    def DeleteMessageByGuid(self, messageId):
        """ DeleteMessageByGuid(self: IMessaging, messageId: Guid) """
        pass

    def DequeueNextMessage(self):
        """ DequeueNextMessage(self: IMessaging) -> DequeueResult """
        pass

    def ExecuteMessageHandler(self, args):
        """ ExecuteMessageHandler(self: IMessaging, args: ExecuteMessageHandlerArgs) -> ExecuteMessageHandlerResult """
        pass

    def ExecuteMessagePublisher(self, args):
        """ ExecuteMessagePublisher(self: IMessaging, args: ExecuteMessagePublisherArgs) -> ExecuteMessagePublisherResult """
        pass

    def GetDistinctTypeList(self, args):
        """ GetDistinctTypeList(self: IMessaging, args: GetDistinctTypeListArgs) -> List[str] """
        pass

    def GetMessage(self, messageId):
        """ GetMessage(self: IMessaging, messageId: Guid) -> IMessage """
        pass

    def GetMessageBodyAsString(self, messageId, decodeAs):
        """ GetMessageBodyAsString(self: IMessaging, messageId: Guid, decodeAs: MessageBodyDecodeAs) -> str """
        pass

    def GetMessageHandlers(self, args, messageHandlers):
        """ GetMessageHandlers(self: IMessaging, args: GetMessageHandlersArgs) -> (int, IList[MessageHandlerDescriptorSerializable]) """
        pass

    def GetMessagePublishers(self, args, messagePublishers):
        """ GetMessagePublishers(self: IMessaging, args: GetMessagePublishersArgs) -> (int, IList[MessagePublisherDescriptorSerializable]) """
        pass

    def GetMessages(self, args, paging, messages):
        """ GetMessages(self: IMessaging, args: GetMessagesArgs, paging: PagingParams) -> (int, Messages) """
        pass

    def ReissueMessage(self, messageId):
        """ ReissueMessage(self: IMessaging, messageId: Guid) """
        pass

    def ReissueMessages(self, messageIds):
        """ ReissueMessages(self: IMessaging, messageIds: List[Guid]) """
        pass

    def SaveMessageBody(self, messageId, decodeAs, messageBody):
        """ SaveMessageBody(self: IMessaging, messageId: Guid, decodeAs: MessageBodyDecodeAs, messageBody: str) """
        pass

    def UpdateMessage(self, message):
        """ UpdateMessage(self: IMessaging, message: IMessage) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return IMessaging()

class INotificationCenter:
    # no doc
    def AddNotification(self, notificationToInsert):
        """ AddNotification(self: INotificationCenter, notificationToInsert: InsertNotificationArgs) """
        pass

    def AddNotificationGroup(self, notificationGroup):
        """ AddNotificationGroup(self: INotificationCenter, notificationGroup: AddNotificationGroupArgs) """
        pass

    def DeleteNotification(self, notificationId):
        """ DeleteNotification(self: INotificationCenter, notificationId: int) """
        pass

    def DeleteNotificationGroup(self, notificationGroup):
        """ DeleteNotificationGroup(self: INotificationCenter, notificationGroup: DeleteNotificationGroupArgs) """
        pass

    def DeleteNotificationsByReference(self, notificationFilter):
        """ DeleteNotificationsByReference(self: INotificationCenter, notificationFilter: DeleteNotificationByReferenceArgs) """
        pass

    def GetAllNotificationGroups(self):
        """ GetAllNotificationGroups(self: INotificationCenter) -> List[NotificationGroup] """
        pass

    def GetNotifications(self, filterOn):
        """ GetNotifications(self: INotificationCenter, filterOn: GetNotificationsArgs) -> List[Notification] """
        pass

    def HasNotifications(self, filterOn):
        """ HasNotifications(self: INotificationCenter, filterOn: HasNotificationsArgs) -> bool """
        pass

    def MarkAsRead(self, notificationId, userId):
        """ MarkAsRead(self: INotificationCenter, notificationId: int, userId: int) """
        pass

    def MarkGroupAsRead(self, groupKey, userId):
        """ MarkGroupAsRead(self: INotificationCenter, groupKey: str, userId: int) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return INotificationCenter()

class INotificationSummary:
    # no doc
    def DeleteConfiguration(self, notificationSummaryId):
        """ DeleteConfiguration(self: INotificationSummary, notificationSummaryId: int) """
        pass

    def DeleteConfigurations(self, notificationSummaryIds):
        """ DeleteConfigurations(self: INotificationSummary, notificationSummaryIds: List[int]) """
        pass

    def ExecuteSummaries(self):
        """ ExecuteSummaries(self: INotificationSummary) """
        pass

    def GetAllConfigurations(self):
        """ GetAllConfigurations(self: INotificationSummary) -> List[NotificationSummaryConfiguration] """
        pass

    def GetAllExecutionSchedules(self):
        """ GetAllExecutionSchedules(self: INotificationSummary) -> List[str] """
        pass

    def GetAllExecutionTypes(self):
        """ GetAllExecutionTypes(self: INotificationSummary) -> List[str] """
        pass

    def GetConfigurationForm(self, executionType):
        """ GetConfigurationForm(self: INotificationSummary, executionType: str) -> UiForm """
        pass

    def SaveConfiguration(self, model):
        """ SaveConfiguration(self: INotificationSummary, model: NotificationSummaryConfiguration) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return INotificationSummary()

class INumberGeneration:
    # no doc
    def AddUsedNumber(self, args):
        """ AddUsedNumber(self: INumberGeneration, args: AddUsedNumberArgs) """
        pass

    def CreateNumberRange(self, dfObject):
        """ CreateNumberRange(self: INumberGeneration, dfObject: DataFlowObject[NumberRange]) -> DataFlowObject[NumberRange] """
        pass

    def DeleteNumberRange(self, dfObject):
        """ DeleteNumberRange(self: INumberGeneration, dfObject: DataFlowObject[NumberRange]) -> DataFlowObject[NumberRange] """
        pass

    def GenerateNumbers(self, dfObject):
        """ GenerateNumbers(self: INumberGeneration, dfObject: DataFlowObject[GenerateBarcodeLabelArgs]) -> DataFlowObject[GenerateBarcodeLabelArgs] """
        pass

    def GetNumberRangeById(self, rangeId):
        """ GetNumberRangeById(self: INumberGeneration, rangeId: int) -> NumberRange """
        pass

    def GetNumberRangesByFilter(self, args):
        """ GetNumberRangesByFilter(self: INumberGeneration, args: GetNumberRangeArgs) -> List[NumberRange] """
        pass

    def IsNumberUsed(self, args):
        """ IsNumberUsed(self: INumberGeneration, args: UsedNumberArgs) -> bool """
        pass

    def ResetNumberRange(self, dfObject):
        """ ResetNumberRange(self: INumberGeneration, dfObject: DataFlowObject[NumberRange]) -> DataFlowObject[NumberRange] """
        pass

    def UpdateNumberRange(self, dfObject):
        """ UpdateNumberRange(self: INumberGeneration, dfObject: DataFlowObject[NumberRange]) -> DataFlowObject[NumberRange] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return INumberGeneration()

class IOfflineScanning:
    # no doc
    def AddScanner(self, args):
        """ AddScanner(self: IOfflineScanning, args: AddScannerArgs) """
        pass

    def BosInboundListenerPullDirect(self):
        """ BosInboundListenerPullDirect(self: IOfflineScanning) -> int """
        pass

    def DeleteScanner(self, args):
        """ DeleteScanner(self: IOfflineScanning, args: DeleteScannerArgs) """
        pass

    def GetAppVersionFileSpec(self, args):
        """ GetAppVersionFileSpec(self: IOfflineScanning, args: GetAppVersionFileSpecArgs) -> str """
        pass

    def GetAppVersions(self):
        """ GetAppVersions(self: IOfflineScanning) -> AppVersions """
        pass

    def GetCurrentAppVersion(self):
        """ GetCurrentAppVersion(self: IOfflineScanning) -> LicenseAppVersion """
        pass

    def GetScanners(self):
        """ GetScanners(self: IOfflineScanning) -> Scanners """
        pass

    def IsBosInboundListenerRunning(self):
        """ IsBosInboundListenerRunning(self: IOfflineScanning) -> bool """
        pass

    def SetCurrentAppVersion(self, args):
        """ SetCurrentAppVersion(self: IOfflineScanning, args: SetCurrentAppVersionArgs) """
        pass

    def StartBosInboundListener(self):
        """ StartBosInboundListener(self: IOfflineScanning) -> bool """
        pass

    def UploadFile(self, name, file, overwrite):
        """ UploadFile(self: IOfflineScanning, name: str, file: Stream, overwrite: bool) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return IOfflineScanning()

class IOutbound:
    # no doc
    def AddDirectOrder(self, args):
        """ AddDirectOrder(self: IOutbound, args: DirectOrderCrudArgs) -> DataFlowObject[DirectOrder] """
        pass

    def AddDirectOrderLine(self, args):
        """ AddDirectOrderLine(self: IOutbound, args: DirectOrderLineCrudArgs) -> DataFlowObject[DirectOrderLine] """
        pass

    def AddDirectOrderLineItemIdentification(self, args):
        """ AddDirectOrderLineItemIdentification(self: IOutbound, args: DirectOrderLineItemIdentificationCrudArgs) -> DataFlowObject[DirectOrderLine] """
        pass

    def AddDirectOrderLineItemIdentifications(self, args):
        """ AddDirectOrderLineItemIdentifications(self: IOutbound, args: DirectOrderLineItemIdentificationsCrudArgs) -> DataFlowObject[DirectOrderLine] """
        pass

    def AddPackageUsingPreset(self, args, newPackageNumber, packages):
        """ AddPackageUsingPreset(self: IOutbound, args: AddTransportPackageArgs) -> (bool, Guid, TransportPackages) """
        pass

    def CheckBatchScan(self, args):
        """ CheckBatchScan(self: IOutbound, args: BatchScanArgs) -> BatchScanResult """
        pass

    def CloseBatchesForPacking(self, args):
        """ CloseBatchesForPacking(self: IOutbound, args: GetCustomersWithPendingPackagesArgs) """
        pass

    def CloseBatchForPickingById(self, id):
        """ CloseBatchForPickingById(self: IOutbound, id: str) -> bool """
        pass

    def CloseTransportPackages(self, packagesKey):
        """ CloseTransportPackages(self: IOutbound, packagesKey: CacheKey) """
        pass

    def CreateBatchByCustomerNumbers(self, customers, createdByClientType, createdBatches, message):
        """ CreateBatchByCustomerNumbers(self: IOutbound, customers: Customers, createdByClientType: BatchCreatedByClientTypeEnum) -> (int, Batches, str) """
        pass

    def CreateBatches(self, orderNumbers, createdByClientType, args, createdBatches, message):
        """ CreateBatches(self: IOutbound, orderNumbers: List[str], createdByClientType: BatchCreatedByClientTypeEnum, args: BatchUpdateArgs) -> (int, Batches, str) """
        pass

    def CreateBatchesByLineIds(self, orderNumbers, orderLineIds, createdByClientType, settings, createdBatches, message):
        """ CreateBatchesByLineIds(self: IOutbound, orderNumbers: List[str], orderLineIds: List[int], createdByClientType: BatchCreatedByClientTypeEnum, settings: BatchUpdateArgs) -> (int, Batches, str) """
        pass

    def DeleteBatchById(self, id):
        """ DeleteBatchById(self: IOutbound, id: str) """
        pass

    def DeleteBatches(self, selectedBatches):
        """ DeleteBatches(self: IOutbound, selectedBatches: Batches) -> bool """
        pass

    def DeleteBatchIfNothingChanged(self, batchCacheKey):
        """ DeleteBatchIfNothingChanged(self: IOutbound, batchCacheKey: CacheKey) """
        pass

    def DisposeTransportPackagesWhenUnchanged(self, dfObject):
        """ DisposeTransportPackagesWhenUnchanged(self: IOutbound, dfObject: DataFlowObject[CacheKey]) -> DataFlowObject[CacheKey] """
        pass

    def GetAllocationProfiles(self, profiles):
        """ GetAllocationProfiles(self: IOutbound) -> (int, AllocationProfiles) """
        pass

    def GetBatchByCacheKey(self, cacheKey, batch):
        """ GetBatchByCacheKey(self: IOutbound, cacheKey: CacheKey) -> (bool, Batch) """
        pass

    def GetBatchById(self, id, cacheKey, batch):
        """ GetBatchById(self: IOutbound, id: str) -> (bool, CacheKey, Batch) """
        pass

    def GetBatchByScan(self, barcode, batch):
        """ GetBatchByScan(self: IOutbound, barcode: str) -> (bool, BatchBase) """
        pass

    def GetBatchesAll(self, batches):
        """ GetBatchesAll(self: IOutbound) -> (int, Batches) """
        pass

    def GetBatchesByFilter(self, args, batches):
        """ GetBatchesByFilter(self: IOutbound, args: BatchFilterArgs) -> (int, Batches) """
        pass

    def GetBatchesIncomplete(self, batches):
        """ GetBatchesIncomplete(self: IOutbound) -> (int, Batches) """
        pass

    def GetBatchesIncompleteByFilter(self, args, batches):
        """ GetBatchesIncompleteByFilter(self: IOutbound, args: GetBatchArgs) -> (int, Batches) """
        pass

    def GetBatchesIncompleteSmall(self, batches):
        """ GetBatchesIncompleteSmall(self: IOutbound) -> (int, FindableList[BatchBase]) """
        pass

    def GetBatchesWithPendingPackages(self, args, batches):
        """ GetBatchesWithPendingPackages(self: IOutbound, args: BatchFilterArgs) -> (int, BatchFilterResult) """
        pass

    def GetBoxColors(self, colors):
        """ GetBoxColors(self: IOutbound) -> Array[Color] """
        pass

    def GetCacheKeyOfTransportPackages(self, dfObject, packagesKey):
        """ GetCacheKeyOfTransportPackages(self: IOutbound, dfObject: DataFlowObject[GetItemsToPackArgs]) -> (DataFlowObject[GetItemsToPackArgs], CacheKey) """
        pass

    def GetCustomers(self, args, customers):
        """ GetCustomers(self: IOutbound, args: GetCustomersArgs) -> (int, Customers) """
        pass

    def GetCustomersPending(self, customers):
        """ GetCustomersPending(self: IOutbound) -> (int, Customers) """
        pass

    def GetCustomersPendingByFilter(self, customers, args):
        """ GetCustomersPendingByFilter(self: IOutbound, args: GetCustomersPendingArgs) -> (int, Customers) """
        pass

    def GetCustomersWithPendingPackages(self, args, customers):
        """ GetCustomersWithPendingPackages(self: IOutbound, args: GetCustomersWithPendingPackagesArgs) -> (int, PackCustomers) """
        pass

    def GetDirectOrder(self, args):
        """ GetDirectOrder(self: IOutbound, args: DirectOrderCrudArgs) -> DataFlowObject[DirectOrder] """
        pass

    def GetDirectOrderHistoryByFilter(self, filter, pagingParams):
        """ GetDirectOrderHistoryByFilter(self: IOutbound, filter: HistoryDirectOrdersFilter, pagingParams: PagingParams) -> DataFlowObject[List[HistoryDirectOrder]] """
        pass

    def GetDirectOrderLineDetailsByLinePk(self, linePk):
        """ GetDirectOrderLineDetailsByLinePk(self: IOutbound, linePk: int) -> DataFlowObject[List[ItemIdentification]] """
        pass

    def GetDirectOrderLineHistoryByFilter(self, filter, pagingParams):
        """ GetDirectOrderLineHistoryByFilter(self: IOutbound, filter: HistoryDirectOrderLinesFilter, pagingParams: PagingParams) -> DataFlowObject[List[HistoryDirectOrderLine]] """
        pass

    def GetDirectOrdersPending(self):
        """ GetDirectOrdersPending(self: IOutbound) -> DataFlowObject[List[DirectOrder]] """
        pass

    def GetHistoryOutboundOrderCustomers(self, args, customers):
        """ GetHistoryOutboundOrderCustomers(self: IOutbound, args: GetHistoryOutboundOrderCustomersArgs) -> (int, Customers) """
        pass

    def GetHistoryOutboundOrderItems(self, args, items):
        """ GetHistoryOutboundOrderItems(self: IOutbound, args: GetHistoryOutboundOrderItemArgs) -> (int, Items) """
        pass

    def GetHistoryOutboundOrders(self, args, outboundOrders):
        """ GetHistoryOutboundOrders(self: IOutbound, args: GetHistoryOutboundOrdersArgs) -> (int, HistoryOutboundOrders) """
        pass

    def GetHistoryPackageNumbers(self, filter, shipmentId, historyShipmentLines):
        """ GetHistoryPackageNumbers(self: IOutbound, filter: OutboundOrdersFilter, shipmentId: int) -> (int, HistoryShipmentLines) """
        pass

    def GetHistoryShipment(self, shipment, packages, shipperId):
        """ GetHistoryShipment(self: IOutbound, shipment: HistoryShipment) -> (bool, TransportPackages, str) """
        pass

    def GetHistoryShipmentItemIdentifications(self, outboundOrdersId, shipmentPackageId, itemIdentifications):
        """ GetHistoryShipmentItemIdentifications(self: IOutbound, outboundOrdersId: int, shipmentPackageId: int) -> (int, ItemIdentifications) """
        pass

    def GetHistoryShipmentLines(self, filter, paging, shipmentPk, historyShipmentLines):
        """ GetHistoryShipmentLines(self: IOutbound, filter: OutboundOrdersFilter, paging: PagingParams, shipmentPk: int) -> (int, HistoryShipmentLines) """
        pass

    def GetHistoryShipmentsAll(self, pagingParams, shipments):
        """ GetHistoryShipmentsAll(self: IOutbound, pagingParams: PagingParams) -> (int, HistoryShipments) """
        pass

    def GetHistoryShipmentsByFilter(self, filter, pagingParams, shipments):
        """ GetHistoryShipmentsByFilter(self: IOutbound, filter: HistoryShipmentFilter, pagingParams: PagingParams) -> (int, HistoryShipments) """
        pass

    def GetHistoryTransportPackages(self, shipmentPk, transportPackages):
        """ GetHistoryTransportPackages(self: IOutbound, shipmentPk: int, transportPackages: TransportPackages) -> TransportPackages """
        pass

    def GetItemIdsFromItemToPack(self, cacheKey, itemCode, itemIds):
        """ GetItemIdsFromItemToPack(self: IOutbound, cacheKey: CacheKey, itemCode: str) -> (bool, ItemIdentifications) """
        pass

    def GetItemsToPack(self, args, itemsToPack, itemsPacked):
        """ GetItemsToPack(self: IOutbound, args: GetItemsToPackArgs) -> (TransportItems, TransportPackages) """
        pass

    def GetItemsToPickOnPickLocation(self, cacheKey, warehouseCode, warehouseLocationCode, items):
        """ GetItemsToPickOnPickLocation(self: IOutbound, cacheKey: CacheKey, warehouseCode: str, warehouseLocationCode: str) -> (int, BatchPickLocations) """
        pass

    def GetMobileShipperById(self, shipperId, shipper):
        """ GetMobileShipperById(self: IOutbound, shipperId: str) -> (bool, MobileShipper) """
        pass

    def GetOutboundOrderLinesBatchableByCustomers(self, customers, batchableOrderLines, nonBatchableOrderLines):
        """ GetOutboundOrderLinesBatchableByCustomers(self: IOutbound, customers: Customers) -> (OutboundOrderLines, OutboundOrderLines) """
        pass

    def GetOutboundOrderLinesBatchableByOrders(self, orderNumbers, batchableOrderlines, nonBatchableOrderlines):
        """ GetOutboundOrderLinesBatchableByOrders(self: IOutbound, orderNumbers: List[str]) -> (OutboundOrderLines, OutboundOrderLines) """
        pass

    def GetOutboundOrdersBatchable(self, args, batchableOrders, nonBatchableOrders):
        """ GetOutboundOrdersBatchable(self: IOutbound, args: GetOutboundOrdersBatchableArgs) -> (OutboundOrders, OutboundOrders) """
        pass

    def GetPackages(self, key, packages):
        """ GetPackages(self: IOutbound, key: CacheKey) -> (bool, TransportPackages) """
        pass

    def GetPickLocationOfItem(self, cacheKey, warehouseCode, itemCode, itemLocations):
        """ GetPickLocationOfItem(self: IOutbound, cacheKey: CacheKey, warehouseCode: str, itemCode: str) -> (int, ItemLocations) """
        pass

    def GetSalesOrder(self, args, salesOrder):
        """ GetSalesOrder(self: IOutbound, args: SalesOrderArgs) -> (bool, SalesOrder) """
        pass

    def GetSalesOrderLines(self, args, salesOrderLines):
        """ GetSalesOrderLines(self: IOutbound, args: SalesOrderLinesArgs) -> (int, SalesOrderLines) """
        pass

    def GetSalesOrdersAll(self, salesOrders):
        """ GetSalesOrdersAll(self: IOutbound) -> (int, SalesOrders) """
        pass

    def GetSalesOrdersByFilter(self, filterBy, salesOrders):
        """ GetSalesOrdersByFilter(self: IOutbound, filterBy: SalesOrderArgs) -> (int, SalesOrders) """
        pass

    def GetShipmentServices(self, shipperId, packagesKey, services):
        """ GetShipmentServices(self: IOutbound, shipperId: str, packagesKey: CacheKey) -> (int, FindableList[MobileService]) """
        pass

    def GetShipperById(self, shipperId, shipper):
        """ GetShipperById(self: IOutbound, shipperId: str) -> (bool, ShipperBase) """
        pass

    def GetShippers(self, shippers):
        """ GetShippers(self: IOutbound) -> (int, FindableList[IShipper]) """
        pass

    def GetShipperServiceLevelsByShipperId(self, shipperId, services):
        """ GetShipperServiceLevelsByShipperId(self: IOutbound, shipperId: str) -> (int, FindableList[MobileService]) """
        pass

    def GetShipperSettingsTableById(self, shipperId):
        """ GetShipperSettingsTableById(self: IOutbound, shipperId: str) -> SystemSettingsTable """
        pass

    def MarkPickLocationAsPicked(self, cacheKey, idOfBatchPickLocation):
        """ MarkPickLocationAsPicked(self: IOutbound, cacheKey: CacheKey, idOfBatchPickLocation: str) -> BatchPickLocation """
        pass

    def MoveTransportItemsBetweenTransportPackages(self, dfObject):
        """ MoveTransportItemsBetweenTransportPackages(self: IOutbound, dfObject: DataFlowObject[MoveTransportItemsBetweenTransportPackagesArgs]) -> DataFlowObject[MoveTransportItemsBetweenTransportPackagesArgs] """
        pass

    def OpenBatchesForPacking(self, args, customers):
        """ OpenBatchesForPacking(self: IOutbound, args: GetCustomersWithPendingPackagesArgs) -> (int, PackCustomers) """
        pass

    def OpenBatchForPickingById(self, id, cacheKey, batch):
        """ OpenBatchForPickingById(self: IOutbound, id: str) -> (bool, CacheKey, Batch) """
        pass

    def OpenTransferPackagesForShipping(self, key, packages):
        """ OpenTransferPackagesForShipping(self: IOutbound, key: CacheKey) -> (bool, TransportPackages) """
        pass

    def PickInBatch(self, dfObject):
        """ PickInBatch(self: IOutbound, dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
        pass

    def PickItemIdInBatch(self, dfObject):
        """ PickItemIdInBatch(self: IOutbound, dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
        pass

    def PickItemIdRangeInBatch(self, dfObject):
        """ PickItemIdRangeInBatch(self: IOutbound, dfObject: DataFlowObject[PickItemIdRangeArgs]) -> DataFlowObject[PickItemIdRangeArgs] """
        pass

    def PickManualSelectedMultipleItemIdsInBatch(self, dfObject):
        """ PickManualSelectedMultipleItemIdsInBatch(self: IOutbound, dfObject: DataFlowObject[PickItemIdsArgs]) -> DataFlowObject[PickItemIdsArgs] """
        pass

    def PickMultipleScannedItemIdsInBatch(self, dfObject):
        """ PickMultipleScannedItemIdsInBatch(self: IOutbound, dfObject: DataFlowObject[PickItemIdsArgs]) -> DataFlowObject[PickItemIdsArgs] """
        pass

    def PrintDocumentsOfShipment(self, args):
        """ PrintDocumentsOfShipment(self: IOutbound, args: PrintShipmentDocumentArgs) -> bool """
        pass

    def PrintDuplicateLabels(self, args):
        """ PrintDuplicateLabels(self: IOutbound, args: PrintDuplicateLabelArgs) -> bool """
        pass

    def PrintPackageSlip(self, args):
        """ PrintPackageSlip(self: IOutbound, args: PrintPackageSlipArgs) -> bool """
        pass

    def PrintTransportPackageLabel(self, cacheKey, boxGuid, label):
        """ PrintTransportPackageLabel(self: IOutbound, cacheKey: CacheKey, boxGuid: Guid, label: PrintLabel) -> bool """
        pass

    def ProcessBatchPacking(self, dfObject):
        """ ProcessBatchPacking(self: IOutbound, dfObject: DataFlowObject[ProcessBatchPackingArgs]) -> DataFlowObject[ProcessBatchPackingArgs] """
        pass

    def ProcessBatchPicking(self, dfObject):
        """ ProcessBatchPicking(self: IOutbound, dfObject: DataFlowObject[ProcessBatchPickingArgs]) -> DataFlowObject[ProcessBatchPickingArgs] """
        pass

    def ProcessDirectOrder(self, args):
        """ ProcessDirectOrder(self: IOutbound, args: DirectOrderCrudArgs) -> DataFlowObject[DirectOrder] """
        pass

    def ProcessSalesOrder(self, args, order):
        """ ProcessSalesOrder(self: IOutbound, args: ProcessSalesOrderLinesArgs, order: KeyValuePair[OutboundOrder, OutboundOrderLines]) -> ErpProcessSalesOrderLinesResult """
        pass

    def ProcessSalesOrderQueued(self, args, order):
        """ ProcessSalesOrderQueued(self: IOutbound, args: ProcessSalesOrderLinesArgs, order: KeyValuePair[OutboundOrder, OutboundOrderLines]) -> ErpProcessSalesOrderLinesResult """
        pass

    def ProcessShipment(self, arg):
        """ ProcessShipment(self: IOutbound, arg: DataFlowObject[ProcessShipmentArgs]) -> DataFlowObject[ProcessShipmentArgs] """
        pass

    def ProcessShipmentWithDefaultServiceLevel(self, arg):
        """ ProcessShipmentWithDefaultServiceLevel(self: IOutbound, arg: CacheKey) """
        pass

    def PutBackFromBatch(self, dfObject):
        """ PutBackFromBatch(self: IOutbound, dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
        pass

    def PutItemIdBackFromBatch(self, dfObject):
        """ PutItemIdBackFromBatch(self: IOutbound, dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
        pass

    def RemoveDirectOrder(self, args):
        """ RemoveDirectOrder(self: IOutbound, args: DirectOrderCrudArgs) """
        pass

    def RemoveDirectOrderLine(self, args):
        """ RemoveDirectOrderLine(self: IOutbound, args: DirectOrderLineCrudArgs) -> DataFlowObject[bool] """
        pass

    def RemoveDirectOrderLineItemIdentification(self, args):
        """ RemoveDirectOrderLineItemIdentification(self: IOutbound, args: DirectOrderLineItemIdentificationCrudArgs) -> DataFlowObject[DirectOrderLine] """
        pass

    def RemovePackage(self, boxGuid, args, itemsToPack, packages):
        """ RemovePackage(self: IOutbound, boxGuid: Guid, args: GetItemsToPackArgs) -> (bool, TransportItems, TransportPackages) """
        pass

    def RemoveTransportPackages(self, packagesKey):
        """ RemoveTransportPackages(self: IOutbound, packagesKey: CacheKey) """
        pass

    def SaveBatch(self, batch):
        """ SaveBatch(self: IOutbound, batch: Batch) -> Batch """
        pass

    def SaveShipperSetting(self, shipperId, memberName, value):
        """ SaveShipperSetting(self: IOutbound, shipperId: str, memberName: str, value: object) """
        pass

    def ScanItemForPacking(self, args, result):
        """ ScanItemForPacking(self: IOutbound, args: ItemPackScanArgs) -> (bool, ScanItemPackArgsResult) """
        pass

    def SkipOrderForProcessingPack(self, batchId, orderNumber):
        """ SkipOrderForProcessingPack(self: IOutbound, batchId: str, orderNumber: str) -> bool """
        pass

    def UpdateBatchWithSettings(self, batchId, args):
        """ UpdateBatchWithSettings(self: IOutbound, batchId: Guid, args: BatchUpdateArgs) """
        pass

    def UpdateColloReference(self, dfObject):
        """ UpdateColloReference(self: IOutbound, dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
        pass

    def UpdateDirectOrderLine(self, args):
        """ UpdateDirectOrderLine(self: IOutbound, args: DirectOrderLineCrudArgs) -> DataFlowObject[DirectOrderLine] """
        pass

    def UpdateDirectOrderLineItemIdentification(self, args):
        """ UpdateDirectOrderLineItemIdentification(self: IOutbound, args: DirectOrderLineItemIdentificationCrudArgs) -> DataFlowObject[DirectOrderLine] """
        pass

    def UpdatePackageData(self, args, newPackageData, packages):
        """ UpdatePackageData(self: IOutbound, args: UpdateTransportPackageArgs, newPackageData: TransportPackage) -> (bool, TransportPackages) """
        pass

    def UpdateTransportPackagesHeader(self, packagesKey, args, packages):
        """ UpdateTransportPackagesHeader(self: IOutbound, packagesKey: CacheKey, args: UpdateTransportPackagesHeaderArgs) -> (bool, TransportPackages) """
        pass

    def ValidateBatchedItem(self, cacheKey, selectedBatchPickLocation, itemCode):
        """ ValidateBatchedItem(self: IOutbound, cacheKey: CacheKey, selectedBatchPickLocation: BatchPickLocation, itemCode: str) -> DataFlowObject[CacheKey] """
        pass

    def ValidateBatchLocation(self, cacheKey, selectedBatchPickLocation, locationCode):
        """ ValidateBatchLocation(self: IOutbound, cacheKey: CacheKey, selectedBatchPickLocation: BatchPickLocation, locationCode: str) -> DataFlowObject[CacheKey] """
        pass

    def VoidShipment(self, shipment):
        """ VoidShipment(self: IOutbound, shipment: DataFlowObject[HistoryShipment]) -> DataFlowObject[HistoryShipment] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return IOutbound()

class IPrinting:
    # no doc
    def GetPickListsAll(self, pickLists):
        """ GetPickListsAll(self: IPrinting) -> (int, ReportItems) """
        pass

    def PrintPickBatchLabel(self, args):
        """ PrintPickBatchLabel(self: IPrinting, args: DataFlowObject[PrintPickbatchLabelArgs]) -> DataFlowObject[PrintPickbatchLabelArgs] """
        pass

    def PrintPickList(self, args):
        """ PrintPickList(self: IPrinting, args: PrintPickingListArgs) -> bool """
        pass

    def PrintSSCCLabels(self, args):
        """ PrintSSCCLabels(self: IPrinting, args: DataFlowObject[PrintSSCCLabelsArgs]) -> DataFlowObject[PrintSSCCLabelsArgs] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return IPrinting()

class IRemotePublishing:
    # no doc
    def AddRemotePublisher(self, args):
        """ AddRemotePublisher(self: IRemotePublishing, args: AddRemotePublisherArgs) -> Publisher """
        pass

    def DeleteRemotePublisher(self, args):
        """ DeleteRemotePublisher(self: IRemotePublishing, args: DeleteRemotePublisherArgs) """
        pass

    def EditRemotePublisher(self, args):
        """ EditRemotePublisher(self: IRemotePublishing, args: EditRemotePublisherArgs) -> Publisher """
        pass

    def GetRemotePublishers(self):
        """ GetRemotePublishers(self: IRemotePublishing) -> Publishers """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return IRemotePublishing()

