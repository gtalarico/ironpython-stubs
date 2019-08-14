from System import *
# encoding: utf-8
# module Wms.RemotingImplementation calls itself RemotingImplementation
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AppHost():
    """ AppHost() """
    Instance = AppHost
    """hardcoded/returns an instance of the class"""
    def CreateContainer(self):
        """ CreateContainer(self: AppHost) -> UnityContainer """
        pass

    def Init(self, appSettings, authoritySystem):
        """ Init(self: AppHost, appSettings: IApplicationSettings, authoritySystem: ICentralAuthoritySystem) """
        pass

    def RegisterQueues(self, container):
        """ RegisterQueues(self: AppHost, container: IUnityContainer) """
        pass


class BusinessLayerExtensions():
    # no doc
    Instance = BusinessLayerExtensions
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def ConvertTo(db, mapExpr):
        pass

    __all__ = [
        'ConvertTo',
    ]


class CallerContext:
    """ CallerContext() """
    Instance = CallerContext
    """hardcoded/returns an instance of the class"""
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserName(self: CallerContext) -> str

"""



class Constants():
    # no doc
    Instance = Constants
    """hardcoded/returns an instance of the class"""
    AdminZoneId = 2
    AutoDisposeDeadObjectInterval = 5
    Batch = 'Batch'
    ItemIdType = None
    ItemMovementTasks = None
    LayoutsDirectory = 'C:\\Program Files (x86)\\TranCon\\BOXwisePro\\Server\\Layouts'
    MaxAllowedTimeDifference = None
    PurchaseOrderLineItemIdTokenFormat = 'PO:{0}{1}{2}'
    RefreshSettingsInterval = 60.0
    ReportsPackageSlipFile = 'PackageSlip.rdlc'
    ReportsPackingSlipFolder = 'C:\\Program Files (x86)\\TranCon\\BOXwisePro\\Server\\Layouts\\PackageSlip'
    ReportsPickListsConfigFile = 'Config.xml'
    ReportsPickListsFolder = 'C:\\Program Files (x86)\\TranCon\\BOXwisePro\\Server\\Layouts\\Picking'
    ReportsPurchaseReceiptFile = 'ReceivingSlip.rdlc'
    ReportsPurchaseReceiptFolder = 'C:\\Program Files (x86)\\TranCon\\BOXwisePro\\Server\\Layouts\\PurchaseReceipt'
    ReportsRmaReceiptFile = 'RmaReceipt.rdlc'
    ReportsRmaReceiptFolder = 'C:\\Program Files (x86)\\TranCon\\BOXwisePro\\Server\\Layouts\\RmaReceipt'
    RmaOrderLineItemIdTokenFormat = 'RMA:{0}{1}{2}'
    SalesOrderLineItemIdTokenFormat = 'SO:{0}{1}{2}'
    Serial = 'Serial'
    ServerClientName = '__SERVER__TASK_{0}'
    ServerUsername = 'server'
    Shipping = None
    StartupSqlConnRetryAttempts = 3
    SupportedImages = None
    ThreadTimeoutGetDeviceInfo = 1200
    ThreadTimeoutGetScreenShot = 1200
    ThreadTimeoutSendBroadcastQuestion = 10000
    ThreadTimeoutVoidShipment = 60000
    TokenDelimiter = '|'
    TraceCategoryDebug = 'Debug'
    __all__ = [
        'AdminZoneId',
        'AutoDisposeDeadObjectInterval',
        'Batch',
        'ItemIdType',
        'ItemMovementTasks',
        'MaxAllowedTimeDifference',
        'PurchaseOrderLineItemIdTokenFormat',
        'RefreshSettingsInterval',
        'RmaOrderLineItemIdTokenFormat',
        'SalesOrderLineItemIdTokenFormat',
        'Serial',
        'ServerClientName',
        'ServerUsername',
        'Shipping',
        'StartupSqlConnRetryAttempts',
        'SupportedImages',
        'ThreadTimeoutGetDeviceInfo',
        'ThreadTimeoutGetScreenShot',
        'ThreadTimeoutSendBroadcastQuestion',
        'ThreadTimeoutVoidShipment',
        'TokenDelimiter',
        'TraceCategoryDebug',
    ]


class DataSet(DataSet):
    """ DataSet() """
    Instance = DataSet
    """hardcoded/returns an instance of the class"""
    def Clone(self):
        """ Clone(self: DataSet) -> DataSet """
        pass

    def DetermineSchemaSerializationMode(self, *args): #cannot find CLR method
        """
        DetermineSchemaSerializationMode(self: DataSet, info: SerializationInfo, context: StreamingContext) -> SchemaSerializationMode
        
            Determines the System.Data.DataSet.SchemaSerializationMode for a System.Data.DataSet.
        
                     System.Data.DataSet.#ctor(System.Runtime.Serialization.SerializationInfo,System.Runtime.Serialization.StreamingContext) is invoked with during deserialization in remoting 
             scenarios.
        
                     System.Data.DataSet.#ctor(System.Runtime.Serialization.SerializationInfo,System.Runtime.Serialization.StreamingContext) is invoked with during deserialization in remoting 
             scenarios.
        
            Returns: An System.Data.SchemaSerializationMode enumeration indicating whether schema information has been omitted from the payload.
        DetermineSchemaSerializationMode(self: DataSet, reader: XmlReader) -> SchemaSerializationMode
        
            Determines the System.Data.DataSet.SchemaSerializationMode for a System.Data.DataSet.
        
            reader: The System.Xml.XmlReader instance that is passed during deserialization of the System.Data.DataSet.
            Returns: An System.Data.SchemaSerializationMode enumeration indicating whether schema information has been omitted from the payload.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: MarshalByValueComponent, disposing: bool)
            Releases the unmanaged resources used by the System.ComponentModel.MarshalByValueComponent and optionally releases the managed resources.
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def GetSchemaSerializable(self, *args): #cannot find CLR method
        """ GetSchemaSerializable(self: DataSet) -> XmlSchema """
        pass

    def GetSerializationData(self, *args): #cannot find CLR method
        """
        GetSerializationData(self: DataSet, info: SerializationInfo, context: StreamingContext)
            Deserializes the table data from the binary or XML stream.
        
            info: The System.Runtime.Serialization.SerializationInfo instance.
            context: The streaming context.
        """
        pass

    @staticmethod
    def GetTypedDataSetSchema(xs):
        """ GetTypedDataSetSchema(xs: XmlSchemaSet) -> XmlSchemaComplexType """
        pass

    def InitializeDerivedDataSet(self, *args): #cannot find CLR method
        """ InitializeDerivedDataSet(self: DataSet) """
        pass

    def IsBinarySerialized(self, *args): #cannot find CLR method
        """
        IsBinarySerialized(self: DataSet, info: SerializationInfo, context: StreamingContext) -> bool
        
            Inspects the format of the serialized representation of the DataSet.
        
            info: The System.Runtime.Serialization.SerializationInfo object.
            context: The System.Runtime.Serialization.StreamingContext object.
            Returns: true if the specified System.Runtime.Serialization.SerializationInfo represents a DataSet serialized in its binary format, false otherwise.
        """
        pass

    def OnPropertyChanging(self, *args): #cannot find CLR method
        """
        OnPropertyChanging(self: DataSet, pcevent: PropertyChangedEventArgs)
            Raises the System.Data.DataSet.OnPropertyChanging(System.ComponentModel.PropertyChangedEventArgs) event.
        
            pcevent: A System.ComponentModel.PropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnRemoveRelation(self, *args): #cannot find CLR method
        """
        OnRemoveRelation(self: DataSet, relation: DataRelation)
            Occurs when a System.Data.DataRelation object is removed from a System.Data.DataTable.
        
            relation: The System.Data.DataRelation being removed.
        """
        pass

    def OnRemoveTable(self, *args): #cannot find CLR method
        """
        OnRemoveTable(self: DataSet, table: DataTable)
            Occurs when a System.Data.DataTable is removed from a System.Data.DataSet.
        
            table: The System.Data.DataTable being removed.
        """
        pass

    def RaisePropertyChanging(self, *args): #cannot find CLR method
        """
        RaisePropertyChanging(self: DataSet, name: str)
            Sends a notification that the specified System.Data.DataSet property is about to change.
        
            name: The name of the property that is about to change.
        """
        pass

    def ReadXmlSerializable(self, *args): #cannot find CLR method
        """ ReadXmlSerializable(self: DataSet, reader: XmlReader) """
        pass

    def ShouldSerializeRelations(self, *args): #cannot find CLR method
        """ ShouldSerializeRelations(self: DataSet) -> bool """
        pass

    def ShouldSerializeTables(self, *args): #cannot find CLR method
        """ ShouldSerializeTables(self: DataSet) -> bool """
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
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this component.

"""

    PurchaseOrders_GetHistoryLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PurchaseOrders_GetHistoryLines(self: DataSet) -> PurchaseOrders_GetHistoryLinesDataTable

"""

    Relations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Relations(self: DataSet) -> DataRelationCollection

"""

    RmaOrders_GetHistoryLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RmaOrders_GetHistoryLines(self: DataSet) -> RmaOrders_GetHistoryLinesDataTable

"""

    SchemaSerializationMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SchemaSerializationMode(self: DataSet) -> SchemaSerializationMode

Set: SchemaSerializationMode(self: DataSet) = value
"""

    Shipment_GetHistoryShipmentLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Shipment_GetHistoryShipmentLines(self: DataSet) -> Shipment_GetHistoryShipmentLinesDataTable

"""

    Tables = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tables(self: DataSet) -> DataTableCollection

"""


    PurchaseOrders_GetHistoryLinesDataTable = None
    PurchaseOrders_GetHistoryLinesRow = None
    PurchaseOrders_GetHistoryLinesRowChangeEvent = None
    PurchaseOrders_GetHistoryLinesRowChangeEventHandler = None
    RmaOrders_GetHistoryLinesDataTable = None
    RmaOrders_GetHistoryLinesRow = None
    RmaOrders_GetHistoryLinesRowChangeEvent = None
    RmaOrders_GetHistoryLinesRowChangeEventHandler = None
    Shipment_GetHistoryShipmentLinesDataTable = None
    Shipment_GetHistoryShipmentLinesRow = None
    Shipment_GetHistoryShipmentLinesRowChangeEvent = None
    Shipment_GetHistoryShipmentLinesRowChangeEventHandler = None


class DocumentQueue(MarshalByRefObject):
    """ DocumentQueue(printingService: IPrintingService, storageProvider: StorageProvider, printJobsQueuer: PrintJobsQueuer) """
    Instance = DocumentQueue
    """hardcoded/returns an instance of the class"""
    def AddPrintJob(self, args):
        """ AddPrintJob(self: DocumentQueue, args: AddPrintJob) -> Task[Guid] """
        pass

    def AddPrintJobScriptOverride(self, args, blobId, blobName):
        """ AddPrintJobScriptOverride(self: DocumentQueue, args: AddPrintJob, blobId: int, blobName: str) -> Guid """
        pass

    def CopyPrintRule(self, printRuleId):
        """ CopyPrintRule(self: DocumentQueue, printRuleId: int) -> PrintRule """
        pass

    def DeletePrintJobs(self, jobIds):
        """ DeletePrintJobs(self: DocumentQueue, jobIds: Array[Guid]) """
        pass

    def DeletePrintRule(self, printRuleId):
        """ DeletePrintRule(self: DocumentQueue, printRuleId: int) """
        pass

    def DeletePrintRules(self, ruleIds):
        """ DeletePrintRules(self: DocumentQueue, ruleIds: List[int]) """
        pass

    def GetBlobContent(self, blobId):
        """ GetBlobContent(self: DocumentQueue, blobId: int) -> BlobContent """
        pass

    def GetFileTypes(self):
        """ GetFileTypes(self: DocumentQueue) -> List[DocumentTypeEnum] """
        pass

    def GetMatchingPrintRules(self, attributes):
        """ GetMatchingPrintRules(self: DocumentQueue, attributes: SerializableDictionary[str, str]) -> List[int] """
        pass

    def GetOperators(self):
        """ GetOperators(self: DocumentQueue) -> List[Operator] """
        pass

    def GetPrinterRules(self, args):
        """ GetPrinterRules(self: DocumentQueue, args: GetPrinterRulesArgs) -> List[PrintRule] """
        pass

    def GetPrinters(self):
        """ GetPrinters(self: DocumentQueue) -> List[Printer] """
        pass

    def GetPrintJobAttributes(self, printJobId):
        """ GetPrintJobAttributes(self: DocumentQueue, printJobId: Guid) -> SerializableDictionary[str, str] """
        pass

    def GetPrintJobAuditLog(self, printJobId, paging):
        """ GetPrintJobAuditLog(self: DocumentQueue, printJobId: Guid, paging: PagingParams) -> PagedList[PrintJobAuditLogEntry] """
        pass

    def GetPrintJobs(self, args, paging):
        """ GetPrintJobs(self: DocumentQueue, args: GetPrintJobsArgs, paging: PagingParams) -> PagedList[QueuedPrintJob] """
        pass

    def GetPrintJobTypes(self):
        """ GetPrintJobTypes(self: DocumentQueue) -> List[PrintJobType] """
        pass

    def GetPrintJobTypesOfConfiguredPrintRules(self):
        """ GetPrintJobTypesOfConfiguredPrintRules(self: DocumentQueue) -> List[PrintJobType] """
        pass

    def GetPrintRuleConditions(self, printRuleId):
        """ GetPrintRuleConditions(self: DocumentQueue, printRuleId: int) -> List[PrintRuleLine] """
        pass

    def GetUsedAttributeNames(self, args):
        """ GetUsedAttributeNames(self: DocumentQueue, args: GetPrintJobAttributesArgs) -> List[PrintJobAttribute] """
        pass

    def GetUsedAttributeValues(self, attributeName):
        """ GetUsedAttributeValues(self: DocumentQueue, attributeName: str) -> List[str] """
        pass

    def GetUsedAttributeValuesAsObject(self, attributeName):
        """ GetUsedAttributeValuesAsObject(self: DocumentQueue, attributeName: str) -> List[AttributeValue] """
        pass

    def GetUsedPrintJobTypes(self):
        """ GetUsedPrintJobTypes(self: DocumentQueue) -> List[PrintJobType] """
        pass

    def InitializeLifetimeService(self):
        """ InitializeLifetimeService(self: DocumentQueue) -> object """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting 
             boundary. A value of false is usually appropriate. true to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls 
             to be routed to the remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def RedispatchPrintJob(self, jobId):
        """ RedispatchPrintJob(self: DocumentQueue, jobId: Guid) """
        pass

    def RedispatchPrintJobWithPrinter(self, args):
        """ RedispatchPrintJobWithPrinter(self: DocumentQueue, args: RedispatchPrintJobArgs) """
        pass

    def SavePrintRule(self, rule):
        """ SavePrintRule(self: DocumentQueue, rule: PrintRule) -> PrintRule """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, printingService, storageProvider, printJobsQueuer):
        """ __new__(cls: type, printingService: IPrintingService, storageProvider: StorageProvider, printJobsQueuer: PrintJobsQueuer) """
        pass


class ExceptionHelper():
    """ ExceptionHelper() """
    Instance = ExceptionHelper
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def IsRetryPossible(ex, currentIdentity):
        """ IsRetryPossible(ex: Exception, currentIdentity: RemotingIdentity) -> bool """
        pass

    @staticmethod
    def WrapException(ex):
        """ WrapException(ex: Exception) -> RemotingException """
        pass


class ExtendedUnityServiceLocator(UnityServiceLocator):
    """ ExtendedUnityServiceLocator(container: IUnityContainer) """
    Instance = ExtendedUnityServiceLocator
    """hardcoded/returns an instance of the class"""
    def DoGetAllInstances(self, *args): #cannot find CLR method
        """ DoGetAllInstances(self: UnityServiceLocator, serviceType: Type) -> IEnumerable[object] """
        pass

    def DoGetInstance(self, *args): #cannot find CLR method
        """ DoGetInstance(self: UnityServiceLocator, serviceType: Type, key: str) -> object """
        pass

    def FormatActivateAllExceptionMessage(self, *args): #cannot find CLR method
        """ FormatActivateAllExceptionMessage(self: ServiceLocatorImplBase, actualException: Exception, serviceType: Type) -> str """
        pass

    def FormatActivationExceptionMessage(self, *args): #cannot find CLR method
        """ FormatActivationExceptionMessage(self: ServiceLocatorImplBase, actualException: Exception, serviceType: Type, key: str) -> str """
        pass

    def IsRegistered(self, type=None):
        """
        IsRegistered[T](self: ExtendedUnityServiceLocator) -> bool
        IsRegistered(self: ExtendedUnityServiceLocator, type: Type) -> bool
        """
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
    def __new__(self, container):
        """ __new__(cls: type, container: IUnityContainer) """
        pass


