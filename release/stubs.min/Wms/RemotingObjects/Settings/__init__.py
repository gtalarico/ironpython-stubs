# encoding: utf-8
# module Wms.RemotingObjects.Settings calls itself Settings
# from Wms.RemotingObjects,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from System.Collections.Generic import *
from ..__init__ import *

# no functions
# classes

class SystemSettings(object):
 """
 Contains the system settings used by BOXwise.
    
    Add the [Serializable] attribute when you inherit this class. BOXwise needs it in order to function properly.
 
 SystemSettings()
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return SystemSettings()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def AddValidValueDelegate(id,delegate):
  """
  AddValidValueDelegate(id: str,delegate: GetValidValues)
   Adds a delegate to the internal collection of delegates for retrieving validvalues.
  """
  pass
 def GetCreateCountForPickDifferencesOption(self):
  """ GetCreateCountForPickDifferencesOption(self: SystemSettings) -> PickDifferenceOptionsEnum """
  pass
 def GetDaysToFutureUsingTypeOfDays(self):
  """ GetDaysToFutureUsingTypeOfDays(self: SystemSettings) -> int """
  pass
 def GetDefaultModeBatchPackProcessing(self):
  """ GetDefaultModeBatchPackProcessing(self: SystemSettings) -> BatchPackProcessingModeEnum """
  pass
 def GetEnumAsHashtable(self,*args):
  """ GetEnumAsHashtable(enum: Type) -> Hashtable """
  pass
 def GetLifeTimes(self):
  """ GetLifeTimes(self: SystemSettings) -> Dictionary[CacheLifeTimes,int] """
  pass
 def GetSplitOutboundOrdersIntoColliOption(self):
  """ GetSplitOutboundOrdersIntoColliOption(self: SystemSettings) -> SplitProcessedOutboundOrdersEnum """
  pass
 def GetTable(self,topLevelOnly):
  """ GetTable(self: SystemSettings,topLevelOnly: bool) -> SystemSettingsTable """
  pass
 def GetTimeSpanFilter(self):
  """ GetTimeSpanFilter(self: SystemSettings) -> TimeFilterEnum """
  pass
 def GetTimeSpanFilters(self):
  """ GetTimeSpanFilters(self: SystemSettings) -> Hashtable """
  pass
 ShipppingDeliveryTimeInterval=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ShipppingDeliveryTimeInterval(self: SystemSettings) -> int

Set: ShipppingDeliveryTimeInterval(self: SystemSettings)=value
"""


 AddReferenceToPurchaseOrders=None
 AdminZoneId=2
 AskPrintInvoice=None
 AskPrintLicensePlateLabels=None
 AskPrintPurchaseOrderLabels=None
 AskPrintRmaInvoice=None
 AskPrintRMALabels=None
 AskPrintSuccessfull=None
 AutoCleanupCacheInterval=None
 AutoSaveCacheInterval=None
 BosDescription='HTTP REST Authentication'
 BosGroupKey='15BOS'
 BosRestApiKey=None
 CacheObjectLiveIntermediate=None
 CacheObjectLiveLong=None
 CacheObjectLiveShort=None
 ChangeDefaultLocation=None
 CheckStockQuantityBeforeOrderProcessing=None
 CheckTransferQuantityWithStockManager=None
 CleanUpLogInterval=None
 CompanyAddress=None
 CompanyCity=None
 CompanyCountryCode=None
 CompanyCountryName=None
 CompanyMailAdress=None
 CompanyName=None
 CompanyPhone=None
 CompanyPrefix=None
 CompanyZipCode=None
 CreateCountForPackDifferences=None
 CreateCountForPickDifferences=None
 DaysToFuture=None
 DecreaseStockWithPickDifferencesCounts=None
 DefaultLanguage=None
 DefaultModeBatchPackProcessing=None
 DefaultPickList=None
 DefaultPickListQuantity=None
 DefaultPrintJobRetryTime=None
 DefaultRmaAdHocReceipts=None
 DefaultVendorAdHocReceipts=None
 DefaultWarehouseCode=None
 DefaultWarehouseCodeAdHocReceipts=None
 DefaultWarehouseLocationCodeOutbound=None
 DefaultWarehouseOutbound=None
 DirectOrderGroupDescription='Direct orders'
 DirectOrderGroupKey='089DIRECTORDERS'
 DirectOrderShowReferenceAfterProcessing=None
 DocumentQueueCleanupInterval=None
 DocumentQueueRetentionTimeInDays=None
 Empty=None
 ErpAutoLockingInterval=None
 ExpiryDate=None
 ExtensionDigit=None
 ExtensionDigitReset=None
 GenerateP2PImage=None
 ImageFolderLarge=None
 ImageFolderSmall=None
 InboundLocationMode=None
 InboundSkipBatchOverview=None
 InnerBarcodeRegex=None
 KillUnresponsiveHostThreshold=None
 LifeTimeOfIsolatedErpHostsInMinutes=None
 LogRetentionTime=None
 ManagementPortalSessionTimeout=None
 MaxAllowedNrOfDecimals=None
 MaxLengthNumbers=None
 MessageQueueCleanupInterval=None
 MessageQueueRetentionTimeInDays=None
 NotificationCleanupInterval=None
 NotificationRetentionTimeInDays=None
 NotificationTargetZone=None
 NumberRangeForPickBatchBarcode=None
 NumberRangeForSscc=None
 PathToCustomReports=None
 PreferredColumnsP2PImage=None
 PrintFieldsRegEx=None
 PrintPackingSlip=None
 PrintPurchaseOrderReceipt=None
 PrintRmaOrderReceipt=None
 RpRestApiKey=None
 ScriptingEnableDebugging=None
 SequentialProcessPacking=None
 ShipmentDeliveryDay=None
 ShipmentPickupDay=None
 SkipVendorSelectionAdHocReceipts=None
 SkipWarehouseSelectionAdHocReceipts=None
 SplitProcessedOutboundOrders=None
 StockReplenishmentInterval=None
 TimeSpanFilter=None
 TransportWarehouseCode=None
 TurnOffErpCommunication=None
 TypeOfDay=None
 UseDelayLoad=None
 ValidValueGetActiveZones='GetActiveZones'
 ValidValueGetBatchPackProcessingModes='ValidValueGetBatchPackProcessingModes'
 ValidValueGetChangeDefaultLocation='ValidValueGetChangeDefaultLocation'
 ValidValueGetDifferFromRouteOptions='GetDifferFromRouteOptions'
 ValidValueGetInboundLocationModes='ValidValueGetInboundLocationModes'
 ValidValueGetPickBatchBarcodeRanges='ValidValueGetPickBatchBarcodeRanges'
 ValidValueGetPickDifferenceOptions='GetPickDifferenceOptions'
 ValidValueGetPickLists='ValidValueGetPickLists'
 ValidValueGetPrinters='GetPrinters'
 ValidValueGetShipmentDayOptions='GetShipmentDayOptions'
 ValidValueGetSplitOutboundOrdersIntoColliOptions='GetSplitSalesOrdersIntoColliOptions'
 ValidValueGetSSCCNumberRanges='ValidValueGetSSCCNumberRanges'
 ValidValueGetStockRegistrationForColli='ValidValueGetStockRegistrationForColli'
 ValidValueGetTimeSpanFilters='GetTimeSpanFilters'
 ValidValueGetTranslations='ValidValueGetTranslations'
 ValidValueGetTypeDays='ValidValueGetTypeDays'


