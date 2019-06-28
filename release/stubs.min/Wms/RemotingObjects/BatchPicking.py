# encoding: utf-8
# module Wms.RemotingObjects.BatchPicking calls itself BatchPicking
# from Wms.RemotingObjects,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ActivityEnum:
 """ enum ActivityEnum,values: BatchCreated (0),BatchFinished (1),ProcessedPack (7),ProcessedPick (6),ProcessShipment (8),StartedPacking (4),StartedPicking (2),StoppedPacking (5),StoppedPicking (3) """
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
 BatchCreated=None
 BatchFinished=None
 ProcessedPack=None
 ProcessedPick=None
 ProcessShipment=None
 StartedPacking=None
 StartedPicking=None
 StoppedPacking=None
 StoppedPicking=None
 value__=None


class BatchBase:
 """ BatchBase() """
 def Clone(self):
  """ Clone(self: BatchBase) -> object """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: BatchBase) -> int """
  pass
 def HasOneOfTags(self,tags):
  """ HasOneOfTags(self: BatchBase,tags: Tags) -> bool """
  pass
 def HasTag(self,*__args):
  """
  HasTag(self: BatchBase,description: str) -> bool
  HasTag(self: BatchBase,tag: Tag) -> bool
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 Active=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Active(self: BatchBase) -> bool

Set: Active(self: BatchBase)=value
"""

 ActivityLog=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ActivityLog(self: BatchBase) -> List[BatchActivityEntry]

Set: ActivityLog(self: BatchBase)=value
"""

 Age=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Age(self: BatchBase) -> str

Set: Age(self: BatchBase)=value
"""

 AssignedUserId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AssignedUserId(self: BatchBase) -> int

Set: AssignedUserId(self: BatchBase)=value
"""

 Barcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Barcode(self: BatchBase) -> str

Set: Barcode(self: BatchBase)=value
"""

 BatchLabelPrinted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BatchLabelPrinted(self: BatchBase) -> bool

Set: BatchLabelPrinted(self: BatchBase)=value
"""

 CompleteString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CompleteString(self: BatchBase) -> str

Set: CompleteString(self: BatchBase)=value
"""

 CreatedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CreatedBy(self: BatchBase) -> str

Set: CreatedBy(self: BatchBase)=value
"""

 CreatedOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CreatedOn(self: BatchBase) -> DateTime

Set: CreatedOn(self: BatchBase)=value
"""

 CurrentPackers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CurrentPackers(self: BatchBase) -> List[Session]

Set: CurrentPackers(self: BatchBase)=value
"""

 CurrentPackersAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CurrentPackersAsString(self: BatchBase) -> str

"""

 CurrentPickers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CurrentPickers(self: BatchBase) -> List[Session]

Set: CurrentPickers(self: BatchBase)=value
"""

 CurrentPickersAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CurrentPickersAsString(self: BatchBase) -> str

"""

 DatabaseId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DatabaseId(self: BatchBase) -> int

Set: DatabaseId(self: BatchBase)=value
"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Description(self: BatchBase) -> str

Set: Description(self: BatchBase)=value
"""

 FinishedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FinishedBy(self: BatchBase) -> str

Set: FinishedBy(self: BatchBase)=value
"""

 FinishedOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FinishedOn(self: BatchBase) -> DateTime

Set: FinishedOn(self: BatchBase)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: BatchBase) -> Guid

Set: Id(self: BatchBase)=value
"""

 IdAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IdAsString(self: BatchBase) -> str

"""

 LastPackProcessedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LastPackProcessedBy(self: BatchBase) -> str

Set: LastPackProcessedBy(self: BatchBase)=value
"""

 LastPackProcessedOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LastPackProcessedOn(self: BatchBase) -> DateTime

Set: LastPackProcessedOn(self: BatchBase)=value
"""

 Lifetime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Lifetime(self: BatchBase) -> CacheLifeTimes

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: BatchBase) -> str

Set: Name(self: BatchBase)=value
"""

 Notes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Notes(self: BatchBase) -> str

Set: Notes(self: BatchBase)=value
"""

 PackStartedOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PackStartedOn(self: BatchBase) -> DateTime

Set: PackStartedOn(self: BatchBase)=value
"""

 PercentComplete=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PercentComplete(self: BatchBase) -> Decimal