class General(MarshalByRefObject):
    """ General(stockManager: IStockManager, passwordHasher: IPasswordHasher, documentQueue: IDocumentQueue) """
    Instance = General
    """hardcoded/returns an instance of the class"""
    def AddOrUpdateErpLock(self, lock):
        """ AddOrUpdateErpLock(self: General, lock: ErpLock) -> int """
        pass

    def AddOrUpdateErpLockDirect(self, lock):
        """ AddOrUpdateErpLockDirect(self: General, lock: ErpLock) -> int """
        pass

    def AddTaskAutoDisposeTask(self):
        """ AddTaskAutoDisposeTask(self: General) """
        pass

    def AddTaskCacheBackgroundTasks(self):
        """ AddTaskCacheBackgroundTasks(self: General) """
        pass

    def AddTaskErpLockingTask(self):
        """ AddTaskErpLockingTask(self: General) """
        pass

    def AddTaskLogCleanupTask(self):
        """ AddTaskLogCleanupTask(self: General) """
        pass

    def AddTaskMessageQueueCleanupTask(self):
        """ AddTaskMessageQueueCleanupTask(self: General) """
        pass

    def AddTaskNotificationCleanupTask(self):
        """ AddTaskNotificationCleanupTask(self: General) """
        pass

    def AddTaskStockStreamTask(self):
        """ AddTaskStockStreamTask(self: General) """
        pass

    def AddUserToZone(self, zone, user):
        """ AddUserToZone(self: General, zone: Zone, user: User) -> bool """
        pass

    def AttachClient(self, endPoint):
        """ AttachClient(self: General, endPoint: str) """
        pass

    def AuthenticateUser(self, args, barcodeSettings):
        """ AuthenticateUser(self: General, args: AuthenticationArgs) -> (RemotingIdentity, BarcodeTypes) """
        pass

    def AuthenticateUserForDefaultZone(self, remId):
        """ AuthenticateUserForDefaultZone(self: General) -> (bool, RemotingIdentity) """
        pass

    def AuthenticateUserForFirstZone(self, remId):
        """ AuthenticateUserForFirstZone(self: General) -> (bool, RemotingIdentity) """
        pass

    def AuthenticateUserForZone(self, selectedZone, remId):
        """ AuthenticateUserForZone(self: General, selectedZone: Zone) -> (bool, RemotingIdentity) """
        pass

    def BeepContinuous(self, endPoint):
        """ BeepContinuous(self: General, endPoint: str) """
        pass

    def ChangeItemBarcode(self, args):
        """ ChangeItemBarcode(self: General, args: ChangeBarcodeArgs) -> bool """
        pass

    def CheckHookVersions(self):
        """ CheckHookVersions(self: General) -> bool """
        pass

    def CheckLicenseFile(self, xml, errors, license):
        """ CheckLicenseFile(self: General, xml: str) -> (bool, List[str], License) """
        pass

    def CheckServerHealth(self):
        """ CheckServerHealth(self: General) -> ServerHealthEnum """
        pass

    def CheckZoneRightAddReferenceOnTransfer(self, warehouseTransferKey):
        """ CheckZoneRightAddReferenceOnTransfer(self: General, warehouseTransferKey: CacheKey) -> bool """
        pass

    def CleanupCacheHistory(self):
        """ CleanupCacheHistory(self: General) """
        pass

    def CleanupUserCacheData(self):
        """ CleanupUserCacheData(self: General) """
        pass

    def ClearResourceCache(self):
        """ ClearResourceCache(self: General) """
        pass

    def CompileScript(self, script):
        """ CompileScript(self: General, script: str) -> List[PythonError] """
        pass

    def ConvertToUsersByZone(self, oZonesUsersProxy):
        """ ConvertToUsersByZone(self: General, oZonesUsersProxy: ViewUsersInZone) -> Users """
        pass

    def CreateBarcodeStructureDefinition(self, arg):
        """ CreateBarcodeStructureDefinition(self: General, arg: DataFlowObject[BarcodeStructureDefinition]) -> DataFlowObject[BarcodeStructureDefinition] """
        pass

    def CreateColliPreset(self, arg):
        """ CreateColliPreset(self: General, arg: DataFlowObject[ColliPreset]) -> DataFlowObject[ColliPreset] """
        pass

    def CreateDatabase(self, message):
        """ CreateDatabase(self: General) -> (bool, str) """
        pass

    def CreateDevice(self, arg):
        """ CreateDevice(self: General, arg: DataFlowObject[Device]) -> DataFlowObject[Device] """
        pass

    def CreateLocationClassification(self, arg):
        """ CreateLocationClassification(self: General, arg: DataFlowObject[LocationClassification]) -> DataFlowObject[LocationClassification] """
        pass

    def CreateModule(self, arg):
        """ CreateModule(self: General, arg: ModuleArgs) -> bool """
        pass

    def CreateOrUpdateBackgroundAgent(self, arg):
        """ CreateOrUpdateBackgroundAgent(self: General, arg: DataFlowObject[BackgroundAgent]) -> DataFlowObject[BackgroundAgent] """
        pass

    def CreatePrintLabel(self, arg):
        """ CreatePrintLabel(self: General, arg: DataFlowObject[PrintLabel]) -> DataFlowObject[PrintLabel] """
        pass

    def CreateScript(self, arg):
        """ CreateScript(self: General, arg: DataFlowObject[ZoneScript]) -> DataFlowObject[ZoneScript] """
        pass

    def CreateScriptTask(self, arg):
        """ CreateScriptTask(self: General, arg: DataFlowObject[ScriptTask]) -> DataFlowObject[ScriptTask] """
        pass

    def CreateShipperServiceLink(self, arg):
        """ CreateShipperServiceLink(self: General, arg: DataFlowObject[ShipperServiceLink]) -> DataFlowObject[ShipperServiceLink] """
        pass

    def CreateSnippetModule(self, arg):
        """ CreateSnippetModule(self: General, arg: ModuleArgs) -> bool """
        pass

    def CreateStorageAssignmentClassification(self, arg):
        """ CreateStorageAssignmentClassification(self: General, arg: DataFlowObject[StorageAssignmentClassification]) -> DataFlowObject[StorageAssignmentClassification] """
        pass

    def CreateTag(self, arg):
        """ CreateTag(self: General, arg: DataFlowObject[Tag]) -> DataFlowObject[Tag] """
        pass

    def CreateUser(self, arg):
        """ CreateUser(self: General, arg: DataFlowObject[User]) -> DataFlowObject[User] """
        pass

    def CreateWarehouseLayoutSetting(self, arg):
        """ CreateWarehouseLayoutSetting(self: General, arg: DataFlowObject[WarehouseLayoutSetting]) -> DataFlowObject[WarehouseLayoutSetting] """
        pass

    def CreateZone(self, arg):
        """ CreateZone(self: General, arg: DataFlowObject[Zone]) -> DataFlowObject[Zone] """
        pass

    def DeleteBackgroundAgent(self, arg):
        """ DeleteBackgroundAgent(self: General, arg: DataFlowObject[BackgroundAgent]) -> DataFlowObject[BackgroundAgent] """
        pass

    def DeleteBarcodeStructureDefinition(self, arg):
        """ DeleteBarcodeStructureDefinition(self: General, arg: DataFlowObject[BarcodeStructureDefinition]) -> DataFlowObject[BarcodeStructureDefinition] """
        pass

    def DeleteColliPreset(self, arg):
        """ DeleteColliPreset(self: General, arg: DataFlowObject[ColliPreset]) -> DataFlowObject[ColliPreset] """
        pass

    def DeleteDevice(self, arg):
        """ DeleteDevice(self: General, arg: DataFlowObject[Device]) -> DataFlowObject[Device] """
        pass

    def DeleteErpLock(self, lock):
        """ DeleteErpLock(self: General, lock: ErpLock) """
        pass

    def DeleteLocationClassification(self, arg):
        """ DeleteLocationClassification(self: General, arg: DataFlowObject[LocationClassification]) -> DataFlowObject[LocationClassification] """
        pass

    def DeleteModule(self, arg):
        """ DeleteModule(self: General, arg: ModuleArgs) -> bool """
        pass

    def DeletePrintLabel(self, arg):
        """ DeletePrintLabel(self: General, arg: DataFlowObject[PrintLabel]) -> DataFlowObject[PrintLabel] """
        pass

    def DeleteScript(self, arg):
        """ DeleteScript(self: General, arg: DataFlowObject[ZoneScript]) -> DataFlowObject[ZoneScript] """
        pass

    def DeleteScriptTask(self, arg):
        """ DeleteScriptTask(self: General, arg: DataFlowObject[ScriptTask]) -> DataFlowObject[ScriptTask] """
        pass

    def DeleteShipperServiceLink(self, arg):
        """ DeleteShipperServiceLink(self: General, arg: DataFlowObject[ShipperServiceLink]) -> DataFlowObject[ShipperServiceLink] """
        pass

    def DeleteStorageAssignmentClassification(self, arg):
        """ DeleteStorageAssignmentClassification(self: General, arg: DataFlowObject[StorageAssignmentClassification]) -> DataFlowObject[StorageAssignmentClassification] """
        pass

    def DeleteTag(self, arg):
        """ DeleteTag(self: General, arg: DataFlowObject[Tag]) -> DataFlowObject[Tag] """
        pass

    def DeleteUser(self, arg):
        """ DeleteUser(self: General, arg: DataFlowObject[User]) -> DataFlowObject[User] """
        pass

    def DeleteWarehouseLayoutSetting(self, arg):
        """ DeleteWarehouseLayoutSetting(self: General, arg: DataFlowObject[WarehouseLayoutSetting]) -> DataFlowObject[WarehouseLayoutSetting] """
        pass

    def DeleteZone(self, arg):
        """ DeleteZone(self: General, arg: DataFlowObject[Zone]) -> DataFlowObject[Zone] """
        pass

    def DiscardPrintLines(self, key):
        """ DiscardPrintLines(self: General, key: CacheKey) """
        pass

    def DisposeCachedObject(self, hashCode):
        """ DisposeCachedObject(self: General, hashCode: int) -> DataFlowObject[object] """
        pass

    def DisposeCachedObjects(self):
        """ DisposeCachedObjects(self: General) """
        pass

    def DisposeCachedObjectWhenUnchanged(self, key):
        """ DisposeCachedObjectWhenUnchanged(self: General, key: CacheKey) """
        pass

    def ExecuteCommand(self, command):
        """ ExecuteCommand(self: General, command: str) -> str """
        pass

    def ExecuteScript(self, script):
        """ ExecuteScript(self: General, script: str) -> object """
        pass

    def ExecuteScriptTaskOnce(self, id):
        """ ExecuteScriptTaskOnce(self: General, id: int) -> object """
        pass

    def ExecuteScriptWithCacheObjectScope(self, script, cacheKey):
        """ ExecuteScriptWithCacheObjectScope(self: General, script: str, cacheKey: int) -> object """
        pass

    def ExecuteScriptWithScope(self, script, scope):
        """ ExecuteScriptWithScope(self: General, script: str, scope: Dictionary[str, object]) -> object """
        pass

    def FinishUploadModule(self, arg):
        """ FinishUploadModule(self: General, arg: ModuleArgs) -> bool """
        pass

    def GenerateSerialNumbers(self, dfObject, numbersGenerated):
        """ GenerateSerialNumbers(self: General, dfObject: DataFlowObject[ItemIdGenerateArgs]) -> (DataFlowObject[ItemIdGenerateArgs], List[str]) """
        pass

    def GetActiveColliPresets(self, colliPresets):
        """ GetActiveColliPresets(self: General) -> (int, ColliPresets) """
        pass

    def GetAppDomainList(self):
        """ GetAppDomainList(self: General) -> List[AppDomainInformation] """
        pass

    def GetBackgroundAgentById(self, id, agent):
        """ GetBackgroundAgentById(self: General, id: str) -> (bool, BackgroundAgent) """
        pass

    def GetBackgroundAgentsAll(self, agents):
        """ GetBackgroundAgentsAll(self: General) -> (int, BackgroundAgents) """
        pass

    def GetBackgroundAgentsByType(self, type, agents):
        """ GetBackgroundAgentsByType(self: General, type: BackgroundAgentType) -> (int, BackgroundAgents) """
        pass

    def GetBackgroundAgentStatusByType(self, type):
        """ GetBackgroundAgentStatusByType(self: General, type: BackgroundAgentType) -> BackgroundAgentStatus """
        pass

    def GetBarcodeSettingsAll(self, types):
        """ GetBarcodeSettingsAll(self: General) -> (int, BarcodeTypes) """
        pass

    def GetBarcodeStructure(self, value, expectedScan, barcodeStructure):
        """ GetBarcodeStructure(self: General, value: str, expectedScan: ExpectScanOfEnum) -> (BarcodeStructureResultEnum, BarcodeStructure) """
        pass

    def GetBarcodeStructureActive(self, definitions):
        """ GetBarcodeStructureActive(self: General) -> (int, BarcodeStructureDefinitions) """
        pass

    def GetBarcodeStructureDefinitionById(self, countId, definition):
        """ GetBarcodeStructureDefinitionById(self: General, countId: int) -> (bool, BarcodeStructureDefinition) """
        pass

    def GetBarcodeStructureDefinitions(self, filterBy, pagingParams, definitions):
        """ GetBarcodeStructureDefinitions(self: General, filterBy: BarcodeStructureDefinitionFilter, pagingParams: PagingParams) -> (int, BarcodeStructureDefinitions) """
        pass

    def GetBarcodeStructureInOrder(self, value, expectedScans, barcodeStructure):
        """ GetBarcodeStructureInOrder(self: General, value: str, expectedScans: List[ExpectScanOfEnum]) -> (BarcodeStructureResultEnum, BarcodeStructure) """
        pass

    def GetCacheObject(self, hashCode):
        """ GetCacheObject(self: General, hashCode: int) -> ICachable """
        pass

    def GetCacheObjectAsXml(self, hashCode):
        """ GetCacheObjectAsXml(self: General, hashCode: int) -> str """
        pass

    def GetChacheStatus(self):
        """ GetChacheStatus(self: General) -> str """
        pass

    def GetColliPresetById(self, id, colliPreset):
        """ GetColliPresetById(self: General, id: int) -> (bool, ColliPreset) """
        pass

    def GetColliPresetsAll(self, colliPresets):
        """ GetColliPresetsAll(self: General) -> (int, ColliPresets) """
        pass

    def GetColliPresetSpecificationCodes(self, searchText, colliSpecificationCodes):
        """ GetColliPresetSpecificationCodes(self: General, searchText: str) -> (int, List[str]) """
        pass

    def GetCopyOfCache(self):
        """ GetCopyOfCache(self: General) -> List[ICachable] """
        pass

    def GetCountriesActive(self, countries):
        """ GetCountriesActive(self: General) -> (int, Countries) """
        pass

    def GetCurrentIdentity(self):
        """ GetCurrentIdentity(self: General) -> RemotingIdentity """
        pass

    def GetDefaultColliPreset(self, colliPreset):
        """ GetDefaultColliPreset(self: General) -> (bool, ColliPreset) """
        pass

    def GetDefaultInboundLocations(self, warehouseCode, locations):
        """ GetDefaultInboundLocations(self: General, warehouseCode: str) -> (bool, Locations) """
        pass

    def GetDeviceById(self, id, device):
        """ GetDeviceById(self: General, id: int) -> (bool, Device) """
        pass

    def GetDeviceByMacAddress(self, macAddress, device):
        """ GetDeviceByMacAddress(self: General, macAddress: str) -> (bool, Device) """
        pass

    def GetDeviceByName(self, name, device):
        """ GetDeviceByName(self: General, name: str) -> (bool, Device) """
        pass

    def GetDeviceInformation(self, endPoint, deviceInfo):
        """ GetDeviceInformation(self: General, endPoint: str) -> (bool, DeviceInformation) """
        pass

    def GetDevicesAll(self, devices):
        """ GetDevicesAll(self: General) -> (int, Devices) """
        pass

    def GetErpLocks(self, locks):
        """ GetErpLocks(self: General) -> (int, List[ErpLock]) """
        pass

    def GetErpName(self):
        """ GetErpName(self: General) -> str """
        pass

    def GetErpSettings(self):
        """ GetErpSettings(self: General) -> SystemSettings """
        pass

    def GetErpSettingsTable(self):
        """ GetErpSettingsTable(self: General) -> SystemSettingsTable """
        pass

    def GetExecutionContexts(self):
        """ GetExecutionContexts(self: General) -> List[SafeRpcExecutionContext] """
        pass

    def GetGeneratedScriptComment(self, script):
        """ GetGeneratedScriptComment(self: General, script: ZoneScript) -> str """
        pass

    def GetImplementedMethods(self):
        """ GetImplementedMethods(self: General) -> ImplementedFunctionalities """
        pass

    def GetItem(self, itemCode, item):
        """ GetItem(self: General, itemCode: str) -> (bool, Item) """
        pass

    def GetItemExists(self, itemCode):
        """ GetItemExists(self: General, itemCode: str) -> bool """
        pass

    def GetItemExistsOnDefaultInboundLocation(self, itemCode, warehouseCode, item):
        """ GetItemExistsOnDefaultInboundLocation(self: General, itemCode: str, warehouseCode: str) -> (bool, LocationItem) """
        pass

    def GetItemExistsOnLocation(self, itemCode, warehouseCode, warehouseLocationCode, item):
        """ GetItemExistsOnLocation(self: General, itemCode: str, warehouseCode: str, warehouseLocationCode: str) -> (bool, LocationItem) """
        pass

    def GetItemIdentificationExists(self, itemCode, itemId):
        """ GetItemIdentificationExists(self: General, itemCode: str, itemId: str) -> bool """
        pass

    def GetItemIdentificationExistsMulti(self, itemCode, itemIds):
        """ GetItemIdentificationExistsMulti(self: General, itemCode: str, itemIds: List[str]) -> bool """
        pass

    def GetItemIdentifications(self, args, selected, itemIdentifications):
        """ GetItemIdentifications(self: General, args: GetItemIdentificationArgs, selected: ItemIdentifications) -> (int, ItemIdentifications) """
        pass

    def GetItemIdentificationsAvailable(self, args, itemIds):
        """ GetItemIdentificationsAvailable(self: General, args: GetItemIdentificationArgs) -> (int, ItemIdentifications) """
        pass

    def GetItemIdentificationsAvailableIncludingBatches(self, cacheKeyOfBatch, args, itemIds):
        """ GetItemIdentificationsAvailableIncludingBatches(self: General, cacheKeyOfBatch: CacheKey, args: GetItemIdentificationArgs) -> (int, ItemIdentifications) """
        pass

    def GetItemImageFromErp(self, itemCode):
        """ GetItemImageFromErp(self: General, itemCode: str) -> Array[Byte] """
        pass

    def GetItemImageLarge(self, itemCode):
        """ GetItemImageLarge(self: General, itemCode: str) -> Array[Byte] """
        pass

    def GetItemImageSmall(self, itemCode):
        """ GetItemImageSmall(self: General, itemCode: str) -> Array[Byte] """
        pass

    def GetItemInfoFromBarcode(self, barcode, itemInfo):
        """ GetItemInfoFromBarcode(self: General, barcode: str) -> (bool, ItemInfo) """
        pass

    def GetItemLocationDefault(self, args, location):
        """ GetItemLocationDefault(self: General, args: GetItemLocationsArgs) -> (bool, ItemLocation) """
        pass

    def GetItemLocations(self, args, locations):
        """ GetItemLocations(self: General, args: GetItemLocationsArgs) -> (int, ItemLocations) """
        pass

    def GetItems(self, args, paging, items):
        """ GetItems(self: General, args: GetItemsArgs, paging: PagingParams) -> (int, Items) """
        pass

    def GetItemsAll(self, args, items):
        """ GetItemsAll(self: General, args: GetItemsOnLocationArgs) -> (int, LocationItems) """
        pass

    def GetItemsOnDefaultInboundLocation(self, warehouseCode, filter, items):
        """ GetItemsOnDefaultInboundLocation(self: General, warehouseCode: str, filter: str) -> (int, LocationItems) """
        pass

    def GetItemsOnLocation(self, args, items):
        """ GetItemsOnLocation(self: General, args: GetItemsOnLocationArgs) -> (int, LocationItems) """
        pass

    def GetItemsOnTransportLocation(self, filter, items):
        """ GetItemsOnTransportLocation(self: General, filter: str) -> (int, LocationItems) """
        pass

    def GetItemStockAvailableIncludingBatches(self, cacheKeyOfBatch, args, itemStock):
        """ GetItemStockAvailableIncludingBatches(self: General, cacheKeyOfBatch: CacheKey, args: GetItemStockListArgs) -> (int, List[ItemStock]) """
        pass

    def GetItemStockList(self, args, itemStockLocationList):
        """ GetItemStockList(self: General, args: GetItemStockListArgs) -> (int, ItemStockLocationList) """
        pass

    def GetItemStockTotals(self, args, totals):
        """ GetItemStockTotals(self: General, args: GetItemStockTotalsArgs) -> (bool, ItemStockTotals) """
        pass

    def GetLibContent(self, arg, contents):
        """ GetLibContent(self: General, arg: GetLibArgs) -> (int, LibContents) """
        pass

    @staticmethod
    def GetLibRoot():
        """ GetLibRoot() -> str """
        pass

    def GetLocationClassificationById(self, id, locationClassification):
        """ GetLocationClassificationById(self: General, id: int) -> (bool, LocationClassification) """
        pass

    def GetLocationClassifications(self, filterBy, locationClassifications):
        """ GetLocationClassifications(self: General, filterBy: LocationClassificationsFilter) -> (int, LocationClassifications) """
        pass

    def GetLocationsByCountGroup(self, countGroup, locations):
        """ GetLocationsByCountGroup(self: General, countGroup: CountGroup) -> (int, Locations) """
        pass

    def GetLocationsByLocationClassification(self, locationClassification, locations):
        """ GetLocationsByLocationClassification(self: General, locationClassification: LocationClassification) -> (int, Locations) """
        pass

    def GetLocationsByStorageAssignmentClassification(self, storageAssignmentClassification, locations):
        """ GetLocationsByStorageAssignmentClassification(self: General, storageAssignmentClassification: StorageAssignmentClassification) -> (int, Locations) """
        pass

    def GetLogLines(self, args):
        """ GetLogLines(self: General, args: GetLogLinesArgs) -> PagedList[LogLine] """
        pass

    def GetMacAddress(self):
        """ GetMacAddress(self: General) -> str """
        pass

    def GetModule(self, arg, module):
        """ GetModule(self: General, arg: ModuleArgs) -> (bool, PythonModule) """
        pass

    def GetPendingPrintLineCount(self, key):
        """ GetPendingPrintLineCount(self: General, key: CacheKey) -> int """
        pass

    def GetPrintDatasetInstance(self, datasetFullTypeName, dataset):
        """ GetPrintDatasetInstance(self: General, datasetFullTypeName: str) -> (bool, PrintDatasetBase) """
        pass

    def GetPrintDatasets(self, datasets):
        """ GetPrintDatasets(self: General) -> (int, List[PrintDatasetBase]) """
        pass

    def GetPrintersTable(self):
        """ GetPrintersTable(self: General) -> Hashtable """
        pass

    def GetPrintLabelByName(self, name, label):
        """ GetPrintLabelByName(self: General, name: str) -> (bool, PrintLabel) """
        pass

    def GetPrintLabelImage(self, labelId):
        """ GetPrintLabelImage(self: General, labelId: str) -> Array[Byte] """
        pass

    def GetPrintLabelMappings(self, labelId, mappings):
        """ GetPrintLabelMappings(self: General, labelId: int) -> (bool, Mappings[str, str, str]) """
        pass

    def GetPrintLabels(self, labels):
        """ GetPrintLabels(self: General) -> (int, PrintLabels) """
        pass

    def GetPrintLabelsOfDataset(self, datasetTypeFullName, labels):
        """ GetPrintLabelsOfDataset(self: General, datasetTypeFullName: str) -> (int, PrintLabels) """
        pass

    def GetPrintLabelsOfPrintLines(self, printsLinesTypes, labels):
        """ GetPrintLabelsOfPrintLines(self: General, printsLinesTypes: IEnumerable[Type]) -> (int, PrintLabels) """
        pass

    def GetProfilingLogEntries(self, userKey, previousMethod, endTime, elapsedMiliSeconds, entries):
        """ GetProfilingLogEntries(self: General, userKey: int, previousMethod: int, endTime: Nullable[DateTime], elapsedMiliSeconds: int) -> (int, ProfilingLogEntries) """
        pass

    def GetProfilingUserNodes(self, userNodes):
        """ GetProfilingUserNodes(self: General) -> (int, ProfilingUserNodes) """
        pass

    def GetProgressOfActivity(self, args, activity):
        """ GetProgressOfActivity(self: General, args: GetActivityProgressArgs) -> (bool, Activity) """
        pass

    def GetProgressUpdate(self, args, progress):
        """ GetProgressUpdate(self: General, args: GetActivityProgressArgs) -> (bool, Progress) """
        pass

    def GetResourcesOfTranslation(self, resourceSet, culture, translation):
        """ GetResourcesOfTranslation(self: General, resourceSet: str, culture: str) -> (bool, Translation) """
        pass

    def GetScreenshot(self, accessId):
        """ GetScreenshot(self: General, accessId: str) -> Array[Byte] """
        pass

    def GetScriptIntellisenseOptions(self, hint):
        """ GetScriptIntellisenseOptions(self: General, hint: str) -> Array[str] """
        pass

    def GetScripts(self, arg, scripts):
        """ GetScripts(self: General, arg: GetScriptArgs) -> (int, ZoneScripts) """
        pass

    def GetScriptsAll(self, scripts):
        """ GetScriptsAll(self: General) -> (int, ZoneScripts) """
        pass

    def GetScriptSnippets(self, snippets):
        """ GetScriptSnippets(self: General) -> (int, List[ScriptSnippet]) """
        pass

    def GetScriptTaskById(self, id, task):
        """ GetScriptTaskById(self: General, id: int) -> (bool, ScriptTask) """
        pass

    def GetScriptTaskByName(self, name, task):
        """ GetScriptTaskByName(self: General, name: str) -> (bool, ScriptTask) """
        pass

    def GetScriptTaskProjectedSchedule(self, id, schedule, firstOccurrence):
        """ GetScriptTaskProjectedSchedule(self: General, id: int) -> (bool, Array[DateTime], DateTime) """
        pass

    def GetScriptTasksActive(self, tasks):
        """ GetScriptTasksActive(self: General) -> (int, ScriptTasks) """
        pass

    def GetScriptTasksAll(self, tasks):
        """ GetScriptTasksAll(self: General) -> (int, ScriptTasks) """
        pass

    def GetScriptTasksInActive(self, tasks):
        """ GetScriptTasksInActive(self: General) -> (int, ScriptTasks) """
        pass

    def GetServerDate(self):
        """ GetServerDate(self: General) -> DateTime """
        pass

    def GetSessions(self, sessions):
        """ GetSessions(self: General) -> (int, Sessions) """
        pass

    def GetSettings(self):
        """ GetSettings(self: General) -> SystemSettings """
        pass

    def GetSettingsTable(self):
        """ GetSettingsTable(self: General) -> SystemSettingsTable """
        pass

    def GetShipperServiceLinkByErpDeliveryMethodCode(self, erpDeliveryMethodCode, shipperServiceLink):
        """ GetShipperServiceLinkByErpDeliveryMethodCode(self: General, erpDeliveryMethodCode: str) -> (bool, ShipperServiceLink) """
        pass

    def GetShipperServiceLinksAll(self, shipperServiceLinks):
        """ GetShipperServiceLinksAll(self: General) -> (int, ShipperServiceLinks) """
        pass

    @staticmethod
    def GetSnippetRoot():
        """ GetSnippetRoot() -> str """
        pass

    def GetSortedItemLocations(self, args, filterOptions, locations):
        """ GetSortedItemLocations(self: General, args: GetItemLocationsArgs, filterOptions: FilterOptions) -> (int, ItemLocations) """
        pass

    @staticmethod
    def GetStdLibRoot(path):
        """ GetStdLibRoot() -> (bool, str) """
        pass

    def GetStorageAssignmentClassificationById(self, id, storageAssignmentClassification):
        """ GetStorageAssignmentClassificationById(self: General, id: int) -> (bool, StorageAssignmentClassification) """
        pass

    def GetStorageAssignmentClassifications(self, filterBy, storageAssignmentClassifications):
        """ GetStorageAssignmentClassifications(self: General, filterBy: StorageAssignmentClassificationsFilter) -> (int, StorageAssignmentClassifications) """
        pass

    def GetTagById(self, id, tag):
        """ GetTagById(self: General, id: int) -> (bool, Tag) """
        pass

    def GetTagsAll(self, tags):
        """ GetTagsAll(self: General) -> (int, Tags) """
        pass

    def GetTagsByDescription(self, filter, tags):
        """ GetTagsByDescription(self: General, filter: str) -> (int, Tags) """
        pass

    def GetTagsByType(self, target, tags):
        """ GetTagsByType(self: General, target: TagTarget) -> (int, Tags) """
        pass

    def GetTranslationsAvailable(self, translations):
        """ GetTranslationsAvailable(self: General) -> (int, Translations) """
        pass

    def GetTranslationsAvailablePerSet(self, resourseSet, translations):
        """ GetTranslationsAvailablePerSet(self: General, resourseSet: str) -> (int, Translations) """
        pass

    def GetUserByUserId(self, userId, user):
        """ GetUserByUserId(self: General, userId: int) -> (bool, User) """
        pass

    def GetUserByUserName(self, username, user):
        """ GetUserByUserName(self: General, username: str) -> (bool, User) """
        pass

    def GetUserCacheData(self, tag):
        """ GetUserCacheData(self: General, tag: str) -> str """
        pass

    def GetUsersActive(self, users):
        """ GetUsersActive(self: General) -> (int, Users) """
        pass

    def GetUsersAll(self, users):
        """ GetUsersAll(self: General) -> (int, Users) """
        pass

    def GetUsersInactive(self, users):
        """ GetUsersInactive(self: General) -> (int, Users) """
        pass

    def GetUsersInZone(self, zoneId, users):
        """ GetUsersInZone(self: General, zoneId: int) -> (int, Users) """
        pass

    def GetVersion(self):
        """ GetVersion(self: General) -> str """
        pass

    def GetWarehouseByCode(self, warehouseCode, warehouse):
        """ GetWarehouseByCode(self: General, warehouseCode: str) -> (bool, Warehouse) """
        pass

    def GetWarehouseExists(self, warehouseCode):
        """ GetWarehouseExists(self: General, warehouseCode: str) -> bool """
        pass

    def GetWarehouseLayoutBySetting(self, warehouseLocation, warehouseLayoutSetting, warehouseLayout):
        """ GetWarehouseLayoutBySetting(self: General, warehouseLocation: str, warehouseLayoutSetting: WarehouseLayoutSetting) -> (bool, WarehouseLayout) """
        pass

    def GetWarehouseLayoutsBySetting(self, warehouseLayoutSetting, warehouseLayouts):
        """ GetWarehouseLayoutsBySetting(self: General, warehouseLayoutSetting: WarehouseLayoutSetting) -> (int, WarehouseLayouts) """
        pass

    def GetWarehouseLayoutSettingById(self, id, warehouseLayoutSetting):
        """ GetWarehouseLayoutSettingById(self: General, id: int) -> (bool, WarehouseLayoutSetting) """
        pass

    def GetWarehouseLayoutSettings(self, filterBy, warehouseLayoutSettings):
        """ GetWarehouseLayoutSettings(self: General, filterBy: WarehouseLayoutSettingFilter) -> (int, WarehouseLayoutSettings) """
        pass

    def GetWarehouseLocationExists(self, warehouseCode, warehouseLocationCode):
        """ GetWarehouseLocationExists(self: General, warehouseCode: str, warehouseLocationCode: str) -> bool """
        pass

    def GetWarehouseLocationFromStockThenErp(self, warehouseCode, warehouseLocationCode):
        """ GetWarehouseLocationFromStockThenErp(self: General, warehouseCode: str, warehouseLocationCode: str) -> Location """
        pass

    def GetWarehouseLocationIfExists(self, warehouseCode, warehouseLocationCode, location):
        """ GetWarehouseLocationIfExists(self: General, warehouseCode: str, warehouseLocationCode: str) -> (bool, Location) """
        pass

    def GetWarehouseLocations(self, args, locations):
        """ GetWarehouseLocations(self: General, args: GetWarehouseLocationsArgs) -> (int, Locations) """
        pass

    def GetWarehousesActive(self, warehouses):
        """ GetWarehousesActive(self: General) -> (int, Warehouses) """
        pass

    def GetWarehousesActiveByLocation(self, warehouseLocationCode, warehouses):
        """ GetWarehousesActiveByLocation(self: General, warehouseLocationCode: str) -> (int, Warehouses) """
        pass

    def GetWarehousesActiveWithDefaultInboundLocation(self, warehouses):
        """ GetWarehousesActiveWithDefaultInboundLocation(self: General) -> (int, Warehouses) """
        pass

    def GetWarehousesAll(self, warehouses):
        """ GetWarehousesAll(self: General) -> (int, Warehouses) """
        pass

    def GetWarehousesInactive(self, warehouses):
        """ GetWarehousesInactive(self: General) -> (int, Warehouses) """
        pass

    def GetZoneById(self, id, zone):
        """ GetZoneById(self: General, id: int) -> (bool, Zone) """
        pass

    def GetZoneByName(self, name, zone):
        """ GetZoneByName(self: General, name: str) -> (bool, Zone) """
        pass

    def GetZoneRightsOfZone(self, zoneId, zoneRights):
        """ GetZoneRightsOfZone(self: General, zoneId: int) -> (bool, ZoneRights) """
        pass

    def GetZonesActive(self, active, zones):
        """ GetZonesActive(self: General, active: bool) -> (int, Zones) """
        pass

    def GetZonesActiveOfCurrentUser(self, zones):
        """ GetZonesActiveOfCurrentUser(self: General) -> (int, Zones) """
        pass

    def GetZonesActiveOfUser(self, user, zones):
        """ GetZonesActiveOfUser(self: General, user: User) -> (int, Zones) """
        pass

    def GetZonesAll(self, zones):
        """ GetZonesAll(self: General) -> (int, Zones) """
        pass

    def GetZoneScriptHook(self, arg, script):
        """ GetZoneScriptHook(self: General, arg: GetScriptArgs) -> (bool, ZoneScript) """
        pass

    def GetZoneScripts(self, arg, scripts):
        """ GetZoneScripts(self: General, arg: GetScriptArgs) -> (int, ZoneScripts) """
        pass

    def GetZoneScriptsOrphan(self, arg, scripts):
        """ GetZoneScriptsOrphan(self: General, arg: GetScriptArgs) -> (int, ZoneScripts) """
        pass

    def GetZonesOfUser(self, user, addActiveOnly, zones):
        """ GetZonesOfUser(self: General, user: User, addActiveOnly: bool) -> (int, Zones) """
        pass

    def GetZoneUsers(self, zoneId, zoneUsers):
        """ GetZoneUsers(self: General, zoneId: int) -> (int, ZoneUsers) """
        pass

    def InitializeLifetimeService(self):
        """ InitializeLifetimeService(self: General) -> object """
        pass

    def IsProfilerRunning(self):
        """ IsProfilerRunning(self: General) -> bool """
        pass

    def KillAppDomain(self, *__args):
        """
        KillAppDomain(self: General, arg: DataFlowObject[AppDomainInformation]) -> DataFlowObject[AppDomainInformation]
        KillAppDomain(self: General, filter: str)
        """
        pass

    def LoadCache(self):
        """ LoadCache(self: General) """
        pass

    def LoadSettings(self, *__args):
        """ LoadSettings(self: General, unsafe: bool)LoadSettings(self: General, settingsObject: SystemSettings) """
        pass

    def LogoutClient(self):
        """ LogoutClient(self: General) """
        pass

    def LogoutUser(self):
        """ LogoutUser(self: General) """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting 
             boundary. A value of false is usually appropriate. true to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls 
             to be routed to the remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def MoveModuleOrDirectory(self, isFile, name, fromDir, toDir):
        """ MoveModuleOrDirectory(self: General, isFile: bool, name: str, fromDir: str, toDir: str) -> bool """
        pass

    def OnPythonEngineBooted(self):
        """ OnPythonEngineBooted(self: General) """
        pass

    def OutputCacheStatusToLog(self):
        """ OutputCacheStatusToLog(self: General) """
        pass

    def PrintPrintLine(self, line, label):
        """ PrintPrintLine(self: General, line: PrintLineBase, label: PrintLabel) -> bool """
        pass

    def PrintPrintLineByObjectAndPrinter(self, line, label, printArgs):
        """ PrintPrintLineByObjectAndPrinter(self: General, line: PrintLineBase, label: PrintLabel, printArgs: PrintBaseArgs) -> bool """
        pass

    def PrintPrintLines(self, key, label):
        """ PrintPrintLines(self: General, key: CacheKey, label: PrintLabel) -> bool """
        pass

    def PrintPrintLinesByObject(self, lines, label):
        """ PrintPrintLinesByObject(self: General, lines: PrintLinesBase, label: PrintLabel) -> bool """
        pass

    def PrintPrintLinesByObjectAndPrinter(self, lines, label, printArgs):
        """ PrintPrintLinesByObjectAndPrinter(self: General, lines: PrintLinesBase, label: PrintLabel, printArgs: PrintBaseArgs) -> bool """
        pass

    def PrintTestLabel(self, labelId, testRun):
        """ PrintTestLabel(self: General, labelId: int, testRun: bool) """
        pass

    def PurgeProfilingLog(self):
        """ PurgeProfilingLog(self: General) """
        pass

    def RegisterBackgroundAgentLastSeen(self, agent):
        """ RegisterBackgroundAgentLastSeen(self: General, agent: BackgroundAgent) """
        pass

    def RemoveUserFromZone(self, zone, user):
        """ RemoveUserFromZone(self: General, zone: Zone, user: User) -> bool """
        pass

    def ResetBarcodeSettingsToDefault(self):
        """ ResetBarcodeSettingsToDefault(self: General) -> bool """
        pass

    def ResetPrintLines(self, key, printLines):
        """ ResetPrintLines(self: General, key: CacheKey) -> (bool, PrintLinesBase) """
        pass

    def RestartScriptEngine(self):
        """ RestartScriptEngine(self: General) """
        pass

    def SaveCache(self):
        """ SaveCache(self: General) """
        pass

    def SaveDefaultInboundLocation(self, warehouse):
        """ SaveDefaultInboundLocation(self: General, warehouse: DataFlowObject[Warehouse]) -> DataFlowObject[Warehouse] """
        pass

    def SaveErpSetting(self, memberName, value):
        """ SaveErpSetting(self: General, memberName: str, value: object) """
        pass

    def SaveModule(self, module):
        """ SaveModule(self: General, module: PythonModule) -> bool """
        pass

    def SavePrintLabelMappings(self, labelId, mappings):
        """ SavePrintLabelMappings(self: General, labelId: int, mappings: Mappings[str, str, str]) -> bool """
        pass

    def SaveSetting(self, memberName, value):
        """ SaveSetting(self: General, memberName: str, value: object) """
        pass

    def SaveTranslations(self, translations):
        """ SaveTranslations(self: General, *translations: Array[SaveTranslationArgs]) """
        pass

    def ScheduleScriptTasks(self):
        """ ScheduleScriptTasks(self: General) """
        pass

    def SendBroadcastMessage(self, message):
        """ SendBroadcastMessage(self: General, message: str) """
        pass

    def SendBroadcastQuestion(self, question, possibleAnswers):
        """ SendBroadcastQuestion(self: General, question: str, possibleAnswers: int) -> Answers """
        pass

    def SendKey(self, endPoint, key):
        """ SendKey(self: General, endPoint: str, key: str) """
        pass

    def SendMessage(self, endPoint, message):
        """ SendMessage(self: General, endPoint: str, message: str) """
        pass

    def SendMouseClick(self, endPoint, x, y):
        """ SendMouseClick(self: General, endPoint: str, x: int, y: int) """
        pass

    def SetPrintLinesQuantitiesAtMax(self, key, printLines):
        """ SetPrintLinesQuantitiesAtMax(self: General, key: CacheKey) -> (bool, PrintLinesBase) """
        pass

    def SetSessionTimeout(self):
        """ SetSessionTimeout(self: General) """
        pass

    def SetUserCacheData(self, tag, data):
        """ SetUserCacheData(self: General, tag: str, data: str) """
        pass

    def SetZoneRightsOfZone(self, zoneId, zoneRights):
        """ SetZoneRightsOfZone(self: General, zoneId: int, zoneRights: ZoneRightViews) -> bool """
        pass

    def Sleep(self, seconds):
        """ Sleep(self: General, seconds: int) -> str """
        pass

    def StartDiscoveryServer(self, tcpPortNumber=None, unsafe=None):
        """ StartDiscoveryServer(self: General)StartDiscoveryServer(self: General, tcpPortNumber: int, unsafe: bool) """
        pass

    def StartProfiler(self):
        """ StartProfiler(self: General) """
        pass

    def StopDiscoveryServer(self, unsafe=None):
        """ StopDiscoveryServer(self: General)StopDiscoveryServer(self: General, unsafe: bool) """
        pass

    def StopMarshalledObjectFactories(self):
        """ StopMarshalledObjectFactories(self: General) """
        pass

    def StopProfiler(self):
        """ StopProfiler(self: General) """
        pass

    def TouchGetSortedItemLocations(self, args, filterOptions, locations):
        """ TouchGetSortedItemLocations(self: General, args: GetItemLocationsArgs, filterOptions: FilterOptions) -> (int, ItemLocations) """
        pass

    def UpdateBarcodeSettings(self, dfObject):
        """ UpdateBarcodeSettings(self: General, dfObject: DataFlowObject[BarcodeTypes]) -> DataFlowObject[BarcodeTypes] """
        pass

    def UpdateCultureOfUserSession(self):
        """ UpdateCultureOfUserSession(self: General) """
        pass

    def UpdateDatabase(self, message):
        """ UpdateDatabase(self: General) -> (bool, str) """
        pass

    def UpdatePrintLine(self, key, line):
        """ UpdatePrintLine(self: General, key: CacheKey, line: PrintLineBase) -> bool """
        pass

    def UploadModule(self, arg):
        """ UploadModule(self: General, arg: AddModuleArgs) -> bool """
        pass

    def UploadNewLicense(self, xml, license):
        """ UploadNewLicense(self: General, xml: str) -> (bool, License) """
        pass

    def ValidateColliReferences(self, dfObject):
        """ ValidateColliReferences(self: General, dfObject: DataFlowObject[ValidateColliReferencesArgs]) -> DataFlowObject[ValidateColliReferencesArgs] """
        pass

    def ValidateColliReferenceScan(self, barcode, result):
        """ ValidateColliReferenceScan(self: General, barcode: str) -> (bool, ColliBarcodeResult) """
        pass

    def ValidateItemIdentification(self, itemCode, itemId, isBatchNumber, errorMessage):
        """ ValidateItemIdentification(self: General, itemCode: str, itemId: str, isBatchNumber: bool) -> (bool, str) """
        pass

    def ValidateItemIdentificationForDelivery(self, dfObject):
        """ ValidateItemIdentificationForDelivery(self: General, dfObject: DataFlowObject[ValidateItemIdentificationArgs]) -> DataFlowObject[ValidateItemIdentificationArgs] """
        pass

    def ValidateOrder(self, orderNumber, orderType):
        """ ValidateOrder(self: General, orderNumber: str, orderType: OrderTypeEnum) -> OrderValidationResult """
        pass

    def ValidateTransportPackageScan(self, barcode, result):
        """ ValidateTransportPackageScan(self: General, barcode: str) -> (bool, TransportPackageScanResult) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, stockManager, passwordHasher, documentQueue):
        """ __new__(cls: type, stockManager: IStockManager, passwordHasher: IPasswordHasher, documentQueue: IDocumentQueue) """
        pass

    CachedSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CachedSettings(self: General) -> SystemSettings

"""

    CurrentLicense = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentLicense(self: General) -> License

