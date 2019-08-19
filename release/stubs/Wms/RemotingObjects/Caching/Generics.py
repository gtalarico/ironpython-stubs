from Wms.RemotingObjects.Caching import *
# encoding: utf-8
# module Wms.RemotingObjects.Caching.Generics calls itself Generics
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Cachable(CacheObject):
    """ Cachable[T](value: T) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, value):
        """
        __new__(cls: type, value: T)
        __new__(cls: type)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Value(self: Cachable[T]) -> T

"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return Cachable()

