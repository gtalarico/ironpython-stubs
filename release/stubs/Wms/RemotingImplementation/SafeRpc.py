from System import Object
# encoding: utf-8
# module Wms.RemotingImplementation.SafeRpc calls itself SafeRpc
# from Wms.RemotingImplementation, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class SafeRpcMethod(Object):
    """
    SafeRpcMethod(id: int)
    SafeRpcMethod(cacheKey: CacheKey)
    """
    def Dispose(self):
        """ Dispose(self: SafeRpcMethod) """
        pass

    def Execute(self, action):
        """ Execute[TResult](self: SafeRpcMethod, action: Func[TResult]) -> TResult """
        pass

    @staticmethod
    def GetExecutionContexts():
        """ GetExecutionContexts() -> List[SafeRpcExecutionContext] """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, id: int)
        __new__(cls: type, cacheKey: CacheKey)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Instance = SafeRpcMethod()
    """hardcoded/returns an instance of the class"""