Set: CurrentLicense(self: General) = value
"""

    DocumentQueue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    StockManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class IApplicationSettings:
    # no doc
    Instance = IApplicationSettings
    """hardcoded/returns an instance of the class"""
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    BosRestBaseUri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BosRestBaseUri(self: IApplicationSettings) -> str

"""

    BosRestLicenseCreationSecret = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BosRestLicenseCreationSecret(self: IApplicationSettings) -> str

"""

    GCloudProjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GCloudProjectId(self: IApplicationSettings) -> str

"""

    GCloudPubSubPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GCloudPubSubPrefix(self: IApplicationSettings) -> str

"""

    MailgunApiKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MailgunApiKey(self: IApplicationSettings) -> str

"""

    MailgunBaseUrl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MailgunBaseUrl(self: IApplicationSettings) -> str

"""

    MailgunDefaultSender = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MailgunDefaultSender(self: IApplicationSettings) -> str

"""

    MailgunDomainBoxwise = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MailgunDomainBoxwise(self: IApplicationSettings) -> str

"""

    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Options(self: IApplicationSettings) -> str

"""

    PdfPrintNetCompany = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PdfPrintNetCompany(self: IApplicationSettings) -> str

"""

    PdfPrintNetLicenseKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PdfPrintNetLicenseKey(self: IApplicationSettings) -> str

"""

    RemotingDictionarySettingName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RemotingDictionarySettingName(self: IApplicationSettings) -> str