Set: PercentComplete(self: BatchBase)=value
"""

 PercentPacked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PercentPacked(self: BatchBase) -> Decimal

Set: PercentPacked(self: BatchBase)=value
"""

 PercentPicked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PercentPicked(self: BatchBase) -> Decimal

Set: PercentPicked(self: BatchBase)=value
"""

 PercentPickedAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PercentPickedAsString(self: BatchBase) -> str

"""

 PicklistPrinted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PicklistPrinted(self: BatchBase) -> bool

Set: PicklistPrinted(self: BatchBase)=value
"""

 PickProcessedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PickProcessedBy(self: BatchBase) -> str

Set: PickProcessedBy(self: BatchBase)=value
"""

 PickProcessedOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PickProcessedOn(self: BatchBase) -> DateTime

Set: PickProcessedOn(self: BatchBase)=value
"""

 PickStartedOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PickStartedOn(self: BatchBase) -> DateTime

Set: PickStartedOn(self: BatchBase)=value
"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreserveState(self: BatchBase) -> bool

"""

 ProcessingMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ProcessingMode(self: BatchBase) -> BatchPackProcessingModeEnum

Set: ProcessingMode(self: BatchBase)=value
"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Tag(self: BatchBase) -> object

Set: Tag(self: BatchBase)=value
"""

 Tags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Tags(self: BatchBase) -> Tags

"""

 TagsAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TagsAsString(self: BatchBase) -> str

"""

 UserId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UserId(self: BatchBase) -> int

Set: UserId(self: BatchBase)=value
"""

 ZoneId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ZoneId(self: BatchBase) -> int

Set: ZoneId(self: BatchBase)=value
"""



class Batch:
 """
 Batch()
 Batch(tag: object)
 """
 def AddOrMergeSoLine(self,line):
  """ AddOrMergeSoLine(self: Batch,line: OutboundOrderLine) """
  pass
 def ApproveBatch(self):
  """ ApproveBatch(self: Batch) """
  pass
 def Clone(self):
  """ Clone(self: Batch) -> object """
  pass
 def DisapproveBatch(self):
  """ DisapproveBatch(self: Batch) """
  pass
 def GetOrderNumbers(self,onlyVisibleOrders):
  """ GetOrderNumbers(self: Batch,onlyVisibleOrders: bool) -> List[str] """
  pass
 def HasOrderLinesOfOrder(self,orderNumber):
  """ HasOrderLinesOfOrder(self: Batch,orderNumber: str) -> bool """
  pass
 def HasTransportPackages(self):
  """ HasTransportPackages(self: Batch) -> bool """
  pass
 def IsProcessedInTotal(self):
  """ IsProcessedInTotal(self: Batch) -> bool """
  pass
 def RegisterBatchCreated(self,identity):
  """ RegisterBatchCreated(self: Batch,identity: RemotingIdentity) """
  pass
 def RegisterBatchFinished(self,session):
  """ RegisterBatchFinished(self: Batch,session: Session) """
  pass
 def RegisterBatchPackProcessed(self,identity,orderNumbers):
  """ RegisterBatchPackProcessed(self: Batch,identity: RemotingIdentity,orderNumbers: IEnumerable[str]) """
  pass
 def RegisterBatchPickProcessed(self,identity):
  """ RegisterBatchPickProcessed(self: Batch,identity: RemotingIdentity) """
  pass
 def RegisterBatchShipment(self,identity):
  """ RegisterBatchShipment(self: Batch,identity: RemotingIdentity) """
  pass
 def RegisterPacker(self,session):
  """ RegisterPacker(self: Batch,session: Session) """
  pass
 def RegisterPicker(self,session):
  """ RegisterPicker(self: Batch,session: Session) """
  pass
 def UnregisterPacker(self,session):
  """ UnregisterPacker(self: Batch,session: Session) """
  pass
 def UnregisterPicker(self,session):
  """ UnregisterPicker(self: Batch,session: Session) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,tag=None):
  """
  __new__(cls: type)
  __new__(cls: type,tag: object)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 AllocationProfile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AllocationProfile(self: Batch) -> int

Set: AllocationProfile(self: Batch)=value
"""

 BatchPickLocations=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BatchPickLocations(self: Batch) -> BatchPickLocations

Set: BatchPickLocations(self: Batch)=value
"""

 CreatedByClientTypeClientType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CreatedByClientTypeClientType(self: Batch) -> BatchCreatedByClientTypeEnum

Set: CreatedByClientTypeClientType(self: Batch)=value
"""

 Customers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Customers(self: Batch) -> PackCustomers