class SystemSettingsTable(List):
 """ SystemSettingsTable() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return SystemSettingsTable()
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

class SystemSettingsTableRow(object):
 """ SystemSettingsTableRow() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return SystemSettingsTableRow()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 GroupName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Name of the group the settings are part of.
   Used for categorization.

Get: GroupName(self: SystemSettingsTableRow) -> str

Set: GroupName(self: SystemSettingsTableRow)=value
"""

 GroupSortKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Sort order of the group settings are grouped in.

Get: GroupSortKey(self: SystemSettingsTableRow) -> str

Set: GroupSortKey(self: SystemSettingsTableRow)=value
"""

 InValidRegexMessage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Error message to be shown when regex is invalid

Get: InValidRegexMessage(self: SystemSettingsTableRow) -> str

Set: InValidRegexMessage(self: SystemSettingsTableRow)=value
"""

 IsMachineSetting=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Wether setting should be saved for a specific machine.

Get: IsMachineSetting(self: SystemSettingsTableRow) -> bool

Set: IsMachineSetting(self: SystemSettingsTableRow)=value
"""

 IsUserSetting=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Wether setting should only be saved for a specific user.

Get: IsUserSetting(self: SystemSettingsTableRow) -> bool

Set: IsUserSetting(self: SystemSettingsTableRow)=value
"""

 Label=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Name of the setting to show in the UI.

Get: Label(self: SystemSettingsTableRow) -> str

Set: Label(self: SystemSettingsTableRow)=value
"""

 MaxLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Maximum amount of characters allowed in the value.

Get: MaxLength(self: SystemSettingsTableRow) -> int

Set: MaxLength(self: SystemSettingsTableRow)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Name of Key the setting is saved under.

Get: Name(self: SystemSettingsTableRow) -> str

Set: Name(self: SystemSettingsTableRow)=value
"""

 Renderer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Type of editor to render in UI for edditing setting.
   from: Wms.RemotingObjects.Settings.MetaData.RenderingTypes.

Get: Renderer(self: SystemSettingsTableRow) -> str

Set: Renderer(self: SystemSettingsTableRow)=value
"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """value type of the setting (string,int,etc).

Get: Type(self: SystemSettingsTableRow) -> str

Set: Type(self: SystemSettingsTableRow)=value
"""

 ValidRegex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Regex that can be used to test if value provided is valid.

Get: ValidRegex(self: SystemSettingsTableRow) -> str

Set: ValidRegex(self: SystemSettingsTableRow)=value
"""

 ValidValues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """List of valid values to choose from.

Get: ValidValues(self: SystemSettingsTableRow) -> Hashtable

Set: ValidValues(self: SystemSettingsTableRow)=value
"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Current value of the setting

Get: Value(self: SystemSettingsTableRow) -> object

Set: Value(self: SystemSettingsTableRow)=value
"""



# variables with complex values

