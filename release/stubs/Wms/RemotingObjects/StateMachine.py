from Wms.RemotingObjects.Caching.Generics import Cachable
# encoding: utf-8
# module Wms.RemotingObjects.StateMachine calls itself StateMachine
# from Wms.RemotingObjects, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CachableState(Cachable):
    """
    CachableState()
    CachableState(state: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, state=None):
        """
        __new__(cls: type)
        __new__(cls: type, state: str)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Lifetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lifetime(self: CachableState) -> CacheLifeTimes

"""

    PreserveState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreserveState(self: CachableState) -> bool

"""


    Instance = CachableState()
    """hardcoded/returns an instance of the class"""