Set: Customers(self: Batch)=value
"""

 CustomFields=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomFields(self: Batch) -> SerializableDictionary[str,object]

Set: CustomFields(self: Batch)=value
"""

 Duration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Duration(self: Batch) -> TimeSpan

"""

 GeneratePick2PlaceImage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GeneratePick2PlaceImage(self: Batch) -> bool

Set: GeneratePick2PlaceImage(self: Batch)=value
"""

 IdAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IdAsString(self: Batch) -> str

Set: IdAsString(self: Batch)=value
"""

 NrOfReallocatedLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: NrOfReallocatedLines(self: Batch) -> int

"""

 OrderLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OrderLines(self: Batch) -> OutboundOrderLines

Set: OrderLines(self: Batch)=value
"""

 OrderLinesProcessed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OrderLinesProcessed(self: Batch) -> OutboundOrderLines

Set: OrderLinesProcessed(self: Batch)=value
"""

 PercentComplete=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PercentComplete(self: Batch) -> Decimal

"""

 PercentPacked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PercentPacked(self: Batch) -> Decimal

"""

 PercentPicked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PercentPicked(self: Batch) -> Decimal

"""

 PreferredColumns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreferredColumns(self: Batch) -> int

Set: PreferredColumns(self: Batch)=value
"""

 References=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: References(self: Batch) -> List[ColloReference]

Set: References(self: Batch)=value
"""

 ShipOrders=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ShipOrders(self: Batch) -> bool

Set: ShipOrders(self: Batch)=value
"""

 Status=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Status(self: Batch) -> BatchStatus

"""

 StatusAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: StatusAsString(self: Batch) -> str

"""

 Warnings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Warnings(self: Batch) -> Warnings

"""



class BatchActivityEntry:
 """ BatchActivityEntry() """
 def Clone(self):
  """ Clone(self: BatchActivityEntry) -> object """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Activity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Activity(self: BatchActivityEntry) -> ActivityEnum

Set: Activity(self: BatchActivityEntry)=value
"""

 ActivityAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ActivityAsString(self: BatchActivityEntry) -> str

"""

 DatabaseId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DatabaseId(self: BatchActivityEntry) -> int

Set: DatabaseId(self: BatchActivityEntry)=value
"""

 Notes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Notes(self: BatchActivityEntry) -> str

Set: Notes(self: BatchActivityEntry)=value
"""

 Session=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Session(self: BatchActivityEntry) -> Session

Set: Session(self: BatchActivityEntry)=value
"""

 Time=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Time(self: BatchActivityEntry) -> DateTime

Set: Time(self: BatchActivityEntry)=value
"""



class BatchAgeSortComparer:
 """ BatchAgeSortComparer() """
 def Compare(self,x,y):
  """ Compare(self: BatchAgeSortComparer,x: Batch,y: Batch) -> int """
  pass
 def __cmp__(self,*args):
  """ x.__cmp__(y) <==> cmp(x,y) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass

class BatchBaseAgeSortComparer:
 """ BatchBaseAgeSortComparer() """
 def Compare(self,x,y):
  """ Compare(self: BatchBaseAgeSortComparer,x: BatchBase,y: BatchBase) -> int """
  pass
 def __cmp__(self,*args):
  """ x.__cmp__(y) <==> cmp(x,y) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass

class BatchBaseList:
 """ BatchBaseList() """
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
 ValueMember='IdAsString'


class BatchCreatedByClientTypeEnum:
 """ enum BatchCreatedByClientTypeEnum,values: AdHocPicking (1),Portal (0),Script (2),Touch (3) """
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
 AdHocPicking=None
 Portal=None
 Script=None
 Touch=None
 value__=None


class Batches:
 """
 Batches()
 Batches(filterBatches: IEnumerable[Batch])
 """
 @staticmethod
 def FromIEnumerable(list):
  """ FromIEnumerable(list: IEnumerable[Batch]) -> Batches """
  pass
 def GetOutboundOrderNumbersDistinct(self):
  """ GetOutboundOrderNumbersDistinct(self: Batches) -> IEnumerable[str] """
  pass
 def GetOutboundOrdersByFilter(self,batchId,customerNumber,orderNumber):
  """ GetOutboundOrdersByFilter(self: Batches,batchId: str,customerNumber: str,orderNumber: str) -> OutboundOrders """
  pass
 def GetPackableBatches(self,batchIds):
  """ GetPackableBatches(self: Batches,batchIds: List[str]) -> Batches """
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
 @staticmethod
 def __new__(self,filterBatches=None):
  """
  __new__(cls: type)
  __new__(cls: type,filterBatches: IEnumerable[Batch])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 DisplayMember='Name'
 ValueMember='IdAsString'


