# encoding: utf-8
# module Wms.RemotingObjects.Caching calls itself Caching
# from Wms.RemotingObjects,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CacheObject:
 # no doc
 def IsLifeExpired(self,lifeTimeConfig):
  """ IsLifeExpired(self: CacheObject,lifeTimeConfig: Dictionary[CacheLifeTimes,int]) -> bool """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 CreatedAt=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CreatedAt(self: CacheObject) -> DateTime

"""

 IsDisposable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDisposable(self: CacheObject) -> bool

"""

 IsUserRemovable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsUserRemovable(self: CacheObject) -> bool

"""

 Key=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Key(self: CacheObject) -> CacheKey

Set: Key(self: CacheObject)=value
"""

 Lifetime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Lifetime(self: CacheObject) -> CacheLifeTimes

"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreserveState(self: CacheObject) -> bool

"""



class CachableByteArray:
 """
 CachableByteArray()
 CachableByteArray(value: Array[Byte])
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,value=None):
  """
  __new__(cls: type)
  __new__(cls: type,value: Array[Byte])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 Lifetime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Lifetime(self: CachableByteArray) -> CacheLifeTimes

"""



class CachableString:
 """
 CachableString()
 CachableString(value: str)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,value=None):
  """
  __new__(cls: type)
  __new__(cls: type,value: str)
  """
  pass
 def __reduce_ex__(self,*args):
  pass

class Cache:
 # no doc
 def Add(self,key,value):
  """ Add(self: Cache,key: CacheKey,value: ICachable) """
  pass
 def GetCacheObjectsOfType(self,type):
  """ GetCacheObjectsOfType(self: Cache,type: Type) -> List[ICachable] """
  pass
 def Remove(self,key):
  """ Remove(self: Cache,key: CacheKey) -> bool """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
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

class CacheKey:
 # no doc
 @staticmethod
 def Construct(subject,subjectInstanceId=None,identity=None,constructionOptions=None):
  """
  Construct(subject: Type) -> CacheKey
  Construct(subject: Type,subjectInstanceId: str) -> CacheKey
  Construct(subject: Type,subjectInstanceId: str,identity: RemotingIdentity,constructionOptions: CacheKeyContructionOptionsEnum) -> CacheKey
  """
  pass
 def Equals(self,obj):
  """ Equals(self: CacheKey,obj: object) -> bool """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: CacheKey) -> int """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __ne__(self,*args):
  pass
 ContructionOptions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ContructionOptions(self: CacheKey) -> CacheKeyContructionOptionsEnum

"""

 ContructionOptionsAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ContructionOptionsAsString(self: CacheKey) -> str

"""

 CreatedByAccessId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CreatedByAccessId(self: CacheKey) -> str

"""

 CreatedByClientName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CreatedByClientName(self: CacheKey) -> str

"""

 CreatedByUserName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CreatedByUserName(self: CacheKey) -> str

"""

 InitialHash=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: InitialHash(self: CacheKey) -> str

Set: InitialHash(self: CacheKey)=value
"""

 InstanceId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: InstanceId(self: CacheKey) -> str

"""



class CacheKeyContructionOptionsEnum:
 """ enum CacheKeyContructionOptionsEnum,values: Global (5),Session (2),System (1),User (0),UserSystemCombination (4),Zone (3) """
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
 Global=None
 Session=None
 System=None
 User=None
 UserSystemCombination=None
 value__=None
 Zone=None


class CacheLifeTimes:
 """ enum CacheLifeTimes,values: ExpireImmediately (4),LiveIntermediate (2),LiveLong (1),LiveShort (3),NeverExpire (0) """
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
 ExpireImmediately=None
 LiveIntermediate=None
 LiveLong=None
 LiveShort=None
 NeverExpire=None
 value__=None


class ICachable:
 # no doc
 def IsLifeExpired(self,lifeTimeConfig):
  """ IsLifeExpired(self: ICachable,lifeTimeConfig: Dictionary[CacheLifeTimes,int]) -> bool """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 CreatedAt=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CreatedAt(self: ICachable) -> DateTime

"""

 IsDisposable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDisposable(self: ICachable) -> bool

"""

 IsUserRemovable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsUserRemovable(self: ICachable) -> bool

"""

 Key=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Key(self: ICachable) -> CacheKey

Set: Key(self: ICachable)=value
"""

 Lifetime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Lifetime(self: ICachable) -> CacheLifeTimes

"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreserveState(self: ICachable) -> bool

"""



class OnCacheObjectEventArgs:
 """ OnCacheObjectEventArgs(key: CacheKey,value: ICachable) """
 @staticmethod
 def __new__(self,key,value):
  """ __new__(cls: type,key: CacheKey,value: ICachable) """
  pass
 Key=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Key(self: OnCacheObjectEventArgs) -> CacheKey

Set: Key(self: OnCacheObjectEventArgs)=value
"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Value(self: OnCacheObjectEventArgs) -> ICachable

Set: Value(self: OnCacheObjectEventArgs)=value
"""



# variables with complex values