"""

    RemotingDictionarySettingPort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RemotingDictionarySettingPort(self: IApplicationSettings) -> str

"""

    RemotingPortNr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RemotingPortNr(self: IApplicationSettings) -> int

"""

    RemotingTcpChannelName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RemotingTcpChannelName(self: IApplicationSettings) -> str

"""

    RpRestBaseUri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RpRestBaseUri(self: IApplicationSettings) -> str

"""

    RpRestLicenseCreationSecret = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RpRestLicenseCreationSecret(self: IApplicationSettings) -> str

"""



class ICentralAuthoritySystem:
    # no doc
    Instance = ICentralAuthoritySystem
    """hardcoded/returns an instance of the class"""
    def RestartGooglePubSubServices(self):
        """ RestartGooglePubSubServices(self: ICentralAuthoritySystem) """
        pass

    def StartBosInboundListener(self):
        """ StartBosInboundListener(self: ICentralAuthoritySystem) -> bool """
        pass

    def StartRemotePublishingInboundListener(self):
        """ StartRemotePublishingInboundListener(self: ICentralAuthoritySystem) -> bool """
        pass

    def WaitStartGooglePubSubServicesUntilValidServerHealth(self):
        """ WaitStartGooglePubSubServicesUntilValidServerHealth(self: ICentralAuthoritySystem) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IExtendedServiceLocator:
    # no doc
    Instance = IExtendedServiceLocator
    """hardcoded/returns an instance of the class"""
    def IsRegistered(self, type=None):
        """
        IsRegistered[T](self: IExtendedServiceLocator) -> bool
        IsRegistered(self: IExtendedServiceLocator, type: Type) -> bool
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class Inbound(MarshalByRefObject):
    """ Inbound(stockManager: IStockManager, messaging: IMessaging, general: IGeneral) """
    Instance = Inbound
    """hardcoded/returns an instance of the class"""
    def AddOrUpdateLicensePlateToReceipt(self, cacheKey, licensePlate):
        """ AddOrUpdateLicensePlateToReceipt(self: Inbound, cacheKey: CacheKey, licensePlate: LicensePlate) -> LicensePlate """
        pass

    def CancelPendingInboundReceiveLines(self, warehouseCode, customerNumber, orderType):
        """ CancelPendingInboundReceiveLines(self: Inbound, warehouseCode: str, customerNumber: str, orderType: InboundOrderTypeEnum) -> bool """
        pass

    def CancelPendingPurchaseOrderReceipts(self, purchaseOrders):
        """ CancelPendingPurchaseOrderReceipts(self: Inbound, purchaseOrders: PurchaseOrders) """
        pass

    def CancelPendingRmaOrderReceipts(self, rmaOrders):
        """ CancelPendingRmaOrderReceipts(self: Inbound, rmaOrders: RmaOrders) """
        pass

    def CreatePreReceipt(self, dfObject):
        """ CreatePreReceipt(self: Inbound, dfObject: DataFlowObject[CreatePreReceiptArgs]) -> DataFlowObject[CreatePreReceiptArgs] """
        pass

    def CreatePreReceiptLines(self, dfObject):
        """ CreatePreReceiptLines(self: Inbound, dfObject: DataFlowObject[CreatePreReceiptArgs]) -> DataFlowObject[CreatePreReceiptArgs] """
        pass

    def DeletePreReceipLines(self, dfObject):
        """ DeletePreReceipLines(self: Inbound, dfObject: DataFlowObject[List[int]]) -> DataFlowObject[List[int]] """
        pass

    def DeletePreReceipt(self, dfObject):
        """ DeletePreReceipt(self: Inbound, dfObject: DataFlowObject[int]) -> DataFlowObject[int] """
        pass

    def DisposeReceiptWhenUnchanged(self, dfObject):
        """ DisposeReceiptWhenUnchanged(self: Inbound, dfObject: DataFlowObject[CacheKey]) -> DataFlowObject[CacheKey] """
        pass

    def GetAdhocRmaCustomersByFilter(self, args, customers):
        """ GetAdhocRmaCustomersByFilter(self: Inbound, args: GetHistoryOutboundOrderCustomersArgs) -> (int, Customers) """
        pass

    def GetHistoryPurchaseOrderPrintLines(self, filter, lines):
        """ GetHistoryPurchaseOrderPrintLines(self: Inbound, filter: GetHistoryPurchaseOrderPrintLinesArgs) -> (int, PurchaseOrderPrintLines) """
        pass

    def GetHistoryPurchaseOrdersByFilter(self, filter, pagingParams, purchaseOrders):
        """ GetHistoryPurchaseOrdersByFilter(self: Inbound, filter: HistoryPurchaseOrdersFilter, pagingParams: PagingParams) -> (int, HistoryPurchaseOrders) """
        pass

    def GetHistoryPurchaseReceiptsByFilter(self, filter, pagingParams, purchaseOrders):
        """ GetHistoryPurchaseReceiptsByFilter(self: Inbound, filter: HistoryPurchaseOrdersFilter, pagingParams: PagingParams) -> (int, HistoryPurchaseOrders) """
        pass

    def GetHistoryRmaOrderLines(self, args, orderLines):
        """ GetHistoryRmaOrderLines(self: Inbound, args: GetHistoryRmaOrderLinesArgs) -> (int, HistoryRmaOrderLines) """
        pass

    def GetHistoryRmaOrdersByFilter(self, filter, pagingParams, rmaOrders):
        """ GetHistoryRmaOrdersByFilter(self: Inbound, filter: HistoryPurchaseOrdersFilter, pagingParams: PagingParams) -> (int, HistoryRmaOrders) """
        pass

    def GetHistoryRmaReceiptById(self, groupGuid):
        """ GetHistoryRmaReceiptById(self: Inbound, groupGuid: Guid) -> HistoryRmaOrder """
        pass

    def GetInboundReceiveLinesByKey(self, cacheKey, receiveLines):
        """ GetInboundReceiveLinesByKey(self: Inbound, cacheKey: CacheKey) -> (bool, InboundReceiveLines) """
        pass

    def GetItemsOfVendor(self, args, items):
        """ GetItemsOfVendor(self: Inbound, args: GetItemsOfVendorArgs) -> (int, Items) """
        pass

    def GetItemVendors(self, args, vendors):
        """ GetItemVendors(self: Inbound, args: GetItemVendorsArgs) -> (int, ItemVendors) """
        pass

    def GetPreReceiptLines(self, args, lines):
        """ GetPreReceiptLines(self: Inbound, args: PreReceiptLinesArgs) -> (int, PagedList[PreReceiptLine]) """
        pass

    def GetPreReceiptReceiveLines(self, dfObject):
        """ GetPreReceiptReceiveLines(self: Inbound, dfObject: DataFlowObject[ReceiveLinesForPreReceiptArgs]) -> DataFlowObject[ReceiveLinesForPreReceiptArgs] """
        pass

    def GetPreReceipts(self, args, preReceipts):
        """ GetPreReceipts(self: Inbound, args: PreReceiptArgs) -> (int, PreReceipts) """
        pass

    def GetPreReceiptSummaries(self, purchaseOrdernumber):
        """ GetPreReceiptSummaries(self: Inbound, purchaseOrdernumber: str) -> List[PreReceiptSummary] """
        pass

    def GetPurchaseOrder(self, args, purchaseOrder):
        """ GetPurchaseOrder(self: Inbound, args: PurchaseOrderArgs) -> (bool, PurchaseOrder) """
        pass

    def GetPurchaseOrderItemIdentifications(self, purchaseOrderId, orderLineId, itemIds):
        """ GetPurchaseOrderItemIdentifications(self: Inbound, purchaseOrderId: int, orderLineId: int) -> (int, ItemIdentifications) """
        pass

    def GetPurchaseOrderLines(self, args, purchaseOrderLines):
        """ GetPurchaseOrderLines(self: Inbound, args: GetPurchaseOrderLinesArgs) -> (int, PurchaseOrderLines) """
        pass

    def GetPurchaseOrderPrintLines(self, key, lines):
        """ GetPurchaseOrderPrintLines(self: Inbound, key: CacheKey) -> (int, PurchaseOrderPrintLines) """
        pass

    def GetPurchaseOrdersAll(self, purchaseOrders):
        """ GetPurchaseOrdersAll(self: Inbound) -> (int, PurchaseOrders) """
        pass

    def GetPurchaseOrdersByFilter(self, args, purchaseOrders):
        """ GetPurchaseOrdersByFilter(self: Inbound, args: PurchaseOrderArgs) -> (int, PurchaseOrders) """
        pass

    def GetPurchaseReceiveLines(self, purchaseOrders, warehouseCode, purchaseReceiveLines):
        """ GetPurchaseReceiveLines(self: Inbound, purchaseOrders: DataFlowObject[PurchaseOrders], warehouseCode: str) -> (DataFlowObject[PurchaseOrders], InboundReceiveLines) """
        pass

    def GetPurchaseReceiveLinesByKey(self, cacheKey, purchaseReceiveLines):
        """ GetPurchaseReceiveLinesByKey(self: Inbound, cacheKey: CacheKey) -> (int, InboundReceiveLines) """
        pass

    def GetRmaCustomersExpected(self, customers):
        """ GetRmaCustomersExpected(self: Inbound) -> (int, Customers) """
        pass

    def GetRmaCustomersExpectedByFilter(self, args, customers):
        """ GetRmaCustomersExpectedByFilter(self: Inbound, args: GetRmaOrderCustomersArgs) -> (int, Customers) """
        pass

    def GetRmaOrder(self, args, rmaOrder):
        """ GetRmaOrder(self: Inbound, args: RmaOrderArgs) -> (bool, RmaOrder) """
        pass

    def GetRmaOrderItemIdentifications(self, rmaOrderId, orderLineId, itemIds):
        """ GetRmaOrderItemIdentifications(self: Inbound, rmaOrderId: int, orderLineId: int) -> (int, ItemIdentifications) """
        pass

    def GetRmaOrderLines(self, args, rmaOrderLines):
        """ GetRmaOrderLines(self: Inbound, args: GetRmaOrderLinesArgs) -> (int, RmaOrderLines) """
        pass

    def GetRmaOrderPrintLines(self, key, lines):
        """ GetRmaOrderPrintLines(self: Inbound, key: CacheKey) -> (int, RmaOrderPrintLines) """
        pass

    def GetRmaOrdersAll(self, rmaOrders):
        """ GetRmaOrdersAll(self: Inbound) -> (int, RmaOrders) """
        pass

    def GetRmaOrdersByFilter(self, filterBy, rmaOrders):
        """ GetRmaOrdersByFilter(self: Inbound, filterBy: RmaOrderArgs) -> (int, RmaOrders) """
        pass

    def GetRmaReasons(self, reasons):
        """ GetRmaReasons(self: Inbound) -> (int, RmaReasons) """
        pass

    def GetRmaReceiveLines(self, rmaOrders, warehouseCode, rmaReceiveLines):
        """ GetRmaReceiveLines(self: Inbound, rmaOrders: DataFlowObject[RmaOrders], warehouseCode: str) -> (DataFlowObject[RmaOrders], InboundReceiveLines) """
        pass

    def GetRmaReceiveLinesByKey(self, cacheKey, rmaReceiveLines):
        """ GetRmaReceiveLinesByKey(self: Inbound, cacheKey: CacheKey) -> (int, InboundReceiveLines) """
        pass

    def GetRmaReceiveLinesUsingOutboundOrders(self, dfObject, rmaReceiveLines):
        """ GetRmaReceiveLinesUsingOutboundOrders(self: Inbound, dfObject: DataFlowObject[PrepareAdhocRmaReceiveLinesArgs]) -> (DataFlowObject[PrepareAdhocRmaReceiveLinesArgs], InboundReceiveLines) """
        pass

    def GetVendors(self, args, vendors):
        """ GetVendors(self: Inbound, args: GetVendorsArgs) -> (int, Vendors) """
        pass

    def GetVendorsExpected(self, vendors):
        """ GetVendorsExpected(self: Inbound) -> (int, PurchaseOrderVendors) """
        pass

    def GetVendorsExpectedByFilter(self, vendors, args):
        """ GetVendorsExpectedByFilter(self: Inbound, args: GetPurchaseOrderVendorArgs) -> (int, PurchaseOrderVendors) """
        pass

    def GetVendorsWithPendingPreReceipts(self, args, vendors):
        """ GetVendorsWithPendingPreReceipts(self: Inbound, args: InboundOrderArgsBase) -> (int, PurchaseOrderVendors) """
        pass

    def InitializeLifetimeService(self):
        """ InitializeLifetimeService(self: Inbound) -> object """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting 
             boundary. A value of false is usually appropriate. true to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls 
             to be routed to the remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def PreCreatePreReceipt(self, dfObject):
        """ PreCreatePreReceipt(self: Inbound, dfObject: DataFlowObject[CreatePreReceiptArgs]) -> DataFlowObject[CreatePreReceiptArgs] """
        pass

    def PrepareInboundReceiveLines(self, args, cacheKey):
        """ PrepareInboundReceiveLines(self: Inbound, args: PrepareInboundReceiveLinesArgs) -> CacheKey """
        pass

    def PrintPurchaseReceipt(self, groupGuid, printer, printingOptions):
        """ PrintPurchaseReceipt(self: Inbound, groupGuid: Guid, printer: str, printingOptions: PrintingOptions) -> bool """
        pass

    def PrintReceiveLabels(self, line, quantity, label):
        """ PrintReceiveLabels(self: Inbound, line: InboundReceiveLine, quantity: Decimal, label: PrintLabel) """
        pass

    def PrintRmaReceipt(self, groupGuid):
        """ PrintRmaReceipt(self: Inbound, groupGuid: Guid) -> bool """
        pass

    def ProcessAdhocRmaOrderLines(self, customerNumber, printRmaInvoice, warehouseCode, orderLines, reference):
        """ ProcessAdhocRmaOrderLines(self: Inbound, customerNumber: str, printRmaInvoice: bool, warehouseCode: str, orderLines: RmaOrderLines, reference: str) -> ErpProcessPurchaseOrderLinesResult """
        pass

    def ProcessPendingReceiveLines(self, dfObject):
        """ ProcessPendingReceiveLines(self: Inbound, dfObject: DataFlowObject[ProcessInboundReceiveLinesArgs]) -> DataFlowObject[ProcessInboundReceiveLinesArgs] """
        pass

    def ProcessPreReceipt(self, preReceiptId, warehouseCode, orderLines, yourReference, transactionId):
        """ ProcessPreReceipt(self: Inbound, preReceiptId: int, warehouseCode: str, orderLines: InboundOrderLines, yourReference: str, transactionId: Guid) -> ErpProcessPurchaseOrderLinesResult """
        pass

    def ReceiveItemIdMulti(self, dfObject):
        """ ReceiveItemIdMulti(self: Inbound, dfObject: DataFlowObject[ReceiveItemIdMultiArgs]) -> DataFlowObject[ReceiveItemIdMultiArgs] """
        pass

    def ReceiveItemIdRange(self, dfObject):
        """ ReceiveItemIdRange(self: Inbound, dfObject: DataFlowObject[ReceiveItemIdRangeArgs]) -> DataFlowObject[ReceiveItemIdRangeArgs] """
        pass

    def RemoveInboundReceiveLine(self, cacheKey, receiveLineId):
        """ RemoveInboundReceiveLine(self: Inbound, cacheKey: CacheKey, receiveLineId: str) -> bool """
        pass

    def RemoveLicensePlateFromReceipt(self, cacheKey, licensePlateId):
        """ RemoveLicensePlateFromReceipt(self: Inbound, cacheKey: CacheKey, licensePlateId: int) """
        pass

    def UpdatePreReceiptStatus(self, dfObject):
        """ UpdatePreReceiptStatus(self: Inbound, dfObject: DataFlowObject[UpdatePreReceiptStatusArgs]) -> DataFlowObject[UpdatePreReceiptStatusArgs] """
        pass

    def UpdateQuantityReceiveLine(self, dfObject, receiveLine):
        """ UpdateQuantityReceiveLine(self: Inbound, dfObject: DataFlowObject[ReceiveArgs]) -> (DataFlowObject[ReceiveArgs], InboundReceiveLine) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, stockManager, messaging, general):
        """ __new__(cls: type, stockManager: IStockManager, messaging: IMessaging, general: IGeneral) """
        pass

    StockManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Inventory(MarshalByRefObject):
    """ Inventory(stockManager: IStockManager, countCacheKeyConstructor: ICacheKeyConstructor[Count]) """
    Instance = Inventory
    """hardcoded/returns an instance of the class"""
    def AddCountItemIdentitification(self, key, itemId, overwriteIfExists):
        """ AddCountItemIdentitification(self: Inventory, key: CacheKey, itemId: ItemIdentification, overwriteIfExists: bool) -> bool """
        pass

    def AddCountItemIdentitificationMulti(self, key, itemIds, overwriteIfExists):
        """ AddCountItemIdentitificationMulti(self: Inventory, key: CacheKey, itemIds: ItemIdentifications, overwriteIfExists: bool) -> bool """
        pass

    def AddCountQuantity(self, key, quantity, overwriteIfExists):
        """ AddCountQuantity(self: Inventory, key: CacheKey, quantity: Decimal, overwriteIfExists: bool) -> bool """
        pass

    def AddWarehouseTransferItemIdentitifications(self, key, args):
        """ AddWarehouseTransferItemIdentitifications(self: Inventory, key: CacheKey, args: AddWarehouseTransferItemIdentitificationArgs) -> bool """
        pass

    def AddWarehouseTransferItems(self, key, itemCodes, overwriteIfExists):
        """ AddWarehouseTransferItems(self: Inventory, key: CacheKey, itemCodes: List[str], overwriteIfExists: bool) -> bool """
        pass

    def AddWarehouseTransferQuantities(self, key, items, overwriteIfExists):
        """ AddWarehouseTransferQuantities(self: Inventory, key: CacheKey, items: WarehouseTransferItems, overwriteIfExists: bool) -> bool """
        pass

    def AddWarehouseTransferQuantity(self, key, args):
        """ AddWarehouseTransferQuantity(self: Inventory, key: CacheKey, args: AddWarehouseTransferQuantityArgs) -> bool """
        pass

    def BatchChangeCountType(self, filterBy, type):
        """ BatchChangeCountType(self: Inventory, filterBy: CountFilter, type: CountTypeEnum) -> int """
        pass

    def CancelProcessCounts(self):
        """ CancelProcessCounts(self: Inventory) """
        pass

    def ChangeDefaultLocationAfterTransfer(self, arg):
        """ ChangeDefaultLocationAfterTransfer(self: Inventory, arg: DataFlowObject[WarehouseTransfer]) -> DataFlowObject[WarehouseTransfer] """
        pass

    def ChangeLicensePlateStatus(self, args):
        """ ChangeLicensePlateStatus(self: Inventory, args: ChangeLicensePlateStatusArgs) """
        pass

    def CheckLicensePlateIntegrity(self, args):
        """ CheckLicensePlateIntegrity(self: Inventory, args: CheckLicensePlateIntegrityArgs) -> CheckLicensePlateIntegrityResult """
        pass

    def CreateCount(self, arg):
        """ CreateCount(self: Inventory, arg: DataFlowObject[Count]) -> DataFlowObject[Count] """
        pass

    def CreateCountFromCache(self, arg):
        """ CreateCountFromCache(self: Inventory, arg: DataFlowObject[CacheKey]) -> DataFlowObject[CacheKey] """
        pass

    def CreateCountGroup(self, arg):
        """ CreateCountGroup(self: Inventory, arg: DataFlowObject[CountGroup]) -> DataFlowObject[CountGroup] """
        pass

    def CreateCountsForPickDifferences(self, batch):
        """ CreateCountsForPickDifferences(self: Inventory, batch: Batch) """
        pass

    def CreateLicensePlate(self, lp):
        """ CreateLicensePlate(self: Inventory, lp: LicensePlate) -> LicensePlate """
        pass

    def CreateLicensePlateAuditLogEntry(self, lpAuditEntry):
        """ CreateLicensePlateAuditLogEntry(self: Inventory, lpAuditEntry: LicensePlateAuditLog) -> LicensePlateAuditLog """
        pass

    def CreateLicensePlateFromReceipt(self, args):
        """ CreateLicensePlateFromReceipt(self: Inventory, args: CreateLicensePlateFromReceiptArgs) -> LicensePlate """
        pass

    def CreateOneCount(self, itemBarcode, warehouseCode, locationCode, countGroupId, itemId):
        """ CreateOneCount(self: Inventory, itemBarcode: str, warehouseCode: str, locationCode: str, countGroupId: int, itemId: str) -> bool """
        pass

    def CreateOrUpdateLicensePlateItem(self, licensePlateId, item):
        """ CreateOrUpdateLicensePlateItem(self: Inventory, licensePlateId: int, item: LicensePlateItem) -> LicensePlateItem """
        pass

    def CreateOrUpdateLicensePlateItems(self, licensePlateId, items):
        """ CreateOrUpdateLicensePlateItems(self: Inventory, licensePlateId: int, items: List[LicensePlateItem]) """
        pass

    def CreateOrUpdateReplenishmentOrderLine(self, line, skipAllocationCheck):
        """ CreateOrUpdateReplenishmentOrderLine(self: Inventory, line: DataFlowObject[ReplenishmentOrderLine], skipAllocationCheck: bool) -> DataFlowObject[ReplenishmentOrderLine] """
        pass

    def CreateReplenishmentOrder(self, order):
        """ CreateReplenishmentOrder(self: Inventory, order: DataFlowObject[ReplenishmentOrder]) -> DataFlowObject[ReplenishmentOrder] """
        pass

    def CreateReplenishmentOrderLine(self, line):
        """ CreateReplenishmentOrderLine(self: Inventory, line: DataFlowObject[ReplenishmentOrderLine]) -> DataFlowObject[ReplenishmentOrderLine] """
        pass

    def CreateReplenishmentOrderLines(self, lines):
        """ CreateReplenishmentOrderLines(self: Inventory, lines: DataFlowObject[ReplenishmentOrderLines]) -> DataFlowObject[ReplenishmentOrderLines] """
        pass

    def CreateReplenishmentOrders(self, dfObject):
        """ CreateReplenishmentOrders(self: Inventory, dfObject: DataFlowObject[ReplenishmentOrders]) -> DataFlowObject[ReplenishmentOrders] """
        pass

    def CreateZeroCount(self, arg):
        """ CreateZeroCount(self: Inventory, arg: DataFlowObject[Count]) -> DataFlowObject[Count] """
        pass

    def CreateZeroCountByCountGroup(self, countGroupId):
        """ CreateZeroCountByCountGroup(self: Inventory, countGroupId: int) """
        pass

    def DeleteCountFromCache(self, arg):
        """ DeleteCountFromCache(self: Inventory, arg: DataFlowObject[CacheKey]) -> DataFlowObject[CacheKey] """
        pass

    def DeleteCountFromCacheAndTable(self, cacheKey):
        """ DeleteCountFromCacheAndTable(self: Inventory, cacheKey: CacheKey) """
        pass

    def DeleteCountFromTable(self, arg):
        """ DeleteCountFromTable(self: Inventory, arg: DataFlowObject[Count]) -> DataFlowObject[Count] """
        pass

    def DeleteCountGroup(self, arg):
        """ DeleteCountGroup(self: Inventory, arg: DataFlowObject[CountGroup]) -> DataFlowObject[CountGroup] """
        pass

    def DeleteLicensePlateById(self, licensePlateId):
        """ DeleteLicensePlateById(self: Inventory, licensePlateId: int) """
        pass

    def DeleteLicensePlateItemById(self, itemId):
        """ DeleteLicensePlateItemById(self: Inventory, itemId: int) """
        pass

    def DeleteReplenishmentOrder(self, order):
        """ DeleteReplenishmentOrder(self: Inventory, order: DataFlowObject[ReplenishmentOrder]) -> DataFlowObject[ReplenishmentOrder] """
        pass

    def DeleteReplenishmentOrderLines(self, dfObject):
        """ DeleteReplenishmentOrderLines(self: Inventory, dfObject: DataFlowObject[ReplenishmentOrderLines]) -> DataFlowObject[ReplenishmentOrderLines] """
        pass

    def DeleteReplenishmentOrders(self, dfObject):
        """ DeleteReplenishmentOrders(self: Inventory, dfObject: DataFlowObject[ReplenishmentOrders]) -> DataFlowObject[ReplenishmentOrders] """
        pass

    def GenerateReplenishmentOrder(self, warehouseToCode):
        """ GenerateReplenishmentOrder(self: Inventory, warehouseToCode: str) -> bool """
        pass

    def GenerateReplenishmentOrders(self, args):
        """ GenerateReplenishmentOrders(self: Inventory, args: GenerateReplenishmentOrdersArgs) -> bool """
        pass

    def GetAllItemIdentifications(self, filterBy):
        """ GetAllItemIdentifications(self: Inventory, filterBy: GetAllItemIdentificationsArgs) -> ItemIdentifications """
        pass

    def GetCount(self, *__args):
        """
        GetCount(self: Inventory, itemCode: str, warehouseCode: str, warehouseLocationCode: str, countGroupId: int, itemId: str) -> (bool, Count)
        GetCount(self: Inventory, key: CacheKey) -> (bool, Count)
        """
        pass

    def GetCountByCountId(self, countId, count):
        """ GetCountByCountId(self: Inventory, countId: int) -> (bool, Count) """
        pass

    def GetCountGroupIdByType(self, type):
        """ GetCountGroupIdByType(self: Inventory, type: CountGroupTypeEnum) -> int """
        pass

    def GetCountGroups(self, filter, countGroups):
        """ GetCountGroups(self: Inventory, filter: str) -> (int, CountGroups) """
        pass

    def GetCountGroupsAll(self, countGroups):
        """ GetCountGroupsAll(self: Inventory) -> (int, CountGroups) """
        pass

    def GetCountGroupsById(self, id):
        """ GetCountGroupsById(self: Inventory, id: int) -> CountGroup """
        pass

    def GetCountGroupsByType(self, type):
        """ GetCountGroupsByType(self: Inventory, type: CountGroupTypeEnum) -> CountGroup """
        pass

    def GetCounts(self, filterBy, pagingParams, counts):
        """ GetCounts(self: Inventory, filterBy: CountFilter, pagingParams: PagingParams) -> (int, Counts) """
        pass

    def GetItemsOnLocationLeftToAddToLp(self, args):
        """ GetItemsOnLocationLeftToAddToLp(self: Inventory, args: GetItemsOnLocationLeftToAddToLpArgs) -> List[LpLocationItem] """
        pass

    def GetItemStockAllocations(self, filterBy, allocations):
        """ GetItemStockAllocations(self: Inventory, filterBy: GetAllocationsArgs) -> (int, ItemStockAllocationList) """
        pass

    def GetLicensePlateAuditLogEntries(self, args, pagingParams, logEntries):
        """ GetLicensePlateAuditLogEntries(self: Inventory, args: GetLicensePlateItemAuditLogEntriesArgs, pagingParams: PagingParams) -> (int, LicensePlateAuditLogs) """
        pass

    def GetLicensePlateByCode(self, args, licensePlate):
        """ GetLicensePlateByCode(self: Inventory, args: GetLicensePlateByCodeArgs) -> (bool, LicensePlate) """
        pass

    def GetLicensePlateById(self, licensePlateId, licensePlate):
        """ GetLicensePlateById(self: Inventory, licensePlateId: int) -> (bool, LicensePlate) """
        pass

    def GetLicensePlateItems(self, args, pagingParams, items):
        """ GetLicensePlateItems(self: Inventory, args: GetLicensePlateItemsArgs, pagingParams: PagingParams) -> (int, LicensePlateItems) """
        pass

    def GetLicensePlates(self, args, pagingParams, licensePlates):
        """ GetLicensePlates(self: Inventory, args: GetLicensePlatesArgs, pagingParams: PagingParams) -> (int, LicensePlates) """
        pass

    def GetProcessCountsProgress(self, percentageComplete, message):
        """ GetProcessCountsProgress(self: Inventory) -> (int, str) """
        pass

    def GetReplenishmentOrder(self, args, replenishmentOrder):
        """ GetReplenishmentOrder(self: Inventory, args: ReplenishmentOrderArgs) -> (bool, ReplenishmentOrder) """
        pass

    def GetReplenishmentOrderLines(self, args, replenishmentOrderLines):
        """ GetReplenishmentOrderLines(self: Inventory, args: ReplenishmentOrderLinesArgs) -> (int, ReplenishmentOrderLines) """
        pass

    def GetReplenishmentOrders(self, filterBy, replenishmentOrders):
        """ GetReplenishmentOrders(self: Inventory, filterBy: ReplenishmentOrderArgs) -> (int, ReplenishmentOrders) """
        pass

    def GetStockManagerList(self, filterBy, pagingParams, stockList):
        """ GetStockManagerList(self: Inventory, filterBy: GetStockManagerListArgs, pagingParams: PagingParams) -> (int, ItemStockWithAllocationsList) """
        pass

    def GetStockOnMatchingFilter(self, args):
        """ GetStockOnMatchingFilter(self: Inventory, args: GetStockManagerListArgs) -> FindableList[ItemStockWithLocations] """
        pass

    def GetWarehousesWithPendingCounts(self, warehouses):
        """ GetWarehousesWithPendingCounts(self: Inventory) -> (int, Warehouses) """
        pass

    def GetWarehouseTransfer(self, key):
        """ GetWarehouseTransfer(self: Inventory, key: CacheKey) -> WarehouseTransfer """
        pass

    def GetWarehouseTransferItems(self, key):
        """ GetWarehouseTransferItems(self: Inventory, key: CacheKey) -> WarehouseTransferItems """
        pass

    def InitializeLifetimeService(self):
        """ InitializeLifetimeService(self: Inventory) -> object """
        pass

    def IsValidItemInCountGroup(self, itemBarcode, countGroup, quantity):
        """ IsValidItemInCountGroup(self: Inventory, itemBarcode: str, countGroup: CountGroup) -> (bool, Decimal) """
        pass

    def IsValidLocationInCountGroup(self, warehouseCode, locationBarcode, countGroup, location):
        """ IsValidLocationInCountGroup(self: Inventory, warehouseCode: str, locationBarcode: str, countGroup: CountGroup) -> (bool, Location) """
        pass

    def ItemBelongsToLicensePlate(self, args):
        """ ItemBelongsToLicensePlate(self: Inventory, args: ItemBelongsToLicensePlateArgs) -> bool """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting 
             boundary. A value of false is usually appropriate. true to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls 
             to be routed to the remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def PreCreateReplenishmentOrderForWarehouse(self, warehouseTo, order):
        """ PreCreateReplenishmentOrderForWarehouse(self: Inventory, warehouseTo: str) -> (bool, ReplenishmentOrder) """
        pass

    def PreCreateReplenishmentOrderLineForItem(self, replenishmentOrderId, itemcode, quantity, line):
        """ PreCreateReplenishmentOrderLineForItem(self: Inventory, replenishmentOrderId: int, itemcode: str, quantity: Decimal) -> (bool, ReplenishmentOrderLine) """
        pass

    def PrepareCount(self, itemCode, warehouseCode, warehouseLocationCode, countGroupId):
        """ PrepareCount(self: Inventory, itemCode: str, warehouseCode: str, warehouseLocationCode: str, countGroupId: int) -> CacheKey """
        pass

    def PrepareCountWithType(self, itemCode, warehouseCode, warehouseLocationCode, countGroupType):
        """ PrepareCountWithType(self: Inventory, itemCode: str, warehouseCode: str, warehouseLocationCode: str, countGroupType: CountGroupTypeEnum) -> CacheKey """
        pass

    def PrepareWarehouseTransfer(self, warehouseCodeFrom, warehouseLocationCodeFrom, warehouseCodeTo, warehouseLocationCodeTo, type):
        """ PrepareWarehouseTransfer(self: Inventory, warehouseCodeFrom: str, warehouseLocationCodeFrom: str, warehouseCodeTo: str, warehouseLocationCodeTo: str, type: WarehouseTransferType) -> CacheKey """
        pass

    def PrepareWarehouseTransferFrom(self, itemCode, warehouseCodeFrom, warehouseLocationCodeFrom):
        """ PrepareWarehouseTransferFrom(self: Inventory, itemCode: str, warehouseCodeFrom: str, warehouseLocationCodeFrom: str) -> CacheKey """
        pass

    def PrepareWarehouseTransferFromInterBranch(self, warehouseCodeFrom, warehouseLocationCodeFrom, transferType):
        """ PrepareWarehouseTransferFromInterBranch(self: Inventory, warehouseCodeFrom: str, warehouseLocationCodeFrom: str, transferType: Nullable[WarehouseTransferType]) -> CacheKey """
        pass

    def PrepareWarehouseTransferItem(self, itemCode, warehouseCodeFrom, warehouseLocationCodeFrom, warehouseCodeTo, warehouseLocationCodeTo):
        """ PrepareWarehouseTransferItem(self: Inventory, itemCode: str, warehouseCodeFrom: str, warehouseLocationCodeFrom: str, warehouseCodeTo: str, warehouseLocationCodeTo: str) -> CacheKey """
        pass

    def PrepareWarehouseTransferReceived(self, itemCode, warehouseCodeFrom, warehouseCodeTo, warehouseLocationCodeTo):
        """ PrepareWarehouseTransferReceived(self: Inventory, itemCode: str, warehouseCodeFrom: str, warehouseCodeTo: str, warehouseLocationCodeTo: str) -> CacheKey """
        pass

    def PrepareWarehouseTransferTo(self, itemCode, warehouseCodeTo, warehouseLocationCodeTo):
        """ PrepareWarehouseTransferTo(self: Inventory, itemCode: str, warehouseCodeTo: str, warehouseLocationCodeTo: str) -> CacheKey """
        pass

    def PrepareWarehouseTransferToMulti(self, itemCodes, warehouseCodeFrom, warehouseLocationCodeFrom, warehouseCodeTo, warehouseLocationTo):
        """ PrepareWarehouseTransferToMulti(self: Inventory, itemCodes: List[str], warehouseCodeFrom: str, warehouseLocationCodeFrom: str, warehouseCodeTo: str, warehouseLocationTo: str) -> CacheKey """
        pass

    def PrepareWarehouseTransferToMultiReceived(self, itemCodes, warehouseCodeFrom, warehouseCodeTo, warehouseLocationTo):
        """ PrepareWarehouseTransferToMultiReceived(self: Inventory, itemCodes: List[str], warehouseCodeFrom: str, warehouseCodeTo: str, warehouseLocationTo: str) -> CacheKey """
        pass

    def PrepareWarehouseTransferToMultiTransport(self, itemCodes, warehouseCodeTo, warehouseLocationTo):
        """ PrepareWarehouseTransferToMultiTransport(self: Inventory, itemCodes: List[str], warehouseCodeTo: str, warehouseLocationTo: str) -> CacheKey """
        pass

    def PrintLicensePlateLabels(self, args):
        """ PrintLicensePlateLabels(self: Inventory, args: PrintLicensePlateLabelArgs) """
        pass

    def ProcessCounts(self, warehouseCode, countGroup, description, date, ledgerCode, started):
        """ ProcessCounts(self: Inventory, warehouseCode: str, countGroup: int, description: str, date: DateTime, ledgerCode: str) -> bool """
        pass

    def ProcessReplenishmentOrder(self, printInvoices, order, orderlines):
        """ ProcessReplenishmentOrder(self: Inventory, printInvoices: bool, order: ReplenishmentOrder, orderlines: List[ReplenishmentOrderLine]) -> ErpProcessSalesOrderLinesResult """
        pass

    def ProcessWarehouseTransfer(self, dfObject):
        """ ProcessWarehouseTransfer(self: Inventory, dfObject: DataFlowObject[ProcessWarehouseTransferArgs]) -> DataFlowObject[ProcessWarehouseTransferArgs] """
        pass

    def RemoveCountItemIdentification(self, key, itemId):
        """ RemoveCountItemIdentification(self: Inventory, key: CacheKey, itemId: str) -> bool """
        pass

    def RemoveWarehouseTransfer(self, key):
        """ RemoveWarehouseTransfer(self: Inventory, key: CacheKey) -> bool """
        pass

    def RemoveWarehouseTransferItemCompletely(self, key, itemCode):
        """ RemoveWarehouseTransferItemCompletely(self: Inventory, key: CacheKey, itemCode: str) -> bool """
        pass

    def RemoveWarehouseTransferItemIdentification(self, key, itemCode, itemId):
        """ RemoveWarehouseTransferItemIdentification(self: Inventory, key: CacheKey, itemCode: str, itemId: str) -> bool """
        pass

    def SubtractWarehouseTransferItemQuantity(self, key, itemCode, quantity):
        """ SubtractWarehouseTransferItemQuantity(self: Inventory, key: CacheKey, itemCode: str, quantity: Decimal) -> bool """
        pass

    def SubtractWarehouseTransferQuantities(self, key, items):
        """ SubtractWarehouseTransferQuantities(self: Inventory, key: CacheKey, items: WarehouseTransferItems) -> bool """
        pass

    def SyncStock(self):
        """ SyncStock(self: Inventory) """
        pass

    def TransferItems(self, arg):
        """ TransferItems(self: Inventory, arg: DataFlowObject[WarehouseTransfer]) -> DataFlowObject[WarehouseTransfer] """
        pass

    def UpdateLicensePlate(self, lp):
        """ UpdateLicensePlate(self: Inventory, lp: LicensePlate) """
        pass

    def UpdateWarehouseTransfer(self, key, warehouseCodeFrom, warehouseLocationCodeFrom, warehouseCodeTo, warehouseLocationTo):
        """ UpdateWarehouseTransfer(self: Inventory, key: CacheKey, warehouseCodeFrom: str, warehouseLocationCodeFrom: str, warehouseCodeTo: str, warehouseLocationTo: str) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, stockManager, countCacheKeyConstructor):
        """ __new__(cls: type, stockManager: IStockManager, countCacheKeyConstructor: ICacheKeyConstructor[Count]) """
        pass

    StockManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Mailer():
    """ Mailer() """
    Instance = Mailer
    """hardcoded/returns an instance of the class"""