class BatchFilterArgs:
 """ BatchFilterArgs() """
 Barcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Barcode(self: BatchFilterArgs) -> str

Set: Barcode(self: BatchFilterArgs)=value
"""

 ExcludePrintedBatchLabels=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExcludePrintedBatchLabels(self: BatchFilterArgs) -> bool

Set: ExcludePrintedBatchLabels(self: BatchFilterArgs)=value
"""

 ExcludePrintedPicklists=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExcludePrintedPicklists(self: BatchFilterArgs) -> bool

Set: ExcludePrintedPicklists(self: BatchFilterArgs)=value
"""

 Filter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Filter(self: BatchFilterArgs) -> str

Set: Filter(self: BatchFilterArgs)=value
"""

 TagsToFilter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TagsToFilter(self: BatchFilterArgs) -> Tags

Set: TagsToFilter(self: BatchFilterArgs)=value
"""



class BatchFilterResult:
 """ BatchFilterResult() """
 BarcodeResult=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BarcodeResult(self: BatchFilterResult) -> str

Set: BarcodeResult(self: BatchFilterResult)=value
"""

 Batches=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Batches(self: BatchFilterResult) -> BatchBaseList

Set: Batches(self: BatchFilterResult)=value
"""

 Customer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Customer(self: BatchFilterResult) -> PackCustomer

Set: Customer(self: BatchFilterResult)=value
"""



class BatchPickLocation:
 """ BatchPickLocation() """
 @staticmethod
 def ConstructUniqueId(itemCode,warehouseCode,locationCode,itemIdNumber,innerReference,outerReference):
  """ ConstructUniqueId(itemCode: str,warehouseCode: str,locationCode: str,itemIdNumber: str,innerReference: str,outerReference: str) -> str """
  pass
 def Equals(self,obj):
  """ Equals(self: BatchPickLocation,obj: object) -> bool """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: BatchPickLocation) -> int """
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
 CustomerDistribution=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomerDistribution(self: BatchPickLocation) -> Dictionary[str,Decimal]

Set: CustomerDistribution(self: BatchPickLocation)=value
"""

 Density=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Density(self: BatchPickLocation) -> Decimal

"""

 HasInstructions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasInstructions(self: BatchPickLocation) -> bool

"""

 InnerReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: InnerReference(self: BatchPickLocation) -> str

Set: InnerReference(self: BatchPickLocation)=value
"""

 Instructions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Instructions(self: BatchPickLocation) -> List[str]

Set: Instructions(self: BatchPickLocation)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemCode(self: BatchPickLocation) -> str

Set: ItemCode(self: BatchPickLocation)=value
"""

 ItemDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemDescription(self: BatchPickLocation) -> str

Set: ItemDescription(self: BatchPickLocation)=value
"""

 ItemDimensions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemDimensions(self: BatchPickLocation) -> Dimensions

Set: ItemDimensions(self: BatchPickLocation)=value
"""

 ItemIdNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemIdNumber(self: BatchPickLocation) -> str

Set: ItemIdNumber(self: BatchPickLocation)=value
"""

 ItemIdNumberFormatted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemIdNumberFormatted(self: BatchPickLocation) -> str

"""

 ItemIdNumberPrefix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemIdNumberPrefix(self: BatchPickLocation) -> str

Set: ItemIdNumberPrefix(self: BatchPickLocation)=value
"""

 ItemIdRegistration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemIdRegistration(self: BatchPickLocation) -> ItemIdentificationRegistration

Set: ItemIdRegistration(self: BatchPickLocation)=value
"""

 ItemPicked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemPicked(self: BatchPickLocation) -> BatchPickLocationIndicatorEnum

"""

 ItemWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemWeight(self: BatchPickLocation) -> Decimal

Set: ItemWeight(self: BatchPickLocation)=value
"""

 OuterReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OuterReference(self: BatchPickLocation) -> str

