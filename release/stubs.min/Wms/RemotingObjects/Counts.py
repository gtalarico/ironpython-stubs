# encoding: utf-8
# module Wms.RemotingObjects.Counts calls itself Counts
# from Wms.RemotingObjects,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Count:
 """ Count() """
 def Clone(self):
  """ Clone(self: Count) -> object """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: Count) -> int """
  pass
 def IsBatchItemCheck(self,checkRegistration):
  """ IsBatchItemCheck(self: Count,checkRegistration: bool) -> bool """
  pass
 def IsLifeExpired(self,lifeTimeConfig):
  """ IsLifeExpired(self: Count,lifeTimeConfig: Dictionary[CacheLifeTimes,int]) -> bool """
  pass
 def IsSerialItemCheck(self,checkRegistration):
  """ IsSerialItemCheck(self: Count,checkRegistration: bool) -> bool """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 AbsoluteValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AbsoluteValue(self: Count) -> Decimal

Set: AbsoluteValue(self: Count)=value
"""

 CountGroupId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CountGroupId(self: Count) -> int

Set: CountGroupId(self: Count)=value
"""

 CreatedAt=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CreatedAt(self: Count) -> DateTime

"""

 ErpErrors=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ErpErrors(self: Count) -> str

Set: ErpErrors(self: Count)=value
"""

 Hidden=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Hidden(self: Count) -> bool

"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: Count) -> int

Set: Id(self: Count)=value
"""

 IsBatchItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsBatchItem(self: Count) -> bool

Set: IsBatchItem(self: Count)=value
"""

 IsDisposable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDisposable(self: Count) -> bool

"""

 IsManuallyModified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsManuallyModified(self: Count) -> bool

Set: IsManuallyModified(self: Count)=value
"""

 IsSerialItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsSerialItem(self: Count) -> bool

Set: IsSerialItem(self: Count)=value
"""

 IsUserRemovable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsUserRemovable(self: Count) -> bool

"""

 ItemAllowsFraction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemAllowsFraction(self: Count) -> bool

Set: ItemAllowsFraction(self: Count)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemCode(self: Count) -> str

Set: ItemCode(self: Count)=value
"""

 ItemDefaultCostPrice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemDefaultCostPrice(self: Count) -> Decimal

Set: ItemDefaultCostPrice(self: Count)=value
"""

 ItemDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemDescription(self: Count) -> str

Set: ItemDescription(self: Count)=value
"""

 ItemIdentifications=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemIdentifications(self: Count) -> ItemIdentifications

Set: ItemIdentifications(self: Count)=value
"""

 ItemIdentificationsAsList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemIdentificationsAsList(self: Count) -> List[ItemIdentification]

Set: ItemIdentificationsAsList(self: Count)=value
"""

 ItemIdRegistration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemIdRegistration(self: Count) -> ItemIdentificationRegistration

Set: ItemIdRegistration(self: Count)=value
"""

 ItemUnitCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemUnitCode(self: Count) -> str

Set: ItemUnitCode(self: Count)=value
"""

 Key=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Key(self: Count) -> CacheKey

Set: Key(self: Count)=value
"""

 Lifetime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Lifetime(self: Count) -> CacheLifeTimes

"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreserveState(self: Count) -> bool

"""

 Stock=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Stock(self: Count) -> Decimal

Set: Stock(self: Count)=value
"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Type(self: Count) -> CountTypeEnum

Set: Type(self: Count)=value
"""

 TypeAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TypeAsString(self: Count) -> str

"""

 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WarehouseCode(self: Count) -> str

Set: WarehouseCode(self: Count)=value
"""

 WarehouseLocationCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WarehouseLocationCode(self: Count) -> str

Set: WarehouseLocationCode(self: Count)=value
"""



class CountFilter:
 """
 CountFilter()
 CountFilter(warehouseCode: str)
 CountFilter(type: CountTypeEnum)
 CountFilter(warehouseCode: str,type: CountTypeEnum,countGroup: int)
 CountFilter(warehouseCode: str,type: CountTypeEnum,countGroup: int,searchText: str)
 """
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)
  __new__(cls: type,warehouseCode: str)
  __new__(cls: type,type: CountTypeEnum)
  __new__(cls: type,warehouseCode: str,type: CountTypeEnum,countGroup: int)
  __new__(cls: type,warehouseCode: str,type: CountTypeEnum,countGroup: int,searchText: str)
  """
  pass
 CountGroup=None
 SearchText=None
 Type=None
 WarehouseCode=None


class CountGroup:
 """ CountGroup() """
 def IsLifeExpired(self,lifeTimeConfig):
  """ IsLifeExpired(self: CountGroup,lifeTimeConfig: Dictionary[CacheLifeTimes,int]) -> bool """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 Active=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Active(self: CountGroup) -> bool

Set: Active(self: CountGroup)=value
"""

 CreatedAt=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CreatedAt(self: CountGroup) -> DateTime

"""

 HasScript=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasScript(self: CountGroup) -> bool

"""

 Hidden=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Hidden(self: CountGroup) -> bool

"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: CountGroup) -> int

Set: Id(self: CountGroup)=value
"""

 IsDisposable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDisposable(self: CountGroup) -> bool

"""

 IsSystem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsSystem(self: CountGroup) -> bool

Set: IsSystem(self: CountGroup)=value
"""

 IsUserRemovable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsUserRemovable(self: CountGroup) -> bool

"""

 Key=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Key(self: CountGroup) -> CacheKey

Set: Key(self: CountGroup)=value
"""

 Lifetime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Lifetime(self: CountGroup) -> CacheLifeTimes

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: CountGroup) -> str

Set: Name(self: CountGroup)=value
"""

 NumberOfCounts=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: NumberOfCounts(self: CountGroup) -> int

Set: NumberOfCounts(self: CountGroup)=value
"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreserveState(self: CountGroup) -> bool

"""

 Script=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Script(self: CountGroup) -> str

Set: Script(self: CountGroup)=value
"""

 StorageAssignmentClassificationsId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: StorageAssignmentClassificationsId(self: CountGroup) -> Nullable[int]

Set: StorageAssignmentClassificationsId(self: CountGroup)=value
"""

 UseScript=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UseScript(self: CountGroup) -> bool

Set: UseScript(self: CountGroup)=value
"""



class CountGroups:
 """ CountGroups() """
 @staticmethod
 def FromIEnumerable(list):
  """ FromIEnumerable(list: IEnumerable[CountGroup]) -> CountGroups """
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
 DisplayMember='Name'
 ValueMember='Id'


class CountGroupTypeEnum:
 """ enum CountGroupTypeEnum,values: ADHOC (1),COLLIREGISTRATION (0),PICKDIFF (2) """
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
 ADHOC=None
 COLLIREGISTRATION=None
 PICKDIFF=None
 value__=None


class Counts:
 """ Counts() """
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
 TotalRowsMatched=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TotalRowsMatched(self: Counts) -> Int64

Set: TotalRowsMatched(self: Counts)=value
"""


 DisplayMember='ItemCode'
 ValueMember='Id'


class CountTypeEnum:
 """ enum (flags) CountTypeEnum,values: All (7),Approved (4),Count (1),SuggestCount (2) """
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
 All=None
 Approved=None
 Count=None
 SuggestCount=None
 value__=None


class ProcessCountResult:
 """ ProcessCountResult(success: bool) """
 @staticmethod
 def __new__(self,success):
  """ __new__(cls: type,success: bool) """
  pass
 ErpCountId=None
 ErpNewStock=None
 Success=None