class Messaging(MarshalByRefObject):
    """ Messaging() """
    Instance = Messaging
    """hardcoded/returns an instance of the class"""
    def ChangeMessagesStatus(self, messageIds, newStatus):
        """ ChangeMessagesStatus(self: Messaging, messageIds: List[Guid], newStatus: MessageStatus) """
        pass

    def ChangeMessageStatus(self, messageId, newStatus):
        """ ChangeMessageStatus(self: Messaging, messageId: Guid, newStatus: MessageStatus) """
        pass

    def CreateMessage(self, message):
        """ CreateMessage(self: Messaging, message: IMessage) """
        pass

    def DeleteMessageByGuid(self, messageId):
        """ DeleteMessageByGuid(self: Messaging, messageId: Guid) """
        pass

    def DequeueNextMessage(self):
        """ DequeueNextMessage(self: Messaging) -> DequeueResult """
        pass

    def ExecuteMessageHandler(self, args):
        """ ExecuteMessageHandler(self: Messaging, args: ExecuteMessageHandlerArgs) -> ExecuteMessageHandlerResult """
        pass

    def ExecuteMessagePublisher(self, args):
        """ ExecuteMessagePublisher(self: Messaging, args: ExecuteMessagePublisherArgs) -> ExecuteMessagePublisherResult """
        pass

    def GetDistinctTypeList(self, args):
        """ GetDistinctTypeList(self: Messaging, args: GetDistinctTypeListArgs) -> List[str] """
        pass

    def GetMessage(self, messageId):
        """ GetMessage(self: Messaging, messageId: Guid) -> IMessage """
        pass

    def GetMessageBodyAsString(self, messageId, decodeAs):
        """ GetMessageBodyAsString(self: Messaging, messageId: Guid, decodeAs: MessageBodyDecodeAs) -> str """
        pass

    def GetMessageHandlers(self, args, messageHandlers):
        """ GetMessageHandlers(self: Messaging, args: GetMessageHandlersArgs) -> (int, IList[MessageHandlerDescriptorSerializable]) """
        pass

    def GetMessagePublishers(self, args, messagePublishers):
        """ GetMessagePublishers(self: Messaging, args: GetMessagePublishersArgs) -> (int, IList[MessagePublisherDescriptorSerializable]) """
        pass

    def GetMessages(self, args, paging, messages):
        """ GetMessages(self: Messaging, args: GetMessagesArgs, paging: PagingParams) -> (int, Messages) """
        pass

    def InitializeLifetimeService(self):
        """ InitializeLifetimeService(self: Messaging) -> object """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting 
             boundary. A value of false is usually appropriate. true to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls 
             to be routed to the remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def ReissueMessage(self, messageId):
        """ ReissueMessage(self: Messaging, messageId: Guid) """
        pass

    def ReissueMessages(self, messageIds):
        """ ReissueMessages(self: Messaging, messageIds: List[Guid]) """
        pass

    def SaveMessageBody(self, messageId, decodeAs, messageBody):
        """ SaveMessageBody(self: Messaging, messageId: Guid, decodeAs: MessageBodyDecodeAs, messageBody: str) """
        pass

    def StartMessageQueueListener(self, cancellationToken):
        """ StartMessageQueueListener(self: Messaging, cancellationToken: CancellationToken) -> Task """
        pass

    def UpdateMessage(self, message):
        """ UpdateMessage(self: Messaging, message: IMessage) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class NotificationCenter(MarshalByRefObject):
    """ NotificationCenter(general: General) """
    Instance = NotificationCenter
    """hardcoded/returns an instance of the class"""
    def AddNotification(self, notificationToInsert):
        """ AddNotification(self: NotificationCenter, notificationToInsert: InsertNotificationArgs) """
        pass

    def AddNotificationGroup(self, notificationGroup):
        """ AddNotificationGroup(self: NotificationCenter, notificationGroup: AddNotificationGroupArgs) """
        pass

    def AddTaskNotificationSummaryTasks(self):
        """ AddTaskNotificationSummaryTasks(self: NotificationCenter) """
        pass

    def DeleteNotification(self, notificationId):
        """ DeleteNotification(self: NotificationCenter, notificationId: int) """
        pass

    def DeleteNotificationGroup(self, notificationGroup):
        """ DeleteNotificationGroup(self: NotificationCenter, notificationGroup: DeleteNotificationGroupArgs) """
        pass

    def DeleteNotificationsByReference(self, notificationFilter):
        """ DeleteNotificationsByReference(self: NotificationCenter, notificationFilter: DeleteNotificationByReferenceArgs) """
        pass

    def GetAllNotificationGroups(self):
        """ GetAllNotificationGroups(self: NotificationCenter) -> List[NotificationGroup] """
        pass

    def GetNotifications(self, filterOn):
        """ GetNotifications(self: NotificationCenter, filterOn: GetNotificationsArgs) -> List[Notification] """
        pass

    def HasNotifications(self, filterOn):
        """ HasNotifications(self: NotificationCenter, filterOn: HasNotificationsArgs) -> bool """
        pass

    def InitializeLifetimeService(self):
        """ InitializeLifetimeService(self: NotificationCenter) -> object """
        pass

    def MarkAsRead(self, notificationId, userId):
        """ MarkAsRead(self: NotificationCenter, notificationId: int, userId: int) """
        pass

    def MarkGroupAsRead(self, groupKey, userId):
        """ MarkGroupAsRead(self: NotificationCenter, groupKey: str, userId: int) """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting 
             boundary. A value of false is usually appropriate. true to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls 
             to be routed to the remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, general):
        """ __new__(cls: type, general: General) """
        pass


class NotificationSummary(MarshalByRefObject):
    """
    NotificationSummary(implementationContainer: NotificationTypeContainer)
    NotificationSummary()
    """
    Instance = NotificationSummary
    """hardcoded/returns an instance of the class"""
    def DeleteConfiguration(self, notificationSummaryId):
        """ DeleteConfiguration(self: NotificationSummary, notificationSummaryId: int) """
        pass

    def DeleteConfigurations(self, notificationSummaryIds):
        """ DeleteConfigurations(self: NotificationSummary, notificationSummaryIds: List[int]) """
        pass

    def ExecuteSummaries(self):
        """ ExecuteSummaries(self: NotificationSummary) """
        pass

    def GetAllConfigurations(self):
        """ GetAllConfigurations(self: NotificationSummary) -> List[NotificationSummaryConfiguration] """
        pass

    def GetAllExecutionSchedules(self):
        """ GetAllExecutionSchedules(self: NotificationSummary) -> List[str] """
        pass

    def GetAllExecutionTypes(self):
        """ GetAllExecutionTypes(self: NotificationSummary) -> List[str] """
        pass

    def GetConfigurationForm(self, executionType):
        """ GetConfigurationForm(self: NotificationSummary, executionType: str) -> UiForm """
        pass

    def InitializeLifetimeService(self):
        """ InitializeLifetimeService(self: NotificationSummary) -> object """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting 
             boundary. A value of false is usually appropriate. true to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls 
             to be routed to the remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def SaveConfiguration(self, model):
        """ SaveConfiguration(self: NotificationSummary, model: NotificationSummaryConfiguration) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, implementationContainer=None):
        """
        __new__(cls: type, implementationContainer: NotificationTypeContainer)
        __new__(cls: type)
        """
        pass