Set: OuterReference(self: BatchPickLocation)=value
"""

 OuterReferenceDisplayValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OuterReferenceDisplayValue(self: BatchPickLocation) -> str

Set: OuterReferenceDisplayValue(self: BatchPickLocation)=value
"""

 PickToPlaceCachedImage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PickToPlaceCachedImage(self: BatchPickLocation) -> Image

"""

 PickToPlaceImage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PickToPlaceImage(self: BatchPickLocation) -> Array[Byte]

Set: PickToPlaceImage(self: BatchPickLocation)=value
"""

 TotalWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TotalWeight(self: BatchPickLocation) -> Decimal

"""

 UniqueId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UniqueId(self: BatchPickLocation) -> str

"""

 VendorBarcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: VendorBarcode(self: BatchPickLocation) -> str

Set: VendorBarcode(self: BatchPickLocation)=value
"""

 VendorItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: VendorItemCode(self: BatchPickLocation) -> str

Set: VendorItemCode(self: BatchPickLocation)=value
"""

 Volume=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Volume(self: BatchPickLocation) -> Decimal

"""


 _itemIds=None


class BatchPickLocationIndicatorEnum:
 """ enum BatchPickLocationIndicatorEnum,values: Complete (2),MarkedAsPicked (3),None (0),Partial (1) """
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
 Complete=None
 MarkedAsPicked=None
 None_ =None
 Partial=None
 value__=None


class BatchPickLocations:
 """ BatchPickLocations() """
 @staticmethod
 def FromIEnumerable(list):
  """ FromIEnumerable(list: IEnumerable[BatchPickLocation]) -> BatchPickLocations """
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
 DisplayMember=None
 ValueMember='UniqueId'


class BatchProcessAction:
 """ enum BatchProcessAction,values: Default (0),Mobile (2),MobileToTerminal (1),Terminal (3) """
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
 Default=None
 Mobile=None
 MobileToTerminal=None
 Terminal=None
 value__=None


class BatchScanArgs:
 """ BatchScanArgs() """
 Barcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Barcode(self: BatchScanArgs) -> str

Set: Barcode(self: BatchScanArgs)=value
"""

 CacheKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CacheKey(self: BatchScanArgs) -> CacheKey

Set: CacheKey(self: BatchScanArgs)=value
"""

 ItemCodeExpected=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemCodeExpected(self: BatchScanArgs) -> str

Set: ItemCodeExpected(self: BatchScanArgs)=value
"""

 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WarehouseCode(self: BatchScanArgs) -> str

Set: WarehouseCode(self: BatchScanArgs)=value
"""

 WarehouseLocationCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WarehouseLocationCode(self: BatchScanArgs) -> str

Set: WarehouseLocationCode(self: BatchScanArgs)=value
"""



class BatchScanResult:
 """ BatchScanResult() """
 BarcodeResult=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BarcodeResult(self: BatchScanResult) -> BarcodeStructureResultEnum

Set: BarcodeResult(self: BatchScanResult)=value
"""

 BarcodeStructure=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BarcodeStructure(self: BatchScanResult) -> BarcodeStructure

Set: BarcodeStructure(self: BatchScanResult)=value
"""

 IsBarcodeValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsBarcodeValid(self: BatchScanResult) -> bool

Set: IsBarcodeValid(self: BatchScanResult)=value
"""

 IsItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsItem(self: BatchScanResult) -> bool

Set: IsItem(self: BatchScanResult)=value
"""

 IsLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsLocation(self: BatchScanResult) -> bool

Set: IsLocation(self: BatchScanResult)=value
"""

 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Message(self: BatchScanResult) -> str

Set: Message(self: BatchScanResult)=value
"""



class BatchStatus:
 """ enum BatchStatus,values: Approved (0),FullyPacked (5),New (-1),Packing (4),Picking (1),PickingAndPacking (2),ReadyToPack (3),Shipping (6) """
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
 Approved=None
 FullyPacked=None
 New=None
 Packing=None
 Picking=None
 PickingAndPacking=None
 ReadyToPack=None
 Shipping=None
 value__=None


class BatchUpdateArgs:
 """ BatchUpdateArgs() """
 AllocationProfileId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AllocationProfileId(self: BatchUpdateArgs) -> int

