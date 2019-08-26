from Wms.RemotingObjects.Caching import *
from Wms.RemotingImplementation.TaskScheduler import *
# encoding: utf-8
# module Wms.RemotingImplementation.Caching calls itself Caching
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
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

# variables with complex values