class NumberGeneration(MarshalByRefObject):
    """ NumberGeneration() """
    Instance = NumberGeneration
    """hardcoded/returns an instance of the class"""
    def AddUsedNumber(self, args):
        """ AddUsedNumber(self: NumberGeneration, args: AddUsedNumberArgs) """
        pass

    def CreateNumberRange(self, dfObject):
        """ CreateNumberRange(self: NumberGeneration, dfObject: DataFlowObject[NumberRange]) -> DataFlowObject[NumberRange] """
        pass

    def DeleteNumberRange(self, dfObject):
        """ DeleteNumberRange(self: NumberGeneration, dfObject: DataFlowObject[NumberRange]) -> DataFlowObject[NumberRange] """
        pass

    def GenerateNumbers(self, dfObject):
        """ GenerateNumbers(self: NumberGeneration, dfObject: DataFlowObject[GenerateBarcodeLabelArgs]) -> DataFlowObject[GenerateBarcodeLabelArgs] """
        pass

    def GetCurrentNumber(self, rangeId):
        """ GetCurrentNumber(self: NumberGeneration, rangeId: int) -> int """
        pass

    def GetNumberRangeById(self, rangeId):
        """ GetNumberRangeById(self: NumberGeneration, rangeId: int) -> NumberRange """
        pass

    def GetNumberRangesByFilter(self, args):
        """ GetNumberRangesByFilter(self: NumberGeneration, args: GetNumberRangeArgs) -> List[NumberRange] """
        pass

    def InitializeLifetimeService(self):
        """ InitializeLifetimeService(self: NumberGeneration) -> object """
        pass

    def IsNumberUsed(self, args):
        """ IsNumberUsed(self: NumberGeneration, args: UsedNumberArgs) -> bool """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting 
             boundary. A value of false is usually appropriate. true to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls 
             to be routed to the remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def ResetNumberRange(self, dfObject):
        """ ResetNumberRange(self: NumberGeneration, dfObject: DataFlowObject[NumberRange]) -> DataFlowObject[NumberRange] """
        pass

    def UpdateNumberRange(self, dfObject):
        """ UpdateNumberRange(self: NumberGeneration, dfObject: DataFlowObject[NumberRange]) -> DataFlowObject[NumberRange] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class OfflineScanning(MarshalByRefObject):
    """ OfflineScanning(appSettings: IApplicationSettings, general: General, messaging: Messaging) """
    Instance = OfflineScanning
    """hardcoded/returns an instance of the class"""
    def AddScanner(self, args):
        """ AddScanner(self: OfflineScanning, args: AddScannerArgs) """
        pass

    def BosInboundListenerPullDirect(self):
        """ BosInboundListenerPullDirect(self: OfflineScanning) -> int """
        pass

    def DeleteScanner(self, args):
        """ DeleteScanner(self: OfflineScanning, args: DeleteScannerArgs) """
        pass

    def DownloadFileAsync(self, filePath):
        """ DownloadFileAsync(self: OfflineScanning, filePath: str) -> Task[Stream] """
        pass

    def EnsureLicenseExists(self):
        """ EnsureLicenseExists(self: OfflineScanning) """
        pass

    def GetAppVersionFileSpec(self, args):
        """ GetAppVersionFileSpec(self: OfflineScanning, args: GetAppVersionFileSpecArgs) -> str """
        pass

    def GetAppVersions(self):
        """ GetAppVersions(self: OfflineScanning) -> AppVersions """
        pass

    def GetCurrentAppVersion(self):
        """ GetCurrentAppVersion(self: OfflineScanning) -> LicenseAppVersion """
        pass

    def GetScanners(self):
        """ GetScanners(self: OfflineScanning) -> Scanners """
        pass

    def InitializeLifetimeService(self):
        """ InitializeLifetimeService(self: OfflineScanning) -> object """
        pass

    def IsBosInboundListenerRunning(self):
        """ IsBosInboundListenerRunning(self: OfflineScanning) -> bool """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting 
             boundary. A value of false is usually appropriate. true to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls 
             to be routed to the remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def SetCurrentAppVersion(self, args):
        """ SetCurrentAppVersion(self: OfflineScanning, args: SetCurrentAppVersionArgs) """
        pass

    def StartBosInboundListener(self):
        """ StartBosInboundListener(self: OfflineScanning) -> bool """
        pass

    def UploadFile(self, name, file, overwrite):
        """ UploadFile(self: OfflineScanning, name: str, file: Stream, overwrite: bool) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, appSettings, general, messaging):
        """ __new__(cls: type, appSettings: IApplicationSettings, general: General, messaging: Messaging) """
        pass

    CurrentLicense = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentLicense(self: OfflineScanning) -> License

