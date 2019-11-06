from Wms.RemotingImplementation.TaskScheduler import TaskBase
from System import Object
from Wms.RemotingObjects.Caching import Cache
# encoding: utf-8
# module Wms.RemotingImplementation.Caching calls itself Caching
# from Wms.RemotingImplementation, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CacheCleanupTask(TaskBase):
    """ CacheCleanupTask(settings: SystemSettings) """
    def Run(self):
        """ Run(self: CacheCleanupTask) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, settings):
        """ __new__(cls: type, settings: SystemSettings) """
        pass

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Settings(self: CacheCleanupTask) -> SystemSettings

Set: Settings(self: CacheCleanupTask) = value
"""


    Instance = CacheCleanupTask()
    """hardcoded/returns an instance of the class"""

class CacheContainer(Cache):
    """ CacheContainer() """
    def Add(self, key, value):
        """ Add(self: CacheContainer, key: CacheKey, value: ICachable) """
        pass

    def Clear(self, onlyDisposable=None):
        """ Clear(self: CacheContainer, onlyDisposable: bool) """
        pass

    def DisposeFirstExpiredObject(self, lifeTimes):
        """ DisposeFirstExpiredObject(self: CacheContainer, lifeTimes: Dictionary[CacheLifeTimes, int]) """
        pass

    def GetCacheObjectsOfType(self, type):
        """ GetCacheObjectsOfType(self: CacheContainer, type: Type) -> List[ICachable] """
        pass

    @staticmethod
    def GetCopy(preserveOnly):
        """ GetCopy(preserveOnly: bool) -> List[ICachable] """
        pass

    def GetObjectsByType(self, *__args):
        """
        GetObjectsByType[T](self: CacheContainer) -> (bool, Dictionary[CacheKey, T])
        GetObjectsByType[T](self: CacheContainer, findDelegate: Func[KeyValuePair[CacheKey, T], bool]) -> (bool, Dictionary[CacheKey, T])
        """
        pass

    def GetObjectsByTypeAsList(self, objectsFound):
        """ GetObjectsByTypeAsList[T](self: CacheContainer) -> (bool, List[T]) """
        pass

    def GetValue(self, hashCode):
        """ GetValue(self: CacheContainer, hashCode: int) -> ICachable """
        pass

    def IsObjectInInitialState(self, key):
        """ IsObjectInInitialState(self: CacheContainer, key: CacheKey) -> bool """
        pass

    @staticmethod
    def LoadFromCopy(copy):
        """ LoadFromCopy(copy: List[ICachable]) """
        pass

    def Remove(self, *__args):
        """
        Remove(self: CacheContainer, key: CacheKey) -> bool
        Remove(self: CacheContainer, hashCode: int) -> bool
        """
        pass

    def ToString(self):
        """ ToString(self: CacheContainer) -> str """
        pass

    def TryAdd(self, cacheKey, value):
        """ TryAdd(self: CacheContainer, cacheKey: CacheKey, value: ICachable) -> bool """
        pass

    def TryFetchObject(self, key, objectFound):
        """
        TryFetchObject(self: CacheContainer, key: CacheKey) -> (bool, object)
        TryFetchObject[T](self: CacheContainer, key: CacheKey) -> (bool, T)
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Settings(self: CacheContainer) -> SystemSettings

Set: Settings(self: CacheContainer) = value
"""


    Instance = None

    Instance = CacheContainer()
    """hardcoded/returns an instance of the class"""

class CacheSaveTask(TaskBase):
    """ CacheSaveTask(settings: SystemSettings) """
    def Run(self):
        """ Run(self: CacheSaveTask) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, settings):
        """ __new__(cls: type, settings: SystemSettings) """
        pass

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Settings(self: CacheSaveTask) -> SystemSettings

Set: Settings(self: CacheSaveTask) = value
"""


    Instance = CacheSaveTask()
    """hardcoded/returns an instance of the class"""

class ICache(Object):
    # no doc
    def AddOrUpdate(self, namespace, key, value, *__args):
        """ AddOrUpdate[T](self: ICache, namespace: str, key: str, value: T)AddOrUpdate[T](self: ICache, namespace: str, key: str, value: T, expiresAt: DateTimeOffset)AddOrUpdate[T](self: ICache, namespace: str, key: str, value: T, expiresIn: TimeSpan) """
        pass

    def AddOrUpdateAll(self, namespace, values, *__args):
        """ AddOrUpdateAll[T](self: ICache, namespace: str, values: IDictionary[str, T])AddOrUpdateAll[T](self: ICache, namespace: str, values: IDictionary[str, T], expiresAt: DateTimeOffset)AddOrUpdateAll[T](self: ICache, namespace: str, values: IDictionary[str, T], expiresIn: TimeSpan) """
        pass

    def Count(self, namespace):
        """ Count(self: ICache, namespace: str) -> int """
        pass

    def Decrement(self, namespace, key, amount):
        """ Decrement(self: ICache, namespace: str, key: str, amount: UInt32) -> Int64 """
        pass

    def FlushAll(self, namespace):
        """ FlushAll(self: ICache, namespace: str) """
        pass

    def GetAll(self, namespace, keys, updateExpiration):
        """ GetAll[T](self: ICache, namespace: str, keys: IEnumerable[str], updateExpiration: bool) -> IDictionary[str, T] """
        pass

    def GetAllKeys(self, namespace):
        """ GetAllKeys(self: ICache, namespace: str) -> IEnumerable[str] """
        pass

    def Increment(self, namespace, key, amount):
        """ Increment(self: ICache, namespace: str, key: str, amount: UInt32) -> Int64 """
        pass

    def RemoveAll(self, namespace, keys):
        """ RemoveAll(self: ICache, namespace: str, keys: IEnumerable[str]) """
        pass

    def TryAdd(self, namespace, key, value, *__args):
        """
        TryAdd[T](self: ICache, namespace: str, key: str, value: T) -> bool
        TryAdd[T](self: ICache, namespace: str, key: str, value: T, expiresAt: DateTimeOffset) -> bool
        TryAdd[T](self: ICache, namespace: str, key: str, value: T, expiresIn: TimeSpan) -> bool
        """
        pass

    def TryGet(self, namespace, key):
        """ TryGet[T](self: ICache, namespace: str, key: str) -> T """
        pass

    def TryRemove(self, namespace, key):
        """ TryRemove(self: ICache, namespace: str, key: str) -> bool """
        pass

    def TryUpdate(self, namespace, key, value, *__args):
        """
        TryUpdate[T](self: ICache, namespace: str, key: str, value: T) -> bool
        TryUpdate[T](self: ICache, namespace: str, key: str, value: T, expiresAt: DateTimeOffset) -> bool
        TryUpdate[T](self: ICache, namespace: str, key: str, value: T, expiresIn: TimeSpan) -> bool
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Instance = ICache()
    """hardcoded/returns an instance of the class"""

# variables with complex values

