# encoding: utf-8
# module Wms.RemotingImplementation.Caching calls itself Caching
# from Wms.RemotingImplementation,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CacheCleanupTask:
 """ CacheCleanupTask(settings: SystemSettings) """
 def Run(self):
  """ Run(self: CacheCleanupTask) """
  pass
 @staticmethod
 def __new__(self,settings):
  """ __new__(cls: type,settings: SystemSettings) """
  pass
 Settings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Settings(self: CacheCleanupTask) -> SystemSettings

Set: Settings(self: CacheCleanupTask)=value
"""



class CacheContainer:
 """ CacheContainer() """
 def Add(self,key,value):
  """ Add(self: CacheContainer,key: CacheKey,value: ICachable) """
  pass
 def Clear(self,onlyDisposable=None):
  """ Clear(self: CacheContainer,onlyDisposable: bool) """
  pass
 def DisposeFirstExpiredObject(self,lifeTimes):
  """ DisposeFirstExpiredObject(self: CacheContainer,lifeTimes: Dictionary[CacheLifeTimes,int]) """
  pass
 def GetCacheObjectsOfType(self,type):
  """ GetCacheObjectsOfType(self: CacheContainer,type: Type) -> List[ICachable] """
  pass
 @staticmethod
 def GetCopy(preserveOnly):
  """ GetCopy(preserveOnly: bool) -> List[ICachable] """
  pass
 def GetObjectsByType(self,*__args):
  """
  GetObjectsByType[T](self: CacheContainer) -> (bool,Dictionary[CacheKey,T])
  GetObjectsByType[T](self: CacheContainer,findDelegate: Func[KeyValuePair[CacheKey,T],bool]) -> (bool,Dictionary[CacheKey,T])
  """
  pass
 def GetObjectsByTypeAsList(self,objectsFound):
  """ GetObjectsByTypeAsList[T](self: CacheContainer) -> (bool,List[T]) """
  pass
 def GetValue(self,hashCode):
  """ GetValue(self: CacheContainer,hashCode: int) -> ICachable """
  pass
 def IsObjectInInitialState(self,key):
  """ IsObjectInInitialState(self: CacheContainer,key: CacheKey) -> bool """
  pass
 @staticmethod
 def LoadFromCopy(copy):
  """ LoadFromCopy(copy: List[ICachable]) """
  pass
 def Remove(self,*__args):
  """
  Remove(self: CacheContainer,key: CacheKey) -> bool
  Remove(self: CacheContainer,hashCode: int) -> bool
  """
  pass
 def ToString(self):
  """ ToString(self: CacheContainer) -> str """
  pass
 def TryAdd(self,cacheKey,value):
  """ TryAdd(self: CacheContainer,cacheKey: CacheKey,value: ICachable) -> bool """
  pass
 def TryFetchObject(self,key,objectFound):
  """
  TryFetchObject(self: CacheContainer,key: CacheKey) -> (bool,object)
  TryFetchObject[T](self: CacheContainer,key: CacheKey) -> (bool,T)
  """
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
 def __str__(self,*args):
  pass
 Settings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Settings(self: CacheContainer) -> SystemSettings

Set: Settings(self: CacheContainer)=value
"""


 Instance=None


class CacheSaveTask:
 """ CacheSaveTask(settings: SystemSettings) """
 def Run(self):
  """ Run(self: CacheSaveTask) """
  pass
 @staticmethod
 def __new__(self,settings):
  """ __new__(cls: type,settings: SystemSettings) """
  pass
 Settings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Settings(self: CacheSaveTask) -> SystemSettings

Set: Settings(self: CacheSaveTask)=value
"""



# variables with complex values