"""



class OnGetDestinationLocationForLine(MulticastDelegate):
    """ OnGetDestinationLocationForLine(object: object, method: IntPtr) """
    Instance = OnGetDestinationLocationForLine
    """hardcoded/returns an instance of the class"""
    def BeginInvoke(self, line, defaultWarehouseLocationCodeOutbound, callback, object):
        """ BeginInvoke(self: OnGetDestinationLocationForLine, line: OutboundOrderLine, defaultWarehouseLocationCodeOutbound: str, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: OnGetDestinationLocationForLine, result: IAsyncResult) -> str """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, line, defaultWarehouseLocationCodeOutbound):
        """ Invoke(self: OnGetDestinationLocationForLine, line: OutboundOrderLine, defaultWarehouseLocationCodeOutbound: str) -> str """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original 
             invocation list.
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


class Outbound(MarshalByRefObject):
    """ Outbound(stockManager: IStockManager, messaging: Messaging) """
    Instance = Outbound
    """hardcoded/returns an instance of the class"""
    def AddDirectOrder(self, args):
        """ AddDirectOrder(self: Outbound, args: DirectOrderCrudArgs) -> DataFlowObject[DirectOrder] """
        pass

    def AddDirectOrderLine(self, args):
        """ AddDirectOrderLine(self: Outbound, args: DirectOrderLineCrudArgs) -> DataFlowObject[DirectOrderLine] """
        pass

    def AddDirectOrderLineItemIdentification(self, args):
        """ AddDirectOrderLineItemIdentification(self: Outbound, args: DirectOrderLineItemIdentificationCrudArgs) -> DataFlowObject[DirectOrderLine] """
        pass

    def AddDirectOrderLineItemIdentifications(self, args):
        """ AddDirectOrderLineItemIdentifications(self: Outbound, args: DirectOrderLineItemIdentificationsCrudArgs) -> DataFlowObject[DirectOrderLine] """
        pass

    def AddPackageUsingPreset(self, args, newPackageNumber, packages):
        """ AddPackageUsingPreset(self: Outbound, args: AddTransportPackageArgs) -> (bool, Guid, TransportPackages) """
        pass

    def CheckBatchScan(self, args):
        """ CheckBatchScan(self: Outbound, args: BatchScanArgs) -> BatchScanResult """
        pass

    def CloseBatchesForPacking(self, args):
        """ CloseBatchesForPacking(self: Outbound, args: GetCustomersWithPendingPackagesArgs) """
        pass

    def CloseBatchForPickingById(self, id):
        """ CloseBatchForPickingById(self: Outbound, id: str) -> bool """
        pass

    def CloseTransportPackages(self, packagesKey):
        """ CloseTransportPackages(self: Outbound, packagesKey: CacheKey) """
        pass

    def CreateBatchByCustomerNumbers(self, customers, createdByClientType, createdBatches, message):
        """ CreateBatchByCustomerNumbers(self: Outbound, customers: Customers, createdByClientType: BatchCreatedByClientTypeEnum) -> (int, Batches, str) """
        pass

    def CreateBatches(self, orderNumbers, createdByClientType, batchSettings, createdBatches, message):
        """ CreateBatches(self: Outbound, orderNumbers: List[str], createdByClientType: BatchCreatedByClientTypeEnum, batchSettings: BatchUpdateArgs) -> (int, Batches, str) """
        pass

    def CreateBatchesAndRoutes(self, batchableSoLines, nonBatchableSoLines, allocationSettings, batchSink, createdByClientType, batchSettings, message):
        """ CreateBatchesAndRoutes(self: Outbound, batchableSoLines: OutboundOrderLines, nonBatchableSoLines: OutboundOrderLines, allocationSettings: AllocationSettings, batchSink: BatchAllocationSink, createdByClientType: BatchCreatedByClientTypeEnum, batchSettings: BatchUpdateArgs) -> (Batches, str) """
        pass

    def CreateBatchesByLineIds(self, orderNumbers, orderLineIds, createdByClientType, settings, createdBatches, message):
        """ CreateBatchesByLineIds(self: Outbound, orderNumbers: List[str], orderLineIds: List[int], createdByClientType: BatchCreatedByClientTypeEnum, settings: BatchUpdateArgs) -> (int, Batches, str) """
        pass

    def DeleteBatchById(self, batchId):
        """ DeleteBatchById(self: Outbound, batchId: str) """
        pass

    def DeleteBatches(self, batchesToDelete):
        """ DeleteBatches(self: Outbound, batchesToDelete: Batches) -> bool """
        pass

    def DeleteBatchIfNothingChanged(self, batchCacheKey):
        """ DeleteBatchIfNothingChanged(self: Outbound, batchCacheKey: CacheKey) """
        pass

    def DisposeTransportPackagesWhenUnchanged(self, dfObject):
        """ DisposeTransportPackagesWhenUnchanged(self: Outbound, dfObject: DataFlowObject[CacheKey]) -> DataFlowObject[CacheKey] """
        pass

    def FinalizeProcessBatchPicking(self, batch, manager, warehouseLocationCodeTo):
        """ FinalizeProcessBatchPicking(self: Outbound, batch: Batch, manager: BatchPickManager, warehouseLocationCodeTo: str) -> str """
        pass

    def GetAllocationProfiles(self, profiles):
        """ GetAllocationProfiles(self: Outbound) -> (int, AllocationProfiles) """
        pass

    def GetAllocationSettingsByProfile(self, id):
        """ GetAllocationSettingsByProfile(self: Outbound, id: int) -> AllocationSettings """
        pass

    def GetBatchByCacheKey(self, cacheKey, batch):
        """ GetBatchByCacheKey(self: Outbound, cacheKey: CacheKey) -> (bool, Batch) """
        pass

    def GetBatchById(self, id, cacheKey, batch):
        """ GetBatchById(self: Outbound, id: str) -> (bool, CacheKey, Batch) """
        pass

    def GetBatchByScan(self, barcode, batch):
        """ GetBatchByScan(self: Outbound, barcode: str) -> (bool, BatchBase) """
        pass

    def GetBatchesAll(self, batches):
        """ GetBatchesAll(self: Outbound) -> (int, Batches) """
        pass

    def GetBatchesByFilter(self, args, batches):
        """ GetBatchesByFilter(self: Outbound, args: BatchFilterArgs) -> (int, Batches) """
        pass

    def GetBatchesIncomplete(self, batches):
        """ GetBatchesIncomplete(self: Outbound) -> (int, Batches) """
        pass

    def GetBatchesIncompleteByFilter(self, args, batches):
        """ GetBatchesIncompleteByFilter(self: Outbound, args: GetBatchArgs) -> (int, Batches) """
        pass

    def GetBatchesIncompleteSmall(self, batches):
        """ GetBatchesIncompleteSmall(self: Outbound) -> (int, FindableList[BatchBase]) """
        pass

    def GetBatchesWithPendingPackages(self, args, result):
        """ GetBatchesWithPendingPackages(self: Outbound, args: BatchFilterArgs) -> (int, BatchFilterResult) """
        pass

    def GetBoxColors(self, colors):
        """ GetBoxColors(self: Outbound) -> Array[Color] """
        pass

    def GetCacheKeyOfTransportPackages(self, dfObject, packagesKey):
        """ GetCacheKeyOfTransportPackages(self: Outbound, dfObject: DataFlowObject[GetItemsToPackArgs]) -> (DataFlowObject[GetItemsToPackArgs], CacheKey) """
        pass

    def GetCustomers(self, args, customers):
        """ GetCustomers(self: Outbound, args: GetCustomersArgs) -> (int, Customers) """
        pass

    def GetCustomersPending(self, customers):
        """ GetCustomersPending(self: Outbound) -> (int, Customers) """
        pass

    def GetCustomersPendingByFilter(self, customers, args):
        """ GetCustomersPendingByFilter(self: Outbound, args: GetCustomersPendingArgs) -> (int, Customers) """
        pass

    def GetCustomersWithPendingPackages(self, args, customers):
        """ GetCustomersWithPendingPackages(self: Outbound, args: GetCustomersWithPendingPackagesArgs) -> (int, PackCustomers) """
        pass

    @staticmethod
    def GetDefaultAllocationSettings():
        """ GetDefaultAllocationSettings() -> AllocationSettings """
        pass

    @staticmethod
    def GetDefaultBatchSink():
        """ GetDefaultBatchSink() -> BatchAllocationSink """
        pass

    def GetDirectOrder(self, args):
        """ GetDirectOrder(self: Outbound, args: DirectOrderCrudArgs) -> DataFlowObject[DirectOrder] """
        pass

    def GetDirectOrderHistoryByFilter(self, filter, pagingParams):
        """ GetDirectOrderHistoryByFilter(self: Outbound, filter: HistoryDirectOrdersFilter, pagingParams: PagingParams) -> DataFlowObject[List[HistoryDirectOrder]] """
        pass

    def GetDirectOrderLineDetailsByLinePk(self, linePk):
        """ GetDirectOrderLineDetailsByLinePk(self: Outbound, linePk: int) -> DataFlowObject[List[ItemIdentification]] """
        pass

    def GetDirectOrderLineHistoryByFilter(self, filter, pagingParams):
        """ GetDirectOrderLineHistoryByFilter(self: Outbound, filter: HistoryDirectOrderLinesFilter, pagingParams: PagingParams) -> DataFlowObject[List[HistoryDirectOrderLine]] """
        pass

    def GetDirectOrdersPending(self):
        """ GetDirectOrdersPending(self: Outbound) -> DataFlowObject[List[DirectOrder]] """
        pass

    def GetDocumentsOfShipment(self, shipmentPk, documents):
        """ GetDocumentsOfShipment(self: Outbound, shipmentPk: int) -> (int, List[Attachment]) """
        pass

    def GetHistoryOutboundOrderCustomers(self, args, customers):
        """ GetHistoryOutboundOrderCustomers(self: Outbound, args: GetHistoryOutboundOrderCustomersArgs) -> (int, Customers) """
        pass

    def GetHistoryOutboundOrderItems(self, args, items):
        """ GetHistoryOutboundOrderItems(self: Outbound, args: GetHistoryOutboundOrderItemArgs) -> (int, Items) """
        pass

    def GetHistoryOutboundOrderLines(self, args, orderLines):
        """ GetHistoryOutboundOrderLines(self: Outbound, args: GetHistoryOutboundOrderItemArgs) -> (int, HistoryOutboundOrderLines) """
        pass

    def GetHistoryOutboundOrders(self, args, outboundOrders):
        """ GetHistoryOutboundOrders(self: Outbound, args: GetHistoryOutboundOrdersArgs) -> (int, HistoryOutboundOrders) """
        pass

    def GetHistoryPackageNumbers(self, filter, shipmentId, historyShipmentLines):
        """ GetHistoryPackageNumbers(self: Outbound, filter: OutboundOrdersFilter, shipmentId: int) -> (int, HistoryShipmentLines) """
        pass

    def GetHistoryShipment(self, shipment, packages, shipperId):
        """ GetHistoryShipment(self: Outbound, shipment: HistoryShipment) -> (bool, TransportPackages, str) """
        pass

    def GetHistoryShipmentItemIdentifications(self, outboundOrdersId, shipmentPackageId, itemIdentifications):
        """ GetHistoryShipmentItemIdentifications(self: Outbound, outboundOrdersId: int, shipmentPackageId: int) -> (int, ItemIdentifications) """
        pass

    def GetHistoryShipmentLines(self, filter, paging, shipmentPk, historyShipmentLines):
        """ GetHistoryShipmentLines(self: Outbound, filter: OutboundOrdersFilter, paging: PagingParams, shipmentPk: int) -> (int, HistoryShipmentLines) """
        pass

    def GetHistoryShipmentsAll(self, pagingParams, shipments):
        """ GetHistoryShipmentsAll(self: Outbound, pagingParams: PagingParams) -> (int, HistoryShipments) """
        pass

    def GetHistoryShipmentsByFilter(self, filter, pagingParams, shipments):
        """ GetHistoryShipmentsByFilter(self: Outbound, filter: HistoryShipmentFilter, pagingParams: PagingParams) -> (int, HistoryShipments) """
        pass

    def GetHistoryShipmentsById(self, shipmentId):
        """ GetHistoryShipmentsById(self: Outbound, shipmentId: int) -> HistoryShipment """
        pass

    def GetHistoryTransportPackages(self, shipmentId, packages):
        """ GetHistoryTransportPackages(self: Outbound, shipmentId: int, packages: TransportPackages) -> TransportPackages """
        pass

    def GetItemIdsFromItemToPack(self, cacheKey, itemCode, itemIds):
        """ GetItemIdsFromItemToPack(self: Outbound, cacheKey: CacheKey, itemCode: str) -> (bool, ItemIdentifications) """
        pass

    def GetItemsToPack(self, args, itemsToPack, itemsPacked):
        """ GetItemsToPack(self: Outbound, args: GetItemsToPackArgs) -> (TransportItems, TransportPackages) """
        pass

    def GetItemsToPickOnPickLocation(self, cacheKey, warehouseCode, warehouseLocationCode, items):
        """ GetItemsToPickOnPickLocation(self: Outbound, cacheKey: CacheKey, warehouseCode: str, warehouseLocationCode: str) -> (int, BatchPickLocations) """
        pass

    def GetMobileShipperById(self, shipperId, shipper):
        """ GetMobileShipperById(self: Outbound, shipperId: str) -> (bool, MobileShipper) """
        pass

    def GetOutboundOrderLinesBatchableByCustomers(self, customers, batchableOrderLines, nonBatchableOrderLines):
        """ GetOutboundOrderLinesBatchableByCustomers(self: Outbound, customers: Customers) -> (OutboundOrderLines, OutboundOrderLines) """
        pass

    def GetOutboundOrderLinesBatchableByOrders(self, orderNumbers, batchableOrderlines, nonBatchableOrderlines):
        """ GetOutboundOrderLinesBatchableByOrders(self: Outbound, orderNumbers: List[str]) -> (OutboundOrderLines, OutboundOrderLines) """
        pass

    def GetOutboundOrderLinesFromBatches(self):
        """ GetOutboundOrderLinesFromBatches(self: Outbound) -> IEnumerable[OutboundOrderLine] """
        pass

    def GetOutboundOrders(self, args, orders):
        """ GetOutboundOrders(self: Outbound, args: GetOutboundOrdersArgs) -> IEnumerable[OutboundOrder] """
        pass

    def GetOutboundOrdersBatchable(self, args, batchableOrders, nonBatchableOrders):
        """ GetOutboundOrdersBatchable(self: Outbound, args: GetOutboundOrdersBatchableArgs) -> (OutboundOrders, OutboundOrders) """
        pass

    def GetPackages(self, key, packages):
        """ GetPackages(self: Outbound, key: CacheKey) -> (bool, TransportPackages) """
        pass

    def GetPickLocationOfItem(self, cacheKey, warehouseCode, itemCode, itemLocations):
        """ GetPickLocationOfItem(self: Outbound, cacheKey: CacheKey, warehouseCode: str, itemCode: str) -> (int, ItemLocations) """
        pass

    @staticmethod
    def GetPrintAllocationSettings():
        """ GetPrintAllocationSettings() -> AllocationSettings """
        pass

    def GetSalesOrder(self, args, salesOrder):
        """ GetSalesOrder(self: Outbound, args: SalesOrderArgs) -> (bool, SalesOrder) """
        pass

    def GetSalesOrderCostLines(self, args, salesOrderCostLines):
        """ GetSalesOrderCostLines(self: Outbound, args: SalesOrderLinesArgs) -> (int, SalesOrderLines) """
        pass

    def GetSalesOrderLines(self, args, salesOrderLines):
        """ GetSalesOrderLines(self: Outbound, args: SalesOrderLinesArgs) -> (int, SalesOrderLines) """
        pass

    def GetSalesOrdersAll(self, salesOrders):
        """ GetSalesOrdersAll(self: Outbound) -> (int, SalesOrders) """
        pass

    def GetSalesOrdersByFilter(self, filterBy, salesOrders):
        """ GetSalesOrdersByFilter(self: Outbound, filterBy: SalesOrderArgs) -> (int, SalesOrders) """
        pass

    def GetShipmentServices(self, shipperId, packagesKey, services):
        """ GetShipmentServices(self: Outbound, shipperId: str, packagesKey: CacheKey) -> (int, FindableList[MobileService]) """
        pass

    def GetShipperById(self, shipperId, shipper):
        """ GetShipperById(self: Outbound, shipperId: str) -> (bool, ShipperBase) """
        pass

    def GetShippers(self, shippers):
        """ GetShippers(self: Outbound) -> (int, FindableList[IShipper]) """
        pass

    def GetShipperServiceLevelsByShipperId(self, shipperId, services):
        """ GetShipperServiceLevelsByShipperId(self: Outbound, shipperId: str) -> (int, FindableList[MobileService]) """
        pass

    def GetShipperSettingsTableById(self, shipperId):
        """ GetShipperSettingsTableById(self: Outbound, shipperId: str) -> SystemSettingsTable """
        pass

    def HandleColliForStockRegistration(self, transportPackages):
        """ HandleColliForStockRegistration(self: Outbound, transportPackages: TransportPackages) -> ColliRegistrationResult """
        pass

    def InitializeLifetimeService(self):
        """ InitializeLifetimeService(self: Outbound) -> object """
        pass

    def InitOrderMatchesCustomerValidator(self):
        """ InitOrderMatchesCustomerValidator(self: Outbound) -> OrderMatchesCustomerValidator """
        pass

    def LogAndCleanupShipment(self, shipment, packages, arg):
        """ LogAndCleanupShipment(self: Outbound, shipment: ShipmentBase, packages: TransportPackages, arg: DataFlowObject[ProcessShipmentArgs]) -> DataFlowObject[ProcessShipmentArgs] """
        pass

    def MarkPickLocationAsPicked(self, cacheKey, idOfBatchPickLocation):
        """ MarkPickLocationAsPicked(self: Outbound, cacheKey: CacheKey, idOfBatchPickLocation: str) -> BatchPickLocation """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting 
             boundary. A value of false is usually appropriate. true to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls 
             to be routed to the remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def MoveTransportItemsBetweenTransportPackages(self, dfObject):
        """ MoveTransportItemsBetweenTransportPackages(self: Outbound, dfObject: DataFlowObject[MoveTransportItemsBetweenTransportPackagesArgs]) -> DataFlowObject[MoveTransportItemsBetweenTransportPackagesArgs] """
        pass

    def OpenBatchesForPacking(self, args, customers):
        """ OpenBatchesForPacking(self: Outbound, args: GetCustomersWithPendingPackagesArgs) -> (int, PackCustomers) """
        pass

    def OpenBatchForPickingById(self, id, cacheKey, batch):
        """ OpenBatchForPickingById(self: Outbound, id: str) -> (bool, CacheKey, Batch) """
        pass

    def OpenTransferPackagesForShipping(self, key, packages):
        """ OpenTransferPackagesForShipping(self: Outbound, key: CacheKey) -> (bool, TransportPackages) """
        pass

    def PickInBatch(self, dfObject):
        """ PickInBatch(self: Outbound, dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
        pass

    def PickItemIdInBatch(self, dfObject):
        """ PickItemIdInBatch(self: Outbound, dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
        pass

    def PickItemIdRangeInBatch(self, dfObject):
        """ PickItemIdRangeInBatch(self: Outbound, dfObject: DataFlowObject[PickItemIdRangeArgs]) -> DataFlowObject[PickItemIdRangeArgs] """
        pass

    def PickManualSelectedMultipleItemIdsInBatch(self, dfObject):
        """ PickManualSelectedMultipleItemIdsInBatch(self: Outbound, dfObject: DataFlowObject[PickItemIdsArgs]) -> DataFlowObject[PickItemIdsArgs] """
        pass

    def PickMultipleScannedItemIdsInBatch(self, dfObject):
        """ PickMultipleScannedItemIdsInBatch(self: Outbound, dfObject: DataFlowObject[PickItemIdsArgs]) -> DataFlowObject[PickItemIdsArgs] """
        pass

    def PrintDocumentsOfShipment(self, args):
        """ PrintDocumentsOfShipment(self: Outbound, args: PrintShipmentDocumentArgs) -> bool """
        pass

    def PrintDuplicateLabels(self, args):
        """ PrintDuplicateLabels(self: Outbound, args: PrintDuplicateLabelArgs) -> bool """
        pass

    def PrintPackageSlip(self, args):
        """ PrintPackageSlip(self: Outbound, args: PrintPackageSlipArgs) -> bool """
        pass

    def PrintTransportPackageLabel(self, cacheKey, boxGuid, label):
        """ PrintTransportPackageLabel(self: Outbound, cacheKey: CacheKey, boxGuid: Guid, label: PrintLabel) -> bool """
        pass

    def ProcessBatchPacking(self, dfObject):
        """ ProcessBatchPacking(self: Outbound, dfObject: DataFlowObject[ProcessBatchPackingArgs]) -> DataFlowObject[ProcessBatchPackingArgs] """
        pass

    def ProcessBatchPicking(self, dfObject):
        """ ProcessBatchPicking(self: Outbound, dfObject: DataFlowObject[ProcessBatchPickingArgs]) -> DataFlowObject[ProcessBatchPickingArgs] """
        pass

    def ProcessBatchPickingToErp(self, dfObject, batch, manager, getDestinationLocationForLineDelegate):
        """ ProcessBatchPickingToErp(self: Outbound, dfObject: DataFlowObject[ProcessBatchPickingArgs], batch: Batch, manager: BatchPickManager, getDestinationLocationForLineDelegate: OnGetDestinationLocationForLine) -> bool """
        pass

    def ProcessDirectOrder(self, args):
        """ ProcessDirectOrder(self: Outbound, args: DirectOrderCrudArgs) -> DataFlowObject[DirectOrder] """
        pass

    def ProcessSalesOrder(self, args, order):
        """ ProcessSalesOrder(self: Outbound, args: ProcessSalesOrderLinesArgs, order: KeyValuePair[OutboundOrder, OutboundOrderLines]) -> ErpProcessSalesOrderLinesResult """
        pass

    def ProcessSalesOrderQueued(self, args, order):
        """ ProcessSalesOrderQueued(self: Outbound, args: ProcessSalesOrderLinesArgs, order: KeyValuePair[OutboundOrder, OutboundOrderLines]) -> ErpProcessSalesOrderLinesResult """
        pass

    def ProcessShipment(self, arg):
        """ ProcessShipment(self: Outbound, arg: DataFlowObject[ProcessShipmentArgs]) -> DataFlowObject[ProcessShipmentArgs] """
        pass

    def ProcessShipmentInfo(self, shipment, packages, arg):
        """ ProcessShipmentInfo(self: Outbound, shipment: ShipmentBase, packages: TransportPackages, arg: DataFlowObject[ProcessShipmentArgs]) -> DataFlowObject[ProcessShipmentArgs] """
        pass

    def ProcessShipmentWithDefaultServiceLevel(self, cacheKey):
        """ ProcessShipmentWithDefaultServiceLevel(self: Outbound, cacheKey: CacheKey) """
        pass

    def PutBackFromBatch(self, dfObject):
        """ PutBackFromBatch(self: Outbound, dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
        pass

    def PutItemIdBackFromBatch(self, dfObject):
        """ PutItemIdBackFromBatch(self: Outbound, dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
        pass

    @staticmethod
    def RemoveBatch(batch):
        """ RemoveBatch(batch: Batch) """
        pass

    def RemoveDirectOrder(self, args):
        """ RemoveDirectOrder(self: Outbound, args: DirectOrderCrudArgs) """
        pass

    def RemoveDirectOrderLine(self, args):
        """ RemoveDirectOrderLine(self: Outbound, args: DirectOrderLineCrudArgs) -> DataFlowObject[bool] """
        pass

    def RemoveDirectOrderLineItemIdentification(self, args):
        """ RemoveDirectOrderLineItemIdentification(self: Outbound, args: DirectOrderLineItemIdentificationCrudArgs) -> DataFlowObject[DirectOrderLine] """
        pass

    def RemovePackage(self, boxGuid, args, itemsToPack, itemsPacked):
        """ RemovePackage(self: Outbound, boxGuid: Guid, args: GetItemsToPackArgs) -> (bool, TransportItems, TransportPackages) """
        pass

    def RemoveTransportPackages(self, packagesKey):
        """ RemoveTransportPackages(self: Outbound, packagesKey: CacheKey) """
        pass

    def SaveBatch(self, batch):
        """ SaveBatch(self: Outbound, batch: Batch) -> Batch """
        pass

    def SaveShipperSetting(self, shipperId, memberName, value):
        """ SaveShipperSetting(self: Outbound, shipperId: str, memberName: str, value: object) """
        pass

    def ScanItemForPacking(self, args, result):
        """ ScanItemForPacking(self: Outbound, args: ItemPackScanArgs) -> (bool, ScanItemPackArgsResult) """
        pass

    def SkipOrderForProcessingPack(self, batchId, orderNumber):
        """ SkipOrderForProcessingPack(self: Outbound, batchId: str, orderNumber: str) -> bool """
        pass

    def UpdateBatchWithSettings(self, batchId, args):
        """ UpdateBatchWithSettings(self: Outbound, batchId: Guid, args: BatchUpdateArgs) """
        pass

    def UpdateColloReference(self, dfObject):
        """ UpdateColloReference(self: Outbound, dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
        pass

    def UpdateDirectOrderLine(self, args):
        """ UpdateDirectOrderLine(self: Outbound, args: DirectOrderLineCrudArgs) -> DataFlowObject[DirectOrderLine] """
        pass

    def UpdateDirectOrderLineItemIdentification(self, args):
        """ UpdateDirectOrderLineItemIdentification(self: Outbound, args: DirectOrderLineItemIdentificationCrudArgs) -> DataFlowObject[DirectOrderLine] """
        pass

    def UpdatePackageData(self, args, newPackageData, packages):
        """ UpdatePackageData(self: Outbound, args: UpdateTransportPackageArgs, newPackageData: TransportPackage) -> (bool, TransportPackages) """
        pass

    def UpdateReference(self, reference, cacheKey):
        """ UpdateReference(self: Outbound, reference: ColloReference, cacheKey: CacheKey) -> bool """
        pass

    def UpdateTransportPackagesHeader(self, packagesKey, args, packages):
        """ UpdateTransportPackagesHeader(self: Outbound, packagesKey: CacheKey, args: UpdateTransportPackagesHeaderArgs) -> (bool, TransportPackages) """
        pass

    def ValidateBatchedItem(self, cacheKey, selectedBatchPickLocation, itemCode):
        """ ValidateBatchedItem(self: Outbound, cacheKey: CacheKey, selectedBatchPickLocation: BatchPickLocation, itemCode: str) -> DataFlowObject[CacheKey] """
        pass

    def ValidateBatchLocation(self, cacheKey, selectedBatchPickLocation, locationCode):
        """ ValidateBatchLocation(self: Outbound, cacheKey: CacheKey, selectedBatchPickLocation: BatchPickLocation, locationCode: str) -> DataFlowObject[CacheKey] """
        pass

    def VoidShipment(self, shipment):
        """ VoidShipment(self: Outbound, shipment: DataFlowObject[HistoryShipment]) -> DataFlowObject[HistoryShipment] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, stockManager, messaging):
        """ __new__(cls: type, stockManager: IStockManager, messaging: Messaging) """
        pass

    Messaging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    StockManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StockManager(self: Outbound) -> IStockManager

"""



class Printing(MarshalByRefObject):
    """ Printing(general: General) """
    Instance = Printing
    """hardcoded/returns an instance of the class"""
    def GetPickListsAll(self, pickLists):
        """ GetPickListsAll(self: Printing) -> (int, ReportItems) """
        pass

    def GetPickListsForSettings(self, pickListNames):
        """ GetPickListsForSettings(self: Printing) -> (int, List[str]) """
        pass

    def GetPickListsTable(self):
        """ GetPickListsTable(self: Printing) -> Hashtable """
        pass

    def InitializeLifetimeService(self):
        """ InitializeLifetimeService(self: Printing) -> object """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting 
             boundary. A value of false is usually appropriate. true to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls 
             to be routed to the remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def PrintPickBatchLabel(self, dfObject):
        """ PrintPickBatchLabel(self: Printing, dfObject: DataFlowObject[PrintPickbatchLabelArgs]) -> DataFlowObject[PrintPickbatchLabelArgs] """
        pass

    def PrintPickList(self, args):
        """ PrintPickList(self: Printing, args: PrintPickingListArgs) -> bool """
        pass

    def PrintSSCCLabels(self, dfObject):
        """ PrintSSCCLabels(self: Printing, dfObject: DataFlowObject[PrintSSCCLabelsArgs]) -> DataFlowObject[PrintSSCCLabelsArgs] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, general):
        """ __new__(cls: type, general: General) """
        pass


class PyLogger():
    # no doc
    Instance = PyLogger
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def Debug(msg):
        """ Debug(msg: str) """
        pass

    @staticmethod
    def Error(*__args):
        """ Error(msg: str)Error(ex: Exception)Error(ex: BaseException) """
        pass

    @staticmethod
    def Fatal(*__args):
        """ Fatal(msg: str)Fatal(ex: Exception)Fatal(ex: BaseException) """
        pass

    @staticmethod
    def Info(msg):
        """ Info(msg: str) """
        pass

    @staticmethod
    def Trace(msg):
        """ Trace(msg: str) """
        pass

    @staticmethod
    def Warn(*__args):
        """ Warn(msg: str)Warn(ex: Exception)Warn(ex: BaseException) """
        pass

    __all__ = [
        'Debug',
        'Error',
        'Fatal',
        'Info',
        'Trace',
        'Warn',
    ]


class RemotePublishing(MarshalByRefObject):
    """ RemotePublishing(appSettings: IApplicationSettings, general: General) """
    Instance = RemotePublishing
    """hardcoded/returns an instance of the class"""
    def AddRemotePublisher(self, req):
        """ AddRemotePublisher(self: RemotePublishing, req: AddRemotePublisherArgs) -> Publisher """
        pass

    def DeleteRemotePublisher(self, req):
        """ DeleteRemotePublisher(self: RemotePublishing, req: DeleteRemotePublisherArgs) """
        pass

    def DownloadFileAsync(self, filePath):
        """ DownloadFileAsync(self: RemotePublishing, filePath: str) -> Task[Stream] """
        pass

    def EditRemotePublisher(self, req):
        """ EditRemotePublisher(self: RemotePublishing, req: EditRemotePublisherArgs) -> Publisher """
        pass

    def EnsureLicenseExists(self):
        """ EnsureLicenseExists(self: RemotePublishing) """
        pass

    def GetRemotePublishers(self):
        """ GetRemotePublishers(self: RemotePublishing) -> Publishers """
        pass

    def InitializeLifetimeService(self):
        """ InitializeLifetimeService(self: RemotePublishing) -> object """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting 
             boundary. A value of false is usually appropriate. true to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls 
             to be routed to the remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, appSettings, general):
        """ __new__(cls: type, appSettings: IApplicationSettings, general: General) """
        pass

    CurrentLicense = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentLicense(self: RemotePublishing) -> License

"""



# variables with complex values