Set: AllocationProfileId(self: BatchUpdateArgs)=value
"""

 Approve=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Approve(self: BatchUpdateArgs) -> bool

Set: Approve(self: BatchUpdateArgs)=value
"""

 AssignedUserId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AssignedUserId(self: BatchUpdateArgs) -> int

Set: AssignedUserId(self: BatchUpdateArgs)=value
"""

 BatchName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BatchName(self: BatchUpdateArgs) -> str

Set: BatchName(self: BatchUpdateArgs)=value
"""

 Notes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Notes(self: BatchUpdateArgs) -> str

Set: Notes(self: BatchUpdateArgs)=value
"""

 PickItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PickItems(self: BatchUpdateArgs) -> bool

Set: PickItems(self: BatchUpdateArgs)=value
"""

 Tags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Tags(self: BatchUpdateArgs) -> Array[Tag]

Set: Tags(self: BatchUpdateArgs)=value
"""



class DifferFromRouteOptions:
 """ enum DifferFromRouteOptions,values: Allow (0),AllowWithMessage (1),DontAllow (2) """
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
 Allow=None
 AllowWithMessage=None
 DontAllow=None
 value__=None


class GetBatchArgs:
 """ GetBatchArgs() """
 CreatedByClientType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CreatedByClientType(self: GetBatchArgs) -> BatchCreatedByClientTypeEnum

Set: CreatedByClientType(self: GetBatchArgs)=value
"""

 Filter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Filter(self: GetBatchArgs) -> str

Set: Filter(self: GetBatchArgs)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: GetBatchArgs) -> str

Set: Id(self: GetBatchArgs)=value
"""

 Status=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Status(self: GetBatchArgs) -> BatchStatus

Set: Status(self: GetBatchArgs)=value
"""

 TagsToFilter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TagsToFilter(self: GetBatchArgs) -> Tags

Set: TagsToFilter(self: GetBatchArgs)=value
"""

 UseCreatedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UseCreatedBy(self: GetBatchArgs) -> bool

Set: UseCreatedBy(self: GetBatchArgs)=value
"""

 UseStatus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UseStatus(self: GetBatchArgs) -> bool

Set: UseStatus(self: GetBatchArgs)=value
"""



class GetBatchToConsolidateToArgs:
 """ GetBatchToConsolidateToArgs() """
 UseComparerToFindBatch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UseComparerToFindBatch(self: GetBatchToConsolidateToArgs) -> bool

Set: UseComparerToFindBatch(self: GetBatchToConsolidateToArgs)=value
"""

 ZoneIdToCheckForPackBatch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ZoneIdToCheckForPackBatch(self: GetBatchToConsolidateToArgs) -> int

Set: ZoneIdToCheckForPackBatch(self: GetBatchToConsolidateToArgs)=value
"""


 Comparer=None


class GetItemsToPackArgs:
 """ GetItemsToPackArgs() """
 BatchIds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BatchIds(self: GetItemsToPackArgs) -> List[str]

Set: BatchIds(self: GetItemsToPackArgs)=value
"""

 CacheKeyOfTransportPackages=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CacheKeyOfTransportPackages(self: GetItemsToPackArgs) -> CacheKey

Set: CacheKeyOfTransportPackages(self: GetItemsToPackArgs)=value
"""

 Customer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Customer(self: GetItemsToPackArgs) -> PackCustomer

Set: Customer(self: GetItemsToPackArgs)=value
"""



class PickArgs:
 """
 PickArgs()
 PickArgs(itemCode: str,warehouseCode: str,locationCode: str,quantity: Decimal)
 PickArgs(itemCode: str,warehouseCode: str,locationCode: str,quantity: Decimal,itemId: str)
 PickArgs(itemCode: str,warehouseCode: str,locationCode: str,quantity: Decimal,itemId: ItemIdentification)
 """
 @staticmethod
 def __new__(self,itemCode=None,warehouseCode=None,locationCode=None,quantity=None,itemId=None):
  """
  __new__(cls: type)
  __new__(cls: type,itemCode: str,warehouseCode: str,locationCode: str,quantity: Decimal)
  __new__(cls: type,itemCode: str,warehouseCode: str,locationCode: str,quantity: Decimal,itemId: str)
  __new__(cls: type,itemCode: str,warehouseCode: str,locationCode: str,quantity: Decimal,itemId: ItemIdentification)
  """
  pass
 CacheKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CacheKey(self: PickArgs) -> CacheKey

