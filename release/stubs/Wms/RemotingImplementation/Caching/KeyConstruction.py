# encoding: utf-8
# module Wms.RemotingImplementation.Caching.KeyConstruction calls itself KeyConstruction
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CountCacheKeyConstructor:
    """ CountCacheKeyConstructor(hashCodeProvider: IUniqueHashCodeProvider, identityProvider: IRemotingIdentityProvider) """
    def Construct(self, cachable):
        """ Construct(self: CountCacheKeyConstructor, cachable: Count) -> CacheKey """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, hashCodeProvider, identityProvider):
        """ __new__(cls: type, hashCodeProvider: IUniqueHashCodeProvider, identityProvider: IRemotingIdentityProvider) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return CountCacheKeyConstructor()

class ICacheKeyConstructor:
    # no doc
    def Construct(self, cachable):
        """ Construct(self: ICacheKeyConstructor[T], cachable: T) -> CacheKey """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ICacheKeyConstructor()

