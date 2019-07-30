# encoding: utf-8
# module Wms.RemotingImplementation.Scripting calls itself Scripting
# from Wms.RemotingImplementation,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from System.Collections.Generic import *
from ..__init__ import *

# no functions
# classes

class PythonScriptEvaluator(object):
 """ PythonScriptEvaluator(general: General,inventory: Inventory,outbound: Outbound,inbound: Inbound,printing: Printing,messaging: Messaging,notificationCenter: NotificationCenter,documentQueue: DocumentQueue) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PythonScriptEvaluator()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def CompileScript(self,pScript):
  """ CompileScript(self: PythonScriptEvaluator,pScript: str) -> List[PythonError] """
  pass
 def Eval(self,pScript,variables):
  """ Eval[T](self: PythonScriptEvaluator,pScript: str,variables: Dictionary[str,object]) -> T """
  pass
 def EvalVoid(self,pScript,variables):
  """ EvalVoid(self: PythonScriptEvaluator,pScript: str,variables: Dictionary[str,object]) """
  pass
 def ExecuteIsolated(self,pScript,variables,retries=None):
  """
  ExecuteIsolated[T](self: PythonScriptEvaluator,pScript: str,variables: Dictionary[str,object]) -> T
  ExecuteIsolated[T](self: PythonScriptEvaluator,pScript: str,variables: Dictionary[str,object],retries: int) -> T
  """
  pass
 def RestartEngine(self):
  """ RestartEngine(self: PythonScriptEvaluator) """
  pass
 @staticmethod
 def __new__(self,general,inventory,outbound,inbound,printing,messaging,notificationCenter,documentQueue):
  """ __new__(cls: type,general: General,inventory: Inventory,outbound: Outbound,inbound: Inbound,printing: Printing,messaging: Messaging,notificationCenter: NotificationCenter,documentQueue: DocumentQueue) """
  pass

class PythonStdoutWriter(StreamWriter):
 """ PythonStdoutWriter(s: Stream) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PythonStdoutWriter()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Dispose(self):
  """
  Dispose(self: StreamWriter,disposing: bool)
   Releases the unmanaged resources used by the System.IO.StreamWriter and optionally releases the managed resources.
  
   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject
  
   Creates a shallow copy of the current System.MarshalByRefObject object.
  
   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the object to be assigned a new identity when it is marshaled across a remoting 
    boundary. A value of false is usually appropriate. true to copy the current System.MarshalByRefObject object's identity to its clone,which will cause remoting client calls 
    to be routed to the remote server object.
  
   Returns: A shallow copy of the current System.MarshalByRefObject object.
  MemberwiseClone(self: object) -> object
  
   Creates a shallow copy of the current System.Object.
   Returns: A shallow copy of the current System.Object.
  """
  pass
 def Write(self,*__args):
  """ Write(self: PythonStdoutWriter,value: str) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,s):
  """ __new__(cls: type,s: Stream) """
  pass
 CoreNewLine=None


class ScriptOverridableAttribute:
 """ ScriptOverridableAttribute() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ScriptOverridableAttribute()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 BaseOutputType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BaseOutputType(self: ScriptOverridableAttribute) -> Type

Set: BaseOutputType(self: ScriptOverridableAttribute)=value
"""

 CustomLocals=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomLocals(self: ScriptOverridableAttribute) -> Dictionary[str,Type]

"""

 CustomLocalsName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomLocalsName(self: ScriptOverridableAttribute) -> Array[str]

Set: CustomLocalsName(self: ScriptOverridableAttribute)=value
"""

 CustomLocalsType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomLocalsType(self: ScriptOverridableAttribute) -> Array[Type]

Set: CustomLocalsType(self: ScriptOverridableAttribute)=value
"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Description(self: ScriptOverridableAttribute) -> str

Set: Description(self: ScriptOverridableAttribute)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: ScriptOverridableAttribute) -> str

Set: Name(self: ScriptOverridableAttribute)=value
"""

 ReturnType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ReturnType(self: ScriptOverridableAttribute) -> Type