Set: CacheKey(self: PickArgs)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemCode(self: PickArgs) -> str

Set: ItemCode(self: PickArgs)=value
"""

 ItemId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemId(self: PickArgs) -> ItemIdentification

Set: ItemId(self: PickArgs)=value
"""

 ItemWasScanned=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemWasScanned(self: PickArgs) -> bool

Set: ItemWasScanned(self: PickArgs)=value
"""

 LocationCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LocationCode(self: PickArgs) -> str

Set: LocationCode(self: PickArgs)=value
"""

 LocationWasScanned=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LocationWasScanned(self: PickArgs) -> bool

Set: LocationWasScanned(self: PickArgs)=value
"""

 NewInnerReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: NewInnerReference(self: PickArgs) -> str

Set: NewInnerReference(self: PickArgs)=value
"""

 NewOuterReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: NewOuterReference(self: PickArgs) -> str

Set: NewOuterReference(self: PickArgs)=value
"""

 PreviousInnerReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreviousInnerReference(self: PickArgs) -> str

Set: PreviousInnerReference(self: PickArgs)=value
"""

 PreviousOuterReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreviousOuterReference(self: PickArgs) -> str

Set: PreviousOuterReference(self: PickArgs)=value
"""

 Quantity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Quantity(self: PickArgs) -> Decimal

Set: Quantity(self: PickArgs)=value
"""

 Result=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Result(self: PickArgs) -> PickResult

Set: Result(self: PickArgs)=value
"""

 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WarehouseCode(self: PickArgs) -> str

Set: WarehouseCode(self: PickArgs)=value
"""



class PickItemIdRangeArgs:
 """ PickItemIdRangeArgs() """
 GenerateArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GenerateArgs(self: PickItemIdRangeArgs) -> ItemIdGenerateArgs

Set: GenerateArgs(self: PickItemIdRangeArgs)=value
"""



class PickItemIdsArgs:
 """ PickItemIdsArgs() """
 ItemIds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemIds(self: PickItemIdsArgs) -> List[ItemIdentification]

Set: ItemIds(self: PickItemIdsArgs)=value
"""



class PickResult:
 """ PickResult() """
 PickLocations=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PickLocations(self: PickResult) -> BatchPickLocations

Set: PickLocations(self: PickResult)=value
"""

 Positions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Positions(self: PickResult) -> SerializableDictionary[str,str]

Set: Positions(self: PickResult)=value
"""



class ProcessBatchPickingArgs:
 """ ProcessBatchPickingArgs() """
 CacheKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CacheKey(self: ProcessBatchPickingArgs) -> CacheKey

Set: CacheKey(self: ProcessBatchPickingArgs)=value
"""

 NewPackBatchId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: NewPackBatchId(self: ProcessBatchPickingArgs) -> str

Set: NewPackBatchId(self: ProcessBatchPickingArgs)=value
"""



class ProcessPickState:
 """ enum ProcessPickState,values: Allocated (3),Deallocated (2),Done (4),NotSet (0),Transferred (1) """
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
 Allocated=None
 Deallocated=None
 Done=None
 NotSet=None
 Transferred=None
 value__=None


class ProcessSalesOrderLinesArgs:
 """ ProcessSalesOrderLinesArgs() """
 AllowToDeliverMoreThanOrdered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AllowToDeliverMoreThanOrdered(self: ProcessSalesOrderLinesArgs) -> bool

Set: AllowToDeliverMoreThanOrdered(self: ProcessSalesOrderLinesArgs)=value
"""

 DocumentPrinter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DocumentPrinter(self: ProcessSalesOrderLinesArgs) -> str

Set: DocumentPrinter(self: ProcessSalesOrderLinesArgs)=value
"""

 PackageSlipLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PackageSlipLayout(self: ProcessSalesOrderLinesArgs) -> str

Set: PackageSlipLayout(self: ProcessSalesOrderLinesArgs)=value
"""

 PrintInvoices=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PrintInvoices(self: ProcessSalesOrderLinesArgs) -> bool

Set: PrintInvoices(self: ProcessSalesOrderLinesArgs)=value
"""

 PrintInvoicesSet=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PrintInvoicesSet(self: ProcessSalesOrderLinesArgs) -> bool

Set: PrintInvoicesSet(self: ProcessSalesOrderLinesArgs)=value
"""



