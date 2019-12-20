from System import Object
# encoding: utf-8
# module Wms.RemotingImplementation.Caching.Removal calls itself Removal
# from Wms.RemotingImplementation, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CachedDirectOrderRemovalHandler(CacheObjectRemovalHandlerBase):
    """ CachedDirectOrderRemovalHandler(stockManager: IStockManager) """
    def Handle(self, cachable):
        """ Handle(self: CachedDirectOrderRemovalHandler, cachable: DirectOrder) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, stockManager):
        """ __new__(cls: type, stockManager: IStockManager) """
        pass

    Instance = CachedDirectOrderRemovalHandler()
    """hardcoded/returns an instance of the class"""

class CachedEnhancedStockAllocationsRemovalHandler(CacheObjectRemovalHandlerBase):
    """ CachedEnhancedStockAllocationsRemovalHandler(stockManager: IStockManager) """
    def Handle(self, cachable):
        """ Handle(self: CachedEnhancedStockAllocationsRemovalHandler, cachable: EnhancedStockAllocations) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, stockManager):
        """ __new__(cls: type, stockManager: IStockManager) """
        pass

    Instance = CachedEnhancedStockAllocationsRemovalHandler()
    """hardcoded/returns an instance of the class"""

class CachedInboundReceiveLinesRemovalHandler(CacheObjectRemovalHandlerBase):
    """ CachedInboundReceiveLinesRemovalHandler(inbound: Inbound) """
    def Handle(self, cachable):
        """ Handle(self: CachedInboundReceiveLinesRemovalHandler, cachable: InboundReceiveLines) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, inbound):
        """ __new__(cls: type, inbound: Inbound) """
        pass

    Instance = CachedInboundReceiveLinesRemovalHandler()
    """hardcoded/returns an instance of the class"""

class CachedRmaReceiveLinesRemovalHandler(CacheObjectRemovalHandlerBase):
    """ CachedRmaReceiveLinesRemovalHandler(inbound: Inbound) """
    def Handle(self, cachable):
        """ Handle(self: CachedRmaReceiveLinesRemovalHandler, cachable: RmaReceiveLines) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, inbound):
        """ __new__(cls: type, inbound: Inbound) """
        pass

    Instance = CachedRmaReceiveLinesRemovalHandler()
    """hardcoded/returns an instance of the class"""

class CacheObjectRemovalHandlerBase(Object):
    # no doc
    def Handle(self, cachable):
        """ Handle(self: CacheObjectRemovalHandlerBase[T], cachable: object)Handle(self: CacheObjectRemovalHandlerBase[T], cachable: T) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Instance = CacheObjectRemovalHandlerBase()
    """hardcoded/returns an instance of the class"""

class ICacheObjectRemovalHandler(Object):
    # no doc
    def Handle(self, cachable):
        """ Handle(self: ICacheObjectRemovalHandler[T], cachable: object)Handle(self: ICacheObjectRemovalHandler[T], cachable: T) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Instance = ICacheObjectRemovalHandler()
    """hardcoded/returns an instance of the class"""