Set: ReturnType(self: ScriptOverridableAttribute)=value
"""

 ShowArguments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ShowArguments(self: ScriptOverridableAttribute) -> bool

Set: ShowArguments(self: ScriptOverridableAttribute)=value
"""

 TreeOrder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TreeOrder(self: ScriptOverridableAttribute) -> int

Set: TreeOrder(self: ScriptOverridableAttribute)=value
"""

 TreePath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TreePath(self: ScriptOverridableAttribute) -> str

Set: TreePath(self: ScriptOverridableAttribute)=value
"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Type(self: ScriptOverridableAttribute) -> ScriptOverridableType

Set: Type(self: ScriptOverridableAttribute)=value
"""

 Version=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Version(self: ScriptOverridableAttribute) -> int

Set: Version(self: ScriptOverridableAttribute)=value
"""



class ScriptOverridableType:
 """ enum ScriptOverridableType,values: AddPackage (119),AddPrintJob (189),AddWarehouseTransferItemIdentitification (90),AddWarehouseTransferItems (152),AddWarehouseTransferQuantities (161),AddWarehouseTransferQuantity (91),CancelPendingPurchaseOrderReceipts (53),CancelPendingRmaOrderReceipts (28),ChangeDefaultLocation (105),ChangeItemBarcode (87),CheckZoneRightAddReferenceOnTransfer (104),CreatePreReceipt (181),CreatePreReceiptLineItemIdentifications (183),CreatePreReceiptLines (182),DeleteBatches (170),DeleteReplenishmentOrder (76),DetermineNewestStock (147),DetermineOldestStock (148),DetermineRoute (168),ExecuteMessageHandler (177),ExecuteMessagePublisher (176),GenerateReplenishmentOrder (74),GenerateReplenishmentOrderMultiple (75),GetAdhocRmaCustomersByFilter (29),GetAllowDifferentRoute (149),GetBarcodeStructure (1),GetBatchesAll (165),GetBatchesIncomplete (166),GetBatchesWithPendingPackages (167),GetBatchToConsolidateTo (172),GetCacheKeyOfTransportPackages (80),GetCustomers (69),GetCustomersPending (66),GetCustomersPendingByFilter (67),GetDefaultAllocationSettings (156),GetDefaultBatchSink (158),GetDefaultPrintAllocationSettings (157),GetHistoryOutboundOrderCustomers (17),GetHistoryPurchaseOrderPrintLines (45),GetHistoryPurchaseOrdersByFilter (43),GetHistoryPurchaseReceiptsByFilter (44),GetHistoryRmaOrderLines (33),GetHistoryRmaOrdersByFilter (32),GetHistoryShipment (120),GetHistoryShipmentsAll (121),GetHistoryShipmentsByFilter (122),GetItem (8),GetItemcodeFromBarcode (106),GetItemExistsOnDefaultInboundLocation (107),GetItemExistsOnLocation (108),GetItemIdentificationExists (109),GetItemIdentifications (111),GetItemImageLarge (112),GetItemImageSmall (113),GetItemLocationDefault (13),GetItemLocations (12),GetItems (9),GetItemsAll (11),GetItemsOnDefaultInboundLocation (114),GetItemsOnLocation (10),GetItemsOnTransportLocation (115),GetItemStockList (116),GetItemStockTotals (117),GetItemsToPack (160),GetItemVendors (35),GetLocationClassificationById (143),GetLocationClassifications (142),GetMobileShipperById (123),GetOrdersForBatch (155),GetOutboundOrderLinesBatchableByOrders (146),GetOutboundOrdersBatchable (169),GetPackages (124),GetPreReceiptLines (185),GetPreReceipts (184),GetPrintJobTypes (190),GetPurchaseOrder (36),GetPurchaseOrderLines (39),GetPurchaseOrderPrintLines (42),GetPurchaseOrdersAll (37),GetPurchaseOrdersByFilter (38),GetPurchaseReceiveLines (46),GetPurchaseReceiveLinesByKey (47),GetReplenishmentOrder (72),GetReplenishmentOrderLines (73),GetReplenishmentOrders (71),GetRmaCustomersExpectedByFilter (16),GetRmaOrder (88),GetRmaOrderItemIdentifications (89),GetRmaOrderLines (19),GetRmaOrderPrintLines (18),GetRmaOrdersAll (14),GetRmaOrdersByFilter (15),GetRmaReasons (30),GetRmaReceiveLines (20),GetRmaReceiveLinesByKey (21),GetSalesOrder (61),GetSalesOrderCostLines (65),GetSalesOrderLines (64),GetSalesOrdersAll (62),GetSalesOrdersBatchable (145),GetSalesOrdersByFilter (63),GetShipmentServices (126),GetShipperById (128),GetShippers (129),GetShipperServiceLevelsByShipperId (127),GetStorageAssignmentClassification (140),GetStorageAssignmentClassificationById (141),GetVendors (34),GetVendorsExpected (40),GetVendorsExpectedByFilter (41),GetVendorsWithPendingPreReceipts (186),GetWarehouseByCode (55),GetWarehouseLayoutsBySetting (139),GetWarehouseLayoutSettingById (138),GetWarehouseLayoutSettings (137),GetWarehouseLocations (3),GetWarehousesActive (7),GetWarehousesActiveByLocation (6),GetWarehousesActiveWithDefaultInboundLocation (5),GetWarehousesAll (2),GetWarehousesInactive (4),HandleColliForStockRegistration (70),IsBatchLimitReached (144),IsValidItemInCountGroup (153),LogAndCleanupShipment (81),MergeErpStock (118),OnMessageStatusChanged (178),OnPythonEngineBooted (0),OpenBatchForPickingById (173),OpenTransferPackagesForShipping (125),OrderMatchesCustomer (68),OrderMatchesCustomerValidator (188),PreCreatePreReceipt (180),PrepareInboundReceiveLines (57),PrepareWarehouseTransfer (92),PrepareWarehouseTransferFrom (93),PrepareWarehouseTransferItem (151),PrepareWarehouseTransferReceived (94),PrepareWarehouseTransferTo (95),PrepareWarehouseTransferToMulti (96),PrepareWarehouseTransferToMultiReceived (97),PrepareWarehouseTransferToMultiTransport (98),PrintBatchLabel (175),PrintDuplicateLabels (130),PrintPickList (174),PrintPrintLine (83),PrintPrintLines (84),PrintPrintLinesByObject (85),PrintPrintLinesByObjectAndPrinter (86),PrintPurchaseReceipt (56),PrintRmaReceipt (31),ProcessAdhocRmaOrderLines (27),ProcessBatchPacking (159),ProcessBatchPicking (77),ProcessCounts (100),ProcessDirectOrder (187),ProcessPendingReceiveLines (54),ProcessPendingRmaReceiveLines (26),ProcessPurchaseOrderLines (58),ProcessReceipt (59),ProcessReplenishmentOrder (79),ProcessRmaOrderLines (60),ProcessSalesOrder (78),ProcessShipment (131),ProcessShipmentInfo (82),PutBack (51),PutBackItemId (52),PutBackRmaItem (24),PutBackRmaItemId (25),Receive (48),ReceiveBs (49),ReceiveItemId (50),ReceiveRmaItem (22),ReceiveRmaItemId (23),RemoveCountItemIdentification (99),RemovePackage (133),RemoveWarehouseTransferItemIdentification (101),SaveBatchInCache (164),SetBatchName (163),SortOutboundOrderLinesForBatchCreation (154),SubtractWarehouseTransferQuantities (162),TransferItemFromBatch (150),TransferItems (102),UpdateBatchWithSettings (171),UpdatePackageData (134),UpdateTransportPackagesHeader (135),UpdateWarehouseTransfer (103),ValidateItemIdentification (110),ValidateOrder (179),ValidateShipment (132),VoidShipment (136) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ScriptOverridableType()
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
 AddPackage=None
 AddPrintJob=None
 AddWarehouseTransferItemIdentitification=None
 AddWarehouseTransferItems=None
 AddWarehouseTransferQuantities=None
 AddWarehouseTransferQuantity=None
 CancelPendingPurchaseOrderReceipts=None
 CancelPendingRmaOrderReceipts=None
 ChangeDefaultLocation=None
 ChangeItemBarcode=None
 CheckZoneRightAddReferenceOnTransfer=None
 CreatePreReceipt=None
 CreatePreReceiptLineItemIdentifications=None
 CreatePreReceiptLines=None
 DeleteBatches=None
 DeleteReplenishmentOrder=None
 DetermineNewestStock=None
 DetermineOldestStock=None
 DetermineRoute=None
 ExecuteMessageHandler=None
 ExecuteMessagePublisher=None
 GenerateReplenishmentOrder=None
 GenerateReplenishmentOrderMultiple=None
 GetAdhocRmaCustomersByFilter=None
 GetAllowDifferentRoute=None
 GetBarcodeStructure=None
 GetBatchesAll=None
 GetBatchesIncomplete=None
 GetBatchesWithPendingPackages=None
 GetBatchToConsolidateTo=None
 GetCacheKeyOfTransportPackages=None
 GetCustomers=None
 GetCustomersPending=None
 GetCustomersPendingByFilter=None
 GetDefaultAllocationSettings=None
 GetDefaultBatchSink=None
 GetDefaultPrintAllocationSettings=None
 GetHistoryOutboundOrderCustomers=None
 GetHistoryPurchaseOrderPrintLines=None
 GetHistoryPurchaseOrdersByFilter=None
 GetHistoryPurchaseReceiptsByFilter=None
 GetHistoryRmaOrderLines=None
 GetHistoryRmaOrdersByFilter=None
 GetHistoryShipment=None
 GetHistoryShipmentsAll=None
 GetHistoryShipmentsByFilter=None
 GetItem=None
 GetItemcodeFromBarcode=None
 GetItemExistsOnDefaultInboundLocation=None
 GetItemExistsOnLocation=None
 GetItemIdentificationExists=None
 GetItemIdentifications=None
 GetItemImageLarge=None
 GetItemImageSmall=None
 GetItemLocationDefault=None
 GetItemLocations=None
 GetItems=None
 GetItemsAll=None
 GetItemsOnDefaultInboundLocation=None
 GetItemsOnLocation=None
 GetItemsOnTransportLocation=None
 GetItemStockList=None
 GetItemStockTotals=None
 GetItemsToPack=None
 GetItemVendors=None
 GetLocationClassificationById=None
 GetLocationClassifications=None
 GetMobileShipperById=None
 GetOrdersForBatch=None
 GetOutboundOrderLinesBatchableByOrders=None
 GetOutboundOrdersBatchable=None
 GetPackages=None
 GetPreReceiptLines=None
 GetPreReceipts=None
 GetPrintJobTypes=None
 GetPurchaseOrder=None
 GetPurchaseOrderLines=None
 GetPurchaseOrderPrintLines=None
 GetPurchaseOrdersAll=None
 GetPurchaseOrdersByFilter=None
 GetPurchaseReceiveLines=None
 GetPurchaseReceiveLinesByKey=None
 GetReplenishmentOrder=None
 GetReplenishmentOrderLines=None
 GetReplenishmentOrders=None
 GetRmaCustomersExpectedByFilter=None
 GetRmaOrder=None
 GetRmaOrderItemIdentifications=None
 GetRmaOrderLines=None
 GetRmaOrderPrintLines=None
 GetRmaOrdersAll=None
 GetRmaOrdersByFilter=None
 GetRmaReasons=None
 GetRmaReceiveLines=None
 GetRmaReceiveLinesByKey=None
 GetSalesOrder=None
 GetSalesOrderCostLines=None
 GetSalesOrderLines=None
 GetSalesOrdersAll=None
 GetSalesOrdersBatchable=None
 GetSalesOrdersByFilter=None
 GetShipmentServices=None
 GetShipperById=None
 GetShippers=None
 GetShipperServiceLevelsByShipperId=None
 GetStorageAssignmentClassification=None
 GetStorageAssignmentClassificationById=None
 GetVendors=None
 GetVendorsExpected=None
 GetVendorsExpectedByFilter=None
 GetVendorsWithPendingPreReceipts=None
 GetWarehouseByCode=None
 GetWarehouseLayoutsBySetting=None
 GetWarehouseLayoutSettingById=None
 GetWarehouseLayoutSettings=None
 GetWarehouseLocations=None
 GetWarehousesActive=None
 GetWarehousesActiveByLocation=None
 GetWarehousesActiveWithDefaultInboundLocation=None
 GetWarehousesAll=None
 GetWarehousesInactive=None
 HandleColliForStockRegistration=None
 IsBatchLimitReached=None
 IsValidItemInCountGroup=None
 LogAndCleanupShipment=None
 MergeErpStock=None
 OnMessageStatusChanged=None
 OnPythonEngineBooted=None
 OpenBatchForPickingById=None
 OpenTransferPackagesForShipping=None
 OrderMatchesCustomer=None
 OrderMatchesCustomerValidator=None
 PreCreatePreReceipt=None
 PrepareInboundReceiveLines=None
 PrepareWarehouseTransfer=None
 PrepareWarehouseTransferFrom=None
 PrepareWarehouseTransferItem=None
 PrepareWarehouseTransferReceived=None
 PrepareWarehouseTransferTo=None
 PrepareWarehouseTransferToMulti=None
 PrepareWarehouseTransferToMultiReceived=None
 PrepareWarehouseTransferToMultiTransport=None
 PrintBatchLabel=None
 PrintDuplicateLabels=None
 PrintPickList=None
 PrintPrintLine=None
 PrintPrintLines=None
 PrintPrintLinesByObject=None
 PrintPrintLinesByObjectAndPrinter=None
 PrintPurchaseReceipt=None
 PrintRmaReceipt=None
 ProcessAdhocRmaOrderLines=None
 ProcessBatchPacking=None
 ProcessBatchPicking=None
 ProcessCounts=None
 ProcessDirectOrder=None
 ProcessPendingReceiveLines=None
 ProcessPendingRmaReceiveLines=None
 ProcessPurchaseOrderLines=None
 ProcessReceipt=None
 ProcessReplenishmentOrder=None
 ProcessRmaOrderLines=None
 ProcessSalesOrder=None
 ProcessShipment=None
 ProcessShipmentInfo=None
 PutBack=None
 PutBackItemId=None
 PutBackRmaItem=None
 PutBackRmaItemId=None
 Receive=None
 ReceiveBs=None
 ReceiveItemId=None
 ReceiveRmaItem=None
 ReceiveRmaItemId=None
 RemoveCountItemIdentification=None
 RemovePackage=None
 RemoveWarehouseTransferItemIdentification=None
 SaveBatchInCache=None
 SetBatchName=None
 SortOutboundOrderLinesForBatchCreation=None
 SubtractWarehouseTransferQuantities=None
 TransferItemFromBatch=None
 TransferItems=None
 UpdateBatchWithSettings=None
 UpdatePackageData=None
 UpdateTransportPackagesHeader=None
 UpdateWarehouseTransfer=None
 ValidateItemIdentification=None
 ValidateOrder=None
 ValidateShipment=None
 value__=None
 VoidShipment=None


# variables with complex values

